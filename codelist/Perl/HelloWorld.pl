use strict;
use warnings;

print "Hello world";

#Perl脚本由Perl解释器解释执行，perl或者perl.exe： perl helloworld.pl [arg0 [arg1 [arg2 ...]]]
#Perl的语法非常宽容，它允许你写出有歧义的或者有不可预期行为的代码。我不会去解释这些诡异的行为是什么样的，因为你最好避开它们。避免这种情况的方法是在你写的每个Perl脚本或者模块的开头加上use strict; use warnings;。use foo;这种语句叫做编译指示（pragmas），编译指示是给perl.exe的一个提示，在程序开始执行之前的语法验证阶段会发挥作用，脚本语句实际执行的时候这些编译指示对于运行结果没有影响。

#分号;是语句结束的标志，井号#表示注释的开始，注释直到这行的结尾结束。Perl没有块注释的语法。