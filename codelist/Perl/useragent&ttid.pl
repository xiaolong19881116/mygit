open FOUT,'>','C:\Users\xianlong.mxl\Desktop\output.txt';
while (<>) {#���ùܵ����ļ�����
	 chomp;#��ȥ��β���з�
	 if($_=~m{(.*?)(WindVane)(.*?)([0-9]{5,}@[^[:blank:]]*)(.*)?})
	 {
	 	print $1;
	 	print "\n";
	 	print $2;
	 	print "\n";
	 	print $3;
	 	print "\n";
	 	print $4;
	 	print "\n";
	 }
	 else
	 {
	 	 print "NO MATCH!\n";
	 	 
	 }
	 #print FOUT $_;
	 #print FOUT "\n";
}
<>