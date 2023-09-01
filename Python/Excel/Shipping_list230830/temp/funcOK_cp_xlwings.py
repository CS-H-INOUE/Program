import os
import openpyxl
import xlwings as xw
from datetime import datetime

def main():
    """
    Main function to copy rows with matching current day from Excel sheet.
    """
    try:
        # Get current year and month
        current_year = datetime.now().year
        current_month = datetime.now().month
        
        # Create Excel file path
        excel_path = f"./{current_year}/{current_month:02}.xlsx"
        sheet_name = f"{current_month}月"
        
        # Check if the file exists
        if os.path.exists(excel_path):
            # Open xlwings application
            app = xw.App(visible=False)
            wb = app.books.open(excel_path)
            sheet = wb.sheets[sheet_name]
            
            # Get current day
            current_day = datetime.now().day
            
            # Create a new workbook
            new_wb = openpyxl.Workbook()
            new_sheet = new_wb.active
            new_sheet.title = "copy"
            
            # Logic: Copy rows with matching current day
            used_range = sheet.used_range
            for row in used_range.rows:
                date_str = row[2].value
                if date_matches_current_day(date_str, current_day):
                    new_row = []
                    for cell in row:
                        if isinstance(cell.value, str) and cell.value.startswith("="):
                            try:
                                value = sheet.range(cell.address).value
                                new_row.append(value)
                            except:
                                new_row.append(cell.value)
                        else:
                            new_row.append(cell.value)
                    new_sheet.append(new_row)
            
            # Save the new file
            new_file_path = f"./copy_{current_year}_{current_month:02}.xlsx"
            new_wb.save(new_file_path)
            
            print("Copy completed.")
            
            # Quit xlwings application
            app.quit()
        else:
            print(f"{excel_path} does not exist.")
    except Exception as e:
        print(f"An error occurred: {e}")

# Logic: Check if date matches current day
def date_matches_current_day(date_str, current_day):
    """
    Check if the given date string matches the current day.
    
    Args:
        date_str (str): The date string in the format 'month/day'.
        current_day (int): The current day of the month.
    
    Returns:
        bool: True if the date matches the current day, False otherwise.
    """
    try:
        month, day = map(int, date_str.split('/'))
        return month == datetime.now().month and day == current_day
    except:
        return False

if __name__ == "__main__":
    main()
