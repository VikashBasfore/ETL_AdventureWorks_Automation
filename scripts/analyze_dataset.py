import pandas as pd

print("=" * 60)
print("AdventureWorks Workbook Analysis")
print("=" * 60)

file_path = r"downloads/AdventureWorks Sales.xlsx"

try:
    # Load workbook
    excel = pd.ExcelFile(file_path)

    print("\nWorkbook loaded successfully!")
    print("\nSheets found:")

    for sheet in excel.sheet_names:
        print(f"  - {sheet}")

    print("\n" + "=" * 60)

    # Analyze each sheet
    for sheet in excel.sheet_names:

        print(f"\nSheet Name : {sheet}")

        df = pd.read_excel(file_path, sheet_name=sheet)

        print(f"Rows       : {df.shape[0]}")
        print(f"Columns    : {df.shape[1]}")

        print("\nColumn Names:")
        print(df.columns.tolist())

        print("\nMissing Values:")
        print(df.isnull().sum())

        print("\nDuplicate Rows:")
        print(df.duplicated().sum())

        print("\nData Types:")
        print(df.dtypes)

        print("\nFirst 5 Rows:")
        print(df.head())

        print("\n" + "=" * 60)

except Exception as e:
    print("\nError occurred:")
    print(e)