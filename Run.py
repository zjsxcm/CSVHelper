import sys
from UI import Ui_Window
from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import QMessageBox

class MyWindow(QtWidgets.QWidget, Ui_Window.Ui_Dialog):
    def __init__(self):
        super(MyWindow, self).__init__()
        self._translate = QtCore.QCoreApplication.translate
        self.window = Ui_Window.Ui_Dialog()
        self.window.setupUi(self)
        self.connect = None
        
    # 链接状态
    def _switchConnectStatus(self, on):
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap("UI/Res/connected.png" if on else "UI/Res/unconnect.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.status.setIcon(icon)

    # 创建一条Mail
    def _createMailItem(self, info):
        item = QtWidgets.QListWidgetItem()
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap("UI/Res/read.png" if info["Read"] else "UI/Res/unread.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        item.setIcon(icon)
        title = info["Title"]
        item.setText(self._translate("Dialog", title))
        item.setToolTip(self._translate("Dialog", "<html><head/><body><p>{0}</p></body></html>".format(title)))
        return item
    
    # 刷新MailList
    def RefreshMailList(self, infos):
        self.mailList.clear()
        mailItems = []
        for info in infos:
            mailItems.append(self._createMailItem(info))
        self.mailList.addItems(mailItems)

    def m_connect(self):
        
        print("m_connect")
    
    def m_showMail(self):
        if self.connect is None:
            QMessageBox.information(self, "Warning!", "尚未登录邮箱", QMessageBox.Yes)
        else:
            print("m_showMail")

    def m_refreshMails(self):
        if self.connect is None:
            QMessageBox.information(self, "Warning!", "尚未登录邮箱", QMessageBox.Yes)
        else:
            print("m_refreshMails")

    def m_execute(self):
        if self.connect is None:
            QMessageBox.information(self, "Warning!", "尚未登录邮箱", QMessageBox.Yes)
        else:
            print("m_execute")
    
    ### 乱七八糟 好像没有的函数
    def setSizeGripEnabled(self, enable):
        pass
    def setModal(self, enable):
        pass
    ###

if __name__=="__main__":
    app = QtWidgets.QApplication(sys.argv)
    win = MyWindow()
    win.show()
    sys.exit(app.exec_())
