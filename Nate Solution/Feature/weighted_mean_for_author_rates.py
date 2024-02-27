import pandas
import ast

final_df = pandas.read_csv(r"Nate Solution\DataBase\improved_dataset.csv")
df_author = pandas.read_csv(r"Nate Solution\additionnal_data\author_info.csv")

def parse_list(s):
    try:
        # Remove square brackets and split by comma
        items = s.strip('[]').split(',')
        # Convert items to integers
        return [int(item.strip()) for item in items]
    except ValueError:
        return []
    
def weighted_avg(row, df2):
    row = ast.literal_eval(row)
    total_weighted_sum = 0
    total_weights = 0
    for author_id in row:
        author_data = df2[df2['author_id'] == int(author_id)]
        if not author_data.empty:
            rate = author_data['average_rating'].values[0]
            num_rates = author_data['ratings_count'].values[0]
            total_weighted_sum += rate * num_rates
            total_weights += num_rates
    if total_weights == 0:
        return None
    return total_weighted_sum / total_weights


# Apply the function to calculate the weighted average
final_df['authors_y'] = final_df['authors_y'].apply(lambda row: weighted_avg(row, df_author))

final_df.rename(columns={'authors_y': 'author_mean_rates'}, inplace=True)
final_df.rename(columns={'authors_x': 'authors'}, inplace=True)

final_df.to_csv(r"Nate Solution\DataBase\improved_dataset.csv", index=False)