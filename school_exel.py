import os
from openpyxl import Workbook

# Define directory and file path
desktop_path = os.path.join(os.path.expanduser("~"), "Desktop")
folder_path = os.path.join(desktop_path, "works")
file_path = os.path.join(folder_path, "list_of_TVET_schools.xlsx")

# Create the directory if it does not exist
if not os.path.exists(folder_path):
    os.makedirs(folder_path)
    print(f"Directory created at: {folder_path}")
else:
    print(f"Directory already exists: {folder_path}")

# Create a new Excel workbook and select the active sheet
wb = Workbook()
ws = wb.active
ws.title = "TVET Schools"

# Add headers
headers = ["District", "School name", "Trade", "Number of students"]
ws.append(headers)

# Ask user for input
district = input("Enter the district: ")
school_name = input("Enter the school name: ")
trade = input("Enter the trade: ")
while True:
    try:
        num_students = int(input("Enter the number of students: "))
        break
    except ValueError:
        print("Please enter a valid number for students.")

# Add user input as a row in Excel
user_data = [district, school_name, trade, num_students]
ws.append(user_data)

# Save the workbook
wb.save(file_path)
print(f"Excel file saved at: {file_path}")
