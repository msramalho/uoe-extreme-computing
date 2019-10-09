# Task 4
### (10+15 marks)
Print the names of the top 10 most popular writers, based on the number of votes that each of the titles they have authored has received. You also need to print the votes for the most popular title for each writer in this top 10.

Note that a writer who is known for certain titles (see the knownForTitles field) does not necessarily mean that they contributed in that capacity in the creation of each of those titles. Thus, apart from a person being known for a title, they should also be among the writers of that title (see title.crew.tsv file).

The output should contain 10 lines in descending order based on the number of votes. No duplicate writer names are allowed.

This task may require more than one MapReduce job. For full marks, you should not need more than two.

```python
[votes:int|writer name:str]
```
