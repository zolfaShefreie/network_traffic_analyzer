import socket
import struct


def decode_ip_addr(addr):
    return '.'.join(map(str, addr))

class PacketDecoder(object):
    def __init__(self, data):
        self.data = data

    def convert_to_json(self):
        decoder_ip = IPDecoder(self.data)
        json_data = decoder_ip.convert_to_json()
        self.data = decoder_ip.remaining_data

        if decoder_ip.protocol == 1:
            decoder_icmp = ICMPDecoder(self.data)
            json_data['icmp'] = decoder_icmp.convert_to_json()

        elif decoder_ip.protocol == 2:
            decoder_igmp = IGMPDecoder(self.data)
            json_data['igmp'] = decoder_igmp.convert_to_json()

        elif decoder_ip.protocol == 6:
            decoder_tcp = TCPDecoder(self.data)
            json_data['tcp'] = decoder_tcp.convert_to_json()
            json_data['data'] = decoder_tcp.remaining_data

        elif decoder_ip.protocol == 17:
            decoder_udp = UDPDecoder(self.data)
            json_data['udp'] = decoder_udp.convert_to_json()
            json_data['data'] = decoder_udp.remaining_data

        else:
            json_data['code'] = self.data

        return json_data

class IPDecoder(object):
    version = None
    header_len = None
    tos = None
    total_len = None
    identification = None
    flags = None
    fragment_offset = None
    ttl = None
    protocol = None
    header_checksum = None
    src_ip = None
    target_ip = None
    options = None

    def __init__(self, data):
        self.data = data
        self.json_data = {}
        self.remaining_data = None

    def decode_ipv4(self):
        version_plus_len = self.data[0]
        self.version = version_plus_len >> 4
        self.header_len = (version_plus_len & 15) * 4
        self.tos, self.total_len, self.identification, flags_plus_offset, self.ttl, self.protocol, \
        self.header_checksum, src, target = struct.unpack('! x B H H H B B H 4s 4s', self.data[:20])
        #self.ttl, self.protocol, src, target = struct.unpack('! 8x B B 2x 4s 4s', self.data[:20])#check beshe
        self.flags = flags_plus_offset >> 13
        self.fragment_offset = (flags_plus_offset & 15) * 4 # check kon
        self.options = self.data[20:self.header_len]
        self.src_ip = decode_ip_addr(src)
        self.target_ip = decode_ip_addr(target)
        self.remaining_data = self.data[self.header_len:]

    def convert_to_json(self):
        self.decode_ipv4()
        self.json_data = {
            'version': self.version,
            'header_len': self.header_len,
            'tos': self.tos,
            'total_len': self.total_len,
            'identification': self.identification,
            'protocol': self.protocol,
            'flags': self.flags,
            'fragment offset': self.fragment_offset,
            'ttl': self.ttl,
            'src': self.src_ip,
            'target': self.target_ip,
            'options': self.options
        }
        return self.json_data


class TCPDecoder(object):
    src_port = None
    dst_port = None
    seq = None
    ack = None
    offset = None
    flags = None
    window = None
    checksum = None
    urgent_pointer = None
    option = None

    def __init__(self, data):
        self.data = data
        self.json_data = {}
        self.remaining_data = None

    def decode_flags(self, offset_reserved_flag):
        flag_urg = (offset_reserved_flag & 32) >> 5
        flag_ack = (offset_reserved_flag & 16) >> 4
        flag_psh = (offset_reserved_flag & 8) >> 3
        flag_rst = (offset_reserved_flag & 4) >> 2
        flag_syn = (offset_reserved_flag & 2) >> 1
        flag_fin = offset_reserved_flag & 1
        return flag_urg, flag_ack, flag_psh, flag_rst, flag_syn, flag_fin

    def decode_tcp(self):
        self.src_port, self.dst_port, self.seq, self.ack, offset_reserved_flag, self.window, \
        self.checksum, self.urgent_pointer = struct.unpack('! H H L L H H H H', self.data[:20])
        self.offset = (offset_reserved_flag >> 12) * 4
        self.option = self.data[20: self.offset]
        self.remaining_data = self.data[self.offset:]
        return offset_reserved_flag

    def convert_to_json(self):
        offset_reserved_flag = self.decode_tcp()
        (flag_urg, flag_ack, flag_psh, flag_rst, flag_syn, flag_fin) = self.decode_flags(offset_reserved_flag)
        self.json_data = {
            'src_port': self.src_port,
            'dst_port': self.dst_port,
            'seq': self.seq,
            'ack' : self.ack,
            'offset': self.offset,
            'flags':{
                'flag_urg': flag_urg,
                'flag_ack': flag_ack,
                'flag_psh': flag_psh,
                'flag_rst': flag_rst,
                'flag_syn': flag_syn,
                'flag_fin': flag_fin
            },
            'window': self.window,
            'checksum': self.checksum,
            'urgent_pointer': self.urgent_pointer,
            'options': self.option
        }
        return self.json_data


class UDPDecoder(object):
    src_port = None
    dst_port = None
    len = None
    checksum = None
    def __init__(self, data):
        self.data = data
        self.json_data = {}
        self.remaining_data = None

    def decode_udp(self):
        self.src_port, self.dst_port, self.len, self.checksum = struct.unpack('! H H H H', self.data[:8])
        self.remaining_data = self.data[8:]

    def convert_to_json(self):
        self.decode_udp()
        self.json_data = {
            'src_port': self.src_port,
            'dst_port': self.dst_port,
            'len': self.len,
            'checksum': self.checksum,
        }
        return self.json_data


class ICMPDecoder(object):
    type = None
    code = None
    checksum = None

    def __init__(self, data):
        self.data = data
        self.json_data = {}
        self.remaining_data = None

    def decode_icmp(self):
        self.type, self.code, self.checksum = struct.unpack('! B B H', self.data[:4])
        self.remaining_data = self.data[4:]

    def convert_to_json(self):
        self.decode_icmp()
        self.json_data = {
            'type': self.type,
            'code': self.code,
            'checksum': self.checksum,
            'data': self.remaining_data
        }
        return self.json_data


class IGMPDecoder(object):
    type = None
    max_resp_time = None
    checksum = None
    def __init__(self, data):
        self.data = data
        self.json_data = {}
        self.group_address = None

    def decode_igmp(self):
        self.type, self.max_resp_time, self.checksum, self.group_address = struct.unpack('! B B H L', self.data[:8])


    def convert_to_json(self):
        self.json_data = {
            'type': self.type,
            'max_resp_time': self.max_resp_time,
            'checksum': self.checksum,
            'group_address': self.group_address
        }
        return self.json_data

