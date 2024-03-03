import csv
import json

# Define the input and output file paths
input_file = r"Nate Solution\additionnal_data\goodreads_books.json"
output_file = r"Nate Solution\additionnal_data\books_info.csv"

# Define the columns you want to select
selected_columns = ["book_id", "country_code", "authors", "isbn13"]

with open(input_file, "r") as f_input, open(output_file, "w", newline="") as f_output:
    # Create CSV writer
    writer = csv.DictWriter(f_output, fieldnames=selected_columns)
    writer.writeheader()

    # Read JSON data line by line
    for line in f_input:
        # Parse JSON object from each line
        data = json.loads(line)
        
        # Filter the data to include only selected columns
        selected_data = {key: data[key] for key in selected_columns if key in data}
        
        # Write selected data to CSV
        writer.writerow(selected_data)