import os
import re

# Regex to match the format: #YYYY-M-D time: MM:SS
date_time_pattern = re.compile(r"#(\d{4}-\d{1,2}-\d{1,2})\s+time:\s*(\d{1,2}:\d{2})")

# Scan for Python files in the current directory
python_files = [f for f in os.listdir() if f.endswith(".py")]

data = []

for file in python_files:
    with open(file, "r", encoding="utf-8") as f:
        first_line = f.readline().strip()  # Read first line
        
        # Check if the line matches the expected format
        match = date_time_pattern.match(first_line)
        if match:
            date, time = match.groups()
            data.append((file, date, time))

# Generate README.md with table format
if data:
    with open("README.md", "w", encoding="utf-8") as readme:
        readme.write("| File Name | Date | Time |\n")
        readme.write("|-----------|------|------|\n")
        for file, date, time in sorted(data):
            readme.write(f"| {file} | {date} | {time} |\n")

    print("✅ README.md generated successfully!")
else:
    print("⚠️ No valid date-time headers found in Python files.")
