# Task 3
### (10+15 marks)
Print the top rated movie of each genre for each decade between 1900 and 1999.

For the titles use the primaryTitle field and account only for entries whose titleType is ‘movie’. 
For calculating the top rated movies use the averageRating field and for the release year use the startYear field.
The output should be sorted by decade and then by genre.

For the movies with the same rating and of the same decade, print only the one with the title that comes first alphabetically.
Each decade should be represented with a single digit, starting with 0 corresponding to 1900-1909.

This task may require more than one MapReduce job. For full marks, you should not need more than two.

```python
[decade:int|genre:str|title:str]
```
