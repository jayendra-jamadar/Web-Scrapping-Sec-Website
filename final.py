import os
import pandas as pd

# Define the source and destination folder paths
source_folder = r'C:\Users\jayen\Output'  # Path to the output folder
destination_folder = r'C:\Users\jayen\final'  # Path for processed files

# Create the destination folder if it doesn't exist
if not os.path.exists(destination_folder):
    os.makedirs(destination_folder)

# Sheets to keep
sheets_to_keep = ['Consolidated Statement of Incom', 'Consolidated Balance Sheet']

# Loop through each company folder in the source directory
for company_folder in os.listdir(source_folder):
    company_path = os.path.join(source_folder, company_folder)

    if os.path.isdir(company_path):
        # Create a corresponding folder in the destination directory
        destination_company_path = os.path.join(destination_folder, company_folder)
        if not os.path.exists(destination_company_path):
            os.makedirs(destination_company_path)

        # Loop through each Excel file in the company folder
        for excel_file in os.listdir(company_path):
            if excel_file.endswith('.xlsx'):  # Only process Excel files
                excel_path = os.path.join(company_path, excel_file)

                # Read the Excel file with multiple sheets
                xls = pd.ExcelFile(excel_path)

                # List to store dataframes for the sheets to keep
                dfs_to_save = []

                # Check for the sheets to keep
                for sheet in sheets_to_keep:
                    if sheet in xls.sheet_names:
                        df = pd.read_excel(xls, sheet_name=sheet)
                        dfs_to_save.append((sheet, df))

                # Only save if there are sheets to save
                if dfs_to_save:
                    with pd.ExcelWriter(os.path.join(destination_company_path, excel_file), engine='openpyxl') as writer:
                        for sheet, df in dfs_to_save:
                            df.to_excel(writer, sheet_name=sheet, index=False)

print("Processing complete. The required sheets are saved in the new folder.")
