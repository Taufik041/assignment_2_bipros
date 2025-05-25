import csv
import os

# File path for the CSV
CSV_FILE = "employees.csv"

# Initialize employee list
employee_list = []

def load_from_csv():
    """Load employees from CSV file"""
    global employee_list
    
    if not os.path.exists(CSV_FILE):
        # Create file with headers if it doesn't exist
        with open(CSV_FILE, 'w', newline='') as file:
            writer = csv.writer(file)
            writer.writerow(['id', 'name', 'company'])
        
        # Add initial data
        employee_list = [
            {"id": 1, "name": "Taufik", "company": "A"},
            {"id": 2, "name": "Taufik2", "company": "B"}
        ]
        save_to_csv()
        return employee_list
    
    # Read existing data
    employee_list = []
    with open(CSV_FILE, 'r', newline='') as file:
        reader = csv.DictReader(file)
        for row in reader:
            employee_list.append({
                "id": int(row['id']),
                "name": row['name'],
                "company": row['company']
            })
    
    return employee_list

def save_to_csv():
    """Save employee list to CSV file"""
    with open(CSV_FILE, 'w', newline='') as file:
        writer = csv.DictWriter(file, fieldnames=['id', 'name', 'company'])
        writer.writeheader()
        writer.writerows(employee_list)

# Initialize by loading from CSV
employee_list = load_from_csv()