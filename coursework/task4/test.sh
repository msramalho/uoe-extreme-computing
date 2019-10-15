cat ../data/small/imdb/name.basics.tsv ../data/small/imdb/title.ratings.tsv ../data/small/imdb/title.crew.tsv | shuf | ./mapper_1.py | sort -t'|' -k1,3 | ./reducer_1.py # | ./mapper_2.py | sort -r -t '|' -g -k1,2 | ./reducer_2.py  > result.txt

cat ../data/samples/task4/part-* | awk '{$1=$1};1'| sort -r -t '|' -k1,2 -g | head -n 10 > test.txt

diff result.txt test.txt

DIFF=$(diff result.txt test.txt) 
if [ "$DIFF" = "" ]; then
	rm result.txt test.txt
	echo "SUCCESS: Results match sample"
fi