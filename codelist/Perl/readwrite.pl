open FOUT,'>','C:\Users\xianlong.mxl\Desktop\output.txt';
while (<>) {#���ùܵ����ļ�����
	 chomp;#��ȥ��β���з� 
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