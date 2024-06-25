import re
import csv

# Step 1: Read from target.txt
with open('data/target.txt', 'r') as file:
    cases = file.readlines()

case_numbers = []
coordinates = []
case_number_counts = {}  # Dictionary to count occurrences of each case number

for case in cases:
    match = re.match(r"Case (\d+): Attack at \((\d+), (\d+)\)", case)
    if match:
        case_number = int(match.group(1))
        x = int(match.group(2))
        y = int(match.group(3))
        case_numbers.append(case_number)
        coordinates.append((x, y))

        # Count occurrences of case numbers
        if case_number in case_number_counts:
            case_number_counts[case_number] += 1
        else:
            case_number_counts[case_number] = 1

# Step 2: Process the cases
# Check for gaps in case numbers
expected_cases = set(range(1, max(case_numbers) + 1))
actual_cases = set(case_numbers)
missing_cases = expected_cases - actual_cases
if missing_cases:
    print(f"Missing case numbers: {sorted(missing_cases)}")

# Identify and print duplicate case numbers
duplicate_case_numbers = [case_number for case_number,
                          count in case_number_counts.items() if count > 1]
if duplicate_case_numbers:
    print(f"Duplicate case numbers: {sorted(duplicate_case_numbers)}")

# Check for duplicate coordinates
if len(coordinates) != len(set(coordinates)):
    print("There are duplicate coordinates.")

# Step 3: Write the results to processed-targets.csv
with open('processed_data/processed-targets.csv', 'w', newline='') as csvfile:
    csvwriter = csv.writer(csvfile)
    csvwriter.writerow(['x', 'y'])  # Writing the header
    for coord in coordinates:
        csvwriter.writerow(list(coord))
