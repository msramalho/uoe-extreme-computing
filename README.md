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

````bash
2019-10-17 17:42:16,738 INFO  [main] mapreduce.Job (Job.java:monitorAndPrintJob(1647)) -  map 0% reduce 0%
2019-10-17 17:42:30,872 INFO  [main] mapreduce.Job (Job.java:monitorAndPrintJob(1647)) -  map 14% reduce 0%
2019-10-17 17:42:34,896 INFO  [main] mapreduce.Job (Job.java:monitorAndPrintJob(1647)) -  map 15% reduce 0%
2019-10-17 17:42:40,930 INFO  [main] mapreduce.Job (Job.java:monitorAndPrintJob(1647)) -  map 16% reduce 0%
2019-10-17 17:42:49,977 INFO  [main] mapreduce.Job (Job.java:monitorAndPrintJob(1647)) -  map 16% reduce 5%
2019-10-17 17:42:52,992 INFO  [main] mapreduce.Job (Job.java:monitorAndPrintJob(1647)) -  map 17% reduce 5%
2019-10-17 17:43:05,051 INFO  [main] mapreduce.Job (Job.java:monitorAndPrintJob(1647)) -  map 18% reduce 5%
2019-10-17 17:43:17,114 INFO  [main] mapreduce.Job (Job.java:monitorAndPrintJob(1647)) -  map 19% reduce 5%
2019-10-17 17:43:29,170 INFO  [main] mapreduce.Job (Job.java:monitorAndPrintJob(1647)) -  map 20% reduce 5%
2019-10-17 17:43:41,220 INFO  [main] mapreduce.Job (Job.java:monitorAndPrintJob(1647)) -  map 21% reduce 5%
2019-10-17 17:43:53,272 INFO  [main] mapreduce.Job (Job.java:monitorAndPrintJob(1647)) -  map 22% reduce 5%
2019-10-17 17:44:05,318 INFO  [main] mapreduce.Job (Job.java:monitorAndPrintJob(1647)) -  map 23% reduce 5%
2019-10-17 17:44:17,366 INFO  [main] mapreduce.Job (Job.java:monitorAndPrintJob(1647)) -  map 24% reduce 5%
2019-10-17 17:44:29,411 INFO  [main] mapreduce.Job (Job.java:monitorAndPrintJob(1647)) -  map 25% reduce 5%
2019-10-17 17:44:41,454 INFO  [main] mapreduce.Job (Job.java:monitorAndPrintJob(1647)) -  map 26% reduce 5%
2019-10-17 17:44:53,495 INFO  [main] mapreduce.Job (Job.java:monitorAndPrintJob(1647)) -  map 27% reduce 5%
2019-10-17 17:45:05,537 INFO  [main] mapreduce.Job (Job.java:monitorAndPrintJob(1647)) -  map 28% reduce 5%
2019-10-17 17:45:17,576 INFO  [main] mapreduce.Job (Job.java:monitorAndPrintJob(1647)) -  map 29% reduce 5%
2019-10-17 17:45:29,625 INFO  [main] mapreduce.Job (Job.java:monitorAndPrintJob(1647)) -  map 30% reduce 5%
2019-10-17 17:45:42,669 INFO  [main] mapreduce.Job (Job.java:monitorAndPrintJob(1647)) -  map 31% reduce 5%
2019-10-17 17:45:54,706 INFO  [main] mapreduce.Job (Job.java:monitorAndPrintJob(1647)) -  map 32% reduce 5%
2019-10-17 17:46:06,744 INFO  [main] mapreduce.Job (Job.java:monitorAndPrintJob(1647)) -  map 33% reduce 5%
2019-10-17 17:46:18,782 INFO  [main] mapreduce.Job (Job.java:monitorAndPrintJob(1647)) -  map 34% reduce 5%
2019-10-17 17:46:30,820 INFO  [main] mapreduce.Job (Job.java:monitorAndPrintJob(1647)) -  map 35% reduce 5%
2019-10-17 17:46:42,861 INFO  [main] mapreduce.Job (Job.java:monitorAndPrintJob(1647)) -  map 36% reduce 5%
2019-10-17 17:46:54,898 INFO  [main] mapreduce.Job (Job.java:monitorAndPrintJob(1647)) -  map 37% reduce 5%
2019-10-17 17:47:06,934 INFO  [main] mapreduce.Job (Job.java:monitorAndPrintJob(1647)) -  map 38% reduce 5%
2019-10-17 17:47:18,972 INFO  [main] mapreduce.Job (Job.java:monitorAndPrintJob(1647)) -  map 39% reduce 5%
2019-10-17 17:47:31,011 INFO  [main] mapreduce.Job (Job.java:monitorAndPrintJob(1647)) -  map 40% reduce 5%
2019-10-17 17:47:43,049 INFO  [main] mapreduce.Job (Job.java:monitorAndPrintJob(1647)) -  map 41% reduce 5%
2019-10-17 17:47:54,085 INFO  [main] mapreduce.Job (Job.java:monitorAndPrintJob(1647)) -  map 46% reduce 5%
2019-10-17 17:47:58,098 INFO  [main] mapreduce.Job (Job.java:monitorAndPrintJob(1647)) -  map 46% reduce 10%
2019-10-17 17:48:01,108 INFO  [main] mapreduce.Job (Job.java:monitorAndPrintJob(1647)) -  map 47% reduce 10%
2019-10-17 17:48:25,181 INFO  [main] mapreduce.Job (Job.java:monitorAndPrintJob(1647)) -  map 48% reduce 10%
2019-10-17 17:48:43,235 INFO  [main] mapreduce.Job (Job.java:monitorAndPrintJob(1647)) -  map 49% reduce 10%
2019-10-17 17:49:01,288 INFO  [main] mapreduce.Job (Job.java:monitorAndPrintJob(1647)) -  map 50% reduce 10%
2019-10-17 17:49:25,359 INFO  [main] mapreduce.Job (Job.java:monitorAndPrintJob(1647)) -  map 51% reduce 10%
2019-10-17 17:49:43,411 INFO  [main] mapreduce.Job (Job.java:monitorAndPrintJob(1647)) -  map 52% reduce 10%
2019-10-17 17:50:02,466 INFO  [main] mapreduce.Job (Job.java:monitorAndPrintJob(1647)) -  map 53% reduce 10%
2019-10-17 17:50:26,537 INFO  [main] mapreduce.Job (Job.java:monitorAndPrintJob(1647)) -  map 54% reduce 10%
2019-10-17 17:50:44,590 INFO  [main] mapreduce.Job (Job.java:monitorAndPrintJob(1647)) -  map 55% reduce 10%
2019-10-17 17:51:02,642 INFO  [main] mapreduce.Job (Job.java:monitorAndPrintJob(1647)) -  map 56% reduce 10%
2019-10-17 17:51:26,712 INFO  [main] mapreduce.Job (Job.java:monitorAndPrintJob(1647)) -  map 57% reduce 10%
2019-10-17 17:51:44,764 INFO  [main] mapreduce.Job (Job.java:monitorAndPrintJob(1647)) -  map 58% reduce 10%
2019-10-17 17:52:02,817 INFO  [main] mapreduce.Job (Job.java:monitorAndPrintJob(1647)) -  map 59% reduce 10%
2019-10-17 17:52:26,886 INFO  [main] mapreduce.Job (Job.java:monitorAndPrintJob(1647)) -  map 60% reduce 10%
2019-10-17 17:52:44,936 INFO  [main] mapreduce.Job (Job.java:monitorAndPrintJob(1647)) -  map 61% reduce 10%
2019-10-17 17:53:09,006 INFO  [main] mapreduce.Job (Job.java:monitorAndPrintJob(1647)) -  map 62% reduce 10%
2019-10-17 17:53:27,058 INFO  [main] mapreduce.Job (Job.java:monitorAndPrintJob(1647)) -  map 63% reduce 10%
2019-10-17 17:53:51,128 INFO  [main] mapreduce.Job (Job.java:monitorAndPrintJob(1647)) -  map 64% reduce 10%
2019-10-17 17:54:09,182 INFO  [main] mapreduce.Job (Job.java:monitorAndPrintJob(1647)) -  map 65% reduce 10%
2019-10-17 17:54:28,236 INFO  [main] mapreduce.Job (Job.java:monitorAndPrintJob(1647)) -  map 66% reduce 10%
2019-10-17 17:54:51,301 INFO  [main] mapreduce.Job (Job.java:monitorAndPrintJob(1647)) -  map 67% reduce 10%
2019-10-17 17:55:10,356 INFO  [main] mapreduce.Job (Job.java:monitorAndPrintJob(1647)) -  map 68% reduce 10%
2019-10-17 17:55:15,371 INFO  [main] mapreduce.Job (Job.java:monitorAndPrintJob(1647)) -  map 72% reduce 10%
2019-10-17 17:55:18,380 INFO  [main] mapreduce.Job (Job.java:monitorAndPrintJob(1647)) -  map 72% reduce 14%
2019-10-17 17:55:22,391 INFO  [main] mapreduce.Job (Job.java:monitorAndPrintJob(1647)) -  map 73% reduce 14%
2019-10-17 17:55:46,462 INFO  [main] mapreduce.Job (Job.java:monitorAndPrintJob(1647)) -  map 74% reduce 14%
2019-10-17 17:56:16,546 INFO  [main] mapreduce.Job (Job.java:monitorAndPrintJob(1647)) -  map 75% reduce 14%
2019-10-17 17:56:36,602 INFO  [main] mapreduce.Job (Job.java:monitorAndPrintJob(1647)) -  map 80% reduce 14%
2019-10-17 17:56:37,606 INFO  [main] mapreduce.Job (Job.java:monitorAndPrintJob(1647)) -  map 80% reduce 19%
2019-10-17 17:56:58,665 INFO  [main] mapreduce.Job (Job.java:monitorAndPrintJob(1647)) -  map 81% reduce 19%
2019-10-17 17:57:40,781 INFO  [main] mapreduce.Job (Job.java:monitorAndPrintJob(1647)) -  map 82% reduce 19%
2019-10-17 17:57:56,825 INFO  [main] mapreduce.Job (Job.java:monitorAndPrintJob(1647)) -  map 100% reduce 100%
2019-10-17 17:57:56,831 INFO  [main] mapreduce.Job (Job.java:monitorAndPrintJob(1660)) - Job job_1567414007728_13184 failed with state KILLED due to: Kill job job_1567414007728_13184 received from s1447836@INF.ED.AC.UK (auth:TOKEN) at 192.168.16.102
Job received Kill while in RUNNING state.
```