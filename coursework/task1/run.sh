TASK=task1
INPUT1=/data/small/imdb/title.basics.tsv
OUTPUT_DIR=/user/$USER/data/output/$TASK/

hdfs dfs -rm -r $OUTPUT_DIR

hadoop jar /opt/hadoop/hadoop-2.9.2/share/hadoop/tools/lib/hadoop-streaming-2.9.2.jar \
-D mapred.job.name="Miguel's task 1 - s2004624" \
-D stream.map.output.field.separator="|" \
-D stream.reduce.input.field.separator="|" \
-input $INPUT1 \
-output $OUTPUT_DIR \
-files ./mapper.py,./reducer.py \
-mapper mapper.py \
-reducer reducer.py

echo "DONE, here is the output:"

hdfs dfs -cat $OUTPUT_DIR/*

echo "-----DONE-----"