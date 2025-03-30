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
    QPlainTextEdit, QPushButton, QSizePolicy, QSpacerItem,
    QTextBrowser, QTextEdit, QVBoxLayout, QWidget)

class Ui_Form(object):
    def setupUi(self, Form):
        if not Form.objectName():
            Form.setObjectName(u"Form")
        Form.resize(754, 660)
        self.verticalLayout_3 = QVBoxLayout(Form)
        self.verticalLayout_3.setObjectName(u"verticalLayout_3")
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

        self.horizontalSpacer = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_2.addItem(self.horizontalSpacer)


        self.verticalLayout_3.addLayout(self.horizontalLayout_2)

        self.textBrowser = QTextBrowser(Form)
        self.textBrowser.setObjectName(u"textBrowser")

        self.verticalLayout_3.addWidget(self.textBrowser)

        self.horizontalLayout_3 = QHBoxLayout()
        self.horizontalLayout_3.setObjectName(u"horizontalLayout_3")
        self.llm_msg_output = QTextEdit(Form)
        self.llm_msg_output.setObjectName(u"llm_msg_output")
        self.llm_msg_output.setMinimumSize(QSize(0, 400))
        self.llm_msg_output.setReadOnly(True)

        self.horizontalLayout_3.addWidget(self.llm_msg_output)

        self.verticalLayout = QVBoxLayout()
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.copy_btn = QPushButton(Form)
        self.copy_btn.setObjectName(u"copy_btn")

        self.verticalLayout.addWidget(self.copy_btn)

        self.clear_btn = QPushButton(Form)
        self.clear_btn.setObjectName(u"clear_btn")

        self.verticalLayout.addWidget(self.clear_btn)


        self.horizontalLayout_3.addLayout(self.verticalLayout)


        self.verticalLayout_3.addLayout(self.horizontalLayout_3)

        self.horizontalLayout = QHBoxLayout()
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.user_input_edit = QPlainTextEdit(Form)
        self.user_input_edit.setObjectName(u"user_input_edit")
        self.user_input_edit.setMaximumSize(QSize(16777215, 400))

        self.horizontalLayout.addWidget(self.user_input_edit)

        self.verticalLayout_2 = QVBoxLayout()
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.clear_btn_2 = QPushButton(Form)
        self.clear_btn_2.setObjectName(u"clear_btn_2")
        self.clear_btn_2.setMinimumSize(QSize(0, 20))

        self.verticalLayout_2.addWidget(self.clear_btn_2)

        self.enter_btn = QPushButton(Form)
        self.enter_btn.setObjectName(u"enter_btn")
        self.enter_btn.setMinimumSize(QSize(0, 20))

        self.verticalLayout_2.addWidget(self.enter_btn)


        self.horizontalLayout.addLayout(self.verticalLayout_2)


        self.verticalLayout_3.addLayout(self.horizontalLayout)


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
    # retranslateUi

