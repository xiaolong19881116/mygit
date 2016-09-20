# jar简介
Java归档文件格式(Java Archive, JAR)能够将多个源码、资源等文件打包到一个归档文件中。这样，有如下好处：
安全性


可以对整个jar包的内容进行签名。


减少了下载时间


如果applet被打包成一个jar文件，那么所有相关的资源就可以在一个HTTP transaction中下载完成，而无需为每一个文件新建一个连接。


压缩
减少了磁盘空间的占用。


容易扩展
通过jar这种格式，可以和容易地将自己的程序打包提供给别人使用。


包密封(Package Sealing)
存储在jar文件中的包可以被密封，来保证版本的一致性。密封可以保证一个包中的所有类都来自同一个jar文件。


包版本说明
一个jar包可以存储关于其内容的信息，包括提供商、版本等。


可移植性
处理jar文件的机制是Java平台核心API的标准模块

----------

## 使用Eclipse的Export功能
1)在要打包的项目上右击，选择Export。

2）在弹出的窗口中，选择Java -> JAR File，然后点击next按钮

3)选出导出的jar文件地址 ->next

4)选择entry point Main Class -> finish

```
//运行jar文件:
java -jar test.jar
```

## 使用Eclipse的Import功能 引用jar包
### 添加内部jar 指的是项目内部jar
选择项目，右键 -> Build Path -> Configure Build Path...，项目Properties对话框
选择：Libraries ->ADD JARs 
在JAR Selection对话框中，选择项目的lib目录中的JAR文件，点击“OK”

### 添加外部jar
选择项目，右键 -> Build Path -> Configure Build Path...，项目Properties对话框
点击Library标签页，点击“Add External JARs...”按钮，在如添加外部JAR方法1中的JAR Selection对话框中，选择外部JAR

