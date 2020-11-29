import socket
import struct
import os
from PyQt5.QtCore import pyqtSignal, QThread
from PyQt5 import QtCore

from decoders import PacketDecoder
from analyzer import Analyzer
import time


queque = []

class Sniffer(QThread):

    #signals
    #send_decoded_packet = pyqtSignal(str)

    def __init__(self):
        super().__init__()
        self.host = socket.gethostbyname(socket.gethostname())
        print(socket.gethostname())
        self.port = 0
        if os.name == 'nt':
            self.win = True
        else:
            self.win = False
        self.packet_analyzer = Analyzer()
        self.socket = socket.socket(socket.AF_INET, socket.SOCK_RAW, socket.IPPROTO_IP)
        self.socket.bind(('192.168.43.180', 0))
        #self.socket.bind((self.host, 0))
        self.socket.setsockopt(socket.IPPROTO_IP, socket.IP_HDRINCL, 1)
        self.socket.ioctl(socket.SIO_RCVALL, socket.RCVALL_ON)

    def close_connection(self):
        self.socket.ioctl(socket.SIO_RCVALL, socket.RCVALL_OFF)
        self.socket.close()

    def run(self):
        while True:
            try:
                raw_data, addr = self.socket.recvfrom(65536)
                queque.append(raw_data)
                # self.decode_packet(raw_data)
            except Exception as e:
                print(str(e))
                self.close_connection()
                break

    def decode_packet(self, data):
        decoder = PacketDecoder(data)
        dict_data = decoder.convert_to_json()
        if dict_data['total_len'] != 0:
            self.send_decoded_packet.emit(str(dict_data))
            self.packet_analyzer.analyse(dict_data)


class ReadyData(QThread):

    send_decoded_packet = pyqtSignal(str)

    def __init__(self):
        super().__init__()
        self.packet_analyzer = Analyzer()
        self.sniffer = Sniffer()
        self.running = True
        self.sniffer.finished.connect(self.colse_sniffer)

    def run(self):
        self.sniffer.start()
        while True:
            time.sleep(0.5)
            if len(queque) == 0 and self.running:
                continue
            elif len(queque) == 0 and self.running == False:
                break
            else:
                data = queque.pop(0)
                decoder = PacketDecoder(data)
                dict_data = decoder.convert_to_json()
                if dict_data['total_len'] != 0:
                    self.send_decoded_packet.emit(str(dict_data))
                    self.packet_analyzer.analyse(dict_data)

    @QtCore.pyqtSlot()
    def colse_sniffer(self):
        self.running = False
        
    



