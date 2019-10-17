TASK=task4

# Job 1/2
INPUT_LOCATION=/data/large
INPUT1_1=$INPUT_LOCATION/imdb/name.basics.tsv
INPUT1_2=$INPUT_LOCATION/imdb/title.ratings.tsv
INPUT1_3=$INPUT_LOCATION/imdb/title.crew.tsv
OUTPUT_1=/user/$USER/assignment/$TASK\_job1/

hdfs dfs -rm -r $OUTPUT_1

# sort -t'|' -k1,2 -k3 
# This job will sort using 3 cols and partition
hadoop jar /opt/hadoop/hadoop-2.9.2/share/hadoop/tools/lib/hadoop-streaming-2.9.2.jar \
-D mapred.job.name="Miguel's $TASK job 1/2- s2004624" \
-D mapreduce.job.output.key.comparator.class=org.apache.hadoop.mapreduce.lib.partition.KeyFieldBasedComparator \
-D stream.map.output.field.separator="|" \
-D stream.reduce.input.field.separator="|" \
-D mapreduce.map.output.key.field.separator='|' \
-D stream.num.map.output.key.fields=3 \
-D mapreduce.partition.keypartitioner.options=-k1,1 \
-D mapreduce.partition.keycomparator.options="-k1,1 -k2,2 -k3,3" \
-files ./mapper1.py,./reducer1.py,./combiner.py,./movie.py \
-partitioner org.apache.hadoop.mapred.lib.KeyFieldBasedPartitioner \
-input $INPUT1_1 \
-input $INPUT1_2 \
-input $INPUT1_3 \
-output $OUTPUT_1 \
-mapper mapper1.py \
-combiner combiner.py \
-reducer reducer1.py



# echo "DONE Job 1/2, here is the output:"
# hdfs dfs -cat $OUTPUT_1/*
echo "-----DONE Job 1/2-----"

# Job 2/2
OUTPUT_2=/user/$USER/assignment/$TASK
hdfs dfs -rm -r $OUTPUT_2 

# sorting by name even though not in assignment
hadoop jar /opt/hadoop/hadoop-2.9.2/share/hadoop/tools/lib/hadoop-streaming-2.9.2.jar \
-D mapred.job.name="Miguel's $TASK job 2/2- s2004624" \
-D mapreduce.job.output.key.comparator.class=org.apache.hadoop.mapreduce.lib.partition.KeyFieldBasedComparator \
-D stream.map.output.field.separator="|" \
-D stream.reduce.input.field.separator="|" \
-D stream.num.map.output.key.fields=2 \
-D mapreduce.partition.keypartitioner.options=-k1,1 \
-D mapreduce.partition.keycomparator.options=-k1,1rn \
-D mapred.reduce.tasks=1 \
-files ./mapper2.py,./reducer2.py \
-partitioner org.apache.hadoop.mapred.lib.KeyFieldBasedPartitioner \
-input $OUTPUT_1 \
-output $OUTPUT_2 \
-mapper mapper2.py \
-combiner reducer2.py \
-reducer reducer2.py

echo "DONE Job 2/2, here is the output:"
hdfs dfs -cat $OUTPUT_2/*
echo "-----DONE Job 2/2-----"