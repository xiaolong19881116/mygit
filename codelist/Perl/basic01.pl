#use strict;
#use warnings;

#Perl的变量有三种类型：标量（scalar）、数组（array）和哈希（hashes）（译者注：下文会继续使用英文原文scalar、array和hash），每种类型都有属于自己的符号：分别是$、@和%。变量定义使用my关键字，生命期直到其所在的代码块结束或者文件的末尾。

my $undef = undef;#undef（对应Python中的None、PHP中的null）
print "this is ".$undef; # 打印空字符串""，并且抛出一个警告
print "\n";

my $num = 40.234;
print $num;
print "\n";

my $string = "world";
print $string; # "world"
print "\n";
print "Hello ".$string; # "Hello world"
print "\n";

my @array = (
	"print",
	"these",
	"strings",
	"out",
	"for",
	"me" # 末尾多余的逗号语法上是允许的
);
print @array;
print "\n";
print $array[0];
print "\n";
print $array[1];
print "\n";
print $array[-1];
print "\n";
print "This array has ".(scalar @array)." elements"; # "This array has 6 elements"
print "\n";
print "The last populated index is ".$#array;       # "The last populated index is 5"
print "\n";
#调用Perl脚本时使用的参数列表被保存在内置的array变量@ARGV中。

my %scientists = (
	"Newton"   => "Isaac",
	"Einstein" => "Albert",
	"Darwin"   => "Charles",
);

print %scientists;
print "\n";

my @ddd = %scientists;
print @ddd;
print "\n";

foreach ( @array ) {
	print $_." ";
}

print "\n";
my $line = <STDIN>;
print $line;
print "\n";