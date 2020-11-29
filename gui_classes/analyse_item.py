from PyQt5 import QtCore, QtGui, QtWidgets
import ast

class AnalyseItem(QtWidgets.QWidget):

    def __init__(self):
        super(AnalyseItem, self).__init__()
        self.widget = QtWidgets.QWidget()
        self.widget.setGeometry(QtCore.QRect(0, 0, 381, 171))
        self.widget.setStyleSheet("background-color:rgb(30, 95, 116);")
        self.widget.setObjectName("widget")
        self.proto = QtWidgets.QLabel(self.widget)
        self.proto.setGeometry(QtCore.QRect(70, 10, 51, 31))
        self.proto.setStyleSheet("color: rgb(252, 218, 183);\n"
        "font: 8pt \"MV Boli\";")
        self.proto.setObjectName("proto")
        self.label_6 = QtWidgets.QLabel(self.widget)
        self.label_6.setGeometry(QtCore.QRect(80, 70, 81, 21))
        self.label_6.setStyleSheet("color: rgb(252, 218, 183);\n"
        "font: 8pt \"MV Boli\";")
        self.label_6.setObjectName("label_6")
        self.label_10 = QtWidgets.QLabel(self.widget)
        self.label_10.setGeometry(QtCore.QRect(20, 120, 101, 21))
        self.label_10.setStyleSheet("color: rgb(252, 218, 183);\n"
        "font: 8pt \"MV Boli\";")
        self.label_10.setObjectName("label_10")
        self.label_13 = QtWidgets.QLabel(self.widget)
        self.label_13.setGeometry(QtCore.QRect(220, 70, 101, 21))
        self.label_13.setStyleSheet("color: rgb(252, 218, 183);\n"
        "font: 8pt \"MV Boli\";")
        self.label_13.setObjectName("label_13")
        self.label_14 = QtWidgets.QLabel(self.widget)
        self.label_14.setGeometry(QtCore.QRect(190, 120, 101, 21))
        self.label_14.setStyleSheet("color: rgb(252, 218, 183);\n"
        "font: 8pt \"MV Boli\";")
        self.label_14.setObjectName("label_14")
        self.packets = QtWidgets.QLabel(self.widget)
        self.packets.setGeometry(QtCore.QRect(170, 70, 41, 16))
        self.packets.setStyleSheet("color: rgb(252, 218, 183);\n"
        "font: 8pt \"MV Boli\";")
        self.packets.setObjectName("packets")
        self.min_size = QtWidgets.QLabel(self.widget)
        self.min_size.setGeometry(QtCore.QRect(120, 120, 41, 16))
        self.min_size.setStyleSheet("color: rgb(252, 218, 183);\n"
        "font: 8pt \"MV Boli\";")
        self.min_size.setObjectName("min_size")
        self.avg_size = QtWidgets.QLabel(self.widget)
        self.avg_size.setGeometry(QtCore.QRect(330, 70, 41, 16))
        self.avg_size.setStyleSheet("color: rgb(252, 218, 183);\n"
        "font: 8pt \"MV Boli\";")
        self.avg_size.setObjectName("avg_size")
        self.max_size = QtWidgets.QLabel(self.widget)
        self.max_size.setGeometry(QtCore.QRect(300, 120, 41, 16))
        self.max_size.setStyleSheet("color: rgb(252, 218, 183);\n"
        "font: 8pt \"MV Boli\";")
        self.max_size.setObjectName("max_size")
        self.port_or_ip = QtWidgets.QLabel(self.widget)
        self.port_or_ip.setGeometry(QtCore.QRect(150, 10, 111, 31))
        self.port_or_ip.setStyleSheet("color: rgb(252, 218, 183);\n"
        "font: 8pt \"MV Boli\";")
        self.port_or_ip.setObjectName("port_or_ip")
        self.tag = QtWidgets.QLabel(self.widget)
        self.tag.setGeometry(QtCore.QRect(280, 10, 71, 31))
        self.tag.setStyleSheet("color: rgb(252, 218, 183);\n"
        "font: 8pt \"MV Boli\";")
        self.tag.setText("")
        self.tag.setObjectName("tag")
        self.toolButton = QtWidgets.QToolButton(self.widget)
        self.toolButton.setGeometry(QtCore.QRect(10, 50, 51, 51))
        self.toolButton.setStyleSheet("background-color: rgb(30, 95, 116);")
        self.toolButton.setText("")
        self.toolButton.setObjectName("toolButton")
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap("gui_classes/icon/analyse.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.toolButton.setIcon(icon)
        self.toolButton.setIconSize(QtCore.QSize(40, 40))

        self.retranslateUi()

        grid_box = QtWidgets.QGridLayout()
        grid_box.addWidget(self.widget, 2, 0)
        self.setLayout(grid_box)
        self.resize(370, 171)
        # self.show()

    def sizeHint(self):
        return QtCore.QSize(370, 171)

    def set_data(self, data):
        # data = ast.literal_eval(data)
        if "src_port" in data.keys():
            if data['protocol'] == "":
                self.set_labels_data(mini=data['min'], maxi=data['max'], avg=data['avg'], num=data['number'], 
                            tag=None, po_ip="src_port: "+ str(data['src_port']))
            else:
                self.set_labels_data(mini=data['min'], maxi=data['max'], avg=data['avg'], num=data['number'],
                             tag="protocol: "+ str(data['protocol']), po_ip="src_port: "+ str(data['src_port']))

        elif "dst_port" in data.keys():
            if data['protocol'] == "":
                self.set_labels_data(mini=data['min'], maxi=data['max'], avg=data['avg'], num=data['number'],
                            tag=None, po_ip="dst_port: "+ str(data['dst_port']))
            else:
                self.set_labels_data(mini=data['min'], maxi=data['max'], avg=data['avg'], num=data['number'],
                            tag="protocol: "+ str(data['protocol']), po_ip="dst_port: "+ str(data['dst_port']))
        
        elif "src_ip" in data.keys():
            self.set_labels_data(mini=data['min'], maxi=data['max'], avg=data['avg'], num=data['number'],
                        po_ip="src_ip: "+ str(data['src_ip']))
        
        elif "target_ip" in data.keys():
            self.set_labels_data(mini=data['min'], maxi=data['max'], avg=data['avg'], num=data['number'],
                        po_ip="dst_ip: "+ str(data['target_ip']))
        
        else:
            self.set_labels_data(mini=data['min'], maxi=data['max'], avg=data['avg'], num=data['number'],
                        proto = data['protocol'])


    def set_labels_data(self, mini, maxi, avg, num, tag=None, proto=None, po_ip=None):
        self.min_size.setText(str(mini))
        self.max_size.setText(str(maxi))
        self.avg_size.setText(str(avg))
        self.packets.setText(str(num))
        if tag:
            self.tag.setText(str(tag))
        if proto:
            self.proto.setText(str(proto))
        if po_ip:
            self.port_or_ip.setText(str(po_ip))

    def retranslateUi(self):
        self.label_6.setText("<html><head/><body><p align=\"center\">Total Packets</p></body></html>")
        self.label_10.setText("<html><head/><body><p align=\"center\">Minimum Packet Size</p></body></html>")
        self.label_13.setText("<html><head/><body><p align=\"center\">Average Packet Size</p></body></html>")
        self.label_14.setText("<html><head/><body><p align=\"center\">Maximum Packet Size</p></body></html>")



