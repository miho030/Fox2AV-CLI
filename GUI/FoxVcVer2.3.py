# -*- coding: utf-8 -*-
# Author : Repubic of Korea, Seoul, JungSan HS  31227 Lee Joon Sung
# youtube : anonymous0korea0@gmail.com ;;;; tayaka
# Email : miho0_0@naver.com

#  구버전 GUI 엔진임.


from PyQt4 import QtCore, QtGui

try:
    _fromUtf8 = QtCore.QString.fromUtf8
except AttributeError:
    def _fromUtf8(s):
        return s

try:
    _encoding = QtGui.QApplication.UnicodeUTF8
    def _translate(context, text, disambig):
        return QtGui.QApplication.translate(context, text, disambig, _encoding)
except AttributeError:
    def _translate(context, text, disambig):
        return QtGui.QApplication.translate(context, text, disambig)

class Ui_FoxVc(object):
    def setupUi(self, FoxVc):
        FoxVc.setObjectName(_fromUtf8("FoxVc"))
        FoxVc.resize(734, 425)
        self.centralwidget = QtGui.QWidget(FoxVc)
        self.centralwidget.setObjectName(_fromUtf8("centralwidget"))
        self.Process = QtGui.QTextEdit(self.centralwidget)
        self.Process.setGeometry(QtCore.QRect(280, 110, 431, 121))
        self.Process.setReadOnly(True)
        self.Process.setObjectName(_fromUtf8("Process"))
        self.InputDirectory = QtGui.QLineEdit(self.centralwidget)
        self.InputDirectory.setGeometry(QtCore.QRect(280, 50, 351, 21))
        self.InputDirectory.setObjectName(_fromUtf8("InputDirectory"))
        self.Logo = QtGui.QLabel(self.centralwidget)
        self.Logo.setGeometry(QtCore.QRect(20, 10, 241, 191))
        self.Logo.setText(_fromUtf8(""))
        self.Logo.setPixmap(QtGui.QPixmap(_fromUtf8("FoxVcICON.jpg")))
        self.Logo.setObjectName(_fromUtf8("Logo"))
        self.SelectDirectory = QtGui.QLabel(self.centralwidget)
        self.SelectDirectory.setGeometry(QtCore.QRect(290, 20, 241, 21))
        self.SelectDirectory.setObjectName(_fromUtf8("SelectDirectory"))
        self.Ok = QtGui.QPushButton(self.centralwidget)
        self.Ok.setGeometry(QtCore.QRect(640, 50, 75, 21))
        self.Ok.setObjectName(_fromUtf8("Ok"))
        self.Author_1 = QtGui.QLabel(self.centralwidget)
        self.Author_1.setGeometry(QtCore.QRect(20, 220, 191, 16))
        self.Author_1.setObjectName(_fromUtf8("Author_1"))
        self.Author_2 = QtGui.QLabel(self.centralwidget)
        self.Author_2.setGeometry(QtCore.QRect(20, 250, 241, 16))
        self.Author_2.setObjectName(_fromUtf8("Author_2"))
        self.rule = QtGui.QLabel(self.centralwidget)
        self.rule.setGeometry(QtCore.QRect(20, 280, 231, 16))
        self.rule.setObjectName(_fromUtf8("rule"))
        self.Indi = QtGui.QLabel(self.centralwidget)
        self.Indi.setGeometry(QtCore.QRect(20, 310, 231, 16))
        self.Indi.setObjectName(_fromUtf8("Indi"))
        self.Youtube = QtGui.QLabel(self.centralwidget)
        self.Youtube.setGeometry(QtCore.QRect(20, 390, 261, 16))
        self.Youtube.setObjectName(_fromUtf8("Youtube"))
        self.Email = QtGui.QLabel(self.centralwidget)
        self.Email.setGeometry(QtCore.QRect(20, 370, 241, 16))
        self.Email.setObjectName(_fromUtf8("Email"))
        self.Cure = QtGui.QTextEdit(self.centralwidget)
        self.Cure.setGeometry(QtCore.QRect(280, 270, 431, 131))
        self.Cure.setReadOnly(True)
        self.Cure.setObjectName(_fromUtf8("Cure"))
        self.ProcessIntro = QtGui.QLabel(self.centralwidget)
        self.ProcessIntro.setGeometry(QtCore.QRect(290, 80, 141, 21))
        self.ProcessIntro.setObjectName(_fromUtf8("ProcessIntro"))
        self.CureIntro = QtGui.QLabel(self.centralwidget)
        self.CureIntro.setGeometry(QtCore.QRect(290, 246, 151, 16))
        self.CureIntro.setObjectName(_fromUtf8("CureIntro"))
        FoxVc.setCentralWidget(self.centralwidget)

        self.retranslateUi(FoxVc)
        QtCore.QMetaObject.connectSlotsByName(FoxVc)

    def retranslateUi(self, FoxVc):
        FoxVc.setWindowTitle(_translate("FoxVc", "Fox-Anti Virus Security Module", None))
        self.SelectDirectory.setText(_translate("FoxVc", "* Select Drive (e.x C or D or C\\Users )", None))
        self.Ok.setText(_translate("FoxVc", "OK", None))
        self.Author_1.setText(_translate("FoxVc", "This program made by nicht,", None))
        self.Author_2.setText(_translate("FoxVc", "Seoul, Jungsan HS, 31227 Lee Joon Sung", None))
        self.rule.setText(_translate("FoxVc", "Program is followed GNU/GPL.Ver 3", None))
        self.Indi.setText(_translate("FoxVc", "Exactly, Author loves Fox.", None))
        self.Youtube.setText(_translate("FoxVc", "YOUTUBE : anonymous0korea0@gmail.com", None))
        self.Email.setText(_translate("FoxVc", "Email : miho0_0@naver.com", None))
        self.ProcessIntro.setText(_translate("FoxVc", "* Process Window *", None))
        self.CureIntro.setText(_translate("FoxVc", "* Cure List Window *", None))


if __name__ == "__main__":
    import sys
    app = QtGui.QApplication(sys.argv)
    FoxVc = QtGui.QMainWindow()
    ui = Ui_FoxVc()
    ui.setupUi(FoxVc)
    FoxVc.show()
    sys.exit(app.exec_())

