open FOUT,'>','C:\Users\xianlong.mxl\Desktop\output.txt';
while (<>) {#利用管道从文件读入
	 chomp;#除去行尾换行符 
	 if((.*?\"timestamp\":\")(\d{2,}?)(.*?\"content\":\")(.*?)(,\"frommid\":)(.*))
	{
		print $2;
		print " ";
		print $4;
	}
	 ##print FOUT $_;
	 ##print FOUT "\n";
}
<>