#/user/bin/env python   

# -*- coding:utf-8 -*-


'''
���Ȱ�װѹ������7Z ������7z��������
7z a pom.zip pom.xml  #ѹ���ļ�pom.xml��pom.zip
7z x pom.zip #��ѹ���ļ�pom.zip
7z a Test.zip Test #ѹ���ļ���Test��Test.zip
7z x Test.zip #��ѹ���ļ�Test.zip���ļ���Test
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
    
#����������滻Ϊ7z, Linux�¿ɸ�Ϊtar��
zip_command = "7z a %s %s" %(target, ' '.join(source))
#ִ������
if os.system(zip_command) == 0:
    print('Successful backup to', target)
else:
    print('Backup failed') 