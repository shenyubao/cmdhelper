#CmdHelper
命令行拓展工具: 为常用命令提供存储和快捷调用,并提供本地命令跨机器同步.

##路线图
    v0.1 - 为常用命令提供快捷调用
    v0.2 - 实现服务器备份,跨机器同步.
    v0.3 - 实现命令同步至alias文件(直接输入Key即可执行命令,Key可自动补全).

##命令表
    ch :CmdHelper管理
    ch set [uid|pwd|host] XXX 设置变量
    ch pull 更新本地命令库
    ch push 提交本地命令库
    ch list 变量一览
    
    chlist 查看现有命令
    chset KEY XXX  设置新命令
    chdel [id|KEY] 删除命令
    chrun [id|KEY] 运行命令
    KEY            运行命令(直接是用Key即可执行命令)
    chmark KEY     存储当前路径

##安装说明
    客户端安装:
    0.安装 python2.7 (yum,apt-get,brew....)
    1.安装 easy_install (yum,apt-get,brew....)
    2.获取发布包: wget https://raw.github.com/Shenyubao/cmdhelper/master/dist/cmdhelper-0.3-py2.7.egg
    3.安装:easy_install cmdhelper-0.3-py2.7.egg
  
    服务端安装:(可选,远程备份命令时需要)
    1.将server内文件部署到服务器上(推荐SAE)
    2.配置server/users.py中的用户名密码
    
##使用说明
###客户端配置
    ch set uid sample_id     :必填,用户ID
    ch set host http://chxxx.sinaapp.com/chserver :选填,存储服务URL
    ch set pwd 123456    :选填,存储服务密码
    
    ch list :查看当前配置项
![](https://raw.github.com/Shenyubao/cmdhelper/master/images/ch.png)
###基础功能
####chlist 
    chlist   #查看Key-Value
    
![](https://raw.github.com/Shenyubao/cmdhelper/master/images/chlist.png)

    
####chset 
    chset key value  #设置Key-Value

![](https://raw.github.com/Shenyubao/cmdhelper/master/images/chset.png)
   


####chdel
    chdel [index|key]  #删除Key-Value
    chdel 1
    chdel db.dev
![](https://raw.github.com/Shenyubao/cmdhelper/master/images/chdel.png)


####chrun
    chrun [index|key]  #执行命令
    chrun 1
    chrun db.dev  
![](https://raw.github.com/Shenyubao/cmdhelper/master/images/chrun.png)

    db.[Tab]
![](https://raw.github.com/Shenyubao/cmdhelper/master/images/alias.png)

    
####chmark
    chmark key   # 收藏当前目录
    chmark ch
  
![](https://raw.github.com/Shenyubao/cmdhelper/master/images/chmark.png)
  
###同步功能
####chpush
    chpush   # 提交当前K-V至服务器
####chpull
    chpull   # 从服务器更新K-V
![](https://raw.github.com/Shenyubao/cmdhelper/master/images/sync.png)

  
  
