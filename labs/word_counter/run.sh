INPUT_DIR=/user/$USER/data/input/
OUTPUT_DIR=/user/$USER/data/output/labs/

hdfs dfs -rm -r $OUTPUT_DIR

hadoop jar /opt/hadoop/hadoop-2.9.2/share/hadoop/tools/lib/hadoop-streaming-2.9.2.jar \
-input $INPUT_DIR \
-output $OUTPUT_DIR \
-mapper mapper.py \
-reducer reducer.py \
-file mapper.py \
-file reducer.py

hdfs dfs -cat $OUTPUT_DIR/*