sed "s/\t/ /g" hightemp.txt
echo ""
tr "\t" " " <hightemp.txt
echo ""
expand -t 1 hightemp.txt
