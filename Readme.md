### 关于
Author：m0sway<br />Mail：m0sway@163.com<br />Github：[https://www.github.com/m0sway/Jud](https://www.github.com/m0sway/Jud)<br />

## JuD是什么
JuD是一款自动化扫描器，其功能主要是遍历所有子域名、及遍历主机所有端口寻找出所有http服务，并使用集成的工具进行扫描，最后集成扫描报告；<br />工具目前有：oneforall、masscan、nmap、Wafw00f、rad、xray、ServerChan等<br />​<br />
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

​<br />
### 后续开发
后续还会加入FOFA的调用、dirsearch扫描目录等，优化代码，兼容Windows。<br />
后续会搭建docker方便大家拉取<br />

### 项目使用
项目是在Linux下开发的，请在Linux环境下使用。<br />rad扫描器是基于Chrome浏览器的，请先安装Chrome浏览器。<br />接着需要安装Oneforall等工具的python依赖库。<br />全部安装完毕之后：<br />将目标填入 `target.txt` <br />启用命令：`sudo python3 Jud.py` <br />可使用单个模块或者使用全自动模式。
