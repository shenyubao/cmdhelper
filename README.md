#CmdHelper
命令行拓展工具: 为常用命令提供存储和快捷调用,并提供本地命令跨机器同步.

##功能说明
    v0.1 - 为常用命令提供快捷调用
    v0.2 - 实现服务器备份,跨机器同步.

##安装说明
    0.服务依赖: python2.7 easy_install
    1.获取发布包: wget https://raw.github.com/Shenyubao/cmdhelper/master/dist/cmdhelper-0.2-py2.7.egg
    2.安装:easy_install cmdhelper-0.2-py2.7.egg
  
    服务端(可选,远程备份命令时需要):
    将server内文件部署到服务器上(推荐SAE)

    
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

  
  
