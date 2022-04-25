i=0
while(true)
do
    uptime >> /home/tongtong/python_project/shell/CPU_uptime_1.txt
    echo $i
    let i++
    if [ $i -eq 10000 ]; then 
        break;
    fi
    sleep 60
done