import json
import sys

if len(sys.argv) < 2:
    print("Usage: python convert.py <plan_name>")
    sys.exit(1)

plan_name = sys.argv[1]

# Load raw JSON
with open(f'plans/{plan_name}_raw.json', 'r') as f:
    data = json.load(f)

# Extract data2
data2 = data['data2']

# Check if it's 2 years (like mcheyne)
total_days = len(data2)
if total_days > 400:  # roughly 2 years
    duration = 2
    days_per_year = 365
else:
    duration = 1
    days_per_year = total_days

# Days per month (non-leap year)
days_per_month = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
month_names = ['January', 'February', 'March', 'April', 'May', 'June', 'July', 'August', 'September', 'October', 'November', 'December']

data_years = {}
for year in range(1, duration + 1):
    year_data = {}
    current_day = (year - 1) * days_per_year
    for month_idx, days in enumerate(days_per_month):
        month_name = month_names[month_idx]
        month_readings = []
        for day in range(days):
            if current_day < len(data2):
                readings = data2[current_day]
                joined = '; '.join(readings)
                month_readings.append(joined)
                current_day += 1
        year_data[month_name] = month_readings
    data_years[f'year{year}'] = year_data

# Create the plan structure
plan = {
    plan_name: {
        "name": data.get('name', f'{plan_name} Bible Reading Plan'),
        "description": data.get('info', f'A Bible reading plan: {plan_name}'),
        "duration": duration,
        "data": data_years
    }
}

# Save to JSON
with open(f'plans/{plan_name}.json', 'w') as f:
    json.dump(plan, f, indent=2)

print(f"Converted {plan_name}")
