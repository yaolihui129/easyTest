# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'D:\pythonScript\PythonWorkspace\easyTest\tool\project\ui_designer\dirCompare.ui'
#
# Created by: PyQt5 UI code generator 5.6
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_Dialog(object):
    def setupUi(self, Dialog):
        Dialog.setObjectName("Dialog")
        Dialog.resize(578, 546)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(Dialog.sizePolicy().hasHeightForWidth())
        Dialog.setSizePolicy(sizePolicy)
        Dialog.setMinimumSize(QtCore.QSize(578, 546))
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap("../icons/cog.ico"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        Dialog.setWindowIcon(icon)
        Dialog.setSizeGripEnabled(True)
        self.gridLayout = QtWidgets.QGridLayout(Dialog)
        self.gridLayout.setObjectName("gridLayout")
        self.groupBox = QtWidgets.QGroupBox(Dialog)
        self.groupBox.setMinimumSize(QtCore.QSize(561, 101))
        self.groupBox.setMaximumSize(QtCore.QSize(16777215, 101))
        self.groupBox.setTitle("")
        self.groupBox.setObjectName("groupBox")
        self.label_result = QtWidgets.QLabel(self.groupBox)
        self.label_result.setGeometry(QtCore.QRect(70, 70, 171, 20))
        self.label_result.setObjectName("label_result")
        self.label = QtWidgets.QLabel(self.groupBox)
        self.label.setGeometry(QtCore.QRect(10, 10, 60, 20))
        self.label.setObjectName("label")
        self.lineEdit_load = QtWidgets.QLineEdit(self.groupBox)
        self.lineEdit_load.setGeometry(QtCore.QRect(70, 40, 400, 20))
        self.lineEdit_load.setReadOnly(True)
        self.lineEdit_load.setObjectName("lineEdit_load")
        self.pushButton_cmp = QtWidgets.QPushButton(self.groupBox)
        self.pushButton_cmp.setGeometry(QtCore.QRect(330, 70, 60, 20))
        self.pushButton_cmp.setObjectName("pushButton_cmp")
        self.pushButton_open1 = QtWidgets.QPushButton(self.groupBox)
        self.pushButton_open1.setGeometry(QtCore.QRect(480, 10, 70, 20))
        self.pushButton_open1.setObjectName("pushButton_open1")
        self.label_2 = QtWidgets.QLabel(self.groupBox)
        self.label_2.setGeometry(QtCore.QRect(10, 40, 60, 20))
        self.label_2.setObjectName("label_2")
        self.label_3 = QtWidgets.QLabel(self.groupBox)
        self.label_3.setGeometry(QtCore.QRect(10, 70, 60, 20))
        self.label_3.setObjectName("label_3")
        self.pushButton_replace = QtWidgets.QPushButton(self.groupBox)
        self.pushButton_replace.setGeometry(QtCore.QRect(400, 70, 60, 20))
        self.pushButton_replace.setObjectName("pushButton_replace")
        self.checkBox_bak = QtWidgets.QCheckBox(self.groupBox)
        self.checkBox_bak.setGeometry(QtCore.QRect(470, 70, 80, 20))
        self.checkBox_bak.setChecked(True)
        self.checkBox_bak.setObjectName("checkBox_bak")
        self.lineEdit_local = QtWidgets.QLineEdit(self.groupBox)
        self.lineEdit_local.setGeometry(QtCore.QRect(70, 10, 400, 20))
        self.lineEdit_local.setReadOnly(True)
        self.lineEdit_local.setObjectName("lineEdit_local")
        self.pushButton_open2 = QtWidgets.QPushButton(self.groupBox)
        self.pushButton_open2.setGeometry(QtCore.QRect(480, 40, 70, 20))
        self.pushButton_open2.setObjectName("pushButton_open2")
        self.pushButton_toggle = QtWidgets.QPushButton(self.groupBox)
        self.pushButton_toggle.setGeometry(QtCore.QRect(250, 70, 70, 20))
        self.pushButton_toggle.setObjectName("pushButton_toggle")
        self.gridLayout.addWidget(self.groupBox, 0, 0, 1, 1)
        self.groupBox_2 = QtWidgets.QGroupBox(Dialog)
        self.groupBox_2.setTitle("")
        self.groupBox_2.setObjectName("groupBox_2")
        self.gridLayout_2 = QtWidgets.QGridLayout(self.groupBox_2)
        self.gridLayout_2.setObjectName("gridLayout_2")
        self.treeWidget_local = QtWidgets.QTreeWidget(self.groupBox_2)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.treeWidget_local.sizePolicy().hasHeightForWidth())
        self.treeWidget_local.setSizePolicy(sizePolicy)
        self.treeWidget_local.setMinimumSize(QtCore.QSize(271, 401))
        self.treeWidget_local.setAutoFillBackground(False)
        self.treeWidget_local.setHorizontalScrollBarPolicy(QtCore.Qt.ScrollBarAsNeeded)
        self.treeWidget_local.setSizeAdjustPolicy(QtWidgets.QAbstractScrollArea.AdjustToContents)
        self.treeWidget_local.setTextElideMode(QtCore.Qt.ElideNone)
        self.treeWidget_local.setHorizontalScrollMode(QtWidgets.QAbstractItemView.ScrollPerItem)
        self.treeWidget_local.setExpandsOnDoubleClick(False)
        self.treeWidget_local.setObjectName("treeWidget_local")
        self.treeWidget_local.headerItem().setBackground(0, QtGui.QColor(0, 170, 127))
        self.gridLayout_2.addWidget(self.treeWidget_local, 0, 0, 1, 1)
        self.treeWidget_load = QtWidgets.QTreeWidget(self.groupBox_2)
        self.treeWidget_load.setMinimumSize(QtCore.QSize(271, 401))
        self.treeWidget_load.setMaximumSize(QtCore.QSize(16777215, 16777215))
        self.treeWidget_load.setHorizontalScrollBarPolicy(QtCore.Qt.ScrollBarAsNeeded)
        self.treeWidget_load.setExpandsOnDoubleClick(False)
        self.treeWidget_load.setObjectName("treeWidget_load")
        self.treeWidget_load.headerItem().setText(0, "下载文件夹")
        self.gridLayout_2.addWidget(self.treeWidget_load, 0, 1, 1, 1)
        self.gridLayout.addWidget(self.groupBox_2, 1, 0, 1, 1)

        self.retranslateUi(Dialog)
        QtCore.QMetaObject.connectSlotsByName(Dialog)

    def retranslateUi(self, Dialog):
        _translate = QtCore.QCoreApplication.translate
        Dialog.setWindowTitle(_translate("Dialog", "目录对比"))
        self.label_result.setText(_translate("Dialog", "???"))
        self.label.setText(_translate("Dialog", "本地目录"))
        self.pushButton_cmp.setText(_translate("Dialog", "对比"))
        self.pushButton_open1.setText(_translate("Dialog", "打开..."))
        self.label_2.setText(_translate("Dialog", "下载目录"))
        self.label_3.setText(_translate("Dialog", "结   果"))
        self.pushButton_replace.setText(_translate("Dialog", "替换"))
        self.checkBox_bak.setText(_translate("Dialog", "替换前备份"))
        self.pushButton_open2.setText(_translate("Dialog", "打开..."))
        self.pushButton_toggle.setText(_translate("Dialog", "展开/收起"))
        self.treeWidget_local.headerItem().setText(0, _translate("Dialog", "本地文件夹"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Dialog = QtWidgets.QDialog()
    ui = Ui_Dialog()
    ui.setupUi(Dialog)
    Dialog.show()
    sys.exit(app.exec_())
