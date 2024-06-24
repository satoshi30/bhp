from ctypes import *
import socket
import struct

class IP(Structure):
	_fields_ = [
		("ver", c_ubyte, 4),			# 4 bit unsigned char
		("ihl", c_ubyte, 4),			# 4 bit unsigned char
		("tos", c_ubyte, 8),			# 1 byte unsigned char
		("len", c_ushort, 16),			# 2 byte unsigned short
		("id", c_ushort, 16),			# 2 byte unsigned short
		("ttl", c_ubyte, 8),			# 1 byte unsigned char
		("protocol_num", c_ubyte, 8),	# 1 byte unsigned char
		("sum", c_ushort, 16),			# 2 byte unsigned short
		("src", c_uint32, 32),			# 4 byte unsigned int
		("dst", c_uint32, 32),			# 4 byte unsigned int
	]

	def __new__(cls, socket_buffer=None):
		#　入力バッファを構造体に格納
		return cls.from_buffer_copy(socket_buffer)
	
	def __init__(self, socket_buffer=None):
		# IPアドレスを可読な形で変数に格納
		self.src_address = socket.inet_ntoa(struct.pack("<L", self.src))
		self.dst_address = socket.inet_ntoa(struct.pack("<L", self.dst))
	