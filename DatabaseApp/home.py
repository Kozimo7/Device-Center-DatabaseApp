# Import pyodbc, so that we can connect to the database
# Import CTkTable library, so that we can display the tables
import pyodbc
from CTkTable import *

# The variable that keeps track of the number of tries to login
nr = 3

# The connection string to the database, so that we can access it
# !! The Server name (ROG-ZEPHYRUS) is the name of the computer on which the database is hosted, it needs to be changed !!
cnxn_str = ("Driver={ODBC Driver 17 for SQL Server};"
            "Server=ROG-ZEPHYRUS;"
            "Database=ServiceDispozitive;"
            "Trusted_Connection=yes;"
            "MARS_Connection=Yes;")

# Connect to the database
cnxn = pyodbc.connect(cnxn_str)
# Create a cursor, so that we can execute SQL queries on the database
cursor = cnxn.cursor()

# Display table functions
# Fuctions for displaying the client table
def afisare_tabel_client(frame3):
    # Clear the table before displaying it
    clear_table(frame3)
    
    # Get the number of rows in the table
    cursor.execute("SELECT COUNT(*) FROM dbo.Client")
    number_of_rows = cursor.fetchone()[0]
    number_of_rows = number_of_rows + 1
    
    # Get all the rows from the table
    cursor.execute("SELECT * FROM dbo.Client")
    rows = cursor.fetchall()
    value = [["First Name", "Last Name", "Email", "Phone Number", "County", "City", "Street", "Postal Code"]]
    # Create the table
    table = CTkTable(master=frame3, row=number_of_rows, column=8, values=value, header_color="#1f538d")
    table.pack(expand=True, fill="both", padx=20, pady=20)
    # Insert the rows into the table
    for i, row in enumerate(rows,start=1):
        table.insert(i, 0, row.first_name)
        table.insert(i, 1, row.last_name)
        table.insert(i, 2, row.email)
        table.insert(i, 3, row.phone_number)
        table.insert(i, 4, row.county)
        table.insert(i, 5, row.city)
        table.insert(i, 6, row.street)
        table.insert(i, 7, row.postal_code)  

# Functions for displaying the device table
def afisare_tabel_device(frame3):
    # Clear the table before displaying it
    clear_table(frame3)
    
    # Get the number of rows in the table
    cursor.execute("SELECT COUNT(*) FROM dbo.Device")
    number_of_rows = cursor.fetchone()[0]
    number_of_rows = number_of_rows + 1
    
    # Get all the rows from the table
    cursor.execute("SELECT * FROM dbo.Device")
    rows = cursor.fetchall()
    value = [["Device Type", "Model", "Serial Number", "Date Bought", "Warranty State"]]
    table = CTkTable(master=frame3, row=number_of_rows, column=5, values=value, header_color="#1f538d")
    table.pack(expand=True, fill="both", padx=20, pady=20)
    # Insert the rows into the table
    for i, row in enumerate(rows,start=1):
        table.insert(i, 0, row.device_type)
        table.insert(i, 1, row.model)
        table.insert(i, 2, row.serial_number)
        table.insert(i, 3, row.date_bought)
        table.insert(i, 4, row.warranty_state)    

# Functions for displaying the device_reparation table   
def afisare_tabel_device_reparation(frame3):
    # Clear the table before displaying it
    clear_table(frame3)
    
    # Get the number of rows in the table
    cursor.execute("SELECT COUNT(*) FROM dbo.Device_Reparation")
    number_of_rows = cursor.fetchone()[0]
    number_of_rows = number_of_rows + 1
    # Get all the rows from the table
    cursor.execute("SELECT Device.model, Spare_Part.part_type, Device_Reparation.reparation_summary, Device_Reparation.reparation_cost \
                    FROM dbo.Device_Reparation \
                    INNER JOIN Device ON Device_Reparation.id_device = Device.id_device \
                    INNER JOIN Spare_Part ON Device_Reparation.id_spare_part = Spare_Part.id_spare_part")

    rows = cursor.fetchall()
    value = [["Model Device", "Part Type", "Reparation Summary", "Reparation Cost"]]
    # Create the table
    table = CTkTable(master=frame3, row=number_of_rows, column=4, values=value, header_color="#1f538d")
    table.pack(expand=True, fill="both", padx=20, pady=20)
    # Insert the rows into the table
    for i, row in enumerate(rows,start=1):
        table.insert(i, 0, row.model)
        table.insert(i, 1, row.part_type)
        table.insert(i, 2, row.reparation_summary)
        table.insert(i, 3, row.reparation_cost)

# Functions for displaying the employee table 
def afisare_tabel_employee(frame3):
    # Clear the table before displaying it
    clear_table(frame3)
    
    # Get the number of rows in the table
    cursor.execute("SELECT COUNT(*) FROM dbo.Employee")
    number_of_rows = cursor.fetchone()[0]
    number_of_rows = number_of_rows + 1
    
    # Get all the rows from the table
    cursor.execute("SELECT * FROM dbo.Employee")
    rows = cursor.fetchall()
    value = [["CNP", "First Name", "Last Name", "Email", "Phone Number", "County", "City", "Street", "Date Hired", "Salary"]]
    # Create the table
    table = CTkTable(master=frame3, row=number_of_rows, column=10, values=value, header_color="#1f538d")
    table.pack(expand=True, fill="both", padx=20, pady=20)
    # Insert the rows into the table
    for i, row in enumerate(rows,start=1):
        table.insert(i, 0, row.cnp)
        table.insert(i, 1, row.first_name)
        table.insert(i, 2, row.last_name)
        table.insert(i, 3, row.email)
        table.insert(i, 4, row.phone_number)
        table.insert(i, 5, row.county)
        table.insert(i, 6, row.city)
        table.insert(i, 7, row.street)
        table.insert(i, 8, row.date_hired)
        table.insert(i, 9, row.salary)

