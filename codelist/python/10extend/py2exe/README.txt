ʹ��py2exe������ִ���ļ�

1.����������guessNumber.py

2.����setup.py�����磺

import distutils
import py2exe 

distutils.core.setup(console=["guessNumber.py"]) #ע������ǿ�����������,����GUI����ֻ��Ҫ��console �޸�Ϊwindows

3.�ڵ�ǰ�ļ����´��ն����У�python setup.py py2exe 
4.ִ�е������󣬻����������ļ��� build & dist :���ɵĿ�ִ�г������dist��

5.py2exe�������������������