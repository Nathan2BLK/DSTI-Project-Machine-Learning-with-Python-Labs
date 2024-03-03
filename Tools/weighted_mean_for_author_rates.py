import pandas as pd
import ast
import argparse

# Define a function to calculate weighted average rating based on author information
def weighted_avg(row, df2):
    row = ast.literal_eval(row)  # Convert the string representation of a list to a list
    total_weighted_sum = 0  # Initialize total weighted sum
    total_weights = 0  # Initialize total weights
    for author in row:
        author_id = author['author_id']  # Get author ID
        author_data = df2[df2['author_id'] == int(author_id)]  # Get author data from df2
        if not author_data.empty:
            rate = author_data['average_rating'].values[0]  # Get average rating of the author
            num_rates = author_data['ratings_count'].values[0]  # Get number of ratings of the author
            total_weighted_sum += rate * num_rates  # Update total weighted sum
            total_weights += num_rates  # Update total weights
    if total_weights == 0:
        return None  # Return None if total weights is 0 to avoid division by zero
    return total_weighted_sum / total_weights  # Calculate and return weighted average

if __name__ == "__main__":
    # Create an argument parser
    parser = argparse.ArgumentParser()
    
    # Add arguments for input and output file paths
    parser.add_argument('final_df', help='Path to the improved_dataframe.csv')
    parser.add_argument('df_author', help='Path to the author_info.csv')
    
    # Parse command-line arguments
    args = parser.parse_args()

    # Read DataFrames from CSV files
    final_df = pd.read_csv(args.final_df)
    df_author = pd.read_csv(args.df_author)

    # Apply the function to calculate the weighted average rating for each row
    final_df['authors_y'] = final_df['authors_y'].apply(lambda row: weighted_avg(row, df_author))

    # Rename columns
    final_df.rename(columns={'authors_y': 'author_mean_rates'}, inplace=True)
    final_df.rename(columns={'authors_x': 'authors'}, inplace=True)

    # Save the updated DataFrame to a CSV file
    final_df.to_csv(args.final_df, index=False)