# Functions for displaying the provider_parts table
def afisare_tabel_provider_parts(frame3):
    # Clear the table before displaying it
    clear_table(frame3)
    
    # Get the number of rows in the table
    cursor.execute("SELECT COUNT(*) FROM dbo.Provider_Parts")
    number_of_rows = cursor.fetchone()[0]
    number_of_rows = number_of_rows + 1
    
    # Get all the rows from the table
    cursor.execute("SELECT * FROM dbo.Provider_Parts")
    rows = cursor.fetchall()
    value = [["Provider Name", "Country", "County", "City", "Street", "Contact Name", "Contact Phone Number", "Contact Email"]]
    # Create the table
    table = CTkTable(master=frame3, row=number_of_rows, column=8, values=value, header_color="#1f538d")
    table.pack(expand=True, fill="both", padx=20, pady=20)
    # Insert the rows into the table
    for i, row in enumerate(rows,start=1):
        table.insert(i, 0, row.provider_name)
        table.insert(i, 1, row.country)
        table.insert(i, 2, row.county)
        table.insert(i, 3, row.city)
        table.insert(i, 4, row.street)
        table.insert(i, 5, row.contact_name)
        table.insert(i, 6, row.contact_phone_number)
        table.insert(i, 7, row.contact_email)

# Functions for displaying the reparation table
def afisare_tabel_reparation(frame3):
    # Clear the table before displaying it
    clear_table(frame3)
    
    # Get the number of rows in the table
    cursor.execute("SELECT COUNT(*) FROM dbo.Reparation")
    number_of_rows = cursor.fetchone()[0]
    number_of_rows = number_of_rows + 1
    
    # Get all the rows from the first table
    cursor.execute("SELECT Client.first_name, Client.last_name, Employee.first_name, Employee.last_name, Reparation.date_submission, Reparation.date_begin_work, Reparation.date_finished_work, Reparation.mentioned_problems, Reparation.final_cost \
                    FROM dbo.Reparation \
                    INNER JOIN Client ON Client.id_client = Reparation.id_client \
                    INNER JOIN Employee ON Employee.id_employee = Reparation.id_employee")
    
    rows = cursor.fetchall()
    
    # Get all the rows from the second table
    cursor.execute("SELECT Client.first_name, Client.last_name \
                    FROM dbo.Client")
    
    rows2 = cursor.fetchall()

    value = [["FirstName Client", "LastName Client", "FirstName Employee", "LastName Employee", "Date Submission", "Date Begin Work", "Date Finished Work", "Mentioned Problems", "Final Cost"]]
    # Create the table
    table = CTkTable(master=frame3, row=number_of_rows, column=9, values=value, header_color="#1f538d")
    table.pack(expand=True, fill="both", padx=20, pady=20)
   
    # Insert the first 2 rows into the table
    for i, row2 in enumerate(rows2,start=1):
        table.insert(i, 0, row2.first_name)
        table.insert(i, 1, row2.last_name)
    # Insert the rest of the rows into the table
    for i, row in enumerate(rows,start=1):
        table.insert(i, 2, row.first_name)
        table.insert(i, 3, row.last_name)
        table.insert(i, 4, row.date_submission)
        table.insert(i, 5, row.date_begin_work)
        table.insert(i, 6, row.date_finished_work)
        table.insert(i, 7, row.mentioned_problems)
        table.insert(i, 8, row.final_cost)

# Functions for displaying the spare_part table
def afisare_tabel_spare_part(frame3):
    # Clear the table before displaying it
    clear_table(frame3)
    # Get the number of rows in the table
    cursor.execute("SELECT COUNT(*) FROM dbo.Spare_Part")
    number_of_rows = cursor.fetchone()[0]
    number_of_rows = number_of_rows + 1
    # Get all the rows from the table
    cursor.execute("SELECT Provider_Parts.provider_name, Spare_Part.model, Spare_Part.part_type, Spare_Part.summary, Spare_Part.part_cost, Spare_Part.stock_quantity\
                    FROM dbo.Spare_Part \
                    INNER JOIN Provider_Parts ON Spare_Part.id_provider = Provider_Parts.id_provider")
    rows = cursor.fetchall()
    value = [["Nume Provider", "Model", "Part Type", "Summary", "Part Cost", "Stock Quantity"]]
    # Create the table
    table = CTkTable(master=frame3, row=number_of_rows, column=6, values=value, header_color="#1f538d")
    table.pack(expand=True, fill="both", padx=20, pady=20)
    # Insert the rows into the table
    for i, row in enumerate(rows,start=1):
        table.insert(i, 0, row.provider_name)
        table.insert(i, 1, row.model)
        table.insert(i, 2, row.part_type)
        table.insert(i, 3, row.summary)
        table.insert(i, 4, row.part_cost)
        table.insert(i, 5, row.stock_quantity)

# Clear table function
def clear_table(frame3):
    # Destroy all the widgets in the frame
    for widget in frame3.winfo_children():
        widget.destroy()
