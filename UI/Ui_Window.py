# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'd:\Workspace\Python\CSVHelper\UI\Window.ui'
#
# Created by: PyQt5 UI code generator 5.11.3
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_Dialog(object):
    def setupUi(self, Dialog):
        Dialog.setObjectName("Dialog")
        Dialog.setWindowModality(QtCore.Qt.NonModal)
        Dialog.resize(838, 574)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Minimum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(Dialog.sizePolicy().hasHeightForWidth())
        Dialog.setSizePolicy(sizePolicy)
        Dialog.setMinimumSize(QtCore.QSize(838, 574))
        Dialog.setMaximumSize(QtCore.QSize(838, 574))
        Dialog.setCursor(QtGui.QCursor(QtCore.Qt.ArrowCursor))
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap(":/icons/csv.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        Dialog.setWindowIcon(icon)
        Dialog.setSizeGripEnabled(False)
        Dialog.setModal(False)
        self.mailList = QtWidgets.QListWidget(Dialog)
        self.mailList.setGeometry(QtCore.QRect(10, 140, 351, 251))
        self.mailList.setHorizontalScrollBarPolicy(QtCore.Qt.ScrollBarAlwaysOff)
        self.mailList.setEditTriggers(QtWidgets.QAbstractItemView.SelectedClicked)
        self.mailList.setObjectName("mailList")
        item = QtWidgets.QListWidgetItem()
        icon1 = QtGui.QIcon()
        icon1.addPixmap(QtGui.QPixmap(":/icons/unread.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        item.setIcon(icon1)
        self.mailList.addItem(item)
        self.sender = QtWidgets.QTextBrowser(Dialog)
        self.sender.setGeometry(QtCore.QRect(440, 230, 391, 61))
        font = QtGui.QFont()
        font.setFamily("Microsoft YaHei UI")
        font.setPointSize(12)
        self.sender.setFont(font)
        self.sender.setInputMethodHints(QtCore.Qt.ImhNone)
        self.sender.setVerticalScrollBarPolicy(QtCore.Qt.ScrollBarAlwaysOff)
        self.sender.setHorizontalScrollBarPolicy(QtCore.Qt.ScrollBarAlwaysOff)
        self.sender.setObjectName("sender")
        self.senderTitle = QtWidgets.QLabel(Dialog)
        self.senderTitle.setGeometry(QtCore.QRect(370, 240, 61, 31))
        self.senderTitle.setObjectName("senderTitle")
        self.titleTitle = QtWidgets.QLabel(Dialog)
        self.titleTitle.setGeometry(QtCore.QRect(390, 140, 41, 31))
        self.titleTitle.setObjectName("titleTitle")
        self.title = QtWidgets.QTextBrowser(Dialog)
        self.title.setGeometry(QtCore.QRect(440, 140, 391, 71))
        font = QtGui.QFont()
        font.setFamily("宋体")
        font.setPointSize(11)
        self.title.setFont(font)
        self.title.setVerticalScrollBarPolicy(QtCore.Qt.ScrollBarAsNeeded)
        self.title.setHorizontalScrollBarPolicy(QtCore.Qt.ScrollBarAlwaysOff)
        self.title.setObjectName("title")
        self.attachmentTitle = QtWidgets.QLabel(Dialog)
        self.attachmentTitle.setGeometry(QtCore.QRect(390, 320, 41, 31))
        self.attachmentTitle.setObjectName("attachmentTitle")
        self.regex = QtWidgets.QTextEdit(Dialog)
        self.regex.setGeometry(QtCore.QRect(100, 410, 731, 41))
        self.regex.setTabChangesFocus(True)
        self.regex.setObjectName("regex")
        self.regexTitle = QtWidgets.QLabel(Dialog)
        self.regexTitle.setGeometry(QtCore.QRect(10, 420, 81, 31))
        self.regexTitle.setObjectName("regexTitle")
        self.sendTo = QtWidgets.QTextEdit(Dialog)
        self.sendTo.setGeometry(QtCore.QRect(100, 470, 731, 41))
        self.sendTo.setTabChangesFocus(True)
        self.sendTo.setObjectName("sendTo")
        self.sendToTitle = QtWidgets.QLabel(Dialog)
        self.sendToTitle.setGeometry(QtCore.QRect(10, 480, 81, 31))
        self.sendToTitle.setObjectName("sendToTitle")
        self.apply = QtWidgets.QPushButton(Dialog)
        self.apply.setGeometry(QtCore.QRect(740, 530, 93, 28))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(10)
        self.apply.setFont(font)
        self.apply.setObjectName("apply")
        self.protocolTitle = QtWidgets.QLabel(Dialog)
        self.protocolTitle.setGeometry(QtCore.QRect(10, 20, 61, 31))
        self.protocolTitle.setObjectName("protocolTitle")
        self.accountTitle = QtWidgets.QLabel(Dialog)
        self.accountTitle.setGeometry(QtCore.QRect(10, 60, 61, 31))
        self.accountTitle.setObjectName("accountTitle")
        self.passwordTitle = QtWidgets.QLabel(Dialog)
        self.passwordTitle.setGeometry(QtCore.QRect(440, 60, 61, 31))
        self.passwordTitle.setObjectName("passwordTitle")
        self.protocol = QtWidgets.QComboBox(Dialog)
        self.protocol.setGeometry(QtCore.QRect(80, 20, 71, 31))
        self.protocol.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.protocol.setObjectName("protocol")
        self.protocol.addItem("")
        self.protocol.addItem("")
        self.address = QtWidgets.QTextEdit(Dialog)
        self.address.setGeometry(QtCore.QRect(200, 20, 451, 31))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.address.setFont(font)
        self.address.setTabletTracking(False)
        self.address.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.address.setAutoFillBackground(False)
        self.address.setStyleSheet("")
        self.address.setInputMethodHints(QtCore.Qt.ImhNone)
        self.address.setVerticalScrollBarPolicy(QtCore.Qt.ScrollBarAlwaysOff)
        self.address.setHorizontalScrollBarPolicy(QtCore.Qt.ScrollBarAlwaysOff)
        self.address.setTabChangesFocus(True)
        self.address.setLineWrapMode(QtWidgets.QTextEdit.NoWrap)
        self.address.setLineWrapColumnOrWidth(0)
        self.address.setAcceptRichText(False)
        self.address.setObjectName("address")
        self.account = QtWidgets.QTextEdit(Dialog)
        self.account.setGeometry(QtCore.QRect(70, 60, 351, 31))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.account.setFont(font)
        self.account.setTabletTracking(False)
        self.account.setInputMethodHints(QtCore.Qt.ImhNone)
        self.account.setVerticalScrollBarPolicy(QtCore.Qt.ScrollBarAlwaysOff)
        self.account.setHorizontalScrollBarPolicy(QtCore.Qt.ScrollBarAlwaysOff)
        self.account.setTabChangesFocus(True)
        self.account.setLineWrapMode(QtWidgets.QTextEdit.NoWrap)
        self.account.setAcceptRichText(False)
        self.account.setObjectName("account")
        self.password = QtWidgets.QTextEdit(Dialog)
        self.password.setGeometry(QtCore.QRect(490, 60, 201, 31))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.password.setFont(font)
        self.password.setTabletTracking(False)
        self.password.setInputMethodHints(QtCore.Qt.ImhHiddenText|QtCore.Qt.ImhSensitiveData)
        self.password.setVerticalScrollBarPolicy(QtCore.Qt.ScrollBarAlwaysOff)
        self.password.setHorizontalScrollBarPolicy(QtCore.Qt.ScrollBarAlwaysOff)
        self.password.setTabChangesFocus(True)
        self.password.setLineWrapMode(QtWidgets.QTextEdit.NoWrap)
        self.password.setAcceptRichText(False)
        self.password.setObjectName("password")
        self.login = QtWidgets.QPushButton(Dialog)
        self.login.setGeometry(QtCore.QRect(700, 60, 81, 31))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(10)
        self.login.setFont(font)
        self.login.setCheckable(False)
        self.login.setChecked(False)
        self.login.setAutoRepeat(False)
        self.login.setAutoExclusive(False)
        self.login.setObjectName("login")
        self.refresh = QtWidgets.QPushButton(Dialog)
        self.refresh.setGeometry(QtCore.QRect(280, 100, 81, 31))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(10)
        self.refresh.setFont(font)
        self.refresh.setObjectName("refresh")
        self.mailListTitle = QtWidgets.QLabel(Dialog)
        self.mailListTitle.setGeometry(QtCore.QRect(10, 100, 81, 31))
        self.mailListTitle.setObjectName("mailListTitle")
        self.status = QtWidgets.QPushButton(Dialog)
        self.status.setEnabled(True)
        self.status.setGeometry(QtCore.QRect(715, 5, 51, 51))
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.status.sizePolicy().hasHeightForWidth())
        self.status.setSizePolicy(sizePolicy)
        self.status.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.status.setMouseTracking(False)
        self.status.setTabletTracking(False)
        self.status.setFocusPolicy(QtCore.Qt.NoFocus)
        self.status.setContextMenuPolicy(QtCore.Qt.NoContextMenu)
        self.status.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.status.setAutoFillBackground(True)
        self.status.setText("")
        icon2 = QtGui.QIcon()
        icon2.addPixmap(QtGui.QPixmap(":/icons/unconnect.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.status.setIcon(icon2)
        self.status.setIconSize(QtCore.QSize(40, 40))
        self.status.setAutoRepeat(False)
        self.status.setAutoDefault(False)
        self.status.setDefault(False)
        self.status.setObjectName("status")
        self.mailNumTitle = QtWidgets.QLabel(Dialog)
        self.mailNumTitle.setGeometry(QtCore.QRect(120, 105, 41, 21))
        self.mailNumTitle.setObjectName("mailNumTitle")
        self.mailNum = QtWidgets.QSpinBox(Dialog)
        self.mailNum.setGeometry(QtCore.QRect(170, 104, 46, 22))
        self.mailNum.setPrefix("")
        self.mailNum.setProperty("value", 10)
        self.mailNum.setDisplayIntegerBase(10)
        self.mailNum.setObjectName("mailNum")
        self.attachment = QtWidgets.QListWidget(Dialog)
        self.attachment.setGeometry(QtCore.QRect(440, 310, 391, 81))
        self.attachment.setHorizontalScrollBarPolicy(QtCore.Qt.ScrollBarAlwaysOff)
        self.attachment.setEditTriggers(QtWidgets.QAbstractItemView.SelectedClicked)
        self.attachment.setObjectName("attachment")
        item = QtWidgets.QListWidgetItem()
        icon3 = QtGui.QIcon()
        icon3.addPixmap(QtGui.QPixmap("Res/csv.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        item.setIcon(icon3)
        self.attachment.addItem(item)

        self.retranslateUi(Dialog)
        self.login.clicked.connect(Dialog.m_connect)
        self.mailList.itemSelectionChanged.connect(Dialog.m_showMail)
        self.refresh.clicked.connect(Dialog.m_refreshMails)
        self.apply.clicked.connect(Dialog.m_execute)
        QtCore.QMetaObject.connectSlotsByName(Dialog)

    def retranslateUi(self, Dialog):
        _translate = QtCore.QCoreApplication.translate
        Dialog.setWindowTitle(_translate("Dialog", "CSVHelper"))
        __sortingEnabled = self.mailList.isSortingEnabled()
        self.mailList.setSortingEnabled(False)
        item = self.mailList.item(0)
        item.setText(_translate("Dialog", "Empty"))
        item.setToolTip(_translate("Dialog", "<html><head/><body><p>total mail title</p></body></html>"))
        self.mailList.setSortingEnabled(__sortingEnabled)
        self.senderTitle.setText(_translate("Dialog", "<html><head/><body><p><span style=\" font-size:12pt;\">发件人</span></p></body></html>"))
        self.titleTitle.setText(_translate("Dialog", "<html><head/><body><p><span style=\" font-size:12pt;\">标题</span></p></body></html>"))
        self.title.setHtml(_translate("Dialog", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'宋体\'; font-size:11pt; font-weight:400; font-style:normal;\">\n"
"<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><br /></p></body></html>"))
        self.attachmentTitle.setText(_translate("Dialog", "<html><head/><body><p><span style=\" font-size:12pt;\">附件</span></p></body></html>"))
        self.regexTitle.setText(_translate("Dialog", "<html><head/><body><p><span style=\" font-size:12pt;\">转化公式</span></p></body></html>"))
        self.sendToTitle.setText(_translate("Dialog", "<html><head/><body><p><span style=\" font-size:12pt;\">发送目标</span></p></body></html>"))
        self.apply.setText(_translate("Dialog", "执行"))
        self.protocolTitle.setText(_translate("Dialog", "<html><head/><body><p><span style=\" font-size:12pt;\">协议</span></p></body></html>"))
        self.accountTitle.setText(_translate("Dialog", "<html><head/><body><p><span style=\" font-size:12pt;\">账户</span></p></body></html>"))
        self.passwordTitle.setText(_translate("Dialog", "<html><head/><body><p><span style=\" font-size:12pt;\">密码</span></p></body></html>"))
        self.protocol.setItemText(0, _translate("Dialog", "pop3"))
        self.protocol.setItemText(1, _translate("Dialog", "imap"))
        self.login.setText(_translate("Dialog", "连接"))
        self.refresh.setText(_translate("Dialog", "刷新"))
        self.refresh.setShortcut(_translate("Dialog", "F5"))
        self.mailListTitle.setText(_translate("Dialog", "<html><head/><body><p><span style=\" font-size:12pt;\">邮件列表</span></p></body></html>"))
        self.mailNumTitle.setText(_translate("Dialog", "<html><head/><body><p><span style=\" font-size:10pt;\">最近:</span></p></body></html>"))
        __sortingEnabled = self.attachment.isSortingEnabled()
        self.attachment.setSortingEnabled(False)
        item = self.attachment.item(0)
        item.setText(_translate("Dialog", "Empty"))
        item.setToolTip(_translate("Dialog", "<html><head/><body><p>total attachment name</p></body></html>"))
        self.attachment.setSortingEnabled(__sortingEnabled)

import window_rc
