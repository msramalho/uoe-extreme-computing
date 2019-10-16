cat ../data/small/imdb/title.basics.tsv | ./mapper.py | sort -t'|' -k1,1 | ./combiner.py | ./reducer.py > result.txt
# cat ../data/large/titles.tsv | ./mapper.py | sort -t'|' -k1,1 | ./combiner.py | ./reducer.py

cat ../data/samples/task1/part-* | awk '{$1=$1};1' | sort -t '|' -k4,4 > test.txt

diff result.txt test.txt

DIFF=$(diff result.txt test.txt) 
if [ "$DIFF" = "" ] 
then
	rm result.txt test.txt
	rm *.pyc
	echo "SUCCESS: Results match sample"
fi