open FOUT,'>','C:\Users\xianlong.mxl\Desktop\output.txt';
open (MYFILE, 'C:\Users\xianlong.mxl\Desktop\input.txt') || die ("Could not open file"); 
while (<MYFILE>) {#���ùܵ����ļ�����
	chomp;#��ȥ��β���з� 
	print FOUT $_;
	print FOUT "\n";
}
print "done��";

close MYFILE;
close FOUT;