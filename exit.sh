ps -ef |grep subdomain |awk '{print $2}'|xargs sudo kill -9
ps -ef |grep xray |awk '{print $2}'|xargs sudo kill -9
sudo cat ./results/result.sqlite3 > ./results/$(date "+%Y%m%d%H%M%S")_result.sqlite3
sudo rm -rf ./results/result.sqlite3
sudo rm -rf ./results/results.sqlite3
sudo rm -rf ./tools/OneForAll/results/*
