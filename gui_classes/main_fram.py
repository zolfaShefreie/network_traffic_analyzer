
from PyQt5 import QtCore, QtGui, QtWidgets
from .list_widget import CustomList


class Ui_Form(object):
    def setupUi(self, Form):
        Form.setObjectName("Form")
        Form.resize(764, 536)
        Form.setStyleSheet("background-color: rgb(29, 45, 80);")

        self.tabWidget = QtWidgets.QTabWidget(Form)
        self.tabWidget.setGeometry(QtCore.QRect(0, 20, 781, 531))
        self.tabWidget.setObjectName("tabWidget")
        self.tab = QtWidgets.QWidget()
        self.tab.setObjectName("tab")
        self.tabWidget.setStyleSheet("background-color: rgb(29, 45, 80);\n"
        "selection-background-color: rgb(29, 45, 80);\n"
        "selection-color: rgb(29, 45, 80);\n"
        "color: rgb(29, 45, 80);")

        self.stackedWidget = QtWidgets.QStackedWidget(self.tab)
        self.stackedWidget.setGeometry(QtCore.QRect(0, 0, 381, 511))
        self.stackedWidget.setStyleSheet("background-color: rgb(29, 45, 80);")
        self.stackedWidget.setObjectName("stackedWidget")

        self.page = QtWidgets.QWidget()
        self.page.setObjectName("page")

        # initial img
        # self.img_net = QtWidgets.QLabel(self.page)
        # self.img_net.setGeometry(QtCore.QRect(80, 60, 221, 181))
        # self.img_net.setStyleSheet("background-color: rgb(29, 45, 80);")
        # self.img_net.setText("")
        # self.img_net.setObjectName("img_net")

        #initial less btn
        self.less_net = QtWidgets.QToolButton(self.page)
        self.less_net.setGeometry(QtCore.QRect(30, 250, 31, 31))
        self.less_net.setStyleSheet("background-color: rgb(29, 45, 80);")
        self.less_net.setObjectName("less_net")
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap("gui_classes/icon/back.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.less_net.setIcon(icon)
        self.less_net.setIconSize(QtCore.QSize(30, 30))

        #initial more btn
        self.more_net = QtWidgets.QToolButton(self.page)
        self.more_net.setGeometry(QtCore.QRect(320, 250, 31, 31))
        self.more_net.setStyleSheet("background-color: rgb(29, 45, 80);")
        self.more_net.setObjectName("more_net")
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap("gui_classes/icon/next.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.more_net.setIcon(icon)
        self.more_net.setIconSize(QtCore.QSize(30, 30))

        #initial total packets label
        self.packets_net = QtWidgets.QLabel(self.page)
        self.packets_net.setGeometry(QtCore.QRect(50, 140, 131, 31))
        self.packets_net.setObjectName("packets_net")
        self.packets_net.setStyleSheet("color: rgb(252, 218, 183);\n"
        "font: 10pt \"MV Boli\";")
        self.packets_net.setAlignment(QtCore.Qt.AlignCenter)

        self.label_6 = QtWidgets.QLabel(self.page)
        self.label_6.setGeometry(QtCore.QRect(50, 170, 131, 51))
        self.label_6.setStyleSheet("color: rgb(252, 218, 183);\n"
        "font: 10pt \"MV Boli\";")
        self.label_6.setObjectName("label_6")
        self.label_13 = QtWidgets.QLabel(self.page)
        self.label_13.setGeometry(QtCore.QRect(200, 170, 131, 51))
        self.label_13.setStyleSheet("color: rgb(252, 218, 183);\n"
        "font: 10pt \"MV Boli\";")
        self.label_13.setObjectName("label_13")

        #initial avg size of packets label
        self.avg_size_net = QtWidgets.QLabel(self.page)
        self.avg_size_net.setGeometry(QtCore.QRect(200, 140, 131, 31))
        self.avg_size_net.setObjectName("avg_size_net")
        self.avg_size_net.setStyleSheet("color: rgb(252, 218, 183);\n"
        "font: 10pt \"MV Boli\";") 
        self.avg_size_net.setAlignment(QtCore.Qt.AlignCenter) 

        self.label_10 = QtWidgets.QLabel(self.page)
        self.label_10.setGeometry(QtCore.QRect(50, 330, 131, 51))
        self.label_10.setStyleSheet("color: rgb(252, 218, 183);\n"
        "font: 10pt \"MV Boli\";")
        self.label_10.setObjectName("label_10")

        #initial min size of packets label
        self.min_size_net = QtWidgets.QLabel(self.page)
        self.min_size_net.setGeometry(QtCore.QRect(50, 300, 131, 31))
        self.min_size_net.setObjectName("min_size_net")
        self.min_size_net.setStyleSheet("color: rgb(252, 218, 183);\n"
        "font: 10pt \"MV Boli\";")
        self.min_size_net.setAlignment(QtCore.Qt.AlignCenter)

        self.label_14 = QtWidgets.QLabel(self.page)
        self.label_14.setGeometry(QtCore.QRect(200, 330, 131, 51))
        self.label_14.setStyleSheet("color: rgb(252, 218, 183);\n"
        "font: 10pt \"MV Boli\";")
        self.label_14.setObjectName("label_14")

        #initial max size of packets label
        self.max_size_net = QtWidgets.QLabel(self.page)
        self.max_size_net.setGeometry(QtCore.QRect(200, 300, 131, 31))
        self.max_size_net.setObjectName("max_size_net")
        self.max_size_net.setStyleSheet("color: rgb(252, 218, 183);\n"
        "font: 10pt \"MV Boli\";")
        self.max_size_net.setAlignment(QtCore.Qt.AlignCenter)

        self.label_2 = QtWidgets.QLabel(self.page)
        self.label_2.setGeometry(QtCore.QRect(80, 10, 221, 41))
        self.label_2.setObjectName("label_2")
        self.label_2.setStyleSheet("color: rgb(252, 218, 183);\n"
        "font: 8pt \"MV Boli\";")
        self.stackedWidget.addWidget(self.page)
        self.page_2 = QtWidgets.QWidget()
        self.page_2.setObjectName("page_2")

        self.label_4 = QtWidgets.QLabel(self.page_2)
        self.label_4.setGeometry(QtCore.QRect(10, 0, 151, 21))
        self.label_4.setStyleSheet("color: rgb(252, 218, 183);\n"
        "font: 11pt \"MV Boli\";")
        self.label_4.setObjectName("label_4")
        #black the port initial
        # self.black_app = QtWidgets.QPushButton(self.page_2)
        # self.black_app.setGeometry(QtCore.QRect(0, 470, 381, 21))
        # self.black_app.setObjectName("black_app")
        # self.black_app.setStyleSheet("background-color: rgb(19, 59, 92);\n"
        # "color: rgb(252, 218, 183);")

        #list with more detail proto
        self.list_app = CustomList(self.page_2)
        self.list_app.setGeometry(QtCore.QRect(0, 30, 381, 471))
        self.list_app.setObjectName("list_app")
        self.list_app.set_background_color('rgb(30, 95, 116)')

        self.stackedWidget.addWidget(self.page_2)
        self.page_5 = QtWidgets.QWidget()
        self.page_5.setObjectName("page_5")

        #list with more detail dest port
        self.list_app_2 = CustomList(self.page_5)
        self.list_app_2.setGeometry(QtCore.QRect(0, 30, 381, 471))
        self.list_app_2.set_background_color('rgb(30, 95, 116)')
        self.list_app_2.setObjectName("list_app_2")
        

        self.label_5 = QtWidgets.QLabel(self.page_5)
        self.label_5.setGeometry(QtCore.QRect(10, 0, 151, 21))
        self.label_5.setStyleSheet("color: rgb(252, 218, 183);\n"
"font: 11pt \"MV Boli\";")
        self.label_5.setObjectName("label_5")
        self.stackedWidget.addWidget(self.page_5)
        self.page_6 = QtWidgets.QWidget()
        self.page_6.setObjectName("page_6")
        self.label_7 = QtWidgets.QLabel(self.page_6)
        self.label_7.setGeometry(QtCore.QRect(10, 0, 151, 21))
        self.label_7.setStyleSheet("color: rgb(252, 218, 183);\n"
"font: 11pt \"MV Boli\";")
        self.label_7.setObjectName("label_7")

        #list with more detail src port
        self.list_app_3 = CustomList(self.page_6)
        self.list_app_3.setGeometry(QtCore.QRect(0, 30, 381, 471))
        self.list_app_3.set_background_color('rgb(30, 95, 116)')
        self.list_app_3.setObjectName("list_app_3")

        self.stackedWidget.addWidget(self.page_6)
        
        self.stackedWidget_2 = QtWidgets.QStackedWidget(self.tab)
        self.stackedWidget_2.setGeometry(QtCore.QRect(380, 0, 381, 511))
        self.stackedWidget_2.setStyleSheet("background-color: rgb(29, 45, 80);")
        self.stackedWidget_2.setObjectName("stackedWidget_2")
        self.page_3 = QtWidgets.QWidget()
        self.page_3.setObjectName("page_3")

        #initial more btn
        self.more_app = QtWidgets.QToolButton(self.page_3)
        self.more_app.setGeometry(QtCore.QRect(30, 250, 31, 31))
        self.more_app.setStyleSheet("background-color: rgb(29, 45, 80);")
        self.more_app.setObjectName("more_app")
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap("gui_classes/icon/back.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.more_app.setIcon(icon)
        self.more_app.setIconSize(QtCore.QSize(30, 30))

        #initial less btn
        self.less_app = QtWidgets.QToolButton(self.page_3)
        self.less_app.setGeometry(QtCore.QRect(320, 250, 31, 31))
        self.less_app.setStyleSheet("background-color: rgb(29, 45, 80);")
        self.less_app.setObjectName("less_app")
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap("gui_classes/icon/next.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.less_app.setIcon(icon)
        self.less_app.setIconSize(QtCore.QSize(30, 30))

        self.label_11 = QtWidgets.QLabel(self.page_3)
        self.label_11.setGeometry(QtCore.QRect(50, 170, 131, 51))
        self.label_11.setStyleSheet("color: rgb(252, 218, 183);\n"
        "font: 10pt \"MV Boli\";")
        self.label_11.setObjectName("label_11")

        #initial total packets label
        self.packets_app = QtWidgets.QLabel(self.page_3)
        self.packets_app.setGeometry(QtCore.QRect(50, 140, 131, 31))
        self.packets_app.setObjectName("packets_app")
        self.packets_app.setStyleSheet("color: rgb(252, 218, 183);\n"
        "font: 10pt \"MV Boli\";")
        self.packets_app.setAlignment(QtCore.Qt.AlignCenter)

        self.label_15 = QtWidgets.QLabel(self.page_3)
        self.label_15.setGeometry(QtCore.QRect(200, 170, 131, 51))
        self.label_15.setStyleSheet("color: rgb(252, 218, 183);\n"
        "font: 10pt \"MV Boli\";")
        self.label_15.setObjectName("label_15")

        #initial avg size of packets label
        self.avg_size_app = QtWidgets.QLabel(self.page_3)
        self.avg_size_app.setGeometry(QtCore.QRect(200, 140, 131, 31))
        self.avg_size_app.setStyleSheet("color: rgb(252, 218, 183);\n"
        "font: 10pt \"MV Boli\";")
        self.avg_size_app.setObjectName("avg_size_app")
        self.avg_size_app.setAlignment(QtCore.Qt.AlignCenter)

        self.label_17 = QtWidgets.QLabel(self.page_3)
        self.label_17.setGeometry(QtCore.QRect(50, 330, 131, 51))
        self.label_17.setStyleSheet("color: rgb(252, 218, 183);\n"
        "font: 10pt \"MV Boli\";")
        self.label_17.setObjectName("label_17")
        self.label_18 = QtWidgets.QLabel(self.page_3)
        self.label_18.setGeometry(QtCore.QRect(200, 330, 131, 51))
        self.label_18.setStyleSheet("color: rgb(252, 218, 183);\n"
        "font: 10pt \"MV Boli\";")
        self.label_18.setObjectName("label_18")

        #initial min size of packets label
        self.min_size_app = QtWidgets.QLabel(self.page_3)
        self.min_size_app.setGeometry(QtCore.QRect(50, 300, 131, 31))
        self.min_size_app.setStyleSheet("color: rgb(252, 218, 183);\n"
        "font: 10pt \"MV Boli\";")
        self.min_size_app.setObjectName("min_size_app")
        self.min_size_app.setAlignment(QtCore.Qt.AlignCenter)

        #initial max size of packets label
        self.max_size_app = QtWidgets.QLabel(self.page_3)
        self.max_size_app.setGeometry(QtCore.QRect(200, 300, 131, 31))
        self.max_size_app.setStyleSheet("color: rgb(252, 218, 183);\n"
        "font: 10pt \"MV Boli\";")
        self.max_size_app.setObjectName("max_size_app")
        self.max_size_app.setAlignment(QtCore.Qt.AlignCenter)

        # initial img
        # self.img_app = QtWidgets.QLabel(self.page_3)
        # self.img_app.setGeometry(QtCore.QRect(80, 60, 221, 181))
        # self.img_app.setStyleSheet("background-color: rgb(29, 45, 80);")
        # self.img_app.setText("")
        # self.img_app.setObjectName("img_app")

        self.label = QtWidgets.QLabel(self.page_3)
        self.label.setGeometry(QtCore.QRect(80, 10, 221, 41))
        self.label.setStyleSheet("color: rgb(252, 218, 183);\n"
        "font: 8pt \"MV Boli\";")
        self.label.setObjectName("label")
        self.stackedWidget_2.addWidget(self.page_3)
        self.page_4 = QtWidgets.QWidget()
        self.page_4.setObjectName("page_4")

        #black the port initial
        # self.black_net = QtWidgets.QPushButton(self.page_4)
        # self.black_net.setGeometry(QtCore.QRect(0, 470, 381, 21))
        # self.black_net.setStyleSheet("background-color: rgb(19, 59, 92);\n"
        # "color: rgb(252, 218, 183);")
        # self.black_net.setObjectName("black_net")

        #list with more detail
        self.list_net = CustomList(self.page_4)
        self.list_net.setGeometry(QtCore.QRect(0, 30, 381, 471))
        self.list_net.setObjectName("list_net")
        self.list_net.set_background_color('rgb(30, 95, 116)')
        self.list_net.setAutoScroll(False)

        self.label_8 = QtWidgets.QLabel(self.page_4)
        self.label_8.setGeometry(QtCore.QRect(10, 0, 151, 21))
        self.label_8.setStyleSheet("color: rgb(252, 218, 183);\n"
"font: 11pt \"MV Boli\";")
        self.label_8.setObjectName("label_8")

        self.stackedWidget_2.addWidget(self.page_4)
        self.page_9 = QtWidgets.QWidget()
        self.page_9.setObjectName("page_9")
        self.label_9 = QtWidgets.QLabel(self.page_9)
        self.label_9.setGeometry(QtCore.QRect(10, 0, 151, 21))
        self.label_9.setStyleSheet("color: rgb(252, 218, 183);\n"
"font: 11pt \"MV Boli\";")
        self.label_9.setObjectName("label_9")

        #list with more detail dst ip
        self.list_net_2 = CustomList(self.page_9)
        self.list_net_2.setGeometry(QtCore.QRect(0, 30, 381, 471))
        self.list_net_2.set_background_color('rgb(30, 95, 116)')
        self.list_net_2.setObjectName("list_net_2")

        self.stackedWidget_2.addWidget(self.page_9)
        self.page_10 = QtWidgets.QWidget()
        self.page_10.setObjectName("page_10")
        self.label_12 = QtWidgets.QLabel(self.page_10)
        self.label_12.setGeometry(QtCore.QRect(10, 0, 151, 21))
        self.label_12.setStyleSheet("color: rgb(252, 218, 183);\n"
"font: 11pt \"MV Boli\";")
        self.label_12.setObjectName("label_12")

        #list with more detail src ip
        self.list_net_3 = CustomList(self.page_10)
        self.list_net_3.setGeometry(QtCore.QRect(0, 30, 381, 471))
        self.list_net_3.set_background_color('rgb(30, 95, 116)')
        self.list_net_3.setObjectName("list_net_3")

        self.stackedWidget_2.addWidget(self.page_10)

        self.tabWidget.addTab(self.tab, "")
        self.tab_2 = QtWidgets.QWidget()
        self.tab_2.setObjectName("tab_2")
        self.tab_2.setStyleSheet("background-color: rgb(29, 45, 80);")

        #packet detail in capture
        self.pacekt_detail = QtWidgets.QTextBrowser(self.tab_2)
        self.pacekt_detail.setGeometry(QtCore.QRect(430, 11, 311, 481))
        self.pacekt_detail.setStyleSheet("color: rgb(252, 218, 183);\n"
        "background-color: rgb(30, 95, 116);\n"
        "font: 9pt \"MV Boli\";")
        self.pacekt_detail.setObjectName("pacekt_detail")

        #list of capture
        self.list_packets = CustomList(self.tab_2)
        self.list_packets.setGeometry(QtCore.QRect(0, 1, 411, 501))
        self.list_packets.setObjectName("list_packets")
        self.list_packets.set_background_color('rgb(19, 59, 92)')

        self.tabWidget.addTab(self.tab_2, "")
        self.label_3 = QtWidgets.QLabel(Form)
        self.label_3.setGeometry(QtCore.QRect(0, 0, 771, 16))
        self.label_3.setStyleSheet("background-color: rgb(29, 45, 80);")
        self.label_3.setText("")
        self.label_3.setObjectName("label_3")

        self.close_btn = QtWidgets.QToolButton(Form)
        self.close_btn.setGeometry(QtCore.QRect(740, 0, 21, 20))
        self.close_btn.setStyleSheet("background-color: rgb(29, 45, 80);\n"
        "color: rgb(252, 218, 183);\n""")

        self.retranslateUi(Form)
        self.tabWidget.setCurrentIndex(0)
        self.stackedWidget.setCurrentIndex(0)
        self.stackedWidget_2.setCurrentIndex(0)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "Form"))
        self.less_net.setToolTip(_translate("Form", "<html><head/><body><p><span style=\" font-size:10pt;\">less detail</span></p></body></html>"))
        self.more_net.setToolTip(_translate("Form", "<html><head/><body><p><span style=\" font-size:10pt;\">more detail</span></p></body></html>"))
        self.packets_net.setText(_translate("Form", "<html><head/><body><p align=\"center\">0</p></body></html>"))
        self.label_6.setText(_translate("Form", "<html><head/><body><p align=\"center\">Total Packets</p></body></html>"))
        self.label_13.setText(_translate("Form", "<html><head/><body><p align=\"center\">Average Packet Size</p></body></html>"))
        self.avg_size_net.setText(_translate("Form", "<html><head/><body><p align=\"center\">0</p></body></html>"))
        self.label_10.setText(_translate("Form", "<html><head/><body><p align=\"center\">Minimum Packet Size</p></body></html>"))
        self.min_size_net.setText(_translate("Form", "<html><head/><body><p align=\"center\">inf</p></body></html>"))
        self.label_14.setText(_translate("Form", "<html><head/><body><p align=\"center\">Maximum Packet Size</p></body></html>"))
        self.max_size_net.setText(_translate("Form", "<html><head/><body><p align=\"center\">0</p></body></html>"))
        self.label_2.setText(_translate("Form", "<html><head/><body><p align=\"center\"><span style=\" font-size:11pt;\">Network Layer Traffic</span></p></body></html>"))
        self.label_4.setText(_translate("Form", "Protocols"))
        self.label_5.setText(_translate("Form", "Destination Port"))
        self.label_7.setText(_translate("Form", "Source Port"))
        self.more_app.setToolTip(_translate("Form", "<html><head/><body><p><span style=\" font-size:10pt;\">more detail</span></p></body></html>"))
        self.less_app.setToolTip(_translate("Form", "<html><head/><body><p><span style=\" font-size:10pt;\">less detail</span></p></body></html>"))
        self.label_11.setText(_translate("Form", "<html><head/><body><p align=\"center\">Total Packets</p></body></html>"))
        self.packets_app.setText(_translate("Form", "<html><head/><body><p align=\"center\">0</p></body></html>"))
        self.label_15.setText(_translate("Form", "<html><head/><body><p align=\"center\">Average Packet Size</p></body></html>"))
        self.avg_size_app.setText(_translate("Form", "<html><head/><body><p align=\"center\">0</p></body></html>"))
        self.label_17.setText(_translate("Form", "<html><head/><body><p align=\"center\">Minimum Packet Size</p></body></html>"))
        self.label_18.setText(_translate("Form", "<html><head/><body><p align=\"center\">Maximum Packet Size</p></body></html>"))
        self.min_size_app.setText(_translate("Form", "<html><head/><body><p align=\"center\">inf</p></body></html>"))
        self.max_size_app.setText(_translate("Form", "<html><head/><body><p align=\"center\">0</p></body></html>"))
        self.label.setText(_translate("Form", "<html><head/><body><p align=\"center\"><span style=\" font-size:11pt;\">Application Layer Traffic</span></p></body></html>"))
        self.label_8.setText(_translate("Form", "Protocols"))
        self.label_9.setText(_translate("Form", "Destination IP"))
        self.label_12.setText(_translate("Form", "Source IP"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab), _translate("Form", "Traffic Analyzer"))
        self.pacekt_detail.setHtml(_translate("Form", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'MV Boli\'; font-size:9pt; font-weight:400; font-style:normal;\">\n"
"<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px; font-family:\'MS Shell Dlg 2\'; font-size:8pt;\"><br /></p></body></html>"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_2), _translate("Form", "Packet Capture"))
        self.close_btn.setText(_translate("Form", "X"))


