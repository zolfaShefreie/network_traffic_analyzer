import math
from PyQt5.QtCore import QObject, pyqtSignal
from gui_classes.chart_maker import ChartMaker

class LocationOfList:

    def __init__(self, index, tag, port_or_ip_data):
        self.index = index
        self.tag = tag
        self.port_or_ip = port_or_ip_data
        self.json_obj = {self.port_or_ip: index}
    

class Analyzer(QObject):

    #signals
    analyse_network_changed = pyqtSignal()
    analyse_app_changed = pyqtSignal()
    protocol_net_changed = pyqtSignal(int)
    protocol_app_changed = pyqtSignal(int)
    src_app_changed = pyqtSignal(int, bool)
    dst_app_changed = pyqtSignal(int, bool)
    src_net_changed = pyqtSignal(int, bool)
    dst_net_changed = pyqtSignal(int, bool)
    imgs_changed = pyqtSignal()

    net = {'number': 0, 'min': math.inf, 'max': 0, 'avg': 0}
    app = {'number': 0, 'min': math.inf, 'max': 0, 'avg': 0}

    net_protocol = [
       {'protocol': 'tcp','number': 0, 'min': math.inf, 'max': 0, 'avg': 0},
       {'protocol': 'udp','number': 0, 'min': math.inf, 'max': 0, 'avg': 0},
       {'protocol': 'icmp','number': 0, 'min': math.inf, 'max': 0, 'avg': 0},
       {'protocol': 'igmp','number': 0, 'min': math.inf, 'max': 0, 'avg': 0},
       {'protocol': 'others','number': 0, 'min': math.inf, 'max': 0, 'avg': 0} 
    ]
    app_protocol = [
        {'protocol': 'tcp','number': 0, 'min': math.inf, 'max': 0, 'avg': 0},
        {'protocol': 'udp','number': 0, 'min': math.inf, 'max': 0, 'avg': 0}
    ]

    net_list_src = []
    net_src_indexs = {}

    net_list_dst = []
    net_dst_indexs = {}

    app_list_src = []
    app_src_indexs = {}

    app_list_dst = []
    app_dst_indexs = {}

    def __init__(self):
        super().__init__()
        # ChartMaker(self.net_protocol, 'net').draw()
        # ChartMaker(self.app_protocol, 'app').draw()

    def compute_fields(self, dict_data, dict_input):
        if dict_input['total_len'] == 0:
            print(dict_input)

        if dict_data['min'] > dict_input['total_len']:
            dict_data['min'] = dict_input['total_len']
        
        if dict_data['max'] < dict_input['total_len']:
            dict_data['max'] = dict_input['total_len']
        
        dict_data['avg'] = ((dict_data['number'] * dict_data['avg']) + dict_input['total_len']) / (dict_data['number'] + 1)
        dict_data['number'] = dict_data['number'] + 1

        return dict_data

    def analyse(self, input_data):
        self.net = self.compute_fields(self.net, input_data)
        self.analyse_network_changed.emit()

        if input_data['protocol'] == 6 or input_data['protocol'] == 17:
            self.app = self.compute_fields(self.app, input_data)
            self.analyse_app_changed.emit()

        if input_data['protocol'] == 6:
            self.net_protocol[0] = self.compute_fields(self.net_protocol[0], input_data)
            self.protocol_net_changed.emit(0)
            self.app_protocol[0] = self.net_protocol[0]
            self.protocol_app_changed.emit(0)
            data = input_data['tcp']
            data['total_len'] = input_data['total_len']
            self.insert_to_list_port(data)
        
        elif input_data['protocol'] == 17:
            self.net_protocol[1] = self.compute_fields(self.net_protocol[1], input_data)
            self.protocol_net_changed.emit(1)
            self.app_protocol[1] = self.net_protocol[1]
            self.protocol_app_changed.emit(1)
            data = input_data['udp']
            data['total_len'] = input_data['total_len']
            self.insert_to_list_port(data)

        elif input_data['protocol'] == 1:
            self.net_protocol[2] = self.compute_fields(self.net_protocol[2], input_data)
            self.protocol_net_changed.emit(2)
        
        elif input_data['protocol'] == 2:
            self.net_protocol[3] = self.compute_fields(self.net_protocol[3], input_data)
            self.protocol_net_changed.emit(3)

        else:
            self.net_protocol[4] = self.compute_fields(self.net_protocol[4], input_data)
            self.protocol_net_changed.emit(4)

        self.insert_to_list_ip(input_data)

        # ChartMaker(self.net_protocol, 'net').draw()
        # ChartMaker(self.app_protocol, 'app').draw()
        # self.imgs_changed.emit()
        
    def insert_to_list_ip(self, input_data):
        index = self.search("src_ip", input_data['src'])
        if index == -1:
            index_src = LocationOfList(len(self.net_list_src), "src_ip", input_data['src'])

            data = {'src_ip': input_data['src'], 'number': 1, 'min': input_data['total_len'],
            "max": input_data['total_len'], "avg": input_data['total_len']}

            self.net_list_src.append(data)
            self.net_src_indexs.update(index_src.json_obj)
            self.src_net_changed.emit(len(self.net_list_src)-1, True)

        else:
           self.net_list_src[index] = self.compute_fields(self.net_list_src[index], input_data)
           self.src_net_changed.emit(index, False) 

        index = self.search("dst_ip", input_data['target'])
        if index == -1:
            index_dst = LocationOfList(len(self.net_list_dst), "dst_ip", input_data['target'])

            data = {'target_ip': input_data['target'], 'number': 1, 'min': input_data['total_len'],
            "max": input_data['total_len'], "avg": input_data['total_len']}

            self.net_list_dst.append(data)
            self.net_dst_indexs.update(index_dst.json_obj)
            self.dst_net_changed.emit(len(self.net_list_dst)-1, True)

        else:
            self.net_list_dst[index] = self.compute_fields(self.net_list_dst[index], input_data) 
            self.dst_net_changed.emit(index, False)

    def insert_to_list_port(self, input_data):
        index = self.search("src_port", input_data['src_port'])

        if index == -1:
            index_src = LocationOfList(len(self.app_list_src), "src_port", input_data['src_port'])

            data = {'src_port': input_data['src_port'], 'number': 1, 'min': input_data['total_len'],
            "max": input_data['total_len'], "avg": input_data['total_len'], 
            "protocol": self.find_app_protocol(input_data['src_port'])}

            self.app_list_src.append(data)
            self.app_src_indexs.update(index_src.json_obj)
            self.src_app_changed.emit(len(self.app_list_src)-1, True)

        else:
            self.app_list_src[index] = self.compute_fields(self.app_list_src[index], input_data) 
            self.src_app_changed.emit(index, False)

        index = self.search("dst_port", input_data['dst_port'])
        if index == -1:
            index_dst = LocationOfList(len(self.app_list_dst), "dst_port", input_data['dst_port'])

            data = {'dst_port': input_data['dst_port'], 'number': 1, 'min': input_data['total_len'],
            "max": input_data['total_len'], "avg": input_data['total_len'],
            "protocol": self.find_app_protocol(input_data['dst_port'])}

            self.app_list_dst.append(data)
            self.app_dst_indexs.update(index_dst.json_obj)
            self.dst_app_changed.emit(len(self.app_list_dst)-1, True)

        else:
            self.app_list_dst[index] = self.compute_fields(self.app_list_dst[index], input_data)
            self.dst_app_changed.emit(index, False) 

    def search(self, tag, port_ip):
        if tag == "src_ip":
            try:
                return self.net_src_indexs[port_ip]
            except KeyError:
                pass

        elif tag == "dst_ip":
            try:
                return self.net_dst_indexs[port_ip]
            except KeyError:
                pass

        elif tag == "src_port":
            try:
                return self.app_src_indexs[port_ip]
            except KeyError:
                pass

        elif tag == "dst_port":
            try:
                return self.app_dst_indexs[port_ip]
            except KeyError:
                pass

        return -1

    def find_app_protocol(self, port):
        port_protocol = {53: 'dsn', 80: 'http', 67: 'dhcp', 68: 'dhcp', 
        25: 'smtp', 587:"smtp", 465: "smtp", 443: 'https'}
        try:
            return port_protocol[port]
        except KeyError:
            return ""

    