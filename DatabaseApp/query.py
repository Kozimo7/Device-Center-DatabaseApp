from home import *

# Simple Queries with 2 or more joins    
# Afisare Device-uri care au fost reparate cu piese mai scumpe decat 30, si stoc mai mare de 5
def query1 (frame2, labelQuery):
    # Update the label with the query
    labelQuery.configure(text="Afisare Device-uri care au fost reparate cu piese mai scumpe decat 30, si stoc mai mare de 5")
    clear_table(frame2)
    # Get the number of rows
    cursor.execute("SELECT COUNT(*)\
                    FROM Device\
                    INNER JOIN Device_Reparation ON Device.id_device = Device_Reparation.id_device\
                    INNER JOIN Spare_Part ON Device_Reparation.id_spare_part = Spare_Part.id_spare_part\
                    WHERE Spare_Part.part_cost >= 30 AND Spare_Part.stock_quantity > 5")
    number_of_rows = cursor.fetchone()[0]
    number_of_rows = number_of_rows + 1
    # Execute the query
    cursor.execute("SELECT Device.model, Device.serial_number, Spare_Part.part_type, Spare_Part.part_cost, Spare_Part.stock_quantity\
                    FROM Device\
                    INNER JOIN Device_Reparation ON Device.id_device = Device_Reparation.id_device\
                    INNER JOIN Spare_Part ON Device_Reparation.id_spare_part = Spare_Part.id_spare_part\
                    WHERE Spare_Part.part_cost >= 30 AND Spare_Part.stock_quantity > 5\
                    ORDER BY Spare_Part.stock_quantity ASC")
    
    rows = cursor.fetchall()
    # Create the table
    value = [["Model", "Serial Number", "Part Type", "Part Cost", "Stock Quantity"]]
    table = CTkTable(master=frame2, row=number_of_rows, column=5,  values=value, header_color="#1f538d")
    table.pack(expand=True, fill="both", padx=20, pady=20)
    # Insert the values into the table
    for i, row in enumerate(rows,start=1):
        table.insert(i, 0, row.model)
        table.insert(i, 1, row.serial_number)
        table.insert(i, 2, row.part_type)
        table.insert(i, 3, row.part_cost)
        table.insert(i, 4, row.stock_quantity)
        
# Afisare Device-uri cu device_type = IOS care au fost reparate de angajati cu salariu mai mare decat 3000
def query2 (frame2, labelQuery):
    # Update the label with the query
    labelQuery.configure(text="Afisare Device-uri cu device_type = IOS care au fost reparate de angajati cu salariu mai mare decat 3000")
    clear_table(frame2)
    # Get the number of rows
    cursor.execute("SELECT COUNT(*)\
                    FROM Device\
                    INNER JOIN Device_Reparation ON Device.id_device = Device_Reparation.id_device\
                    INNER JOIN Reparation ON Device_Reparation.id_reparation = Reparation.id_reparation\
                    INNER JOIN Employee ON Reparation.id_employee = Employee.id_employee\
                    WHERE Device.device_type = 'IOS' AND Employee.salary > 3000")
    number_of_rows = cursor.fetchone()[0]
    number_of_rows = number_of_rows + 1
    # Execute the query
    cursor.execute("SELECT Device.model, Device.serial_number, Employee.first_name, Employee.last_name, Employee.salary\
                    FROM Device\
                    INNER JOIN Device_Reparation ON Device.id_device = Device_Reparation.id_device\
                    INNER JOIN Reparation ON Device_Reparation.id_reparation = Reparation.id_reparation\
                    INNER JOIN Employee ON Reparation.id_employee = Employee.id_employee\
                    WHERE Device.device_type = 'IOS' AND Employee.salary > 3000\
                    ORDER BY Device.model DESC")
    
    rows = cursor.fetchall()
    # Create the table
    value = [["Model", "Serial Number", "First Name", "Last Name", "Salary"]]
    table = CTkTable(master=frame2, row=number_of_rows, column=5, values=value, header_color="#1f538d")
    table.pack(expand=True, fill="both", padx=20, pady=20)
    # Insert the values into the table
    for i, row in enumerate(rows,start=1):
        table.insert(i, 0, row.model)
        table.insert(i, 1, row.serial_number)
        table.insert(i, 2, row.first_name)
        table.insert(i, 3, row.last_name)
        table.insert(i, 4, row.salary)

