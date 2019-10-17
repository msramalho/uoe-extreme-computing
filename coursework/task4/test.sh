# cat ../data/large/name.basics.tsv ../data/large/title.ratings.tsv ../data/large/title.crew.tsv | shuf | \
cat ../data/small/imdb/name.basics.tsv ../data/small/imdb/title.ratings.tsv ../data/small/imdb/title.crew.tsv | shuf | \
./mapper1.py | sort -t'|' -k1,3 | \
./reducer1.py | shuf | \
./mapper2.py | sort -r -t '|' -g -k1,2 | \
./reducer2.py
# ./reducer2.py > result.txt

exit 

cat ../data/samples/task4/part-* | awk '{$1=$1};1'| sort -r -t '|' -k1,2 -g | head -n 10 > test.txt

diff result.txt test.txt

DIFF=$(diff result.txt test.txt) 
if [ "$DIFF" = "" ]; then
	rm result.txt test.txt
	echo "SUCCESS: Results match sample"
fi