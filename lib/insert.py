from lib import sql_connect
from rich.console import Console
import requests

console = Console()

def ip_insert():
    sql_connect.task_sql_check()
    sql_connect.subdomain_sql_check()
    sql_connect.vuln_sql_check()
    sql_connect.ip_sql_check()
    ip_list = []
    for ip in open("ip.txt"):
        ip_list.append(ip[:-1])
    try:
        sql_connect.insert_ip_sql(ip_list)
        console.print('IP插入成功', style="#ADFF2F")
    except:
        console.print('IP插入失败', style="bold red")

def task_insert():
    sql_connect.task_sql_check()
    sql_connect.subdomain_sql_check()
    sql_connect.vuln_sql_check()
    sql_connect.ip_sql_check()
    task_list = []
    headers = {
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/86.0.4240.111 Safari/537.36",
        "Content-Type": "application/x-www-form-urlencoded",
        "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9",
    }
    for domain in open("task.txt"):
        if domain[:4] == 'http':
            task = domain
        else:
            task = 'http://' + domain
            # r = requests.get(url=task, timeout=5, headers=headers, verify=False)
            tasks = 'https://' + domain
        try:
            r = requests.get(url=task[:-1], timeout=5, headers=headers, verify=False)
            task_list.append(task[:-1])
            console.print('http insert task_list success', style="#ADFF2F")
        except:
            try:
                r = requests.get(url=tasks[:-1], timeout=5, headers=headers, verify=False)
                task_list.append(tasks[:-1])
                console.print('https insert task_list success', style="#ADFF2F")
            except:
                console.print('insert task_list fail', style="bold red")
    try:
        sql_connect.insert_task_sql(task_list)
        console.print('TASK插入成功', style="#ADFF2F")
    except:
        console.print('TASK插入失败', style="bold red")