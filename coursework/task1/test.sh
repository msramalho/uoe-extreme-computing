cat ../data/small/imdb/title.basics.tsv | ./mapper.py | sort -t'|' -k1,1 | ./reducer.py > result.txt

cat ../data/samples/task1/part-* | tr -d "[:blank:]" | sort -t '|' -k4,4 > test.txt

diff result.txt test.txt

DIFF=$(diff result.txt test.txt) 
if [ "$DIFF" = "" ] 
then
	rm result.txt test.txt
fi