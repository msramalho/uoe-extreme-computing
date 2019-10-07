INPUT_DIR=/data/supplementary/title.basics.tsv
OUTPUT_DIR=/user/$USER/data/output/labs/

hdfs dfs -rm -r $OUTPUT_DIR

hadoop jar /opt/hadoop/hadoop-2.9.2/share/hadoop/tools/lib/hadoop-streaming-2.9.2.jar \
-input $INPUT_DIR \
-output $OUTPUT_DIR \
-file ./mapper.py \
-mapper mapper.py \
-file ./reducer.py \
-reducer reducer.py

hdfs dfs -cat $OUTPUT_DIR/*