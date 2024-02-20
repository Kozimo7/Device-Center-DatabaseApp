from home import *

# Insert function
def insert_device(entry1, entry2, entry3, entry4, entry5, box, textconsole):
    # Statement for inserting a device, with empty values, to be filled in
    statement = ("INSERT INTO dbo.Device (device_type, model, serial_number, date_bought, warranty_state) \
                VALUES ('{}', '{}', '{}', '{}', '{}')"
                )
    # Get the values from all the entries
    entry1_get = entry1.get()
    entry2_get = entry2.get()
    entry3_get = entry3.get()
    entry4_get = entry4.get()
    entry5_get = entry5.get()
    
    # Check if any of the entries is empty, if so, return and print a message in the console
    if entry1_get == "":
        string = "Device type is empty\n"
        textconsole.insert('end', string)
        return
    if entry2_get == "":
        string = "Model is empty\n"
        textconsole.insert('end', string)
        return
    if entry3_get == "":
        string = "Serial number is empty\n"
        textconsole.insert('end', string)
        return
    if entry4_get == "":
        string = "Date bought is empty\n"
        textconsole.insert('end', string)
        return
    if entry5_get == "":
        string = "Warranty state is empty\n"
        textconsole.insert('end', string)
        return
    
    # Fill in the statement with the values from the entries
    statement = statement.format(entry1_get, entry2_get, entry3_get, entry4_get, entry5_get)
    # Execute the statement, and commit it to the database
    cursor.execute(statement)
    cnxn.commit()
    # Print a message in the console
    string = "Device inserted\n"
    textconsole.insert('end', string)
    
    # Delete the values from the entries
    entry1.delete(0, 'end')
    entry2.delete(0, 'end')
    entry3.delete(0, 'end')
    entry4.delete(0, 'end')
    entry5.delete(0, 'end')
    # Display the table
    afisare_tabel_device(box)

# Update function 
def update_device(entry1, entry2, entry3, entry4, entry5, box, textconsole):
    # Statement for updating a device, with empty values, to be filled in
    entry1_get = entry1.get()
    entry2_get = entry2.get()
    entry3_get = entry3.get()
    entry4_get = entry4.get()
    entry5_get = entry5.get()
    
    # Check if the variable is 0, if so, return and print a message in the console that no update was made
    nr = 0
    
    # Check if any of the entries are filled in, if so, update the database with the new values and nr = 1
    if entry1_get != "":
        # Statement for updating the device type
        statement = ("UPDATE dbo.Device \
                    SET device_type = '{}' \
                    WHERE serial_number = '{}'"
                    )
        # Fill in the statement with the values from the entries
        statement = statement.format(entry1_get, entry3_get)
        # Execute the statement, and commit it to the database
        cursor.execute(statement)
        cnxn.commit()
        # Print a message in the console
        string = "Device type updated\n"
        textconsole.insert('end', string)
        entry1.delete(0, 'end')
        nr = 1
        
    if entry2_get != "":
        # Statement for updating the device model
        statement = ("UPDATE dbo.Device \
                    SET model = '{}' \
                    WHERE serial_number = '{}'"
                    )
        # Fill in the statement with the values from the entries
        statement = statement.format(entry2_get, entry3_get)
        # Execute the statement, and commit it to the database
        cursor.execute(statement)
        cnxn.commit()
        # Print a message in the console
        string = "Device model updated\n"
        textconsole.insert('end', string)
        entry2.delete(0, 'end')
        nr = 1
        
    if entry4_get != "":
        # Statement for updating the device date bought
        statement = ("UPDATE dbo.Device \
                    SET date_bought = '{}' \
                    WHERE serial_number = '{}'"
                    )
        # Fill in the statement with the values from the entries
        statement = statement.format(entry4_get, entry3_get)
        # Execute the statement, and commit it to the database
        cursor.execute(statement)
        cnxn.commit()
        # Print a message in the console
        string = "Device date bought updated\n"
        textconsole.insert('end', string)
        entry4.delete(0, 'end')
        nr = 1
        
    if entry5_get != "":
        # Statement for updating the device warranty state
        statement = ("UPDATE dbo.Device \
                    SET warranty_state = '{}' \
                    WHERE serial_number = '{}'"
                    )
        # Fill in the statement with the values from the entries
        statement = statement.format(entry5_get, entry3_get)
        # Execute the statement, and commit it to the database
        cursor.execute(statement)
        cnxn.commit()
        # Print a message in the console
        string = "Device warranty updated\n"
        textconsole.insert('end', string)
        entry5.delete(0, 'end')
        nr = 1
        
    # If no update was made, print a message in the console
    if nr == 0:
        string = "No update\n"
        textconsole.insert('end', string)
        return
    else:
        afisare_tabel_device(box)

# Delete function
def delete_device(entry3, box, textconsole):
    # Statement for deleting a device, with empty values, to be filled in
    statement = ("DELETE FROM dbo.Device \
                WHERE serial_number = '{}'"
                )
    entry3_get = entry3.get()
    
    # Check if the entry is empty, if so, return and print a message in the console
    if entry3_get == "":
        string = "Serial number is empty\n"
        textconsole.insert('end', string)
        return
    
    # Fill in the statement with the values from the entries
    statement = statement.format(entry3_get)
    # Execute the statement, and commit it to the database
    cursor.execute(statement)
    cnxn.commit()
    # Print a message in the console
    string = "Device deleted\n"
    textconsole.insert('end', string)
    
    entry3.delete(0, 'end')
    
    afisare_tabel_device(box)
