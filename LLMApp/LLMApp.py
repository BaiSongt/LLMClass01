from PySide6.QtWidgets import QApplication, QWidget, QProgressBar, QVBoxLayout
from PySide6.QtCore import QThread, Signal
from PySide6.QtGui import QTextCursor
from PySide6.QtWidgets import QFileDialog
from llm_ui import Ui_Form
from llmchat import LLMChat
import sys, time


# 使用专用工作线程处理流式输出
class LLMWorker(QThread):
    progress = Signal(str)  # 改为逐行传输
    finished = Signal()

    def __init__(self, agent_executor, user_input):  # 修改参数名
        super().__init__()
        self.agent_executor = agent_executor  # 保存executor实例
        self.user_input = user_input

    def run(self):
        try:
            # 正确获取流式响应
            stream = self.agent_executor.stream({"input": self.user_input})
            for chunk in stream:
                line = chunk.get("answer", "")  # 更安全的键名获取
                self.progress.emit(line)
                time.sleep(0.05)
        except Exception as e:
            self.progress.emit(f"Error: {str(e)}")
        finally:
            self.finished.emit()


# 主窗口类，继承自 QWidget 和 Ui_Form
class LLMApp(QWidget, Ui_Form):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.LLM_once_chat_content = ""
        self.llm_models = self.get_ollama_models()
        self.llm_temperature = self.lineEdit.text()
        self.llm_chain_verbose = self.checkBox.isChecked()
        self.llm = self.llm_init()

        self.llm_comboBox.addItems(self.llm_models)
        self.llm_comboBox.setCurrentText(self.llm_models[0])
        self.user_input_edit.setPlaceholderText("请输入您的问题...")
        self.worker = LLMWorker(self.llm, "你好")

        self.bind_buttons()
        self.worker.progress.connect(self.update_text_browser)
        self.worker.finished.connect(self.on_stream_finished)

    def update_text_browser(self, line):
        cursor = self.textBrowser.textCursor()
        cursor.movePosition(QTextCursor.End)
        cursor.insertText(line)
        self.textBrowser.ensureCursorVisible()

    def on_stream_finished(self):
        self.textBrowser.moveCursor(QTextCursor.End)
        self.progressBar.setValue(100)
        # self.statusBar.showMessage("Stream completed", 3000)
        # self.statusTip.showMessage("Stream completed", 3000)

    def llm_init(self):
        selected_model = self.llm_comboBox.currentText()
        llm = LLMChat(
            model_name=selected_model,
            temperature=self.llm_temperature,
            is_Verbose=self.llm_chain_verbose,
        )
        print(f"LLM {selected_model} 初始化完成。")
        return llm

    def bind_buttons(self):
        self.enter_btn.clicked.connect(self.on_button_click)
        self.btn_load_file.clicked.connect(self.add_file)
        self.btn_rm_file.clicked.connect(self.remove_file)
        self.llm_comboBox.currentTextChanged.connect(self.on_model_change)
        self.clear_btn.clicked.connect(self.clear_output)
        self.clear_btn_2.clicked.connect(self.clear_input)
        self.user_input_edit.setPlaceholderText("请输入您的问题...")

    def on_button_click(self):
        user_input = self.user_input_edit.toPlainText().strip()
        if not user_input:
            return

        # 初始化流式输出容器
        once_container = f"​**Question**: {user_input}\n\n ​**Answer**: \n"
        self.llm_msg_output.setMarkdown(once_container)
        self.textBrowser.moveCursor(QTextCursor.Start)

        # 直接使用预初始化的agent
        self.worker = LLMWorker(self.llm.chat_memory_agent, user_input)
        self.worker.progress.connect(self.update_text_browser)
        self.worker.finished.connect(self.on_stream_finished)
        self.worker.start()

        # 流式输出
        agent = self.llm.chat_memory_agent(self.llm.chat_model, False)
        for line in agent.stream({"input": user_input}):
            self.textBrowser.moveCursor(QTextCursor.MoveOperation.End)
            self.textBrowser.insertPlainText(line)  # 插入新内容
            once_container += line
            QApplication.processEvents()  # 刷新界面，确保流式输出实时显示

        # 完成后输出一次性内容
        self.LLM_once_chat_content += f"{once_container} \n\n\n"
        self.output_message(once_container)
        self.llm_msg_output.setMarkdown(f"\n {self.LLM_once_chat_content} \n")
        self.llm_msg_output.moveCursor(QTextCursor.MoveOperation.End)

        # 清空输入框
        once_container = ""

    def on_model_change(self, model_name):
        self.llm_init()
        self.llm_msg_output.setPlainText(f"Selected model: {model_name}")
        self.clear_output()

    def clear_input(self):
        self.user_input_edit.clear()

    def clear_output(self):
        self.llm_msg_output.clear()
        self.LLM_once_chat_content = ""

    def output_message(self, message):
        print(message, end="", flush=True)

    def get_ollama_models(self):
        import subprocess

        result = subprocess.run(["ollama", "list"], capture_output=True, text=True)
        # print("标准输出:", result.stdout)

        if result.returncode != 0:
            print("Run Ollama List Error: ", result.stderr)
        else:
            # 使用正则表达式匹配并分组
            import re

            pattern = r"(\S+)\s+(\S+)\s+([\d.]+\s\w+)\s+(.+)"
            matches = re.findall(pattern, result.stdout)

            # 将匹配结果存入 ollama_list 列表
            ollama_list = []
            for match in matches:
                ollama_list.append(
                    {
                        "name": match[0],
                        "id": match[1],
                        "size": match[2],
                        "modified": match[3],
                    }
                )

            # 打印分组后的结果
            models = []
            for model in ollama_list:
                models.append(model["name"])

            print("Ollama list :\n", models)
            return models

    def add_file(self):
        file_dialog = self.open_file_dialog()
        if file_dialog:
            print("selected_files: \n", file_dialog)
            list_files = [
                self.listWidget_files.item(i).text()
                for i in range(self.listWidget_files.count())
            ]
            for file_path in file_dialog:
                include_file = False
                for o_path in list_files:
                    if o_path == file_path:
                        include_file = True
                if include_file == False:
                    self.listWidget_files.addItem(
                        file_path
                    )  # 在 listView 中显示加载的文件路径

        # 获取文件后缀
        # file_extension = os.path.splitext(file_name)[1].lower()

    def open_file_dialog(self):
        file_dialog = QFileDialog(self)
        file_dialog.setFileMode(QFileDialog.FileMode.ExistingFile)
        if file_dialog.exec():
            selected_files = file_dialog.selectedFiles()
            if selected_files:
                return selected_files
        return None

    def remove_file(self):
        selected_items = self.listWidget_files.selectedItems()
        if not selected_items:
            return
        for item in selected_items:
            self.listWidget_files.takeItem(self.listWidget_files.row(item))
