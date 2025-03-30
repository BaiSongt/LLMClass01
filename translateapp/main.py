from PySide6.QtWidgets import QApplication, QWidget
from PySide6.QtCore import Qt
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
            "llama3.1:8b",
            "codellama:7b-code"
        ]

        self.llm_comboBox.addItems(self.llm_models)
        self.llm_comboBox.setCurrentText(self.llm_models[0])
        self.user_input_edit.setPlaceholderText("请输入您的问题...")
        self.bind_buttons()

    def bind_buttons(self):
        self.enter_btn.clicked.connect(self.on_button_click)
        self.llm_comboBox.currentTextChanged.connect(self.on_model_change)
        self.clear_btn.clicked.connect(self.clear_output)
        self.user_input_edit.setPlaceholderText("请输入您的问题...")

    def on_button_click(self):
        user_input = self.user_input_edit.toPlainText()
        selected_model = self.llm_comboBox.currentText()
        llm = LLMChat(model_name=selected_model)
        response = llm.getStream(user_input)
        once_container = ""
        for line in response:
            self.llm_msg_output.setMarkdown(once_container)
            once_container += line + "\n"
        self.LLM_once_chat_content += f"**{selected_model}**: {user_input}\n"
        self.LLM_once_chat_content += f"**Assistant**: {self.llm_msg_output.toPlainText()}\n"
        self.output_message(self.LLM_once_chat_content)
        self.user_input_edit.clear()

    def on_model_change(self, model_name):
        self.llm_msg_output.setMarkdown(f"Selected model: {model_name}")
        self.bind_buttons()

    def clear_input(self):
        self.user_input_edit.clear()
        self.llm_msg_output.clear()

    def clear_output(self):
        self.llm_msg_output.clear()
        self.LLM_once_chat_content = ""

    def output_message(self, message):
        print(message)

if __name__ == "__main__":
    import sys
    app = QApplication(sys.argv)
    window = MyWindow()
    window.setWindowTitle("LLM App")
    window.show()
    sys.exit(app.exec())