# Afisare Device-uri care au fost reparate de angajatii din Bucuresti, angajatii dupa 2022-01-01  
def query3 (frame2, labelQuery):
    # Update the label with the query
    labelQuery.configure(text="Afisare Device-uri care au fost reparate de angajatii din Bucuresti, angajatii dupa 2022-01-01")
    clear_table(frame2)
    # Get the number of rows
    cursor.execute("SELECT COUNT(*)\
                    FROM Device\
                    INNER JOIN Device_Reparation ON Device.id_device = Device_Reparation.id_device\
                    INNER JOIN Reparation ON Device_Reparation.id_reparation = Reparation.id_reparation\
                    INNER JOIN Employee ON Reparation.id_employee = Employee.id_employee\
                    WHERE Employee.city = 'Bucharest' AND Employee.date_hired > '2022-01-01'")
    number_of_rows = cursor.fetchone()[0]
    number_of_rows = number_of_rows + 1
    # Execute the query
    cursor.execute("SELECT Device.model, Device.serial_number, Employee.first_name, Employee.last_name, Employee.city, Employee.date_hired\
                    FROM Device\
                    INNER JOIN Device_Reparation ON Device.id_device = Device_Reparation.id_device\
                    INNER JOIN Reparation ON Device_Reparation.id_reparation = Reparation.id_reparation\
                    INNER JOIN Employee ON Reparation.id_employee = Employee.id_employee\
                    WHERE Employee.city = 'Bucharest' AND Employee.date_hired > '2022-01-01'\
                    ORDER BY Employee.first_name ASC")
    
    rows = cursor.fetchall()
    # Create the table
    value = [["Model", "Serial Number", "First Name", "Last Name", "City", "Date Hired"]]
    table = CTkTable(master=frame2, row=number_of_rows, column=6, values=value, header_color="#1f538d")
    table.pack(expand=True, fill="both", padx=20, pady=20)
    # Insert the values into the table
    for i, row in enumerate(rows,start=1):
        table.insert(i, 0, row.model)
        table.insert(i, 1, row.serial_number)
        table.insert(i, 2, row.first_name)
        table.insert(i, 3, row.last_name)
        table.insert(i, 4, row.city)
        table.insert(i, 5, row.date_hired)
    
# Afisare Angajati si numarul total de reparatii pe care le-au facut   
def query4 (frame2, labelQuery):
    # Update the label with the query
    labelQuery.configure(text="Afisare Angajati si numarul total de reparatii pe care le-au facut")
    clear_table(frame2)
    # Get the number of rows
    cursor.execute("SELECT COUNT(*)\
                    FROM Employee")
    number_of_rows = cursor.fetchone()[0]
    number_of_rows = number_of_rows + 1
    # Execute the query
    cursor.execute("SELECT Employee.first_name, Employee.last_name, Employee.date_hired, Employee.salary, COUNT(*) as NrTotalReparatii\
                    FROM Employee\
                    INNER JOIN Reparation ON Reparation.id_employee = Employee.id_employee\
                    INNER JOIN Device_Reparation ON Device_Reparation.id_reparation = Reparation.id_reparation\
                    GROUP BY Employee.first_name, Employee.last_name, Employee.date_hired, Employee.salary\
                    ORDER BY NrTotalReparatii DESC")
    
    rows = cursor.fetchall()
    # Create the table
    value = [["First Name", "Last Name", "Date Hired", "Salary", "NrTotalReparatii"]]
    table = CTkTable(master=frame2, row=number_of_rows, column=5, values=value, header_color="#1f538d")
    table.pack(expand=True, fill="both", padx=20, pady=20)
    # Insert the values into the table
    for i, row in enumerate(rows,start=1):
        table.insert(i, 0, row.first_name)
        table.insert(i, 1, row.last_name)
        table.insert(i, 2, row.date_hired)
        table.insert(i, 3, row.salary)
        table.insert(i, 4, row.NrTotalReparatii)

