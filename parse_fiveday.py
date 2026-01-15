import json
import re

# Read the text file
with open('fiveday_text.txt', 'r', encoding='utf-8') as f:
    content = f.read()

print("Content length:", len(content))

# Find the start of WEEK 1
week1_start = content.find('WEEK 1')
print("week1_start:", week1_start)
if week1_start == -1:
    print("WEEK 1 not found")
    exit(1)
# Find the start of readings
start_line = "Isaiah 45-48; 1 Corinthians 13"
start_idx = content.find(start_line)
if start_idx == -1:
    print("Start of readings not found")
    exit(1)
content_from_readings = content[start_idx:]

# Find all reading lines
reading_lines = []
lines = content_from_readings.split('\n')
for line in lines:
    line = line.strip()
    if line and not line.startswith('[') and not line.startswith('WEEK') and not line.startswith('>>>') and not line.startswith('Read') and not line.startswith('www') and not line.startswith('Lower') and not 'EDITION' in line and not 'TRACK' in line and not 'Check out' in line and not re.match(r'^\d+$', line) and not '-' in line or ';' in line:
        # Looks like a reading (has ; or is a reading)
        line = re.sub(r'\s+', ' ', line)
        reading_lines.append(line)

print(f"Found {len(reading_lines)} reading lines")

# Group into weeks of 5
data_year1 = {}
for i in range(52):
    start = i * 5
    end = start + 5
    if end <= len(reading_lines):
        data_year1[f'Week{i+1}'] = reading_lines[start:end]
    else:
        print(f"Not enough readings for week {i+1}")
        break

plan = {
    "fiveday2026": {
        "name": "2026 5-Day Bible Reading Schedule",
        "description": "Read the entire Bible in one year with 5 readings per week",
        "type": "weekly",
        "duration": 1,
        "data": {
            "year1": data_year1
        }
    }
}

with open('plans/fiveday2026.json', 'w') as f:
    json.dump(plan, f, indent=2)

print("Parsed and saved fiveday2026.json")
