cat ../data/small/imdb/title.basics.tsv ../data/small/imdb/title.ratings.tsv | shuf | ./mapper_1.py | sort -t'|' -k1 | ./reducer_1.py | ./mapper_2.py | sort -t '|' -k1,2 | ./reducer_2.py > result.txt

cat ../data/samples/task3/part-* | awk '{$1=$1};1'| sort -t '|' -k1,2 > test.txt

diff result.txt test.txt

DIFF=$(diff result.txt test.txt) 
if [ "$DIFF" = "" ]; then
	rm result.txt test.txt
	echo "SUCCESS: Results match sample"
fi