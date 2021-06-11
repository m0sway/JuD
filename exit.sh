ps -ef |grep subdomain |awk '{print $2}'|xargs sudo kill -9
ps -ef |grep xray |awk '{print $2}'|xargs sudo kill -9
ps -ef |grep webhook.py |awk '{print $2}'|xargs sudo kill -9
sudo cat ./results/results.sqlite3 > ./results/$(date "+%Y%m%d%H%M%S")_results.sqlite3
sudo cat ./results/xray.html > ./results/$(date "+%Y%m%d%H%M%S")_xray.html
sudo rm -rf ./results/results.sqlite3
sudo rm -rf ./results/xray.html
sudo rm -rf ./Tools/OneForAll/results/*
