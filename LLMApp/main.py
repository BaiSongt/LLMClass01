from PySide6.QtWidgets import QApplication, QWidget,QProgressBar, QVBoxLayout
from PySide6.QtCore import QThread, Signal
from PySide6.QtGui import QTextCursor
from llm_ui import Ui_Form
from llmchat import LLMChat
import sys

class LLMWorker(QThread):
    # 定义两个信号：progress 和 finished
    # progress 信号用于传递进度信息（整数类型）
    # finished 信号用于通知任务完成
    progress = Signal(int)
    finished = Signal()

    def __init__(self, llm, user_input):
        """
        初始化 LLMWorker 类。
        :param llm: 一个语言模型对象，提供 getStream 方法。
        :param user_input: 用户输入的文本，传递给语言模型进行处理。
        """
        super().__init__()  # 调用父类 QThread 的初始化方法
        self.llm = llm  # 保存语言模型对象
        self.user_input = user_input  # 保存用户输入
        self.reponse = self.llm.getStream(self.user_input) # 初始化响应

    def run(self):
        """
        线程的主逻辑，处理用户输入并通过信号更新进度。
        """
        # 调用语言模型的 getStream 方法获取响应（生成器对象）
        # self.reponse = self.llm.getStream(self.user_input)

        # 计算响应中的总行数（通过遍历生成器）
        total_lines = sum(1 for _ in  self.reponse)

        # 重新初始化生成器，因为上一步已经遍历完了
        self.reponse = self.llm.getStream(self.user_input)

        # 遍历生成器中的每一行
        for i, line in enumerate( self.reponse, start=1):
            # 计算当前进度的百分比，并通过 progress 信号发送
            self.progress.emit(int((i / total_lines) * 100))

        # 当所有行处理完成后，发送 finished 信号通知任务结束
        self.finished.emit()

# 主窗口类，继承自 QWidget 和 Ui_Form
class MyWindow(QWidget, Ui_Form):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.LLM_once_chat_content = ""

        self.llm_models = [
            "qwen2.5:latest",
            "deepseek-r1:1.5b",
            "llama3.1:8b"
        ]

        self.llm_comboBox.addItems(self.llm_models)
        self.llm_comboBox.setCurrentText(self.llm_models[0])
        self.user_input_edit.setPlaceholderText("请输入您的问题...")
        self.bind_buttons()

    def bind_buttons(self):
        self.enter_btn.clicked.connect(self.on_button_click)
        self.llm_comboBox.currentTextChanged.connect(self.on_model_change)
        self.clear_btn.clicked.connect(self.clear_output)
        self.clear_btn_2.clicked.connect(self.clear_input)
        self.user_input_edit.setPlaceholderText("请输入您的问题...")

    def on_button_click(self):
        user_input = self.user_input_edit.toPlainText()
        selected_model = self.llm_comboBox.currentText()
        llm = LLMChat(model_name=selected_model)
        self.worker = LLMWorker(llm, user_input)
        # self.worker.progress.connect(self.update_progress)
        # self.worker.finished.connect(self.on_finished)
        # self.worker.start()
        once_container = f"**Question**: {user_input}\n\n **Answer**: \n"
        # 流式输出
        for line in self.worker.reponse:
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
        self.llm_msg_output.setPlainText(f"Selected model: {model_name}")
        self.clear_output()

    def clear_input(self):
        self.user_input_edit.clear()

    def clear_output(self):
        self.llm_msg_output.clear()
        self.LLM_once_chat_content = ""

    def output_message(self, message):
        print(message, end="", flush=True)

if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = MyWindow()
    window.setWindowTitle("LLM App")
    window.show()
    sys.exit(app.exec())
