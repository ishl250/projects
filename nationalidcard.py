from datetime import datetime
from fpdf import FPDF
import qrcode
import os

# -----------------------------
# Calculate age
# -----------------------------
def calculate_age(birthdate):
    today = datetime.today()
    age = today.year - birthdate.year
    if (today.month, today.day) < (birthdate.month, birthdate.day):
        age -= 1
    return age

# -----------------------------
# Generate simplified ID card
# -----------------------------
def generate_id_card(name, age, district, village):
    # QR code with info
    qr_data = f"Name: {name}\nAge: {age}\nDistrict: {district}\nVillage: {village}"
    qr_img = qrcode.make(qr_data)

    # Save QR temporarily
    desktop = os.path.join(os.path.expanduser("~"), "Desktop")
    folder = os.path.join(desktop, "NationalIDCards")
    os.makedirs(folder, exist_ok=True)
    qr_path = os.path.join(folder, "temp_qr.png")
    qr_img.save(qr_path)

    # Create PDF card
    filename = os.path.join(folder, f"{name.replace(' ', '_')}_National_ID.pdf")
    pdf = FPDF('P', 'mm', (85, 55))  # ID card size
    pdf.add_page()
    pdf.set_auto_page_break(auto=False)

    # Background & border
    pdf.set_fill_color(230, 230, 250)
    pdf.rect(0, 0, 85, 55, 'F')
    pdf.set_line_width(0.5)
    pdf.rect(1, 1, 83, 53)

    # Title
    pdf.set_font("Arial", "B", 12)
    pdf.cell(0, 8, "REPUBLIC OF RWANDA", ln=True, align="C")
    pdf.set_font("Arial", "", 8)
    pdf.cell(0, 5, "National Identification Card (Mock)", ln=True, align="C")
    pdf.ln(5)

    # Left margin
    left_margin = 5
    line_height = 5

    # Personal info
    pdf.set_font("Arial", "", 10)
    fields = [
        ("Name:", name),
        ("Age:", str(age)),
        ("District:", district),
        ("Village:", village)
    ]

    for label, value in fields:
        pdf.set_x(left_margin)
        pdf.multi_cell(60, line_height, f"{label} {value}")

    # QR Code
    pdf.image(qr_path, x=60, y=25, w=20, h=20)

    # Footer
    pdf.set_y(-10)
    pdf.set_font("Arial", "I", 6)
    pdf.cell(0, 5, "Ministry of Local Government - Rwanda", ln=True, align="C")

    pdf.output(filename)
    os.remove(qr_path)
    print(f"National ID card generated: {filename}")

# -----------------------------
# Main Program
# -----------------------------
print("=== Rwanda National ID Eligibility Checker ===")
name = input("Enter student's full name: ")
dob_input = input("Enter student's date of birth (YYYY-MM-DD): ")
district = input("Enter District: ")
village = input("Enter Village: ")

# Validate DOB
try:
    birthdate = datetime.strptime(dob_input, "%Y-%m-%d")
except ValueError:
    print("Invalid date format. Please enter in YYYY-MM-DD format.")
    exit()

age = calculate_age(birthdate)
MIN_AGE = 16

print(f"{name} is {age} years old.")
if age >= MIN_AGE:
    print(f"{name} is allowed to apply for a National ID card.")
else:
    print(f"{name} is NOT allowed to apply for a National ID card yet.")

generate_id_card(name, age, district, village)
