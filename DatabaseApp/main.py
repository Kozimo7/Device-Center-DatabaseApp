# Import all the files that contain the functions for the program to run
from home import *
from client import *
from device import *
from query import *

# For the app to run, you need to install the following packages:
# pip install pyodbc
# pip install customtkinter
# pip install CTkTable

import customtkinter
from CTkTable import *

customtkinter.set_appearance_mode("Dark")
customtkinter.set_default_color_theme("dark-blue")

# Create the root window, that contains the login page
root = customtkinter.CTk()
root.geometry("600x450")
root.resizable(1,1)
root.title("Login System")

#! The username is "admin" and the password is "1234"
def showUser():
    # Verify if the username and password are correct
    global nr
    if (entry1.get() == "admin" and entry2.get() == "1234"):
        label1.configure(text = "Hello " + entry1.get() + "!")
        entry1.destroy()
        entry2.destroy()
        button1.destroy()
        label1.place(relx=0.5, rely=0.5, anchor="center")
    
        root.after(2000,openMain()) 
    else:   # if the username and password are incorrect, the user has 2 more tries to enter the correct ones
        nr = nr - 1
        if nr == 1:
            label1.configure(text = "Wrong username or password!\n" + str(nr) + " try left")
        else:
            label1.configure(text = "Wrong username or password!\n" + str(nr) + " tries left")
        if nr == 0: # if the user fails to enter the correct username and password, the program closes
            root.destroy()
     
