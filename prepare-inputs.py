import csv


def process_input_to_output(input_file_path, output_file_path):
    with open(input_file_path, mode='r') as infile, open(output_file_path, mode='w', newline='') as outfile:
        reader = csv.reader(infile)
        writer = csv.writer(outfile)

        # Write the header for the output file
        writer.writerow(['grid_id', 'col', 'row_mod_8', 'status'])

        grid_id = 1
        row_count = 0
        entries_seen = set()  # Set to keep track of unique entries

        next(reader)  # Skip the header row

        for row in reader:
            for col, value in enumerate(row):
                # Determine the status based on the cell value
                if value == 'M':
                    status = 'B'
                elif value == 'S':
                    status = 'H'
                else:
                    status = 'N'

                # Create a unique identifier for the current entry
                entry_identifier = (grid_id, col, row_count % 8, status)

                # Check for duplicates
                if entry_identifier in entries_seen:
                    # Print the grid_id if duplicate
                    print(f"Duplicate found for grid_id: {grid_id}")
                else:
                    # Write the processed data to the output file
                    writer.writerow([grid_id, col, row_count % 8, status])
                    # Update the tracking structure
                    entries_seen.add(entry_identifier)

            row_count += 1
            if row_count % 8 == 0:  # Increment grid_id after every 8 rows
                grid_id += 1


# Example usage
input_file_path = 'data/board-data.csv'
output_file_path = 'processed_data/processed-inputs.csv'
process_input_to_output(input_file_path, output_file_path)
