#use strict;
#use warnings;

#Perl�ı������������ͣ�������scalar�������飨array���͹�ϣ��hashes��������ע�����Ļ����ʹ��Ӣ��ԭ��scalar��array��hash����ÿ�����Ͷ��������Լ��ķ��ţ��ֱ���$��@��%����������ʹ��my�ؼ��֣�������ֱ�������ڵĴ������������ļ���ĩβ��

my $undef = undef;#undef����ӦPython�е�None��PHP�е�null��
print "this is ".$undef; # ��ӡ���ַ���""�������׳�һ������
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
	"me" # ĩβ����Ķ����﷨���������
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
#����Perl�ű�ʱʹ�õĲ����б����������õ�array����@ARGV�С�

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