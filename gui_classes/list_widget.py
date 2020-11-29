from PyQt5 import QtCore, QtGui, QtWidgets
from .analyse_item import AnalyseItem
from .packet_item import PacketItem


class CustomList(QtWidgets.QListWidget):

    def __init__(self, parent):
        super(CustomList, self).__init__(parent)
        self.style_str = """
        QScrollBar:vertical {              
            border: none;
            background:white;
            width:3px;
            margin: 0px 0px 0px 0px;
        }
        QScrollBar::handle:vertical {
            background: qlineargradient(x1:0, y1:0, x2:1, y2:0,
            stop: 0 rgb(32, 47, 130), stop: 0.5 rgb(32, 47, 130), stop:1 rgb(32, 47, 130));
            min-height: 0px;
        }
        QScrollBar::add-line:vertical {
            background: qlineargradient(x1:0, y1:0, x2:1, y2:0,
            stop: 0 rgb(32, 47, 130), stop: 0.5 rgb(32, 47, 130),  stop:1 rgb(32, 47, 130));
            height: 0px;
            subcontrol-position: bottom;
            subcontrol-origin: margin;
        }
        QScrollBar::sub-line:vertical {
            background: qlineargradient(x1:0, y1:0, x2:1, y2:0,
            stop: 0  rgb(32, 47, 130), stop: 0.5 rgb(32, 47, 130),  stop:1 rgb(32, 47, 130));
            height: 0 px;
            subcontrol-position: top;
            subcontrol-origin: margin;
        }
        """

    def set_background_color(self, color):
        style = """QListWidget{
            background-color:"""+ color +""";    
        }\n""" + self.style_str
        self.setStyleSheet(style)

    def add_packet_item(self, json):
        custom_item = PacketItem()
        custom_item.set_json(json)
        item = QtWidgets.QListWidgetItem(self)
        item.setSizeHint(custom_item.sizeHint())
        self.addItem(item)
        self.setItemWidget(item, custom_item)

    def add_analyse_item(self, data):
        custom_item = AnalyseItem()
        custom_item.set_data(data)
        item = QtWidgets.QListWidgetItem(self)
        item.setSizeHint(custom_item.sizeHint())
        self.addItem(item)
        self.setItemWidget(item, custom_item)

    def change_analyse_item(self, data, index):
        
        custom_item = AnalyseItem()
        custom_item.set_data(data)
        # item = QtWidgets.QListWidgetItem(self)
        item = self.item(index)
        item.setSizeHint(custom_item.sizeHint())
        # self.insertItem(index, item)
        self.setItemWidget(item, custom_item)




        

