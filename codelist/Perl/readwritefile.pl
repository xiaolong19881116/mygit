open FOUT,'>','C:\Users\xianlong.mxl\Desktop\output.txt';
open (MYFILE, 'C:\Users\xianlong.mxl\Desktop\input.txt') || die ("Could not open file"); 
while (<MYFILE>) {#利用管道从文件读入
	chomp;#除去行尾换行符 
	print FOUT $_;
	print FOUT "\n";
}
print "done！";

close MYFILE;
close FOUT;