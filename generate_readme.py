import os
import re

# Regex to match the format: #YYYY-M-D time: MM:SS
date_time_pattern = re.compile(r"#(\d{4}-\d{1,2}-\d{1,2})\s+time:\s*(\d{1,2}:\d{2})")

# Regex to extract leading number from filename
def extract_number(filename):
    match = re.match(r"(\d+)", filename)
    return int(match.group(1)) if match else float('inf')

# Get all Python files in current directory
python_files = [f for f in os.listdir() if f.endswith(".py")]

data = []

# Read and extract timestamp info
for file in python_files:
    with open(file, "r", encoding="utf-8") as f:
        first_line = f.readline().strip()
        match = date_time_pattern.match(first_line)
        if match:
            date, time = match.groups()
            data.append((file, date, time))

# Count of solved problems
solved_count = len(data)

# Write to README.md
with open("README.md", "w", encoding="utf-8") as readme:
    readme.write("# Daniel's LeetCode\n\n")
    
    # Add dynamic badge (rendered as static on GitHub)
    readme.write(f"![Solved Problems](https://img.shields.io/badge/Solved_Problems-{solved_count}-blue)\n\n")

    readme.write("This repository contains my Python solutions to various LeetCode problems. "
                 "Each script includes a timestamp indicating when I worked on it.\n\n")

    if data:
        readme.write("## Solved Problems\n\n")
        readme.write("| File Name | Date | Time |\n")
        readme.write("|-----------|------|------|\n")
        for file, date, time in sorted(data, key=lambda x: extract_number(x[0])):
            readme.write(f"| {file} | {date} | {time} |\n")
    else:
        readme.write("No solved problems found yet.\n")

print("✅ README.md updated successfully!")
