#!/bin/bash

# Check if IP is provided
if [ -z "$1" ]; then
    echo "Usage: $0 <target_ip>"
    exit 1
fi

TARGET=$1
DATE=$(date +%F)
OUTPUT="scan_${TARGET}_${DATE}.txt"

PORTS=(21 22 80 443 3306)

echo "Scanning $TARGET..." 
echo "Scan Report for $TARGET on $DATE" > $OUTPUT
echo "-----------------------------------" >> $OUTPUT

open_count=0

for port in "${PORTS[@]}"; do
    timeout 1 bash -c "echo > /dev/tcp/$TARGET/$port" 2>/dev/null
    
    if [ $? -eq 0 ]; then
        echo "Port $port is OPEN" | tee -a $OUTPUT
        ((open_count++))
    else
        echo "Port $port is CLOSED" >> $OUTPUT
    fi
done

echo "-----------------------------------" >> $OUTPUT
echo "Total Open Ports: $open_count" | tee -a $OUTPUT
