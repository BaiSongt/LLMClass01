#!/opt/homebrew/Caskroom/miniconda/base/envs/translate_app/bin/ python3
# -*- coding: utf-8 -*-
from PySide6.QtWidgets import QApplication
from LLMApp import LLMApp as llm_app


if __name__ == "__main__":
    import sys
    app = QApplication(sys.argv)
    window = llm_app()
    window.setWindowTitle("LLM App")
    window.show()
    sys.exit(app.exec())