# Afisare Device-uri care au piesele de la ElectroParts
def query5 (frame2, labelQuery):
    # Update the label with the query
    labelQuery.configure(text="Afisare Device-uri care au piesele de la ElectroParts")
    clear_table(frame2)
    # Get the number of rows
    cursor.execute("SELECT COUNT(*)\
                    FROM Device\
                    INNER JOIN Device_Reparation ON Device.id_device = Device_Reparation.id_device\
                    INNER JOIN Spare_Part ON Device_Reparation.id_spare_part = Spare_Part.id_spare_part\
                    INNER JOIN Provider_Parts ON Spare_Part.id_provider = Provider_Parts.id_provider\
                    WHERE Provider_Parts.provider_name = 'ElectroParts'")
    number_of_rows = cursor.fetchone()[0]
    number_of_rows = number_of_rows + 1
    # Execute the query
    cursor.execute("SELECT Device.model, Device.serial_number, Spare_Part.part_type, Provider_Parts.provider_name, Provider_Parts.contact_name, Provider_Parts.contact_phone_number, Provider_Parts.contact_email\
                    FROM Device\
                    INNER JOIN Device_Reparation ON Device.id_device = Device_Reparation.id_device\
                    INNER JOIN Spare_Part ON Device_Reparation.id_spare_part = Spare_Part.id_spare_part\
                    INNER JOIN Provider_Parts ON Spare_Part.id_provider = Provider_Parts.id_provider\
                    WHERE Provider_Parts.provider_name = 'ElectroParts'\
                    ORDER BY Device.serial_number ASC")
    
    rows = cursor.fetchall()
    # Create the table
    value = [["Model", "Serial Number", "Part Type", "Provider Name", "Contact Name", "Contact Phone Number", "Contact Email"]]
    table = CTkTable(master=frame2, row=number_of_rows, column=7, values=value, header_color="#1f538d")
    table.pack(expand=True, fill="both", padx=20, pady=20)
    # Insert the values into the table
    for i, row in enumerate(rows,start=1):
        table.insert(i, 0, row.model)
        table.insert(i, 1, row.serial_number)
        table.insert(i, 2, row.part_type)
        table.insert(i, 3, row.provider_name)
        table.insert(i, 4, row.contact_name)
        table.insert(i, 5, row.contact_phone_number)
        table.insert(i, 6, row.contact_email)
 
# Afisare Device-uri si piesele lor, daca pretul final de reparatie este mai mare sau egal decat x    
def query6 (frame2, labelQuery, entry3, textconsole):
    # Get the value from the entry
    entry_get = entry3.get()
    # Check if the entry is empty, if so, return and print a message in the console
    if entry_get == "":
        string = "Final cost is empty\n"
        textconsole.insert('end', string)
        return
    # Check if the entry is a number, if not, return and print a message in the console
    if not entry_get.isdigit():
        string = "Final cost is not a number\n"
        textconsole.insert('end', string)
        entry3.delete(0, 'end')
        return
    # Create the statements, that get the number of rows and the values
    statement1 = ("SELECT COUNT(*)\
                    FROM Device\
                    INNER JOIN Device_Reparation ON Device.id_device = Device_Reparation.id_device\
                    INNER JOIN Reparation ON Device_Reparation.id_reparation = Reparation.id_reparation\
                    INNER JOIN Spare_Part ON Device_Reparation.id_spare_part = Spare_Part.id_spare_part\
                    WHERE Reparation.final_cost >= {}")
    statement2 = ("SELECT Device.model, Device.serial_number, Spare_Part.part_type, Spare_Part.summary, Spare_Part.part_cost, Device_Reparation.reparation_cost, Reparation.final_cost\
                    FROM Device\
                    INNER JOIN Device_Reparation ON Device.id_device = Device_Reparation.id_device\
                    INNER JOIN Reparation ON Device_Reparation.id_reparation = Reparation.id_reparation\
                    INNER JOIN Spare_Part ON Device_Reparation.id_spare_part = Spare_Part.id_spare_part\
                    WHERE Reparation.final_cost >= {}\
                    ORDER BY Reparation.final_cost ASC")
    # Fill in the statements with the values from the entry
    statement1 = statement1.format(entry_get)
    statement2 = statement2.format(entry_get)
    # Execute the first statement and get the number of rows
    cursor.execute(statement1)
    number_of_rows = cursor.fetchone()[0]
    number_of_rows = number_of_rows + 1
    # Update the label with the query
    labelQuery.configure(text="Afisare Device-uri si piesele lor, daca pretul final de reparatie este mai mare sau egal decat {}")
    labelQuery.configure(text=labelQuery.cget("text").format(entry_get))
    clear_table(frame2)
    # Execute the second statement and get the values
    cursor.execute(statement2)
    rows = cursor.fetchall()
    # Create the table
    value = [["Model", "Serial Number", "Part Type", "Summary", "Part Cost", "Reparation Cost", "Final Cost"]]
    table = CTkTable(master=frame2, row=number_of_rows, column=7, values=value, header_color="#1f538d")
    table.pack(expand=True, fill="both", padx=20, pady=20)
    # Insert the values into the table
    for i, row in enumerate(rows,start=1):
        table.insert(i, 0, row.model)
        table.insert(i, 1, row.serial_number)
        table.insert(i, 2, row.part_type)
        table.insert(i, 3, row.summary)
        table.insert(i, 4, row.part_cost)
        table.insert(i, 5, row.reparation_cost)
        table.insert(i, 6, row.final_cost)
        
    entry3.delete(0, 'end')

    
