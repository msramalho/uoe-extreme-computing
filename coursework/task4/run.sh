TASK=task4

# Job 1/2

INPUT1_1=/data/small/imdb/name.basics.tsv
INPUT1_2=/data/small/imdb/title.ratings.tsv
INPUT1_3=/data/small/imdb/title.crew.tsv
OUTPUT_1=/user/$USER/data/output/$TASK\_job1/
# hdfs dfs -cat /user/$USER/data/output/task4_job1/*
# hdfs dfs -cat /user/$USER/data/output/task4_job1/* | grep "tt0416960"

hdfs dfs -rm -r $OUTPUT_1

# sort -t'|' -k1,2 -k3 
# This job will sort using 3 cols and partition
hadoop jar /opt/hadoop/hadoop-2.9.2/share/hadoop/tools/lib/hadoop-streaming-2.9.2.jar \
-D mapred.job.name="Miguel's $TASK job 1/2- s2004624" \
-D mapreduce.job.output.key.comparator.class=org.apache.hadoop.mapreduce.lib.partition.KeyFieldBasedComparator \
-D stream.reduce.input.field.separator="|" \
-D map.output.key.field.separator="|" \
-D stream.map.output.field.separator="|" \
	-D mapreduce.map.output.key.field.separator="|" \
-D stream.num.map.output.key.fields=1 \
-D num.key.fields.for.partition=3 \
-D mapred.text.key.partitioner.options=-k1,3 \
-D mapred.reduce.tasks=10 \
-files ./mapper1.py,./reducer1.py \
-partitioner org.apache.hadoop.mapred.lib.KeyFieldBasedPartitioner \
-input $INPUT1_1 \
-input $INPUT1_2 \
-input $INPUT1_3 \
-output $OUTPUT_1 \
-mapper mapper1.py \
-reducer cat
	# -D mapreduce.partition.keypartitioner.options=-k1,1 \
	# -D mapreduce.partition.keycomparator.options="-k1,1 -k2,2 -k3,3" \
	# -D mapreduce.partition.keycomparator.options="-k1,3" \

# -D num.key.fields.for.partition=1 \
# -D mapreduce.partition.keycomparator.options=-k1,2 \
# -D mapreduce.partition.keypartitioner.options=-k3 \

echo "DONE Job 1/2, here is the output:"

# hdfs dfs -cat $OUTPUT_1/*
hdfs dfs -cat $OUTPUT_1/* | grep "tt0416960"

exit
echo "-----DONE Job 1/2-----"

# Job 2/2

OUTPUT_2=/user/$USER/data/output/$TASK/
hdfs dfs -rm -r $OUTPUT_2 

# -r -t '|' -g -k1,2
# sorting by name even though not in assignment
hadoop jar /opt/hadoop/hadoop-2.9.2/share/hadoop/tools/lib/hadoop-streaming-2.9.2.jar \
-D mapred.job.name="Miguel's $TASK job 2/2- s2004624" \
 -D mapreduce.job.output.key.comparator.class=org.apache.hadoop.mapreduce.lib.partition.KeyFieldBasedComparator \
-D mapred.text.key.comparator.options=-nr
-D mapreduce.partition.keypartitioner.options=-k1,2 \
-D stream.map.output.field.separator="|" \
-D stream.reduce.input.field.separator="|" \
-D stream.num.map.output.key.fields=2 \
-D mapred.reduce.tasks=1 \
-files ./mapper2.py,./reducer2.py \
-input $OUTPUT_1 \
-output $OUTPUT_2 \
-mapper mapper2.py \
-reducer reducer2.py

echo "DONE Job 2/2, here is the output:"

hdfs dfs -cat $OUTPUT_2/*

echo "-----DONE Job 2/2-----"