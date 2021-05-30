import sys
import nmap
import json
import subprocess
from lib import config
from lib import sql_connect, check_cdn
from rich.console import Console
from rich.progress import track

console = Console()

# masscan端口检测函数
def masscan_port_check(ip):
    ip_list = []
    url_list = []
    results_list = []
    console.print('正在进行端口探测', style="#ADFF2F")
    cmd = 'sudo ' + config.masscan_path + " " + ip + ' -p ' + config.masscan_port + ' -oJ ' +  config.masscan_file + ' --rate '+ config.masscan_rate
    rsp = subprocess.Popen(cmd, stdout=subprocess.PIPE, stderr=subprocess.PIPE, shell=True)
    while True:
        if rsp.poll() == None:
            pass
        else:
            break
    try:
        with open (config.masscan_file, 'r') as wr:
            for line in json.loads(wr.read()):
                ip = line['ip']
                port = line['ports'][0]['port']
                result_dict = {
                    'ip':ip,
                    'port':port
                }
                ip_list.append(result_dict)
            if len(ip_list) > config.port_num_max:
                ip_list.clear()
            else:
                results_list.extend(ip_list)
            for result in results_list:
                ip = result['ip']
                port = str(result['port'])
                url = service_check(ip,port)
                if len(url) > 0:
                    url_list.append(url)
                else:
                    url = 'http://' + result['ip'] + ':' + str(result['port'])
                    url_list.append(url)
                sql_connect.insert_task_sql(url_list)
                console.print('插入TASK数据库成功', style="#ADFF2F")
    except:
        pass


# service检测函数
def service_check(ip,port):
    url_list = []
    nm = nmap.PortScanner()
    ret = nm.scan(ip,port, arguments = '-Pn,-sS')
    service_name = ret['scan'][ip]['tcp'][int(port)]['name']
    if 'http' in service_name or service_name == 'sun-answerbook':
        if service_name == 'https' or service_name == 'https-alt':
            url = 'https://' + ip + ':' + port
        else:
            url = 'http://' + ip + ':' + port
        return url


# 判断subdomain cdn
def subdomain_port_check(subdomain):
    for domain in subdomain:
        url = []
        try:
            if len(check_cdn.check_cdn(domain[1])) == 1:
                ip = check_cdn.check_cdn(domain[1])
                sql_connect.insert_ip_sql(ip)
                url.append(domain[1])
                sql_connect.insert_task_sql(url)
            else:
                console.print('目标存在CDN', style="bold red")
                url.append(domain[1])
                sql_connect.insert_task_sql(url)
        except:
            console.print('目标' + domain[1] + '查询异常', style="bold red")