# Complex queries with subqueries
# Afisare Device-uri care au fost reparate de angajatul cu cel mai mare salariu
def queryComplex1 (frame2, labelQuery):
    # Update the label with the query
    labelQuery.configure(text="Afisare Device-uri care au fost reparate de angajatul cu cel mai mare salariu")
    clear_table(frame2)
    # Get the number of rows
    cursor.execute("SELECT COUNT(*)\
                    FROM Device\
                    INNER JOIN Device_Reparation ON Device.id_device = Device_Reparation.id_device\
                    INNER JOIN Reparation ON Device_Reparation.id_reparation = Reparation.id_reparation\
                    INNER JOIN Employee ON Reparation.id_employee = Employee.id_employee\
                    WHERE Employee.salary = (SELECT MAX(salary) FROM Employee)")
    number_of_rows = cursor.fetchone()[0]
    number_of_rows = number_of_rows + 1
    # Execute the query
    cursor.execute("SELECT Device.model, Device.serial_number, Employee.first_name, Employee.last_name, Employee.salary\
                    FROM Device\
                    INNER JOIN Device_Reparation ON Device.id_device = Device_Reparation.id_device\
                    INNER JOIN Reparation ON Device_Reparation.id_reparation = Reparation.id_reparation\
                    INNER JOIN Employee ON Reparation.id_employee = Employee.id_employee\
                    WHERE Employee.salary = (SELECT MAX(salary) FROM Employee)")
    
    rows = cursor.fetchall()
    # Create the table
    value = [["Model", "Serial Number", "First Name", "Last Name", "Salary"]]
    table = CTkTable(master=frame2, row=number_of_rows, column=5, values=value, header_color="#1f538d")
    table.pack(expand=True, fill="both", padx=20, pady=20)
    # Insert the values into the table
    for i, row in enumerate(rows,start=1):
        table.insert(i, 0, row.model)
        table.insert(i, 1, row.serial_number)
        table.insert(i, 2, row.first_name)
        table.insert(i, 3, row.last_name)
        table.insert(i, 4, row.salary)

