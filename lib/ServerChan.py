import requests
from lib import config
from lib import sql_connect
import time
from rich.console import Console

console = Console()

# 子域收集状态提醒
def subdomain_status_push():
    console.log('子域收集完成')
    sql_connect.task_sql_check()
    sql_connect.subdomain_sql_check()
    sql_connect.vuln_sql_check()
    sql_connect.ip_sql_check()
    sql_connect.insert_subdomain_sql(sql_connect.oneforall_results_sql())
    subdomain_num = len(sql_connect.read_subdomain_sql())
    content = """``` 子域收集完成```
    #### 结果:  共收集到了{subdomain_num}个子域
    #### 发现时间: {now_time}
""".format(subdomain_num=subdomain_num, now_time=time.strftime("%Y_%m_%d_%H_%M_%S", time.localtime()))
    url = 'https://sc.ftqq.com/' + config.sckey + '.send'
    try:
        resp = requests.post(url,data={"text": "子域收集提醒", "desp": content})
    except:
        console.print('子域提醒失败，请检查sckey是否正确配置', style="bold red")
