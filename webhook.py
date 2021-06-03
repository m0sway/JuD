from flask import Flask, request
import datetime
import logging
import requests
from lib import config, sql_connect

app = Flask(__name__)

def Server_vuln(content):
    url = 'https://sc.ftqq.com/' + config.sckey + '.send'
    resp = requests.post(url,
                         data={"text": "xray漏洞通知", "desp": content})
    if resp.json()["errno"] != 0:
        raise ValueError("push ftqq failed, %s" % resp.text)

@app.route('/webhook', methods=['POST'])
def xray_webhook():
    data = request.json
    data_type = data.get("type")
    data = data.get("data")
    # 因为还会收到 https://chaitin.github.io/xray/#/api/statistic 的数据
    if data_type == 'web_vuln':
        detail = data.get('detail')
        target = data.get("target")
        content = """##爸爸 xray 发现了新漏洞

url: {url}

插件: {plugin}

payload: {vuln_payload}

发现时间: {create_time}

请及时查看和处理
""".format(url=target['url'], plugin=data.get('plugin'),
           vuln_payload=detail['payload'],
           create_time=str(datetime.datetime.fromtimestamp(data["create_time"] / 1000)))
        sql_connect.insert_vuln_sql(target['url'], data.get('plugin'), detail['payload'])
        try:
            Server_vuln(content)
        except Exception as e:
            logging.exception(e)
        return 'ok'
    else:
        return 'ok'


if __name__ == '__main__':
    app.run(
        port=2333
    )