# Afisare Device-uri care au fost reparate de angajati cu salariu mai mare decat media, si este din Bucuresti
def queryComplex2 (frame2, labelQuery):
    # Update the label with the query
    labelQuery.configure(text="Afisare Device-uri care au fost reparate de angajati cu salariu mai mare decat media, si este din Bucuresti")
    clear_table(frame2)
    # Get the number of rows
    cursor.execute("SELECT COUNT(*)\
                    FROM Device\
                    INNER JOIN Device_Reparation ON Device.id_device = Device_Reparation.id_device\
                    INNER JOIN Reparation ON Device_Reparation.id_reparation = Reparation.id_reparation\
                    INNER JOIN Employee ON Reparation.id_employee = Employee.id_employee\
                    WHERE Employee.salary > (SELECT AVG(salary) FROM Employee) AND Employee.county = 'Bucharest'")
    number_of_rows = cursor.fetchone()[0]
    number_of_rows = number_of_rows + 1
    # Execute the query
    cursor.execute("SELECT Device.model, Device.serial_number, Employee.first_name, Employee.last_name, Employee.salary\
                    FROM Device\
                    INNER JOIN Device_Reparation ON Device.id_device = Device_Reparation.id_device\
                    INNER JOIN Reparation ON Device_Reparation.id_reparation = Reparation.id_reparation\
                    INNER JOIN Employee ON Reparation.id_employee = Employee.id_employee\
                    WHERE Employee.salary > (SELECT AVG(salary) FROM Employee) AND Employee.county = 'Bucharest'\
                    ORDER BY Employee.salary DESC")
    
    rows = cursor.fetchall()
    # Create the table
    value = [["Model", "Serial Number", "First Name", "Last Name", "Salary"]]
    table = CTkTable(master=frame2, row=number_of_rows, column=5, values=value, header_color="#1f538d")
    table.pack(expand=True, fill="both", padx=20, pady=20)
    # Insert the values into the table
    for i, row in enumerate(rows,start=1):
        table.insert(i, 0, row.model)
        table.insert(i, 1, row.serial_number)
        table.insert(i, 2, row.first_name)
        table.insert(i, 3, row.last_name)
        table.insert(i, 4, row.salary)
        
# Afisare Angajati si piese/model, care au folosit piese in reparatii de la providerul ElectroParts, au salariu mai mare decat media si este din Bucuresti
def queryComplex3 (frame2, labelQuery):
    # Update the label with the query
    labelQuery.configure(text="Afisare Angajati si piese/model, care au folosit piese in reparatii de la providerul ElectroParts, au salariu mai mic decat media si este din Bucuresti")
    clear_table(frame2)
    # Get the number of rows
    cursor.execute("SELECT COUNT(*)\
                    FROM Employee\
                    INNER JOIN Reparation ON Employee.id_employee = Reparation.id_employee\
                    INNER JOIN Device_Reparation ON Reparation.id_reparation = Device_Reparation.id_reparation\
                    INNER JOIN Spare_Part ON Device_Reparation.id_spare_part = Spare_Part.id_spare_part\
                    INNER JOIN Provider_Parts ON Spare_Part.id_provider = Provider_Parts.id_provider\
                    WHERE Provider_Parts.provider_name = 'ElectroParts' AND Employee.salary < (SELECT AVG(salary) FROM Employee) AND Employee.county = 'Bucharest'")
    number_of_rows = cursor.fetchone()[0]
    number_of_rows = number_of_rows + 1
    # Execute the query
    cursor.execute("SELECT Employee.first_name, Employee.last_name, Employee.salary, Spare_Part.model, Spare_Part.part_type\
                    FROM Employee\
                    INNER JOIN Reparation ON Employee.id_employee = Reparation.id_employee\
                    INNER JOIN Device_Reparation ON Reparation.id_reparation = Device_Reparation.id_reparation\
                    INNER JOIN Spare_Part ON Device_Reparation.id_spare_part = Spare_Part.id_spare_part\
                    INNER JOIN Provider_Parts ON Spare_Part.id_provider = Provider_Parts.id_provider\
                    WHERE Provider_Parts.provider_name = 'ElectroParts' AND Employee.salary < (SELECT AVG(salary) FROM Employee) AND Employee.county = 'Bucharest'")
    
    rows = cursor.fetchall()
    # Create the table
    value = [["First Name", "Last Name", "Salary", "Model", "Part Type"]]
    table = CTkTable(master=frame2, row=number_of_rows, column=5, values=value, header_color="#1f538d")
    table.pack(expand=True, fill="both", padx=20, pady=20)
    # Insert the values into the table
    for i, row in enumerate(rows,start=1):
        table.insert(i, 0, row.first_name)
        table.insert(i, 1, row.last_name)
        table.insert(i, 2, row.salary)
        table.insert(i, 3, row.model)
        table.insert(i, 4, row.part_type)
        
