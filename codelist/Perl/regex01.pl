chomp($_ = <>);
print $_; 
print "\n";
if(m/[0-9]+/){
print "match\n";
}
else {
print "not match!\n"
}

chomp($str = <>);
print $str; 
print "\n";
if($str =~ m/[0-9]+/){
print "match\n";
}
else {
print "not match!\n"
}

my $dino = "28and300days";
if ($dino =~ m/(\d*)and(\d*)days/){
print "matched \n";
print "age:$1\n";
print "days:$2\n";
}
else {
print "not match!\n";
}

$_ = "abc and efg";
s/abc/ABC/; #把abc替换成ABC
print $_;

my @fields = split /:/ , "abc:def:g:f";#分割
print @fields;
foreach $x (@fields){
print $x;
print "\n";
}

foreach (@fields){
print $_;
print "\n";
}

print "最后一个元素下标：".$#fields;

print "\n";
my $y = join "-",@fields;
print $y;
print "\n";