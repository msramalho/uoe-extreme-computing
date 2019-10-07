TASK=task1
INPUT1=/data/small/imdb/title.basics.tsv
OUTPUT_DIR=/user/$USER/data/output/$TASK/

hdfs dfs -rm -r $OUTPUT_DIR

hadoop jar /opt/hadoop/hadoop-2.9.2/share/hadoop/tools/lib/hadoop-streaming-2.9.2.jar \
-input $INPUT1 \
-output $OUTPUT_DIR \
-file ./mapper.py \
-mapper mapper.py \
-file ./reducer.py \
-reducer reducer.py

echo "DONE, here is the output:"

hdfs dfs -cat $OUTPUT_DIR/*

echo "-----DONE-----"