### 关于
Author：m0sway<br />Mail：m0sway@163.com<br />Github：[https://www.github.com/m0sway/Jud](https://www.github.com/m0sway/Jud)<br />

## JuD是什么
JuD是一款自动化扫描器，其功能主要是遍历所有子域名、及遍历主机所有端口寻找出所有http服务，并使用集成的工具进行扫描，最后集成扫描报告；<br />工具目前有：oneforall、masscan、nmap、Wafw00f、rad、xray、ServerChan等<br />

### 工作流程

- 使用Oneforall遍历子域名
- 遍历结束后，Server酱会发送提醒到WeChat
- 使用masscan遍历主机所有开放端口
- 使用nmap扫描开放端口；得出所有http服务端口
- 使用Wafw00f进行WAF判断
- 若无WAF，传递到rad
- 使用rad进行扫描
- 扫描到的URL传递到Xray
- 使用Xray进行被动扫描
- 扫描时发现漏洞Server酱会发送提醒到WeChat
- 扫描结束后生成Xray报告
- 每次项目的数据都会存入sqlite数据库，后续个人可查看



### 后续开发
后续还会加入FOFA的调用、dirsearch扫描目录等，优化代码，兼容Windows。<br />

### 项目使用
项目是在Linux下开发的，请在Linux环境下使用。<br />rad扫描器是基于Chrome浏览器的，请先安装Chrome浏览器(若使用的时候报Chrome相关错误，打开Chrome的文件注释掉最后一行即可)。<br />接着将自己的Oneforall、Xray工具放入Tools中对应的文件夹(文件夹已经创建，将文件放入即可，不要套娃)<br />安装Oneforall所需Python库<br />配置文件在lib下的config.py,填入自己的server酱的key，其他相关配置也可做相应的更改。<br />全部安装完毕之后：<br />将目标填入 `target.txt` ,若是从ip开始扫描将目标填入 `ip.txt` ，若是直接扫描web将目标填入 `task.txt` <br />启用命令： `sudo python3 JuD.py`  <br />可使用单个模块或者使用全自动模式。<br />扫描结果保存在results目录下，每次的扫描结果都会根据时间戳重命名。<br />结束时一定要使用工具中的退出选项，否则下次运行时会报错。

## 如有问题请提交Issues

### 2021/6/10 更新
> 更新了IP_SCAN表和TASK表的数据去重，避免多次扫描同一目标。
> 在全自动模式下注释了WAF判断(单模块依旧可以使用)。代码做了一些小优化。

### 2021/6/11 更新
>新增了从IP开始全自动扫描
>新增了从TASK开始全自动扫描
