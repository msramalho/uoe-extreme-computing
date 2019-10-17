# cat ../data/large/titles.tsv ../data/large/title.ratings.tsv | shuf | \
cat ../data/small/imdb/title.basics.tsv ../data/small/imdb/title.ratings.tsv | shuf | \
./mapper.py | sort -t'|' -k1 | \
./combiner1.py | \
./reducer1.py | \
shuf | cat | sort -t '|' -k1,3 | \
./combiner2.py | \
./reducer2.py > result.txt

cat ../data/samples/task3/part-* | awk '{$1=$1};1'| sort -t '|' -k1,2 > test.txt

diff result.txt test.txt

DIFF=$(diff result.txt test.txt) 
if [ "$DIFF" = "" ]; then
	rm result.txt test.txt
	rm *.pyc
	echo "SUCCESS: Results match sample"
fi