import pandas as pd

file_path_csv = r"C:\Users\student\Desktop\DS\Book1.csv"
file_path_excel = r"C:\Users\student\Desktop\DS\MOBILE.xlsx"
file_path_text = r"C:\Users\student\Desktop\DS\Name.txt"

# Read CSV file
df_csv = pd.read_csv(file_path_csv)
print("CSV File:")
print(df_csv)

# Read Excel file
df_excel = pd.read_excel(file_path_excel)
print("\nExcel File:")
print(df_excel.head())

# Read Text file
with open(file_path_text, "r") as f:
    text = f.read()

print("\nText File:")
print(text)