# Afisare piese care sunt de la TechSupplies, au stoc mai mare sau egal decat x, si au fost folosite in reparatii de angajati cu salariu mai mare decat media
def queryComplex4 (frame2, labelQuery, entry3, textconsole):
    # Get the value from the entry
    entry_get = entry3.get()
    
    # Check if the entry is empty, if so, return and print a message in the console
    if entry_get == "":
        string = "Stock quantity is empty\n"
        textconsole.insert('end', string)
        return
    # Check if the entry is a number, if not, return and print a message in the console
    if not entry_get.isdigit():
        string = "Stock quantity is not a number\n"
        textconsole.insert('end', string)
        entry3.delete(0, 'end')
        return
    # Create the statements, that get the number of rows and the values
    statement1 = ("SELECT COUNT(*)\
                    FROM Spare_Part\
                    INNER JOIN Provider_Parts ON Provider_Parts.id_provider = Spare_Part.id_provider\
                    INNER JOIN Device_Reparation ON Spare_Part.id_spare_part = Device_Reparation.id_spare_part\
                    INNER JOIN Reparation ON Device_Reparation.id_reparation = Reparation.id_reparation\
                    INNER JOIN Employee ON Reparation.id_employee = Employee.id_employee\
                    WHERE Spare_Part.stock_quantity >= {} AND Provider_Parts.provider_name = 'TechSupplies' AND Employee.salary > (SELECT AVG(salary) FROM Employee)")
    
    statement2 = ("SELECT Spare_Part.part_type, Spare_Part.summary, Spare_Part.part_cost, Spare_Part.stock_quantity, Employee.first_name, Employee.last_name, Employee.salary\
                    FROM Spare_Part\
                    INNER JOIN Provider_Parts ON Provider_Parts.id_provider = Spare_Part.id_provider\
                    INNER JOIN Device_Reparation ON Spare_Part.id_spare_part = Device_Reparation.id_spare_part\
                    INNER JOIN Reparation ON Device_Reparation.id_reparation = Reparation.id_reparation\
                    INNER JOIN Employee ON Reparation.id_employee = Employee.id_employee\
                    WHERE Spare_Part.stock_quantity >= {} AND Provider_Parts.provider_name = 'TechSupplies' AND Employee.salary > (SELECT AVG(salary) FROM Employee)")
    # Fill in the statements with the values from the entry
    statement1 = statement1.format(entry_get)
    statement2 = statement2.format(entry_get)
    # Execute the first statement and get the number of rows
    cursor.execute(statement1)
    number_of_rows = cursor.fetchone()[0]
    number_of_rows = number_of_rows + 1
    # Update the label with the query
    labelQuery.configure(text="Afisare piese care sunt de la TechSupplies, au stoc mai mare decat {}, si au fost folosite in reparatii de angajati cu salariu mai mare decat media")
    labelQuery.configure(text=labelQuery.cget("text").format(entry_get))
    clear_table(frame2)
    # Execute the second statement and get the values
    cursor.execute(statement2)
    rows = cursor.fetchall()
    # Create the table
    value = [["Part Type", "Summary", "Part Cost", "Stock Quantity", "First Name", "Last Name", "Salary"]]
    table = CTkTable(master=frame2, row=number_of_rows, column=7, values=value, header_color="#1f538d")
    table.pack(expand=True, fill="both", padx=20, pady=20)
    # Insert the values into the table
    for i, row in enumerate(rows,start=1):
        table.insert(i, 0, row.part_type)
        table.insert(i, 1, row.summary)
        table.insert(i, 2, row.part_cost)
        table.insert(i, 3, row.stock_quantity)
        table.insert(i, 4, row.first_name)
        table.insert(i, 5, row.last_name)
        table.insert(i, 6, row.salary)
        
    entry3.delete(0, 'end')
    