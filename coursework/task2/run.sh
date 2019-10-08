TASK=task2
INPUT1=/data/small/imdb/title.basics.tsv
INPUT2=/data/small/imdb/title.ratings.tsv
OUTPUT_DIR=/user/$USER/data/output/$TASK/

hdfs dfs -rm -r $OUTPUT_DIR

hadoop jar /opt/hadoop/hadoop-2.9.2/share/hadoop/tools/lib/hadoop-streaming-2.9.2.jar \
-D mapreduce.job.output.key.comparator.class=org.apache.hadoop.mapreduce.lib.partition.KeyFieldBasedComparator \
-D mapreduce.map.output.key.field.separator="|" \
-input $INPUT1 \
-input $INPUT2 \
-output $OUTPUT_DIR \
-file ./mapper.py \
-mapper mapper.py \
-file ./reducer.py \
-reducer reducer.py


echo "DONE, here is the output:"

hdfs dfs -cat $OUTPUT_DIR/*

echo "-----DONE-----"