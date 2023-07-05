# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'DialogForm.ui'
#
# Created by: PyQt5 UI code generator 5.15.7
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_Dialog(object):
    def setupUi(self, Dialog):
        Dialog.setObjectName("Dialog")
        Dialog.resize(418, 508)
        Dialog.setStyleSheet("background-color: qlineargradient(spread:pad, x1:0, y1:0, x2:1, y2:1,\n"
"  stop:0 #4158D0,\n"
"  stop:0.46 #C850C0,\n"
"  stop:1 #4B1061);\n"
"\n"
"font-family:Cambria\n"
"\n"
"")
        self.verticalLayout_3 = QtWidgets.QVBoxLayout(Dialog)
        self.verticalLayout_3.setObjectName("verticalLayout_3")
        self.frame = QtWidgets.QFrame(Dialog)
        self.frame.setStyleSheet("background-color:rgba(255,255,255,70);\n"
"border: 1px solid rgba(255,255,255,40);\n"
"border-radius: 7px;")
        self.frame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame.setObjectName("frame")
        self.verticalLayout_2 = QtWidgets.QVBoxLayout(self.frame)
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.verticalLayout = QtWidgets.QVBoxLayout()
        self.verticalLayout.setContentsMargins(25, 25, 25, 25)
        self.verticalLayout.setSpacing(25)
        self.verticalLayout.setObjectName("verticalLayout")
        self.label = QtWidgets.QLabel(self.frame)
        self.label.setMaximumSize(QtCore.QSize(16777215, 16777215))
        self.label.setStyleSheet("color:white;\n"
"font-weight:bold;\n"
"font-size:20pt;\n"
"background-color:none;\n"
"border:none")
        self.label.setAlignment(QtCore.Qt.AlignCenter)
        self.label.setObjectName("label")
        self.verticalLayout.addWidget(self.label)
        self.cb_category = QtWidgets.QComboBox(self.frame)
        self.cb_category.setStyleSheet("QComboBox{\n"
"font-size:16pt;\n"
"color:white;\n"
"\n"
"}\n"
"QComboBox:item{\n"
"color:white;\n"
"font-size:14pt;\n"
"\n"
"}")
        self.cb_category.setObjectName("cb_category")
        self.cb_category.addItem("")
        self.cb_category.addItem("")
        self.cb_category.addItem("")
        self.cb_category.addItem("")
        self.cb_category.addItem("")
        self.cb_category.addItem("")
        self.cb_category.addItem("")
        self.verticalLayout.addWidget(self.cb_category)
        self.date = QtWidgets.QDateEdit(self.frame)
        self.date.setStyleSheet("font-size:16pt;\n"
"color:white;\n"
"padding-left: 10px;")
        self.date.setButtonSymbols(QtWidgets.QAbstractSpinBox.NoButtons)
        self.date.setDate(QtCore.QDate(2023, 1, 1))
        self.date.setObjectName("date")
        self.verticalLayout.addWidget(self.date)
        self.le_description = QtWidgets.QLineEdit(self.frame)
        self.le_description.setStyleSheet("font-size:16pt;\n"
"color:white;\n"
"padding-left:10px;")
        self.le_description.setObjectName("le_description")
        self.verticalLayout.addWidget(self.le_description)
        self.le_balance = QtWidgets.QLineEdit(self.frame)
        self.le_balance.setStyleSheet("font-size:16pt;\n"
"color:white;\n"
"padding-left:10px;")
        self.le_balance.setObjectName("le_balance")
        self.verticalLayout.addWidget(self.le_balance)
        self.cb_typebudget = QtWidgets.QComboBox(self.frame)
        self.cb_typebudget.setStyleSheet("QComboBox{\n"
"font-size:16pt;\n"
"color:white;\n"
"\n"
"}\n"
"QComboBox:item{\n"
"color:white;\n"
"font-size:14pt;\n"
"\n"
"}")
        self.cb_typebudget.setObjectName("cb_typebudget")
        self.cb_typebudget.addItem("")
        self.cb_typebudget.addItem("")
        self.verticalLayout.addWidget(self.cb_typebudget)
        self.btn_transaction = QtWidgets.QPushButton(self.frame)
        self.btn_transaction.setStyleSheet("QPushButton {\n"
"font-size:22px;\n"
"color: white;\n"
"background-color:rgba(255,255,255,30);\n"
"border: 1px solid rgba(255,255,255,40);\n"
"border-radius:7px;\n"
"width:230px;\n"
"height:50px\n"
"}    \n"
"QPushButton::hover{\n"
"background-color:rgba(255,255,255,50);\n"
"}\n"
"\n"
"QPushButton::pressed{\n"
"background-color:rgba(255,255,255,70);\n"
"}\n"
"")
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap(":/newPrefix/icons8-accept-48.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.btn_transaction.setIcon(icon)
        self.btn_transaction.setIconSize(QtCore.QSize(30, 30))
        self.btn_transaction.setObjectName("btn_transaction")
        self.verticalLayout.addWidget(self.btn_transaction)
        self.verticalLayout_2.addLayout(self.verticalLayout)
        self.verticalLayout_3.addWidget(self.frame)

        self.retranslateUi(Dialog)
        self.cb_category.setCurrentIndex(0)
        QtCore.QMetaObject.connectSlotsByName(Dialog)

    def retranslateUi(self, Dialog):
        _translate = QtCore.QCoreApplication.translate
        Dialog.setWindowTitle(_translate("Dialog", "Dialog"))
        self.label.setText(_translate("Dialog", "Новый заказ"))
        self.cb_category.setItemText(0, _translate("Dialog", "Спецодежда"))
        self.cb_category.setItemText(1, _translate("Dialog", "Спецобувь"))
        self.cb_category.setItemText(2, _translate("Dialog", "Средства защиты"))
        self.cb_category.setItemText(3, _translate("Dialog", "Защита рук"))
        self.cb_category.setItemText(4, _translate("Dialog", "Вендинг"))
        self.cb_category.setItemText(5, _translate("Dialog", "Экзоскелеты"))
        self.cb_category.setItemText(6, _translate("Dialog", "Другое"))
        self.le_description.setPlaceholderText(_translate("Dialog", "Описание"))
        self.le_balance.setPlaceholderText(_translate("Dialog", "Сумма"))
        self.cb_typebudget.setItemText(0, _translate("Dialog", "Доход"))
        self.cb_typebudget.setItemText(1, _translate("Dialog", "Расход"))
        self.btn_transaction.setText(_translate("Dialog", "Сохранить заказ"))
import IconsPackage_rc
