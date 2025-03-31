# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'llm.ui'
##
## Created by: Qt User Interface Compiler version 6.8.2
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide6.QtCore import (QCoreApplication, QDate, QDateTime, QLocale,
    QMetaObject, QObject, QPoint, QRect,
    QSize, QTime, QUrl, Qt)
from PySide6.QtGui import (QBrush, QColor, QConicalGradient, QCursor,
    QFont, QFontDatabase, QGradient, QIcon,
    QImage, QKeySequence, QLinearGradient, QPainter,
    QPalette, QPixmap, QRadialGradient, QTransform)
from PySide6.QtWidgets import (QApplication, QComboBox, QHBoxLayout, QLabel,
    QListView, QPlainTextEdit, QProgressBar, QPushButton,
    QSizePolicy, QSpacerItem, QSplitter, QTextBrowser,
    QTextEdit, QVBoxLayout, QWidget)

class Ui_Form(object):
    def setupUi(self, Form):
        if not Form.objectName():
            Form.setObjectName(u"Form")
        Form.resize(503, 585)
        self.verticalLayout_4 = QVBoxLayout(Form)
        self.verticalLayout_4.setObjectName(u"verticalLayout_4")
        self.horizontalLayout_2 = QHBoxLayout()
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.llm_lable_select = QLabel(Form)
        self.llm_lable_select.setObjectName(u"llm_lable_select")
        font = QFont()
        font.setPointSize(20)
        self.llm_lable_select.setFont(font)

        self.horizontalLayout_2.addWidget(self.llm_lable_select)

        self.llm_comboBox = QComboBox(Form)
        self.llm_comboBox.setObjectName(u"llm_comboBox")
        self.llm_comboBox.setMinimumSize(QSize(200, 20))
        font1 = QFont()
        font1.setPointSize(14)
        self.llm_comboBox.setFont(font1)

        self.horizontalLayout_2.addWidget(self.llm_comboBox)

        self.progressBar = QProgressBar(Form)
        self.progressBar.setObjectName(u"progressBar")
        self.progressBar.setValue(24)

        self.horizontalLayout_2.addWidget(self.progressBar)


        self.verticalLayout_4.addLayout(self.horizontalLayout_2)

        self.splitter = QSplitter(Form)
        self.splitter.setObjectName(u"splitter")
        self.splitter.setOrientation(Qt.Orientation.Vertical)
        self.textBrowser = QTextBrowser(self.splitter)
        self.textBrowser.setObjectName(u"textBrowser")
        self.textBrowser.setMinimumSize(QSize(0, 20))
        self.textBrowser.setMaximumSize(QSize(16777215, 100))
        self.splitter.addWidget(self.textBrowser)
        self.widget = QWidget(self.splitter)
        self.widget.setObjectName(u"widget")
        self.horizontalLayout_4 = QHBoxLayout(self.widget)
        self.horizontalLayout_4.setObjectName(u"horizontalLayout_4")
        self.horizontalLayout_4.setContentsMargins(0, 0, 0, 0)
        self.llm_msg_output = QTextEdit(self.widget)
        self.llm_msg_output.setObjectName(u"llm_msg_output")
        self.llm_msg_output.setMinimumSize(QSize(0, 100))
        self.llm_msg_output.setReadOnly(True)

        self.horizontalLayout_4.addWidget(self.llm_msg_output)

        self.verticalLayout = QVBoxLayout()
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.verticalSpacer = QSpacerItem(20, 40, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding)

        self.verticalLayout.addItem(self.verticalSpacer)

        self.copy_btn = QPushButton(self.widget)
        self.copy_btn.setObjectName(u"copy_btn")

        self.verticalLayout.addWidget(self.copy_btn)

        self.clear_btn = QPushButton(self.widget)
        self.clear_btn.setObjectName(u"clear_btn")

        self.verticalLayout.addWidget(self.clear_btn)


        self.horizontalLayout_4.addLayout(self.verticalLayout)

        self.splitter.addWidget(self.widget)
        self.widget1 = QWidget(self.splitter)
        self.widget1.setObjectName(u"widget1")
        self.horizontalLayout_5 = QHBoxLayout(self.widget1)
        self.horizontalLayout_5.setObjectName(u"horizontalLayout_5")
        self.horizontalLayout_5.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout = QHBoxLayout()
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.user_input_edit = QPlainTextEdit(self.widget1)
        self.user_input_edit.setObjectName(u"user_input_edit")
        self.user_input_edit.setMinimumSize(QSize(200, 0))
        self.user_input_edit.setMaximumSize(QSize(16777215, 400))

        self.horizontalLayout.addWidget(self.user_input_edit)

        self.verticalLayout_2 = QVBoxLayout()
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.clear_btn_2 = QPushButton(self.widget1)
        self.clear_btn_2.setObjectName(u"clear_btn_2")
        self.clear_btn_2.setMinimumSize(QSize(0, 20))

        self.verticalLayout_2.addWidget(self.clear_btn_2)

        self.enter_btn = QPushButton(self.widget1)
        self.enter_btn.setObjectName(u"enter_btn")
        self.enter_btn.setMinimumSize(QSize(0, 20))

        self.verticalLayout_2.addWidget(self.enter_btn)


        self.horizontalLayout.addLayout(self.verticalLayout_2)


        self.horizontalLayout_5.addLayout(self.horizontalLayout)

        self.horizontalLayout_3 = QHBoxLayout()
        self.horizontalLayout_3.setObjectName(u"horizontalLayout_3")
        self.listView_files = QListView(self.widget1)
        self.listView_files.setObjectName(u"listView_files")

        self.horizontalLayout_3.addWidget(self.listView_files)

        self.verticalLayout_3 = QVBoxLayout()
        self.verticalLayout_3.setObjectName(u"verticalLayout_3")
        self.btn_load_file = QPushButton(self.widget1)
        self.btn_load_file.setObjectName(u"btn_load_file")

        self.verticalLayout_3.addWidget(self.btn_load_file)

        self.btn_rm_file = QPushButton(self.widget1)
        self.btn_rm_file.setObjectName(u"btn_rm_file")

        self.verticalLayout_3.addWidget(self.btn_rm_file)


        self.horizontalLayout_3.addLayout(self.verticalLayout_3)


        self.horizontalLayout_5.addLayout(self.horizontalLayout_3)

        self.splitter.addWidget(self.widget1)

        self.verticalLayout_4.addWidget(self.splitter)


        self.retranslateUi(Form)

        QMetaObject.connectSlotsByName(Form)
    # setupUi

    def retranslateUi(self, Form):
        Form.setWindowTitle(QCoreApplication.translate("Form", u"Form", None))
        self.llm_lable_select.setText(QCoreApplication.translate("Form", u"\u6a21\u578b\u9009\u62e9", None))
        self.copy_btn.setText(QCoreApplication.translate("Form", u"copy", None))
        self.clear_btn.setText(QCoreApplication.translate("Form", u"clear", None))
        self.user_input_edit.setPlainText("")
        self.clear_btn_2.setText(QCoreApplication.translate("Form", u"clear", None))
        self.enter_btn.setText(QCoreApplication.translate("Form", u" Ask ", None))
        self.btn_load_file.setText(QCoreApplication.translate("Form", u"Load", None))
        self.btn_rm_file.setText(QCoreApplication.translate("Form", u"Rm", None))
    # retranslateUi

