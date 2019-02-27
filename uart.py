#!/usr/bin/env  python3
# coding=UTF-8

import serial


#打开串口
def uart_open():
    try:
        Ser = serial.Serial("/dev/ttyUSB0",115200,timeout=1.0)
        if Ser.isOpen():
            print("open success")
        else:
            print("open failed")
        return Ser
    except:
        print("Uart open failed");

Uart = uart_open();

####################################################################



###################################################
#
# 功 能: 将接收到的数据已hex显示
# 参 数: 串口接受到的数据
# 返 回: 转换后的数据
#
###################################################

def hexshow(data):
    hex_data = ''
    hLen = len(data)
    #int_data = []
    for i in range(hLen):
        hvol = data[i]
        hhex = '%02x' % hvol
        hex_data += hhex+' '
        #int_data.append(hvol)
    #print ('hexshow:', hex_data)
    print (hex_data)
    #print (int_data)

def strshow(data):
    print (data.decode(),end='')

###################################################
#
# 功 能: 将Int类型数据按字节转换成Bytes，
# 参 数: 待转换的Int数据
# 返 回: 转换后的Bytes数据
#
###################################################
def int2byte(din):
    data = din
    a = []
    while data != 0:
        a.append(data % 256)
        data = data // 256;
    return  (bytes(a[::-1]))


def puthex(hdata):
    Uart.write(int2byte(hdata))

def putstr(data):
    bdata = bytes(data,'utf-8')
    Uart.write(bdata)

