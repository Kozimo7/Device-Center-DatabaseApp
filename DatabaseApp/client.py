from home import *

# Insert function
def insert_client(entry1, entry2, entry3, entry4, entry5, entry6, entry7, entry8, box, textconsole):
    # Statement for inserting a client, with empty values, to be filled in
    statement = ("INSERT INTO dbo.Client (first_name, last_name, email, phone_number, county, city, street, postal_code) \
                VALUES ('{}', '{}', '{}', '{}', '{}', '{}', '{}', '{}')"
                )
    # Get the values from all the entries
    entry1_get = entry1.get()
    entry2_get = entry2.get()
    entry3_get = entry3.get()
    entry4_get = entry4.get()
    entry5_get = entry5.get()
    entry6_get = entry6.get()
    entry7_get = entry7.get()
    entry8_get = entry8.get()
    
    # Check if any of the entries is empty, if so, return and print a message in the console
    if entry1_get == "":
        string = "First name is empty\n"
        textconsole.insert('end', string)
        return
    if entry2_get == "":
        string = "Last name is empty\n"
        textconsole.insert('end', string)
        return
    if entry3_get == "":
        string = "Email is empty\n"
        textconsole.insert('end', string)
        return
    if entry4_get == "":
        string = "Phone number is empty\n"
        textconsole.insert('end', string)
        return
    if entry5_get == "":
        string = "County is empty\n"
        textconsole.insert('end', string)
        return
    if entry6_get == "":
        string = "City is empty\n"
        textconsole.insert('end', string)
        return
    if entry7_get == "":
        string = "Street is empty\n"
        textconsole.insert('end', string)
        return
    if entry8_get == "":
        string = "Postal code is empty\n"
        textconsole.insert('end', string)
        return
    # Fill in the statement with the values from the entries
    statement = statement.format(entry1_get, entry2_get, entry3_get, entry4_get, entry5_get, entry6_get, entry7_get, entry8_get)
    # Execute the statement, and commit it to the database
    cursor.execute(statement)
    cnxn.commit()
    # Print a message in the console
    string = "Client inserted\n"
    textconsole.insert('end', string)
    
    # Delete the values from the entries
    entry1.delete(0, 'end')
    entry2.delete(0, 'end')
    entry3.delete(0, 'end')
    entry4.delete(0, 'end')
    entry5.delete(0, 'end')
    entry6.delete(0, 'end')
    entry7.delete(0, 'end')
    entry8.delete(0, 'end')
    # Display the table
    afisare_tabel_client(box)

