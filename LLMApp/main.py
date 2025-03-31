from PySide6.QtWidgets import QApplication, QWidget
from PySide6.QtCore import Qt
from PySide6.QtGui import QTextCursor
from llm_ui import Ui_Form
from llmchat import LLMChat

import sys

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
        response = llm.getStream(user_input)
        once_container = f"**Question**: {user_input}\n\n **Answer**: \n"
        # 流式输出
        for line in response:
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
    import sys
    app = QApplication(sys.argv)
    window = MyWindow()
    window.setWindowTitle("LLM App")
    window.show()
    sys.exit(app.exec())
