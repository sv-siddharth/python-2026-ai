# =========================================================
# DAY 25 — CSV DATA HANDLING IN PYTHON
# Complete Practice File
# =========================================================

# Topics Covered:
# 1. Reading CSV files
# 2. Writing CSV files
# 3. csv module
# 4. pandas basics
# 5. DataFrames
# 6. Filtering data
# 7. Statistics
# 8. Creating CSV analytics
# =========================================================


# =========================================================
# 1. WRITING A CSV FILE USING csv MODULE
# =========================================================

import csv

student_data = [
    ["name", "marks", "city"],
    ["Rahul", 90, "Delhi"],
    ["Aman", 85, "Mumbai"],
    ["Priya", 95, "Pune"],
    ["Neha", 70, "Bangalore"]
]

with open("students.csv", mode="w", newline="") as file:
    writer = csv.writer(file)
    writer.writerows(student_data)

print("students.csv file created successfully!\n")


# =========================================================
# 2. READING CSV FILE USING csv MODULE
# =========================================================

print("Reading CSV using csv module:\n")

with open("students.csv") as file:
    data = csv.reader(file)

    for row in data:
        print(row)

print("\n")


# =========================================================
# 3. SKIPPING HEADER ROW
# =========================================================

print("Skipping header row:\n")

with open("students.csv") as file:
    data = csv.reader(file)

    next(data)  # Skip first row

    for row in data:
        print(row)

print("\n")


# =========================================================
# 4. EXTRACTING ONLY MARKS
# =========================================================

marks = []

with open("students.csv") as file:
    data = csv.reader(file)

    next(data)

    for row in data:
        marks.append(int(row[1]))

print("Marks List:")
print(marks)
print()


# =========================================================
# 5. CALCULATING AVERAGE MARKS
# =========================================================

average_marks = sum(marks) / len(marks)

print("Average Marks:", average_marks)
print()


# =========================================================
# 6. FINDING HIGHEST MARKS
# =========================================================

highest_marks = max(marks)

print("Highest Marks:", highest_marks)
print()


# =========================================================
# 7. USING PANDAS
# =========================================================

import pandas

print("Reading CSV using pandas:\n")

data = pandas.read_csv("students.csv")

print(data)
print()


# =========================================================
# 8. ACCESSING A COLUMN
# =========================================================

print("Student Names:\n")

print(data["name"])
print()


# =========================================================
# 9. CONVERT COLUMN TO LIST
# =========================================================

mark_list = data["marks"].to_list()

print("Marks converted to list:")
print(mark_list)
print()


# =========================================================
# 10. CALCULATE STATISTICS USING PANDAS
# =========================================================

print("Statistics:\n")

print("Average:", data["marks"].mean())
print("Maximum:", data["marks"].max())
print("Minimum:", data["marks"].min())
print()


# =========================================================
# 11. ACCESSING A ROW
# =========================================================

print("First Row:\n")

print(data.loc[0])
print()


# =========================================================
# 12. FILTERING DATA
# =========================================================

print("Students with marks > 85:\n")

high_scores = data[data["marks"] > 85]

print(high_scores)
print()


# =========================================================
# 13. FINDING TOPPER
# =========================================================

highest = data["marks"].max()

topper = data[data["marks"] == highest]

print("Topper Details:\n")

print(topper)
print()


# =========================================================
# 14. CREATING DATAFRAME FROM DICTIONARY
# =========================================================

employee_data = {
    "employee": ["Siddharth", "Rahul", "Aman"],
    "salary": [90000, 70000, 65000]
}

employee_df = pandas.DataFrame(employee_data)

print("Employee DataFrame:\n")

print(employee_df)
print()


# =========================================================
# 15. SAVING DATAFRAME TO CSV
# =========================================================

employee_df.to_csv("employees.csv", index=False)

print("employees.csv created successfully!\n")


# =========================================================
# 16. FILTERING EMPLOYEES WITH HIGH SALARY
# =========================================================

high_salary = employee_df[employee_df["salary"] > 70000]

print("Employees with salary > 70000:\n")

print(high_salary)
print()


# =========================================================
# 17. WEATHER DATA MINI PROJECT
# =========================================================

weather_data = {
    "day": ["Monday", "Tuesday", "Wednesday", "Thursday"],
    "temperature": [32, 35, 30, 28]
}

weather_df = pandas.DataFrame(weather_data)

weather_df.to_csv("weather.csv", index=False)

print("Weather Data:\n")

print(weather_df)
print()


average_temp = weather_df["temperature"].mean()

print("Average Temperature:", average_temp)
print()


hot_days = weather_df[weather_df["temperature"] > 30]

print("Hot Days:\n")

print(hot_days)
print()


# =========================================================
# 18. SIMPLE EXPENSE TRACKER
# =========================================================

expenses = {
    "category": ["Food", "Travel", "Shopping", "Bills"],
    "amount": [500, 1200, 2500, 3000]
}

expense_df = pandas.DataFrame(expenses)

expense_df.to_csv("expenses.csv", index=False)

print("Expense Data:\n")

print(expense_df)
print()


total_expense = expense_df["amount"].sum()

print("Total Expense:", total_expense)
print()


highest_expense = expense_df["amount"].max()

print("Highest Expense:", highest_expense)
print()


# =========================================================
# 19. ITERATING THROUGH DATAFRAME ROWS
# =========================================================

print("Iterating through student rows:\n")

for index, row in data.iterrows():
    print(
        f"Name: {row['name']} | "
        f"Marks: {row['marks']} | "
        f"City: {row['city']}"
    )

print()


# =========================================================
# 20. FINAL SUMMARY
# =========================================================

print("=================================================")
print("DAY 25 COMPLETE")
print("You learned:")
print("- CSV reading")
print("- CSV writing")
print("- csv module")
print("- pandas basics")
print("- DataFrames")
print("- Filtering")
print("- Statistics")
print("- CSV mini projects")
print("=================================================")