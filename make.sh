#!/bin/sh
clear
python3 -m da.compiler pastry.da

python3 -m da --message-buffer-size 32000 main.da 100 0 200 2 16 2> /dev/null

# ctr=10
# while [ $ctr -lt 11 ]; do
#    echo  The number of processes is $ctr
#    python3 -m da --message-buffer-size 8000 main.da $ctr 0 10
#    ctr=$((ctr+10))
#    wait
# done
echo "all jobs are done"