def openMain():
    # Function for the buttons in the sidebar, to switch between pages
    def update_switch(page):
        delete_page(w2)
        page()
    
    # Function to delete the page, except the sidebar, so that the new page can be displayed
    def delete_page(window):
        for frame in window.winfo_children():
            if frame != sidebar_frame:
                frame.destroy()

    def home_page():
        # Frame Buttons for SQL tables
        frame1 = customtkinter.CTkFrame(master=w2)
        frame1.pack(pady=20, padx=20)
    
        butonsql1 = customtkinter.CTkButton(master=frame1, text="Afisare Tabel Client",command=lambda: afisare_tabel_client(frame2))
        butonsql1.pack(pady=12, padx=10, side = "left")
    
        butonsql2 = customtkinter.CTkButton(master=frame1, text="Afisare Tabel Device",command=lambda: afisare_tabel_device(frame2))
        butonsql2.pack(pady=12, padx=10, side = "left")
    
        butonsql3 = customtkinter.CTkButton(master=frame1, text="Afisare Tabel Device Reparation",command=lambda: afisare_tabel_device_reparation(frame2))
        butonsql3.pack(pady=12, padx=10, side = "left")
    
        butonsql4 = customtkinter.CTkButton(master=frame1, text="Afisare Tabel Employee",command=lambda: afisare_tabel_employee(frame2))
        butonsql4.pack(pady=12, padx=10, side = "left")
    
        butonsql5 = customtkinter.CTkButton(master=frame1, text="Afisare Tabel Provider Parts",command=lambda: afisare_tabel_provider_parts(frame2))
        butonsql5.pack(pady=12, padx=10, side = "left")
    
        butonsql6 = customtkinter.CTkButton(master=frame1, text="Afisare Tabel Reparation",command=lambda: afisare_tabel_reparation(frame2))
        butonsql6.pack(pady=12, padx=10, side = "left")
    
        butonsql7 = customtkinter.CTkButton(master=frame1, text="Afisare Tabel Spare Part",command=lambda: afisare_tabel_spare_part(frame2))
        butonsql7.pack(pady=12, padx=10, side = "left")
        
        # Frame Table
        frame2 = customtkinter.CTkFrame(master=w2)
        frame2.pack(pady=20, padx=20)
    
    def device_page():
        # Frame for device entries
        frame1 = customtkinter.CTkFrame(master=w2)
        frame1.pack(side = "left", fill="both", padx = 20, pady = 60)
        
        # Entry boxes for device page
        entryInsert1 = customtkinter.CTkEntry(master=frame1, placeholder_text="Device Type")
        entryInsert1.pack(pady=12, padx=10)
    
        entryInsert2 = customtkinter.CTkEntry(master=frame1, placeholder_text="Model")
        entryInsert2.pack(pady=12, padx=10)
    
        entryInsert3 = customtkinter.CTkEntry(master=frame1, placeholder_text="Serial Number")
        entryInsert3.pack(pady=12, padx=10)
    
        entryInsert4 = customtkinter.CTkEntry(master=frame1, placeholder_text="Date Bought")
        entryInsert4.pack(pady=12, padx=10)
    
        entryInsert5 = customtkinter.CTkEntry(master=frame1, placeholder_text="Warranty State")
        entryInsert5.pack(pady=12, padx=10)
        
        # Frame for device buttons
        frame2 = customtkinter.CTkFrame(master=frame1)
        frame2.pack(pady=120, padx=20)
        
        # Buttons for device page
        butonInsert = customtkinter.CTkButton(master=frame2, text="Insert",command=lambda: insert_device(entryInsert1,entryInsert2,entryInsert3,entryInsert4,entryInsert5, frame3, consoleText))
        butonInsert.pack(pady=12, padx=10, side = "top")
    
        butonUpdate = customtkinter.CTkButton(master=frame2, text="Update",command=lambda: update_device(entryInsert1,entryInsert2,entryInsert3,entryInsert4,entryInsert5, frame3, consoleText))
        butonUpdate.pack(pady=12, padx=10, side = "top")
    
        butonDelete = customtkinter.CTkButton(master=frame2, text="Delete",command=lambda: delete_device(entryInsert3, frame3, consoleText))
        butonDelete.pack(pady=12, padx=10, side = "top") 
        
        butonsql1 = customtkinter.CTkButton(master=frame2, text="Afisare Tabel Device",command=lambda: afisare_tabel_device(frame3))
        butonsql1.pack(pady=12, padx=10, side = "top")
        
        # Frame for device table 
        frame3 = customtkinter.CTkFrame(master=w2)
        frame3.pack(pady=20, padx=20)
        
        # Frame for console log
        frame4 = customtkinter.CTkFrame(master=w2)
        frame4.pack(pady=20, padx=20)
        
        consoleText = customtkinter.CTkTextbox(master=frame4, height=100, width=200)
        consoleText.pack(pady=12, padx=10)
    
    def client_page():
        # Frame for client entries
        frame1 = customtkinter.CTkFrame(master=w2)
        frame1.pack(side = "left", fill="both", padx = 20, pady = 60)
    
        # Entry boxes for client page
        entryInsert1 = customtkinter.CTkEntry(master=frame1, placeholder_text="First Name")
        entryInsert1.pack(pady=12, padx=10)
    
        entryInsert2 = customtkinter.CTkEntry(master=frame1, placeholder_text="Last Name")
        entryInsert2.pack(pady=12, padx=10)
    
        entryInsert3 = customtkinter.CTkEntry(master=frame1, placeholder_text="Email")
        entryInsert3.pack(pady=12, padx=10)
    
        entryInsert4 = customtkinter.CTkEntry(master=frame1, placeholder_text="Phone Number")
        entryInsert4.pack(pady=12, padx=10)
    
        entryInsert5 = customtkinter.CTkEntry(master=frame1, placeholder_text="County")
        entryInsert5.pack(pady=12, padx=10)
        
        entryInsert6 = customtkinter.CTkEntry(master=frame1, placeholder_text="City")
        entryInsert6.pack(pady=12, padx=10)
        
        entryInsert7 = customtkinter.CTkEntry(master=frame1, placeholder_text="Street")
        entryInsert7.pack(pady=12, padx=10)
        
        entryInsert8 = customtkinter.CTkEntry(master=frame1, placeholder_text="Postal Code")
        entryInsert8.pack(pady=12, padx=10)
        
        # Frame for client buttons
        frame2 = customtkinter.CTkFrame(master=frame1)
        frame2.pack(pady=30, padx=20)
        
        butonInsert = customtkinter.CTkButton(master=frame2, text="Insert",command=lambda: insert_client(entryInsert1,entryInsert2,entryInsert3,entryInsert4,entryInsert5,entryInsert6,entryInsert7,entryInsert8, frame3, consoleText))
        butonInsert.pack(pady=12, padx=10, side = "top")
    
        butonUpdate = customtkinter.CTkButton(master=frame2, text="Update",command=lambda: update_client(entryInsert1,entryInsert2,entryInsert3,entryInsert4,entryInsert5,entryInsert6,entryInsert7,entryInsert8, frame3, consoleText))
        butonUpdate.pack(pady=12, padx=10, side = "top")
    
        butonDelete = customtkinter.CTkButton(master=frame2, text="Delete",command=lambda: delete_client(entryInsert3, frame3, consoleText))
        butonDelete.pack(pady=12, padx=10, side = "top") 
        
        butonSql1 = customtkinter.CTkButton(master=frame2, text="Afisare Tabel Client",command=lambda: afisare_tabel_client(frame3))
        butonSql1.pack(pady=12, padx=10, side = "top")
        
        # Frame for client table
        frame3 = customtkinter.CTkFrame(master=w2)
        frame3.pack(pady=20, padx=20)
        
        # Frame for console log
        frame4 = customtkinter.CTkFrame(master=w2)
        frame4.pack(pady=20, padx=20)
        
        consoleText = customtkinter.CTkTextbox(master=frame4, height=100, width=200)
        consoleText.pack(pady=12, padx=10)
        
    def queries_page():
        # Frame for queries buttons
        frame1 = customtkinter.CTkFrame(master=w2)
        frame1.pack(side = "left", fill="both", padx = 20, pady = 60)
        query_font = customtkinter.CTkFont(family="Helvetica", size=20)
        
        # Frame for simple queries
        frame2 = customtkinter.CTkFrame(master=frame1)
        frame2.pack(pady=30, padx=20)
        
        # Frame for complex queries
        frame3 = customtkinter.CTkFrame(master=frame1)
        frame3.pack(pady=30, padx=20)
        
        # Simple queries with 2 or more joins
        butonQuery1 = customtkinter.CTkButton(master=frame2, text="Simple query 1", command= lambda: query1(frame5, labelQuery))    # de pus comanda si modificat labelQuery
        butonQuery1.pack(pady=12, padx=10, side = "top")
        
        butonQuery2 = customtkinter.CTkButton(master=frame2, text="Simple query 2", command = lambda: query2(frame5, labelQuery))
        butonQuery2.pack(pady=12, padx=10, side = "top")
        
        butonQuery3 = customtkinter.CTkButton(master=frame2, text="Simple query 3", command = lambda: query3(frame5, labelQuery))
        butonQuery3.pack(pady=12, padx=10, side = "top")
          
        butonQuery4 = customtkinter.CTkButton(master=frame2, text="Simple query 4", command = lambda: query4(frame5, labelQuery))
        butonQuery4.pack(pady=12, padx=10, side = "top")
        
        butonQuery5 = customtkinter.CTkButton(master=frame2, text="Simple query 5", command = lambda: query5(frame5, labelQuery))
        butonQuery5.pack(pady=12, padx=10, side = "top")
        
        butonQuery6 = customtkinter.CTkButton(master=frame2, text="Simple query 6", command = lambda: query6(frame5, labelQuery, entryQuery6, consoleText))
        butonQuery6.pack(pady=12, padx=10, side = "top")
        entryQuery6 = customtkinter.CTkEntry(master=frame2, placeholder_text="Insert minimun final cost")
        entryQuery6.pack(pady=12, padx=10)
        
        # Complex queries with subqueries
        butonQuery7 = customtkinter.CTkButton(master=frame3, text="Complex query 1", command = lambda: queryComplex1(frame5, labelQuery))
        butonQuery7.pack(pady=12, padx=10, side = "top")
        
        butonQuery8 = customtkinter.CTkButton(master=frame3, text="Complex query 2", command = lambda: queryComplex2(frame5, labelQuery))
        butonQuery8.pack(pady=12, padx=10, side = "top")
        
        butonQuery9 = customtkinter.CTkButton(master=frame3, text="Complex query 3", command = lambda: queryComplex3(frame5, labelQuery))
        butonQuery9.pack(pady=12, padx=10, side = "top")
        
        butonQuery10 = customtkinter.CTkButton(master=frame3, text="Complex query 4", command = lambda: queryComplex4(frame5, labelQuery, entryQuery10, consoleText))
        butonQuery10.pack(pady=12, padx=10, side = "top")
        entryQuery10 = customtkinter.CTkEntry(master=frame3, placeholder_text="Insert minimun stock")
        entryQuery10.pack(pady=12, padx=10)
    
        # Frame for query label
        frame4 = customtkinter.CTkFrame(master=w2)
        frame4.pack(pady=20, padx=20)
        
        labelQuery = customtkinter.CTkLabel(master=frame4, text="Press a button to see the query results", font = query_font)
        labelQuery.pack(pady=12, padx=10)
        
        # Frame for query table
        frame5 = customtkinter.CTkFrame(master=w2)
        frame5.pack(pady=20, padx=20)
        
        # Frame for console log
        frame6 = customtkinter.CTkFrame(master=w2)
        frame6.pack(pady=20, padx=20)
        
        consoleText = customtkinter.CTkTextbox(master=frame6, height=100, width=200)
        consoleText.pack(pady=12, padx=10)              
    
    # Main window
    # Create a new window, that contains the sidebar and the pages
    w2 = customtkinter.CTkToplevel()
    w2.geometry("1800x880")
    w2.resizable(1,1)
    w2.title("Device Management System")
    
    # After 2 seconds, the login window is hidden
    root.after(2000, lambda: root.withdraw())
    
    # Sidebar frame, tabview with buttons
    sidebar_frame = customtkinter.CTkFrame(master=w2, width=380, corner_radius=1)
    sidebar_frame.pack(side="left", fill="both")
    
    sidebar_font = customtkinter.CTkFont(family="Helvetica", size=28, weight="bold")
    label_sidebar = customtkinter.CTkLabel(master=sidebar_frame, text="Tab Selection", font=sidebar_font)
    label_sidebar.pack(pady=12, padx=10)
    
    # Sidebar buttons, that switch between pages    
    home_button = customtkinter.CTkButton(master=sidebar_frame, text="Home", fg_color='#201599', hover_color='#140d63', height=50, font = ('Bold', 20), command=lambda: update_switch(home_page))
    home_button.place(x = 40, y = 130)
    
    device_button = customtkinter.CTkButton(master=sidebar_frame, text="Device", fg_color='#201599', hover_color='#140d63', height=50, font = ('Bold', 20), command=lambda: update_switch(device_page))
    device_button.place(x = 40, y = 230)
    
    client_button = customtkinter.CTkButton(master=sidebar_frame, text="Client", fg_color='#201599', hover_color='#140d63', height=50, font = ('Bold', 20), command=lambda: update_switch(client_page))
    client_button.place(x = 40, y = 330)
    
    queries_button = customtkinter.CTkButton(master=sidebar_frame, text="Queries", fg_color='#201599', hover_color='#140d63', height=50, font = ('Bold', 20), command=lambda: update_switch(queries_page))
    queries_button.place(x = 40, y = 430)
    
    # When the main window is closed, the login window is closed too, and the program stops
    w2.protocol("WM_DELETE_WINDOW", root.destroy)
    
# Main login window
frame1 = customtkinter.CTkFrame(master=root)
frame1.pack(pady=20, padx=60, fill="both", expand=True)

label1 = customtkinter.CTkLabel(master=frame1, text="Login System", font=("Arial", 20))
label1.pack(pady=12, padx=10)

# Entry boxes for username and password
entry1 = customtkinter.CTkEntry(master=frame1, placeholder_text="Username")
entry1.pack(pady=12, padx=10)

entry2 = customtkinter.CTkEntry(master=frame1, placeholder_text="Password", show="*")
entry2.pack(pady=12, padx=10)

# Button for login
button1 = customtkinter.CTkButton(master=frame1, text="Login", command=showUser)
button1.pack(pady=12, padx=10)

root.mainloop()
