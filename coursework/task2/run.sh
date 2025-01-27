TASK=task2
INPUT_LOCATION=/data/large
INPUT1=$INPUT_LOCATION/imdb/title.basics.tsv
INPUT2=$INPUT_LOCATION/imdb/title.ratings.tsv
OUTPUT_DIR=/user/$USER/assignment/$TASK
SEP="|"

hdfs dfs -rm -r $OUTPUT_DIR

hadoop jar /opt/hadoop/hadoop-2.9.2/share/hadoop/tools/lib/hadoop-streaming-2.9.2.jar \
-D mapred.job.name="Miguel's $TASK - s2004624" \
-D stream.map.output.field.separator=$SEP \
-D stream.reduce.input.field.separator=$SEP \
-D stream.num.map.output.key.fields=1 \
-files ./mapper.py,./reducer.py,./movie.py,./combiner.py \
-input $INPUT1 \
-input $INPUT2 \
-output $OUTPUT_DIR \
-mapper mapper.py \
-combiner combiner.py \
-reducer reducer.py

echo "DONE, here is the output:"

hdfs dfs -cat $OUTPUT_DIR/* | sort

echo "-----DONE-----"