
# Full Stack Python Projects

Welcome to **[ishl250’s Full Stack Python Projects](https://www.github.com/ishl250/)**!
This repository contains multiple Python projects developed as part of full-stack development exercises. These projects demonstrate practical skills in banking systems, shopping cart applications, Excel file generation, calculators, student age verification, national ID card generation, and deployment automation scripts.

---

## Table of Contents

1. [Bank Transactions System](#1-bank-transactions-system)
2. [Shopping Cart System](#2-shopping-cart-system)
3. [TVET Schools Excel Generator](#3-tvet-schools-excel-generator)
4. [Simple Calculator](#4-simple-calculator)
5. [Advanced Bank Account with OOP](#5-advanced-bank-account-with-oop)
6. [Student Age Verification for National ID](#6-student-age-verification-for-national-id)
7. [Deployment Automation Script for BERWA School](#7-deployment-automation-script-for-berwa-school)

---

## 1. Bank Transactions System

**Description:**
Python program to perform basic bank transactions (deposit and withdraw) while ensuring a minimum balance of 100 Rwf. All transactions display messages confirming the actions.

**Features:**

* Deposit funds
* Withdraw funds with minimum balance check
* Transaction messages displayed

**Usage:**
Run the Python script and follow the prompts to perform deposits or withdrawals.

---

## 2. Shopping Cart System

**Description:**
Developed for **CODEX DEV LTD**, this Python program implements a shopping cart feature. Users can add, remove, or empty items from the cart. Cart data is stored in a CSV file `cart.csv`.

**Features:**

* Add items to cart
* Remove items from cart
* Empty the cart
* Persist cart data in `cart.csv`

**Usage:**
Run the Python script and follow prompts to manage the shopping cart.

---

## 3. TVET Schools Excel Generator

**Description:**
Python program that generates an Excel file containing a list of TVET schools. The file includes headers (`District`, `School Name`, `Trade`, `Number of Students`) and sample data. Saved in a `works` folder on Desktop.

**Features:**

* Creates Excel file with headers
* Adds sample data
* Automatically creates folder if missing

**Usage:**
Run the Python script; the Excel file will be generated on your Desktop.

---

## 4. Simple Calculator

**Description:**
Python program for basic calculations (addition, subtraction, multiplication, division) based on user input.

**Features:**

* Accepts two numbers
* Supports add, subtract, multiply, divide
* Displays results

**Usage:**
Run the script, input numbers, select operation, and see results.

---

## 5. Advanced Bank Account with OOP

**Description:**
Python bank account system demonstrating **Object-Oriented Programming**. Features deposit, withdrawal, balance display, transaction history, and PDF report generation. Uses **class, inheritance, polymorphism, and encapsulation**.

**Features:**

* Deposit and withdrawal with rules
* Encapsulation of account data
* Polymorphism for withdrawal behavior
* Transaction history
* PDF report generation

**Usage:**
Run the Python script and interact with the account system.

---

## 6. Student Age Verification for National ID

**Description:**
Python program to calculate the age of students and determine eligibility for a national ID card. Generates a PDF ID card with QR code containing Name, Age, District, and Village.

**Features:**

* Calculate age from date of birth
* Check eligibility for national ID
* Generate ID card PDF with QR code

**Usage:**
Run the script, input student details, check eligibility, and generate a PDF ID card.

---

## 7. Deployment Automation Script for BERWA School

**Description:**
Python script to automate tasks after deployment of BERWA School web application. Automates server configuration, database backup, and sends email notifications.

**Features:**

* Server configuration (permissions, setup)
* Database backup with timestamp
* Email notifications after deployment
* Secure, modular design

**Usage:**
Run the script after deploying the web application to automate tasks.

---

## Requirements

* Python 3.x
* Libraries: `fpdf`, `qrcode[pil]`, `openpyxl`
* MySQL for database backup
* Email credentials for notifications (SMTP)

Install dependencies with:

```bash
pip install fpdf qrcode[pil] openpyxl
```

---

## Folder Structure

```
FullStackPythonProjects/
│
├─ bank_transactions/       # Bank transactions program
├─ shopping_cart/           # Shopping cart CSV system
├─ tvet_schools_excel/      # Excel generator
├─ simple_calculator/       # Calculator
├─ bank_oop/                # OOP-based bank account system
├─ national_id_card/        # Age verification & ID card generation
├─ deployment_automation/   # BERWA School deployment script
└─ README.md
```

---

## Author

**ishl250** – Full Stack Developer
GitHub: [https://github.com/ishl250](https://github.com/ishl250)
Email: [ishimwejeanclaude088@gmail.com](mailto:ishimwejeanclaude088@gmail.com)


