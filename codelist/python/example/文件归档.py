#/user/bin/env python   

# -*- coding:utf-8 -*-


'''
首先安装压缩工具7Z 并配置7z环境变量
7z a pom.zip pom.xml  #压缩文件pom.xml到pom.zip
7z x pom.zip #解压缩文件pom.zip
7z a Test.zip Test #压缩文件夹Test到Test.zip
7z x Test.zip #解压缩文件Test.zip到文件夹Test
'''

import os  
import time 

source = [r'D:\Test']

target_dir = 'D:\\backup\\'

today = target_dir + time.strftime('%Y%m%d')
now = time.strftime('%H%M%S')

target = today + os.sep + now + '.zip'

if not os.path.exists(today):
    os.makedirs(today)
    print('Successfully created directory', today)
    
#备份命令，可替换为7z, Linux下可改为tar等
zip_command = "7z a %s %s" %(target, ' '.join(source))
#执行命令
if os.system(zip_command) == 0:
    print('Successful backup to', target)
else:
    print('Backup failed') 