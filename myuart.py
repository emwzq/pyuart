#!/usr/bin/env  python3
# coding=UTF-8

import serial
import serial.tools.list_ports
from time import sleep
from mystring import *

#´ò¿ª´®¿Ú
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

def puthex(hdata):
    Uart.write(int2byte(hdata))

def putstr(data):
    Uart.write( str2byte(data) )

def gethex():
    count = Uart.inWaiting()
    if count > 0:
        data = Uart.read(count);
        return byte2hex(data)        
    
def getstr():
    count = Uart.inWaiting()
    if count > 0:
        data = Uart.read(count)
        return byte2str(data)

def getline():
    recdata = Uart.readline()
    try:
        print("in:",recdata.decode(),end='')
    except:
        print("decode error:",recdata);


def reg_wr(a,d):
    aa = '%02x' % a
    dd = '%02x' % d
    Uart.flushInput()
    putstr('S ' + aa + ' ' + dd + '\n')
    getline()

def reg_rd(a):
    aa = '%02x' % a
    Uart.flushInput()
    putstr('G ' + aa +'\n')
    getline()

def spi_wr(a,d):
    aa = '%02x' % a
    dd = '%02x' % d
    Uart.flushInput()
    putstr('W ' + aa + ' ' + dd + '\n')
    getline()


def spi_rd(a):
    aa = '%02x' % a
    Uart.flushInput()
    putstr('R ' + aa +'\n')
    getline()

def send_file(file_name):
    print(getstr())
    f = open(file_name,'rt')
    Uart.flushInput()
    for line in f:
        putstr(line)
        getline()
