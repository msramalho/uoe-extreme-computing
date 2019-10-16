TASK=task1
INPUT1=/data/small/imdb/title.basics.tsv
OUTPUT_DIR=/user/$USER/data/output/$TASK/
OUT_DELI="|"

hdfs dfs -rm -r $OUTPUT_DIR

hadoop jar /opt/hadoop/hadoop-2.9.2/share/hadoop/tools/lib/hadoop-streaming-2.9.2.jar \
-D mapred.job.name="Miguel's $TASK - s2004624" \
-D stream.map.output.field.separator=$OUT_DELI \
-D stream.reduce.input.field.separator=$OUT_DELI \
-D stream.num.map.output.key.fields=1 \
-D mapred.reduce.tasks=10 \
-files ./mapper.py,./reducer.py,./statistics.py,./combiner.py \
-input $INPUT1 \
-output $OUTPUT_DIR \
-mapper mapper.py \
-combiner combiner.py \
-reducer reducer.py

# -D mapreduce.job.output.key.comparator.class=org.apache.hadoop.mapreduce.lib.partition.KeyFieldBasedComparator \
# -D mapreduce.partition.keypartitioner.options=-k1,1 \
# -D mapreduce.partition.keycomparator.options=-k1,1 \
# -partitioner org.apache.hadoop.mapred.lib.KeyFieldBasedPartitioner \

# -D mapreduce.map.output.key.field.separator=$OUT_DELI \
# -D map.output.key.field.separator=$OUT_DELI \
# -D mapreduce.fieldsel.data.field.separator=$OUT_DELI \
# -D mapred.textoutputformat.separator= \
# -D map.output.key.field.separator=$OUT_DELI \
echo "DONE, here is the output:"

hdfs dfs -cat $OUTPUT_DIR/*

echo "-----DONE-----"