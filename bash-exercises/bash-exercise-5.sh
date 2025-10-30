#!/bin/bash
cut -d',' -f1,3 Basic-scripting/backup/sales.csv
#!/bin/bash
awk -F',' '{print $1, $3}' Basic-scripting/backup/sales.csv
#!/bin/bash
grep "Shoes" Basic-scripting/backup/sales.csv
