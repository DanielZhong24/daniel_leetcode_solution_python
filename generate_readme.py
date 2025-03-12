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

# Generate README.md with title and description
with open("README.md", "w", encoding="utf-8") as readme:
    readme.write("# Daniel's LeetCode 2025\n\n")
    readme.write("This repository contains my Python solutions to various LeetCode problems in 2025. "
                 "Each script includes a timestamp indicating when I worked on it.\n\n")
    
    if data:
        readme.write("## Solved Problems\n\n")
        readme.write("| File Name | Date | Time |\n")
        readme.write("|-----------|------|------|\n")
        for file, date, time in sorted(data):
            readme.write(f"| {file} | {date} | {time} |\n")
    else:
        readme.write("No solved problems found yet.\n")

print("✅ README.md updated successfully!")
