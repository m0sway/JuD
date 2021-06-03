import sys
import os
import time
from rich.console import Console
from rich.table import Column, Table
from lib import config,check_cdn,port_check,read_target,rad_to_xray,ServerChan,sql_connect,subdomain_scan,waf_check


console = Console()


# banner生成函数
def banner():
    msg = '''
                
                                                                    
                                          / /                   
                                         / /           ___   /  
                                        / / //   / / //   ) /   
                                       / / //   / / //   / /    
                                 ((___/ / ((___( ( ((___/ /     
                                                                Author : m0sway
    '''

    console.print(msg, style="bold red")
    help_table = Table(show_header=True, header_style="bold magenta")
    help_table.add_column("ID", style="dim", width=39)
    help_table.add_column("参数", style="dim", width=39)
    help_table.add_column("说明", style="dim", width=39)

    help_table.add_row(
    "1",
    "Subdomain_Scan",
    "获取子域"
    )
    help_table.add_row(
    "2",
    "Port_Check",
    "端口检测"
    )
    help_table.add_row(
    "3",
    "Waf_Check",
    "WAF检测"
    )
    help_table.add_row(
    "4",
    "Rad_To_Xray",
    "爬虫爬取 + 漏洞探测 + 消息通知"
    )
    help_table.add_row(
    "5",
    "attack",
    "全自动"
    )
    help_table.add_row(
    "6",
    "Exit",
    "退出"
    )
    console.print('参数说明,一款适用于红队快速初步攻击的全自动化工具', style="#ADFF2F")
    console.print(help_table)


# 结束函数
def end():
    console.print("shutting down at {0}".format(time.strftime("%X")), style="#ADFF2F")


def main():
    banner()
    while True:
        console.print('请输入要执行的参数ID：[bold cyan]1-6[/bold cyan]', style="#ADFF2F")
        args = input('> ')
        if args == '1':
            subdomain_scan.oneforall_scan(config.target_path)
        elif args == '2':
            port_check.subdomain_port_check(sql_connect.read_subdomain_sql())
            for domain in sql_connect.read_ip_sql():
                port_check.masscan_port_check(domain[1])
        elif args == '3':
            waf_check.waf_check(sql_connect.read_task_sql())
        elif args == '4':
            rad_to_xray.rad_to_xray(sql_connect.read_task_sql())
        elif args == '5':
            subdomain_scan.oneforall_scan(config.target_path)
            os.system("python3 ./subdomain_monitor.py")
            port_check.subdomain_port_check(sql_connect.read_subdomain_sql())
            for domain in sql_connect.read_ip_sql():
                port_check.masscan_port_check(domain[1])
            waf_check.waf_check(sql_connect.read_task_sql())
            os.system("nohup python3 webhook.py > logs/webhook.log 2>&1 &")
            os.system("nohup ./Tools/xray/xray_linux_amd64 webscan --listen 127.0.0.1:23333 --html-output ./results/xray.html --webhook-output http://127.0.0.1:2333/webhook > logs/xray.log 2>&1 &")
            rad_to_xray.rad_to_xray(sql_connect.read_task_sql())
        elif args == '6':
            os.system("sudo bash exit.sh")
            break
        else:
            console.print('输入参数有误，请检查后输入', style="bold red")
            sys.exit()
    end()


if __name__ == '__main__':
    main()
