n=7

length=$(wc -l ./hightemp.txt | cut -f 1 -d " ")

a=$(expr $length + $n)
b=$(expr $a - 1)
batch=$(expr $b / $n)
echo $batch
split -l $batch --numeric-suffixes=1 --additional-suffix=.txt hightemp.txt ./child/child

#split -n 5 -d hightemp.txt -n ./child/child -a ".txt"
