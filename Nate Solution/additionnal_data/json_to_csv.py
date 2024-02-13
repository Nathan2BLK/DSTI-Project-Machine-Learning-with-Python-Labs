import csv
import json

# Define the input and output file paths
input_file = r"Nate Solution\additionnal_data\goodreads_book_authors.json"
output_file = r"Nate Solution\additionnal_data\author_info.csv"

# Read JSON data
with open(input_file, "r") as f_input, open(output_file, "w", newline="") as f_output:
    # Define field names
    field_names_author = ["average_rating", "author_id", "text_reviews_count", "name", "ratings_count"]

    writer = csv.DictWriter(f_output, fieldnames=field_names_author)
    writer.writeheader()

    # Read JSON data line by line
    for line in f_input:
        # Parse JSON object from each line
        data = json.loads(line)
        
        # Write parsed data to CSV
        writer.writerow(data)