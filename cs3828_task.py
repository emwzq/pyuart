#!/usr/bin/env  python3
# coding=UTF-8

import serial
import serial.tools.list_ports
from time import sleep
from mystring import *
from myuart import *

def sample_continue():
    putstr('T 1;')

def sample_disable():
    putstr('T 1;')

def sample_one():
    putstr('V 0;');

def read_img():
    Uart.flushInput()
    putstr('I 0;');
    cnt = 0
    img = []
    while cnt < 324*244 :
        count = Uart.inWaiting()
        if count > 0:
            data = Uart.read(count)
            for i in range(len(data)):
                img.append(data[i]);
                cnt = cnt + 1;
    return img


def chip_init():
    #使能LCD显示
    reg_wr(0x40060004,0x0)
    #陪在图像数据直接存入LCD缓存区域
    reg_wr(0x40070000,0x10)

