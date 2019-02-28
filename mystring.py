#!/usr/bin/env python3


##########################################
#   函数名：int2byte( int_data )
#   功能：将整数转化成byte类型的16进制数据
##########################################
def int2byte(din):
    data = din
    a = []
    while data != 0:
        a.append(data % 256)
        data = data // 256;
    b = bytes( a[::-1] )
    return b

###################################################
# 功 能: 将string类型数据转换成bytes类型
# 参 数: 待转换的字符串
# 返 回: 转换后的数据
###################################################
def str2byte(data):
    return(bytes(data,'utf-8'))


###################################################
# 功 能: 将接收到的数据已hex显示
# 参 数: 串口接受到的数据
# 返 回: 转换后的数据
###################################################
def byte2hex(data):
    hex_data = ''
    hLen = len(data)
    for i in range( len(data) ):
        hhex = '%02x' % data[i]
        hex_data += hhex+' '
    return hex_data

###################################################
# 功 能: 将接收到的数据以string显示
# 参 数: 串口接受到的数据
# 返 回: 转换后的数据
###################################################
def byte2str(data):
    try:
        return data.decode()
    except:
        print("byte,decode() error")
        return ''

###################################################
# 功 能: 将string类型数据转换成bytes类型
# 参 数: 待转换的字符串
# 返 回: 转换后的数据
###################################################
def str2byte(data):
    return(bytes(data,'utf-8'))



