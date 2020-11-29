from PyQt5 import QtCore, QtGui, QtWidgets
import ast

class PacketItem(QtWidgets.QWidget):
    def __init__(self):
        super(PacketItem, self).__init__()
        self.widget = QtWidgets.QWidget()
        self.widget.setGeometry(QtCore.QRect(0, 0, 411, 81))
        self.widget.setStyleSheet("background-color:rgb(19, 59, 92);")
        self.widget.setObjectName("widget")
        self.label = QtWidgets.QLabel(self.widget)
        self.label.setGeometry(QtCore.QRect(20, 20, 35, 16))
        self.label.setStyleSheet("color: rgb(252, 218, 183);\n"
        "font: 8pt \"MV Boli\";")
        self.label.setObjectName("label")
        self.label_2 = QtWidgets.QLabel(self.widget)
        self.label_2.setGeometry(QtCore.QRect(110, 20, 61, 16))
        self.label_2.setStyleSheet("color: rgb(252, 218, 183);\n"
        "font: 8pt \"MV Boli\";")
        self.label_2.setObjectName("label_2")
        self.label_3 = QtWidgets.QLabel(self.widget)
        self.label_3.setGeometry(QtCore.QRect(220, 20, 21, 16))
        self.label_3.setStyleSheet("color: rgb(252, 218, 183);\n"
        "font: 8pt \"MV Boli\";")
        self.label_3.setObjectName("label_3")
        self.label_4 = QtWidgets.QLabel(self.widget)
        self.label_4.setGeometry(QtCore.QRect(300, 20, 35, 16))
        self.label_4.setStyleSheet("color: rgb(252, 218, 183);\n"
        "font: 8pt \"MV Boli\";")
        self.label_4.setObjectName("label_4")
        self.label_5 = QtWidgets.QLabel(self.widget)
        self.label_5.setGeometry(QtCore.QRect(20, 50, 41, 16))
        self.label_5.setStyleSheet("color: rgb(252, 218, 183);\n"
        "font: 8pt \"MV Boli\";")
        self.label_5.setObjectName("label_5")
        self.label_6 = QtWidgets.QLabel(self.widget)
        self.label_6.setGeometry(QtCore.QRect(190, 50, 41, 16))
        self.label_6.setStyleSheet("color: rgb(252, 218, 183);\n"
        "font: 8pt \"MV Boli\";")
        self.label_6.setObjectName("label_6")
        self.ip_target = QtWidgets.QLabel(self.widget)
        self.ip_target.setGeometry(QtCore.QRect(70, 50, 81, 16))
        self.ip_target.setStyleSheet("color: rgb(252, 218, 183);\n"
        "font: 8pt \"MV Boli\";")
        self.ip_target.setObjectName("ip_target")
        self.ip_source = QtWidgets.QLabel(self.widget)
        self.ip_source.setGeometry(QtCore.QRect(240, 50, 71, 16))
        self.ip_source.setStyleSheet("color: rgb(252, 218, 183);\n"
        "font: 8pt \"MV Boli\";")
        self.ip_source.setObjectName("ip_source")
        self.version = QtWidgets.QLabel(self.widget)
        self.version.setGeometry(QtCore.QRect(60, 20, 21, 16))
        self.version.setStyleSheet("color: rgb(252, 218, 183);\n"
        "font: 8pt \"MV Boli\";")
        self.version.setObjectName("version")
        self.total_len = QtWidgets.QLabel(self.widget)
        self.total_len.setGeometry(QtCore.QRect(170, 20, 31, 16))
        self.total_len.setStyleSheet("color: rgb(252, 218, 183);\n"
        "font: 8pt \"MV Boli\";")
        self.total_len.setObjectName("header_len")
        self.ttl = QtWidgets.QLabel(self.widget)
        self.ttl.setGeometry(QtCore.QRect(240, 20, 21, 16))
        self.ttl.setStyleSheet("color: rgb(252, 218, 183);\n"
        "font: 8pt \"MV Boli\";")
        self.ttl.setObjectName("ttl")
        self.protocol = QtWidgets.QLabel(self.widget)
        self.protocol.setGeometry(QtCore.QRect(340, 20, 31, 16))
        self.protocol.setStyleSheet("color: rgb(252, 218, 183);\n"
        "font: 8pt \"MV Boli\";")
        self.protocol.setObjectName("protocol")
        self.toolButton = QtWidgets.QToolButton(self.widget)
        self.toolButton.setGeometry(QtCore.QRect(350, 20, 51, 51))
        self.toolButton.setStyleSheet("background-color: rgb(19, 59, 92);")
        self.toolButton.setText("")
        self.toolButton.setObjectName("toolButton")
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap("gui_classes/icon/packet.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.toolButton.setIcon(icon)
        self.toolButton.setIconSize(QtCore.QSize(30, 30))

        self.json = None
        self.retranslateUi()

        grid_box = QtWidgets.QGridLayout()
        grid_box.addWidget(self.widget, 2, 0)
        self.setLayout(grid_box)
        self.resize(400, 81)

    def sizeHint(self):
        return QtCore.QSize(400, 81)

    def set_json(self, json_data):
        self.json = ast.literal_eval(json_data)
        self.set_date(self.json['version'], self.json['src'], self.json['target'], self.json['ttl'], 
        self.json['total_len'], self.json['protocol'])

    def get_json(self):
        return self.json

    def str_json(self):
        return pretty(self.json, indent=0)

    def set_date(self, ver, src_ip, t_ip, ttl, len_total, proto):
        self.version.setText(str(ver))
        self.ip_source.setText(str(src_ip))
        self.ip_target.setText(str(t_ip))
        self.ttl.setText(str(ttl))
        self.total_len.setText(str(len_total))
        self.protocol.setText(str(proto))


    def retranslateUi(self):
        self.label.setText("Version")
        self.label_2.setText("Total Length")
        self.label_3.setText("TTL")
        self.label_4.setText("Protocol")
        self.label_5.setText("Target Ip")
        self.label_6.setText("Source Ip")
        self.ip_target.setText("192.168.117.100")
        self.ip_source.setText("192.168.117.100")
        self.version.setText("4")
        self.total_len.setText("23")
        self.ttl.setText("4")
        self.protocol.setText("4")

def pretty(d, indent=0):
    string = ''
    for key, value in d.items():
        string += ('\t' * indent + str(key) + ":\n")
        if isinstance(value, dict):
            string += pretty(value, indent+1)
        else:
            string += ('\t' * (indent+1) + str(value) + "\n")
    return string