# Update function  
def update_client(entry1, entry2, entry3, entry4, entry5, entry6, entry7, entry8, box, textconsole):
    # Statement for updating a client, with empty values, to be filled in
    entry1_get = entry1.get()
    entry2_get = entry2.get()
    entry3_get = entry3.get()
    entry4_get = entry4.get()
    entry5_get = entry5.get()
    entry6_get = entry6.get()
    entry7_get = entry7.get()
    entry8_get = entry8.get()
    
    # Check if variable is empty, if so, return and print a message in the console that no update was made
    nr = 0
    
    # Check if any of the entries are filled in, if so, update the database with the new values
    if entry1_get != "":
        # Statement for updating a client, with empty values, to be filled in
        statement = ("UPDATE dbo.Client \
                    SET first_name = '{}' \
                    WHERE email = '{}'"
                    )
        # Fill in the statement with the values from the entries
        statement = statement.format(entry1_get, entry3_get)
        # Execute the statement, and commit it to the database
        cursor.execute(statement)
        cnxn.commit()
        # Print a message in the console
        string = "Client first name updated\n"
        textconsole.insert('end', string)
        entry1.delete(0, 'end')
        nr = 1
    
    if entry2_get != "":
        # Statement for updating a client, with empty values, to be filled in
        statement = ("UPDATE dbo.Client \
                    SET last_name = '{}' \
                    WHERE email = '{}'"
                    )
        # Fill in the statement with the values from the entries
        statement = statement.format(entry2_get, entry3_get)
        # Execute the statement, and commit it to the database
        cursor.execute(statement)
        cnxn.commit()
        # Print a message in the console
        string = "Client last name updated\n"
        textconsole.insert('end', string)
        entry2.delete(0, 'end')
        nr = 1
        
    if entry4_get != "":
        # Statement for updating a client, with empty values, to be filled in
        statement = ("UPDATE dbo.Client \
                    SET phone_number = '{}' \
                    WHERE email = '{}'"
                    )
        # Fill in the statement with the values from the entries
        statement = statement.format(entry4_get, entry3_get)
        # Execute the statement, and commit it to the database
        cursor.execute(statement)
        cnxn.commit()
        # Print a message in the console
        string = "Client phone number updated\n"
        textconsole.insert('end', string)
        entry4.delete(0, 'end')
        nr = 1
        
    if entry5_get != "":
        # Statement for updating a client, with empty values, to be filled in
        statement = ("UPDATE dbo.Client \
                    SET county = '{}' \
                    WHERE email = '{}'"
                    )
        # Fill in the statement with the values from the entries
        statement = statement.format(entry5_get, entry3_get)
        # Execute the statement, and commit it to the database
        cursor.execute(statement)
        cnxn.commit()
        # Print a message in the console
        string = "Client county updated\n"
        textconsole.insert('end', string)
        entry5.delete(0, 'end')
        nr = 1
        
    if entry6_get != "":
        # Statement for updating a client, with empty values, to be filled in
        statement = ("UPDATE dbo.Client \
                    SET city = '{}' \
                    WHERE email = '{}'"
                    )
        # Fill in the statement with the values from the entries
        statement = statement.format(entry6_get, entry3_get)
        # Execute the statement, and commit it to the database
        cursor.execute(statement)
        cnxn.commit()
        # Print a message in the console
        string = "Client city updated\n"
        textconsole.insert('end', string)
        entry6.delete(0, 'end')
        nr = 1
        
    if entry7_get != "":
        # Statement for updating a client, with empty values, to be filled in
        statement = ("UPDATE dbo.Client \
                    SET street = '{}' \
                    WHERE email = '{}'"
                    )
        # Fill in the statement with the values from the entries
        statement = statement.format(entry7_get, entry3_get)
        # Execute the statement, and commit it to the database
        cursor.execute(statement)
        cnxn.commit()
        # Print a message in the console
        string = "Client street updated\n"
        textconsole.insert('end', string)
        entry7.delete(0, 'end')
        nr = 1
    
    if entry8_get != "":
        # Statement for updating a client, with empty values, to be filled in
        statement = ("UPDATE dbo.Client \
                    SET postal_code = '{}' \
                    WHERE email = '{}'"
                    )
        # Fill in the statement with the values from the entries
        statement = statement.format(entry8_get, entry3_get)
        # Execute the statement, and commit it to the database
        cursor.execute(statement)
        cnxn.commit()
        # Print a message in the console
        string = "Client postal code updated\n"
        textconsole.insert('end', string)
        entry8.delete(0, 'end')
        nr = 1
    
    # If no update was made, print a message in the console
    if nr == 0:
        string = "No update\n"
        textconsole.insert('end', string)
        return
    else:
        afisare_tabel_client(box)

# Delete function
def delete_client(entry3, box, textconsole):
    # Statement for deleting a client, with empty values, to be filled in
    statement = ("DELETE FROM dbo.Client \
                WHERE email = '{}'"
                )
    entry3_get = entry3.get()
    
    # Check if any of the entries is empty, if so, return and print a message in the console
    if entry3_get == "":
        string = "Email is empty\n"
        textconsole.insert('end', string)
        return
    
    # Fill in the statement with the values from the entries
    statement = statement.format(entry3_get)
    # Execute the statement, and commit it to the database
    cursor.execute(statement)
    cnxn.commit()
    # Print a message in the console
    string = "Client deleted\n"
    textconsole.insert('end', string)
    
    entry3.delete(0, 'end')
    
    afisare_tabel_client(box)
