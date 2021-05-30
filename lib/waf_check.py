from lib import config
from rich.console import Console
import sqlite3
import subprocess

console = Console()

def waf_check(domain_list):
    console.print('正在进行WAF检测',style="#ADFF2F")
    # console.print('任务数据库连接成功',style="#ADFF2F")
    conn = sqlite3.connect(config.sql_path)
    sql = conn.cursor()
    for domain in domain_list:
        domain = domain[1]
        cmd = ['python3', config.wafw00f_path, domain]
        rsp = subprocess.Popen(cmd, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
        if 'No WAF' in rsp.stdout.read().decode("GBK").split('\n')[-3]:
            sql.execute("UPDATE TASK set WAF = '%s' where URL = '%s' " % ('N', domain))
        else:
            sql.execute("UPDATE TASK set WAF = '%s' where URL = '%s' " % ('Y', domain))
        sql.execute("UPDATE TASK set STATUS = 'WAF检测完成' where URL = '%s' " % (domain,))
        conn.commit()
        while True:
            if rsp.poll() == None:
                pass
            else:
                break
    console.print('WAF检测完成\n\n',style="#ADFF2F")
    conn.close()