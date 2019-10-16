TASK=task3

# Job 1/2

INPUT1_1=/data/small/imdb/title.basics.tsv
INPUT1_2=/data/small/imdb/title.ratings.tsv
OUTPUT_1=/user/$USER/data/output/$TASK\_job1/

hdfs dfs -rm -r $OUTPUT_1

hadoop jar /opt/hadoop/hadoop-2.9.2/share/hadoop/tools/lib/hadoop-streaming-2.9.2.jar \
-D mapred.job.name="Miguel's $TASK job 1/2- s2004624" \
-D stream.map.output.field.separator="|" \
-D stream.reduce.input.field.separator="|" \
-files ./mapper.py,./reducer_1.py,./movie1.py,./combiner_1.py \
-input $INPUT1_1 \
-input $INPUT1_2 \
-output $OUTPUT_1 \
-mapper mapper.py \
-combiner combiner_1.py \
-reducer reducer_1.py

echo "DONE Job 1/2, here is the output:"

hdfs dfs -cat $OUTPUT_1/*

echo "-----DONE Job 1/2-----"

# Job 2/2

OUTPUT_2=/user/$USER/data/output/$TASK/
hdfs dfs -rm -r $OUTPUT_2

hadoop jar /opt/hadoop/hadoop-2.9.2/share/hadoop/tools/lib/hadoop-streaming-2.9.2.jar \
-D mapred.job.name="Miguel's $TASK job 2/2- s2004624" \
-D stream.map.output.field.separator="|" \
-D stream.reduce.input.field.separator="|" \
-D stream.num.map.output.key.fields=3 \
-D mapred.reduce.tasks=1 \
-files ./reducer_2.py,./movie2.py,./combiner_2.py \
-input $OUTPUT_1 \
-output $OUTPUT_2 \
-mapper cat \
-combiner combiner_2.py \
-reducer reducer_2.py

echo "DONE Job 2/2, here is the output:"

hdfs dfs -cat $OUTPUT_2/*

echo "-----DONE Job 2/2-----"