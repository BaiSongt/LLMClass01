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
from PySide6.QtWidgets import (QApplication, QCheckBox, QComboBox, QGridLayout,
    QHBoxLayout, QLabel, QLineEdit, QListView,
    QPlainTextEdit, QProgressBar, QPushButton, QSizePolicy,
    QSpacerItem, QSplitter, QTextBrowser, QTextEdit,
    QVBoxLayout, QWidget)

class Ui_Form(object):
    def setupUi(self, Form):
        if not Form.objectName():
            Form.setObjectName(u"Form")
        Form.resize(694, 474)
        self.verticalLayout_2 = QVBoxLayout(Form)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.splitter = QSplitter(Form)
        self.splitter.setObjectName(u"splitter")
        self.splitter.setOrientation(Qt.Orientation.Vertical)
        self.textBrowser = QTextBrowser(self.splitter)
        self.textBrowser.setObjectName(u"textBrowser")
        self.textBrowser.setMinimumSize(QSize(0, 20))
        self.textBrowser.setMaximumSize(QSize(16777215, 100))
        self.splitter.addWidget(self.textBrowser)
        self.layoutWidget = QWidget(self.splitter)
        self.layoutWidget.setObjectName(u"layoutWidget")
        self.horizontalLayout_4 = QHBoxLayout(self.layoutWidget)
        self.horizontalLayout_4.setObjectName(u"horizontalLayout_4")
        self.horizontalLayout_4.setContentsMargins(0, 0, 0, 0)
        self.llm_msg_output = QTextEdit(self.layoutWidget)
        self.llm_msg_output.setObjectName(u"llm_msg_output")
        self.llm_msg_output.setMinimumSize(QSize(0, 100))
        self.llm_msg_output.setReadOnly(True)

        self.horizontalLayout_4.addWidget(self.llm_msg_output)

        self.verticalLayout = QVBoxLayout()
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.verticalSpacer = QSpacerItem(20, 40, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding)

        self.verticalLayout.addItem(self.verticalSpacer)

        self.copy_btn = QPushButton(self.layoutWidget)
        self.copy_btn.setObjectName(u"copy_btn")

        self.verticalLayout.addWidget(self.copy_btn)

        self.clear_btn = QPushButton(self.layoutWidget)
        self.clear_btn.setObjectName(u"clear_btn")

        self.verticalLayout.addWidget(self.clear_btn)


        self.horizontalLayout_4.addLayout(self.verticalLayout)

        self.splitter.addWidget(self.layoutWidget)
        self.user_input_edit = QPlainTextEdit(self.splitter)
        self.user_input_edit.setObjectName(u"user_input_edit")
        self.user_input_edit.setMinimumSize(QSize(199, 0))
        self.user_input_edit.setMaximumSize(QSize(16777215, 400))
        self.splitter.addWidget(self.user_input_edit)

        self.verticalLayout_2.addWidget(self.splitter)

        self.horizontalLayout_2 = QHBoxLayout()
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.horizontalLayout = QHBoxLayout()
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.listView_files = QListView(Form)
        self.listView_files.setObjectName(u"listView_files")
        self.listView_files.setMaximumSize(QSize(16777215, 60))

        self.horizontalLayout.addWidget(self.listView_files)

        self.verticalLayout_3 = QVBoxLayout()
        self.verticalLayout_3.setObjectName(u"verticalLayout_3")
        self.btn_load_file = QPushButton(Form)
        self.btn_load_file.setObjectName(u"btn_load_file")

        self.verticalLayout_3.addWidget(self.btn_load_file)

        self.btn_rm_file = QPushButton(Form)
        self.btn_rm_file.setObjectName(u"btn_rm_file")

        self.verticalLayout_3.addWidget(self.btn_rm_file)


        self.horizontalLayout.addLayout(self.verticalLayout_3)


        self.horizontalLayout_2.addLayout(self.horizontalLayout)

        self.gridLayout = QGridLayout()
        self.gridLayout.setObjectName(u"gridLayout")
        self.lineEdit = QLineEdit(Form)
        self.lineEdit.setObjectName(u"lineEdit")

        self.gridLayout.addWidget(self.lineEdit, 1, 1, 1, 1)

        self.checkBox = QCheckBox(Form)
        self.checkBox.setObjectName(u"checkBox")

        self.gridLayout.addWidget(self.checkBox, 1, 2, 1, 1)

        self.llm_lable_select = QLabel(Form)
        self.llm_lable_select.setObjectName(u"llm_lable_select")
        font = QFont()
        font.setPointSize(13)
        font.setBold(False)
        self.llm_lable_select.setFont(font)
        self.llm_lable_select.setText(u"Select model:")

        self.gridLayout.addWidget(self.llm_lable_select, 0, 0, 1, 1)

        self.label = QLabel(Form)
        self.label.setObjectName(u"label")
        self.label.setMaximumSize(QSize(16777215, 20))

        self.gridLayout.addWidget(self.label, 1, 0, 1, 1)

        self.clear_btn_2 = QPushButton(Form)
        self.clear_btn_2.setObjectName(u"clear_btn_2")
        self.clear_btn_2.setMinimumSize(QSize(0, 30))

        self.gridLayout.addWidget(self.clear_btn_2, 1, 3, 1, 1)

        self.enter_btn = QPushButton(Form)
        self.enter_btn.setObjectName(u"enter_btn")
        self.enter_btn.setMinimumSize(QSize(0, 30))

        self.gridLayout.addWidget(self.enter_btn, 0, 3, 1, 1)

        self.llm_comboBox = QComboBox(Form)
        self.llm_comboBox.setObjectName(u"llm_comboBox")
        self.llm_comboBox.setMinimumSize(QSize(100, 20))
        font1 = QFont()
        font1.setPointSize(14)
        self.llm_comboBox.setFont(font1)

        self.gridLayout.addWidget(self.llm_comboBox, 0, 1, 1, 2)


        self.horizontalLayout_2.addLayout(self.gridLayout)


        self.verticalLayout_2.addLayout(self.horizontalLayout_2)

        self.progressBar = QProgressBar(Form)
        self.progressBar.setObjectName(u"progressBar")
        self.progressBar.setValue(24)

        self.verticalLayout_2.addWidget(self.progressBar)


        self.retranslateUi(Form)

        QMetaObject.connectSlotsByName(Form)
    # setupUi

    def retranslateUi(self, Form):
        Form.setWindowTitle(QCoreApplication.translate("Form", u"Form", None))
        self.copy_btn.setText(QCoreApplication.translate("Form", u"copy", None))
        self.clear_btn.setText(QCoreApplication.translate("Form", u"clear", None))
        self.user_input_edit.setPlainText("")
        self.btn_load_file.setText(QCoreApplication.translate("Form", u"Load", None))
        self.btn_rm_file.setText(QCoreApplication.translate("Form", u"Rm", None))
        self.lineEdit.setText(QCoreApplication.translate("Form", u"0", None))
        self.checkBox.setText(QCoreApplication.translate("Form", u"Verbose", None))
        self.label.setText(QCoreApplication.translate("Form", u"Temperature:", None))
        self.clear_btn_2.setText(QCoreApplication.translate("Form", u"clear", None))
        self.enter_btn.setText(QCoreApplication.translate("Form", u" Ask ", None))
    # retranslateUi

