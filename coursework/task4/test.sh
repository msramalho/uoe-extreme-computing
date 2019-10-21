# cat ../data/large/name.basics.tsv ../data/large/title.ratings.tsv ../data/large/title.crew.tsv | shuf | \
cat ../data/small/imdb/title.ratings.tsv ../data/small/imdb/title.crew.tsv | shuf | \
./mapper1.py | sort -t'|' -k1,1  | \
./combiner1.py | \
./reducer1.py > temp.txt

cat temp.txt ../data/small/imdb/name.basics.tsv | shuf | \
./mapper2.py | shuf | \
./combiner2.py | sort -t '|' -g -k1,2 | \
./reducer2.py
# ./reducer2.py > result.txt

exit
rm temp.txt

cat ../data/samples/task4/part-* | awk '{$1=$1};1'| sort -r -t '|' -k1,2 -g | head -n 10 > test.txt

diff result.txt test.txt

DIFF=$(diff result.txt test.txt) 
if [ "$DIFF" = "" ]; then
	rm result.txt test.txt
	rm *.pyc
	echo "SUCCESS: Results match sample"
fi