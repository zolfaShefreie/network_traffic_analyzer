
import PyQt5
from PyQt5 import QtCore, QtGui, uic, QtWidgets
from PyQt5.QtWidgets import QWidget
from gui_classes.main_fram import Ui_Form
from sniffer import Sniffer, ReadyData
from gui_classes.widget import CustomForm

import ast

if hasattr(QtCore.Qt, 'AA_EnableHighDpiScaling'):
    PyQt5.QtWidgets.QApplication.setAttribute(QtCore.Qt.AA_EnableHighDpiScaling, True)

if hasattr(QtCore.Qt, 'AA_UseHighDpiPixmaps'):
    PyQt5.QtWidgets.QApplication.setAttribute(QtCore.Qt.AA_UseHighDpiPixmaps, True)


class MainWindow(Ui_Form, CustomForm):
    def __init__(self, parent=None):
        super(MainWindow, self).__init__()
        self.setupUi(self)
        self.setWindowFlags(QtCore.Qt.FramelessWindowHint)
        self.pressing = False
        self.setMouseTracking(True)

        # self.sniffer = Sniffer()
        self.sniffer = ReadyData()
        self.fill_the_lists()
        
        # connect signals to listeners
        self.more_app.clicked.connect(self.show_app_details)
        self.less_app.clicked.connect(self.show_app_less)
        self.more_net.clicked.connect(self.show_net_details)
        self.less_net.clicked.connect(self.show_net_less)
        self.close_btn.clicked.connect(self.close_app)
        self.list_packets.itemClicked.connect(self.show_data_of_packet)

        self.sniffer.send_decoded_packet.connect(self.add_to_capture)
        self.sniffer.packet_analyzer.analyse_app_changed.connect(self.change_the_data_app)
        self.sniffer.packet_analyzer.analyse_network_changed.connect(self.change_the_data_net)
        self.sniffer.packet_analyzer.protocol_net_changed.connect(self.update_list_net_proto)
        self.sniffer.packet_analyzer.protocol_app_changed.connect(self.update_list_app_proto)
        self.sniffer.packet_analyzer.src_app_changed.connect(self.update_list_app_src)
        self.sniffer.packet_analyzer.dst_app_changed.connect(self.update_list_app_dst)
        self.sniffer.packet_analyzer.src_net_changed.connect(self.update_list_net_src)
        self.sniffer.packet_analyzer.dst_net_changed.connect(self.update_list_net_dst)
        #self.sniffer.packet_analyzer.imgs_changed.connect(self.update_img)
        self.sniffer.finished.connect(self.close)
        
        # self.pixmap_net = QtGui.QPixmap('./net.png')
        # self.pixmap_app = QtGui.QPixmap('./app.png')
        # self.img_net.setAlignment(QtCore.Qt.AlignCenter)
        # self.img_app.setAlignment(QtCore.Qt.AlignCenter)
        # self.img_net.setPixmap(self.pixmap_net)
        # self.img_net.setScaledContents(True)
        # self.img_app.setPixmap(self.pixmap_app)
        # self.img_app.setScaledContents(True)

    def fill_the_lists(self):
        for each in self.sniffer.packet_analyzer.net_protocol:
            self.list_net.add_analyse_item(each)
        for each in self.sniffer.packet_analyzer.app_protocol:
            self.list_app.add_analyse_item(each)
        

    def show_data_of_packet(self, item):
        custom_item = self.list_packets.itemWidget(item)
        self.pacekt_detail.setText(custom_item.str_json())

    # @QtCore.pyqtSlot()
    # def update_img(self):
    #     self.pixmap_net = QtGui.QPixmap('./net.png')
    #     self.pixmap_app = QtGui.QPixmap('./app.png')
    #     self.img_net.setAlignment(QtCore.Qt.AlignCenter)
    #     self.img_app.setAlignment(QtCore.Qt.AlignCenter)
    #     self.img_net.setPixmap(self.pixmap_net)
    #     self.img_net.setScaledContents(True)
    #     self.img_app.setPixmap(self.pixmap_app)
    #     self.img_app.setScaledContents(True) 

    @QtCore.pyqtSlot(str)
    def add_to_capture(self, json_data):
        if self.list_packets.count() == 200:
            self.list_packets.takeItem(0)
        self.list_packets.add_packet_item(json_data)
        # self.list_packets.scrollToBottom()

    @QtCore.pyqtSlot()
    def change_the_data_net(self):
        dict_data = self.sniffer.packet_analyzer.net
        self.packets_net.setText(str(dict_data['number']))
        self.min_size_net.setText(str(dict_data['min']))
        self.max_size_net.setText(str(dict_data['max']))
        self.avg_size_net.setText(str(dict_data['avg']))

    @QtCore.pyqtSlot()
    def change_the_data_app(self):
        dict_data = self.sniffer.packet_analyzer.app
        self.packets_app.setText(str(dict_data['number']))
        self.min_size_app.setText(str(dict_data['min']))
        self.max_size_app.setText(str(dict_data['max']))
        self.avg_size_app.setText(str(dict_data['avg']))


    @QtCore.pyqtSlot(int)
    def update_list_net_proto(self, index):
        dict_data = self.sniffer.packet_analyzer.net_protocol[index]
        self.list_net.change_analyse_item(dict_data, index)
        

    @QtCore.pyqtSlot(int)
    def update_list_app_proto(self, index):
        dict_data = self.sniffer.packet_analyzer.app_protocol[index]
        self.list_app.change_analyse_item(dict_data, index)

    @QtCore.pyqtSlot(int, bool)
    def update_list_app_src(self, index, is_new):
        dict_data = self.sniffer.packet_analyzer.app_list_src[index]
        if is_new:
            self.list_app_3.add_analyse_item(dict_data)
        else:
            self.list_app_3.change_analyse_item(dict_data, index)

    @QtCore.pyqtSlot(int, bool)
    def update_list_app_dst(self, index, is_new):
        dict_data = self.sniffer.packet_analyzer.app_list_dst[index]
        if is_new:
            self.list_app_2.add_analyse_item(dict_data)
        else:
            self.list_app_2.change_analyse_item(dict_data, index)

    @QtCore.pyqtSlot(int, bool)
    def update_list_net_src(self, index, is_new):
        dict_data = self.sniffer.packet_analyzer.net_list_src[index]
        if is_new:
            self.list_net_3.add_analyse_item(dict_data)
        else:
            self.list_net_3.change_analyse_item(dict_data, index)

    @QtCore.pyqtSlot(int, bool)
    def update_list_net_dst(self, index, is_new):
        dict_data = self.sniffer.packet_analyzer.net_list_dst[index]
        if is_new:
            self.list_net_2.add_analyse_item(dict_data)
        else:
            self.list_net_2.change_analyse_item(dict_data, index)

    def show_net_details(self):
        index = self.stackedWidget_2.currentIndex() + 1
        index %= 4
        if index == 0:
            index = 1
        self.stackedWidget_2.setCurrentIndex(index)

    def show_net_less(self):
        self.stackedWidget_2.setCurrentIndex(0)

    def show_app_details(self):
        index = self.stackedWidget.currentIndex() + 1
        index %= 4
        if index == 0:
            index = 1
        self.stackedWidget.setCurrentIndex(index)

    def show_app_less(self):
        self.stackedWidget.setCurrentIndex(0)

    def show_error_box(self, msg):
        msg_box = QtWidgets.QMessageBox()
        msg_box.setText(msg)
        msg_box.setStandardButtons(QtWidgets.QMessageBox.Ok)
        msg_box.setWindowFlags(QtCore.Qt.FramelessWindowHint)
        msg_box.setStyleSheet("""
        QMessageBox {
            background-color: rgb(1, 14, 30);
        }

        QMessageBox QLabel {
            color: rgb(200, 200, 200);
        }
        QMessageBox QPushButton {
            background-color: rgb(255, 255, 30);
            color: rgb(255, 255, 255);
        }""")
        msg_box.exec_()
        msg_box.show()

    def close_app(self):
        self.sniffer.sniffer.quit()
        self.sniffer.quit()
        self.close()



if __name__ == "__main__":
    import sys

    app = QtWidgets.QApplication(sys.argv)
    w = MainWindow()
    w.show()
    w.sniffer.start()
    sys.exit(app.exec_())



