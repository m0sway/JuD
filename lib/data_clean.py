import sqlite3
from lib import config,sql_connect
from rich.console import Console

console = Console()

def ip_clean():
    try:
        ip_list = []
        for ip in sql_connect.read_ip_sql():
            ip = ip[1]
            ip_list.append(ip)

        ip_set = set(ip_list)
        ip_list = list(ip_set)*3

        ip_conn = sqlite3.connect(config.sql_path)
        ip_sql = ip_conn.cursor()
        ip_sql.execute("DELETE FROM IP_SCAN")
        ip_conn.commit()
        sql_connect.insert_ip_sql(ip_list)
        console.print('IP_SCAN表去重自增成功', style="#ADFF2F")
    except:
        console.print('IP_SCAN表去重自增失败', style="bold red")

def task_clean():
    try:
        task_list = []
        for task in sql_connect.read_task_sql():
            task = task[1]
            task_list.append(task)

        task_set = set(task_list)
        task_list = list(task_set)

        task_conn = sqlite3.connect(config.sql_path)
        task_sql = task_conn.cursor()
        task_sql.execute("DELETE FROM TASK")
        task_conn.commit()
        sql_connect.insert_task_sql(task_list)
        console.print('TASK表去重成功', style="#ADFF2F")
    except:
        console.print('TASK表去重失败', style="bold red")