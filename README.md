

部分内容转自：https://blog.csdn.net/absinjun/article/details/81407790

## pyserial常用函数
```
serial = serial.Serial(‘COM1’, 115200) 打开COM1并设置波特率为115200，COM1只适用于Windows

serial = serial.Serial(‘/dev/ttyS0’, 115200) 打开/dev/ttyS0并设置波特率为115200, 只适用于Linux

print serial .portstr 能看到第一个串口的标识

serial .write(“hello”) 往串口里面写数据

serial .close() 关闭serial 表示的串口

serial .open() 打开串口

data = serial .read(num) 读num个字符

data = serial .readline() 读一行数据，以/n结束，要是没有/n就一直读，阻塞。

serial .baudrate = 9600 设置波特率

print serial 可查看当前串口的状态信息

serial .isOpen() 当前串口是否已经打开

serial.inWaiting() 判断当前接收的数据

serial.flushInput() 清除输入缓冲区数据

serial.flushOutput() 中止当前输出并清除输出缓冲区数据
```

 实例: 获取从其他串口发送来的数据并回显
```
#!/usr/bin/python
# coding=UTF-8

import serial

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
    for i in xrange(hLen):
        hvol = ord(data[i])
        hhex = '%02x' % hvol
        hex_data += hhex+' '
    print 'hexshow:', hex_data


###################################################
#
# 功 能: 将需要发送的字符串以hex形式发送
# 参 数: 待发送的数据
# 返 回: 转换后的数据
#
###################################################

def hexsend(string_data=''):
    hex_data = string_data.decode("hex")
    return hex_data



if __name__ == '__main__':
    serial = serial.Serial('/dev/ttyS0', 115200)
    print serial
    if serial.isOpen():
       print("open success")
    else:
        print("open failed")


    try:
        while True:
            count = serial.inWaiting()
            if count > 0:
                data = serial.read(count)
                if data != b'':
                    print("receive:", data)
                    serial.write(data)
                else:
                    serial.write(hexsend(data))
    except KeyboardInterrupt:
        if serial != None:
            serial.close()
```

