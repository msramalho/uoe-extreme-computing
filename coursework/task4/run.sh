TASK=task4
INPUT_LOCATION=/data/large

# Job 1/2
INPUT1_1=$INPUT_LOCATION/imdb/title.ratings.tsv
INPUT1_2=$INPUT_LOCATION/imdb/title.crew.tsv
OUTPUT_1=/user/$USER/assignment/$TASK\_job1/

hdfs dfs -rm -r $OUTPUT_1

hadoop jar /opt/hadoop/hadoop-2.9.2/share/hadoop/tools/lib/hadoop-streaming-2.9.2.jar \
-D mapred.job.name="Miguel's $TASK job 1/2- s2004624" \
-D mapreduce.job.output.key.comparator.class=org.apache.hadoop.mapreduce.lib.partition.KeyFieldBasedComparator \
-D stream.map.output.field.separator="|" \
-D stream.reduce.input.field.separator="|" \
-D mapreduce.map.output.key.field.separator='|' \
-D stream.num.map.output.key.fields=1 \
-files ./mapper1.py,./reducer1.py,./movie.py,./combiner1.py \
-input $INPUT1_1 \
-input $INPUT1_2 \
-output $OUTPUT_1 \
-mapper mapper1.py \
-combiner combiner1.py \
-reducer reducer1.py

# echo "DONE Job 1/2, here is the output:"
# hdfs dfs -cat $OUTPUT_1/*
echo "-----DONE Job 1/2-----"

# Job 2/2
INPUT2_1=$INPUT_LOCATION/imdb/name.basics.tsv
OUTPUT_2=/user/$USER/assignment/$TASK
hdfs dfs -rm -r $OUTPUT_2 

hadoop jar /opt/hadoop/hadoop-2.9.2/share/hadoop/tools/lib/hadoop-streaming-2.9.2.jar \
-D mapred.job.name="Miguel's $TASK job 2/2- s2004624" \
-D stream.map.output.field.separator="|" \
-D stream.reduce.input.field.separator="|" \
-D mapreduce.map.output.key.field.separator='|' \
-D stream.num.map.output.key.fields=2 \
-D mapred.reduce.tasks=1 \
-files ./reducer2.py,./mapper2.py,./writer.py,./combiner2.py \
-input $INPUT2_1 \
-input $OUTPUT_1 \
-output $OUTPUT_2 \
-mapper mapper2.py \
-combiner combiner2.py \
-reducer reducer2.py
# -reducer reducer2.py

echo "DONE Job 2/2, here is the output:"
hdfs dfs -cat $OUTPUT_2/*
echo "-----DONE Job 2/2-----"