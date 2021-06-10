from rich.console import Console
import sqlite3
import subprocess
from lib import sql_connect
from lib import config

console = Console()

def rad_to_xray(domain_list):
    console.print('正在进行爬虫探测+漏洞检测',style="#ADFF2F")
    console.print('任务数据库连接成功',style="#ADFF2F")
    conn = sqlite3.connect(config.sql_path)
    sql = conn.cursor()
    for domain in domain_list:
        # if domain[3] == 'N':
        domain = domain[1]
        cmd = config.rad_path + " -t " + domain + " -http-proxy " + "127.0.0.1:" + config.xray_listen_port
        console.print('即将开启爬虫模块，可通过[bold cyan]tail -f logs/xray.log[/bold cyan]查看进度信息',style="#ADFF2F")
        rsp = subprocess.Popen(cmd, shell=True)
        while True:
            if rsp.poll() == None:
                pass
            else:
                break
