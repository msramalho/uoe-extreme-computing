# uoe-extreme-computing


# Resources
* Documentation: https://hadoop.apache.org/docs/r2.9.1/hadoop-streaming/HadoopStreaming.html
* HDFS lab: http://www.inf.ed.ac.uk/teaching/courses/exc/labs/hdfs.html
* Hadoop Streaming: http://www.inf.ed.ac.uk/teaching/courses/exc/labs/designing_for_streaming.html
* Example of task: http://www.inf.ed.ac.uk/teaching/courses/exc/labs/hadoop_streaming.html

# Development
* log into DICE
* `ssh hadoop.exc` to enter the cluster's resource manager node scutter02
* use `hdfs` commands

`cat title.basics.tsv | ./mapper.py | sort -t'|' -k1,1 | ./reducer.py`

### Deployment Scripts
[coursework/meta-run.sh](coursework/meta-run.sh) should be executed as `sh meta-run.sh <TASK-NO>` and will copy mapper and reducer files to DICE and then it will execute the `run.sh` which is custom made for each task. This allows for quick deployment.