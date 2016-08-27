使用py2exe创建可执行文件

1.开发程序，如guessNumber.py

2.开发setup.py程序，如：

import distutils
import py2exe 

distutils.core.setup(console=["guessNumber.py"]) #注这里就是开发的主程序,对于GUI程序，只需要把console 修改为windows

3.在当前文件夹下打开终端运行：python setup.py py2exe 
4.执行第三步后，会生成两个文件夹 build & dist :生成的可执行程序就在dist下

5.py2exe的其他方法请查阅资料