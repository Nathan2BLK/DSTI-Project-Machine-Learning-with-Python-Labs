RateBooks notebook

on RateBooks notebook I tried a first join between authors after 
transforming it from jsom to csv (script on notebook), and our first 
books csv.

the merge is helpful but not very useful because the most interesting 
column (average rating author) has not been updated for columns with 
multiple authors names even though we tried splitting this column By
creating additionnal author names columns for each additional name.

this doesnt give us the average value of author rating for all of the
authors but only the first one, first row.

improved solution notebook 

we thought about merging books and genre so we get author IDs and add 
some other features (result on DB/improved dataset)

we are trying a first training to be able to have results and See
what we can do next.



Why lightGBM?

We chose LightGBM for our ratings book predictions due to its exceptional 
performance and efficiency in handling large datasets with high-dimensional
features. 
LightGBM, a gradient boosting framework developed by Microsoft,offers 
advantages such as high speed, lower memory usage, and scalability.
Its ability to handle categorical features without requiring one-hot 
encoding and its optimization techniques, such as leaf-wise tree growth,
make it particularly suitable for our ratings book prediction task.

Feature engineering notebook 

When dealing with a large number of unique genres (1620 in our case), one-hot encoding can lead to a high-dimensional and sparse feature space.
Label encoding, may introduce a false ordinal relationship between genres, which is not desirable. 
Instead of using label encoding, we can encode each genre based on its frequency in the dataset. This can provide a meaningful representation, 
indicating how common or rare each genre is. 