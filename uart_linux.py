#!/usr/bin/env  python3
# coding=UTF-8

import serial

###################################################
#
# �� ��: �����յ���������hex��ʾ
# �� ��: ���ڽ��ܵ�������
# �� ��: ת���������
#
###################################################

def hexshow(data):
    hex_data = ''
    hLen = len(data)
    int_data = []
    for i in range(hLen):
        hvol = data[i]
        hhex = '%02x' % hvol
        hex_data += hhex+' '
        int_data.append(hvol)
    print ('hexshow:', hex_data)
    #print (int_data)

def strshow(data):
    print (data.decode(),end='')

###################################################
#
# �� ��: ��Int�������ݰ��ֽ�ת����Bytes��
# �� ��: ��ת����Int����
# �� ��: ת�����Bytes����
#
###################################################
def int2byte(din):
    data = din
    a = []
    while data != 0:
        y = data % 256;
        data = data // 256;
        a.append(y)
    c = a[::-1]
    b = bytes(c)
    return b


if __name__ == '__main__':
    Ser = serial.Serial("/dev/ttyUSB0",115200,timeout=1.5)
    print (Ser)
    if Ser.isOpen():
       print("open success")
    else:
        print("open failed")

    Ser.write(bytes(0x38,))
    try:
        while True:
            count = Ser.inWaiting()
            if count > 0:
                data = Ser.read(count)
                if data != b'':
                    #hexshow(data)
                    strshow(data)
                    #for i in range(0,dl):
                    #    a = (data[i]+1)
                    #    a = int2byte(a);
                    #    Ser.write(a)

    except KeyboardInterrupt:
        if Ser != None:
            Ser.close()