import csv  # This imports csv library(for database)
from tkinter import *  # This imports everything from tkinter
from tkinter import messagebox  # This import just messagebox from tkinter library
import pandas as pd  # This imports pandas libray as an alias(pd)
import os  # This imports os library(for checking if a file is empty)


#  Here I created a "Search" class, which creates an object of this class when the search bar button from start_program
#  library is clicked, and once it's created, we can check the employee's details, such as Name, Last name etc... and
#  we can edit and save the employee's information
class Search:
    # This lists I'll use later for button's options of states and vehicles
    states = ['active', 'inactive', 'fired']
    vehicles = ['Company scooter', 'Company bike', 'Company car', 'Personal car',
                'Personal scooter/moto', 'Personal electric scooter/bike']

    #  These variables I'll use later for get the actual(which will be the old) email, phone number, status and vehicle
    #  and compare them with the new email, phone number etc... when someone wants to edit them
    old_email = ''
    old_phone_number = ''
    old_status = ''
    old_vehicle = ''

    #  These variables I'll use for checking if the new email is valid
    extensions = ['gmail.com', 'yahoo.com', 'gmail.ro', 'yahoo.ro']
    extension_validation = False

    def __init__(self, frame):

        #  This is the window where the all widgets will be working with
        self.frame = frame

        #  Search bar box
        #  The next three lines create an entry widget(which is an input box) that belongs to the frame,
        #  with some specified arguments, such as font, width etc... and inserts a specific message for helping the user
        #  that wants to search an employee, what to type in, and ofc placed depending on x and y-axis(in this case
        #  is placed in the middle of the frame, close to the top edge). In this widget we search for employee's details
        #  (by his phone number or email(because these two are unique, and belong to one employee)).
        self.search_bar_input = Entry(frame, width=40, font=('Calibre', 14), fg='#b3b3b3', relief='sunken',
                                      highlightthickness=3, highlightbackground='gray')
        self.search_bar_input.insert(0, 'Search for employees(by email or phone)')
        self.search_bar_input.place(relx=0.5, y=50, anchor=CENTER)
        #  The next two lines create a label widget(which is a text) that belongs to the frame too, with some specified
        #  arguments, and placed depending on x and y. This widget will show a message, depending on what was searched
        #  in search_bar_input.
        self.search_bar_label_info = Label(frame, font=('Arial', 10, 'bold'), bg='#ffdd99')
        self.search_bar_label_info.place(x=200, y=70)

        #  Name
        #  The next four lines create two label widgets(one for the NAME itself, and one for the name that will be
        #  displayed next to 'NAME' if that employee exists), and placed them depending on x and y-axis.
        self.name_employee = Label(frame, font=('Arial', 14, 'bold'), bg='#ffdd99')
        self.name_employee.place(x=100, y=100)
        self.name_description = Label(frame, text='NAME:', font=('Calibre', 16, 'bold italic'), bg='#ffdd99')
        self.name_description.place(x=20, y=100)

        #  Last Name
        #  Same as above, but now for LAST NAME
        self.last_name_employee = Label(frame, font=('Arial', 14, 'bold'), bg='#ffdd99')
        self.last_name_employee.place(x=170, y=200)
        self.last_name_description = Label(frame, text='LAST NAME:', font=('Calibre', 16, 'bold italic'), bg='#ffdd99')
        self.last_name_description.place(x=20, y=200)

        #  CNP
        #  Same as above, but now for CNP
        self.cnp_employee = Label(frame, font=('Arial', 14, 'bold'), bg='#ffdd99')
        self.cnp_employee.place(x=80, y=300)
        self.cnp_description = Label(frame, text='CNP:', font=('Calibre', 16, 'bold italic'), bg='#ffdd99')
        self.cnp_description.place(x=20, y=300)

        #  Email
        #  Same as above, but now for EMAIL, with small differences: Here I created extra an entry widget and a label
        #  widget, with some specified arguments, that belong to the frame, and where it can be edited the
        #  new employee's email, and a message will be displayed after the email was edited(to tell if the new email
        #  is valid or not), and the all three labels(excepting the entry), are placed depending on x and y-axis.
        self.email_employee = Label(frame, font=('Arial', 14, 'bold'), bg='#ffdd99')
        self.email_employee.place(x=500, y=100)
        self.email_description = Label(frame, text='EMAIL:', font=('Calibre', 16, 'bold italic'), bg='#ffdd99')
        self.email_description.place(x=420, y=100)
        self.email_edit = Entry(frame, bg='#ffdd99', width=25, font=('Arial', 14, 'bold'))
        self.new_email_info = Label(frame, bg='#ffdd99', font=('Arial', 8, 'bold'))
        self.new_email_info.place(x=420, y=132)

        #  Phone Number
        #  Same as Email, but now for PHONE NUMBER
        self.phone_number_employee = Label(frame, font=('Arial', 14, 'bold'), bg='#ffdd99')
        self.phone_number_employee.place(x=610, y=200)
        self.phone_number_description = Label(frame, text='PHONE NUMBER:', font=('Calibre', 16, 'bold italic'),
                                              bg='#ffdd99')
        self.phone_number_description.place(x=420, y=200)
        self.phone_number_edit = Entry(frame, bg='#ffdd99', width=11, font=('Arial', 14, 'bold'))
        self.new_phone_number_info = Label(frame, bg='#ffdd99', font=('Arial', 8, 'bold'))
        self.new_phone_number_info.place(x=420, y=225)

        #  Status
        #  Same as above, but now for STATUS, with small differences: Here I created extra an option-menu widget(which
        #  is a menu with some options to choose(that are stored in states list)) instead of a new label and entry,
        #  with some specified arguments, that belongs to the frame, and the first option that will be displayed once
        #  the button is displayed, will be the actual status of the employee. And just those two labels are placed
        #  depending on x and y-axis. This option-menu widget is created for edit the employee's status.
        self.status_employee = Label(frame, font=('Arial', 14, 'bold'), bg='#ffdd99', fg='red')
        self.status_employee.place(x=530, y=300)
        self.status_description = Label(frame, text='STATUS:', font=('Calibre', 16, 'bold italic'), bg='#ffdd99')
        self.status_description.place(x=420, y=300)
        self.status_variable = StringVar(frame)
        self.status_variable.set("")
        self.select_status_button = OptionMenu(frame, self.status_variable, *self.states)
        self.select_status_button.config(bg='#ffdd99', relief='solid', font=('Arial', 14, 'bold'), width=20,
                                         highlightthickness=0, bd=1)

        #  Vehicle
        #  Same as STATUS, but now for VEHICLE(here, the options are stored in vehicles list)
        self.vehicle_employee = Label(frame, font=('Arial', 14, 'bold'), bg='#ffdd99')
        self.vehicle_employee.place(x=380, y=401)
        self.vehicle_description = Label(frame, text='VEHICLE:', font=('Calibre', 16, 'bold italic'), bg='#ffdd99')
        self.vehicle_description.place(x=250, y=400)
        self.vehicle_edit = Entry(frame, bg='#ffdd99', width=20, font=('Arial', 14, 'bold'))
        self.vehicle_variable = StringVar(frame)
        self.vehicle_variable.set("")
        self.select_vehicle_button = OptionMenu(frame, self.vehicle_variable, *self.vehicles)
        self.select_vehicle_button.config(bg='#ffdd99', relief='solid', font=('Arial', 14, 'bold'), width=26,
                                          highlightthickness=0, bd=1)

        #  Bind functions
        #  The next three lines bind a specified function to be called over a widget every time, depending on a specific
        #  action: if that widget is focused, or is not focused, or a specific key was pressed etc... In our case,
        #  bind those functions to be called every time when search_bar_input(which is the search bar entry) is focused,
        #  is not focused and when the 'ENTER' key is pressed.
        self.search_bar_input.bind("<FocusIn>", self.search_bar_focusin)
        self.search_bar_input.bind("<FocusOut>", self.search_bar_focusout)
        self.search_bar_input.bind("<Return>", self.search_for_employee)

        #  Edit
        #  This one creates the EDIT button, with some specified arguments, and executes a specific function when it's
        #  clicked, and is placed depending on x and y-axis.
        self.edit_btn = Button(frame, font=('Arial', 10, 'bold'), text='Edit', relief='solid', bd=1,
                               command=lambda: self.edit_employee())

        #  This one creates the SAVE button, with some specified arguments, and executes a specific function when it's
        #  clicked, and is placed depending on x and y-axis.
        #  Save
        self.save_btn = Button(frame, font=('Arial', 10, 'bold'), text='Save changes', relief='solid', bd=1,
                               command=lambda: self.save_changes())

    #  This function is called when the 'ENTER' key is pressed in the search bar, and does the next thing:
    #  check if the text that was written in the search bar corresponds with an email or phone number from database(in
    #  this case: employed_information.csv file), and if it does, displays the all information about that employee, and
    #  makes visible the EDIT button(because, implicitly, the EDIT button isn't visible), but, if it doesn't exist that
    #  employee, a red message will be displayed and makes the EDIT button invisible(ofc, if it's already visible).
    #  And that 'event' variable I placed it as argument, but I don't use it, and if I'll delete it from there, I will
    #  get and error, and I couldn't bind this function(that's why is there).
    def search_for_employee(self, event):
        if len(self.search_bar_input.get()) == 0:
            self.search_bar_label_info.config(text=' ')
        else:
            with open('employed_information.csv') as employed:
                reader = csv.reader(employed)
                next(reader)
                for row in reader:
                    if self.search_bar_input.get() == row[3] or self.search_bar_input.get() == row[4]:
                        self.name_employee.config(text=row[0])
                        self.last_name_employee.config(text=row[1])
                        cnp = row[2]
                        self.cnp_employee.config(text=cnp[0:3] + '*' * 8 + cnp[-2:])
                        self.email_employee.config(text=row[3])
                        self.phone_number_employee.config(text=row[4])
                        #  Here, the status label is colored in green(if the status is 'active') to highlight that
                        #  employee is employed
                        if row[6] == 'active':
                            self.status_employee.config(fg='#00b300')
                        self.status_employee.config(text=row[6])
                        self.status_variable.set(self.status_employee['text'])
                        self.select_status_button.config(textvariable=self.status_variable)
                        self.vehicle_employee.config(text=row[7])
                        self.vehicle_variable.set(self.vehicle_employee['text'])
                        self.select_vehicle_button.config(textvariable=self.vehicle_variable)
                        self.search_bar_label_info.config(text=' ')
                        self.edit_btn.place(x=450, y=460)
                        return True
                    else:
                        self.name_employee.config(text=" ")
                        self.last_name_employee.config(text=" ")
                        self.cnp_employee.config(text=" ")
                        self.email_employee.config(text=" ")
                        self.phone_number_employee.config(text=" ")
                        self.status_employee.config(text=" ")
                        self.vehicle_employee.config(text=' ')
                        text = '*There is no employee with this email or phone number'
                        self.search_bar_label_info.config(text=text, fg='red')
                        self.edit_btn.place_forget()

    #  This function is called when the search bar is focused, and does the next thing:
    #  if the text from search bar is still 'Search for employees(by email or phone)', deletes this message, changes
    #  the foreground, for coloring different the text that user types in. At the end, changes the background color.
    def search_bar_focusin(self, event):
        if self.search_bar_input.get() == 'Search for employees(by email or phone)':
            self.search_bar_input.delete(0, 'end')
            self.search_bar_input.config(fg='black')
        self.search_bar_input.config(bg='#32dae6')

    #  This function is called when the search bar loses the focus, and does the next thing:
    #  if the length of the text from search bar == 0, inserts back that specific message, and changes the foreground
    #  color, for coloring different that specific message. At the end, changes the background color.
    def search_bar_focusout(self, event):
        if len(self.search_bar_input.get()) == 0:
            self.search_bar_input.insert(0, 'Search for employees(by email or phone)')
            self.search_bar_input.config(fg='#b3b3b3')
        self.search_bar_input.config(bg='white')

    #  This functions checks if the new_email is a valid one at first, and shows a message, depending on the text that
    #  was typed in. It checks in the next way:
    #  First, checks if the new email contains '@', and if does, checks if what is after that '@' is a valid extension(
    #  if it's in extension list), and also, if it's a valid extension, checks if the email already exists and if the
    #  new email is different from the old email in our database, and if it's in database, displays a red message, but
    #  if it isn't in our database, is different from the old email, and still has a valid  extension, it means that the
    #  new email is a valid one, and shows a green message.
    def check_new_email(self):
        new_email = self.email_edit.get()
        if len(new_email) > 0 and '@' in new_email:
            new_email_split = new_email.split('@')
            new_email_extension = new_email_split[1]
            for extension in self.extensions:
                if extension == new_email_extension:
                    if os.stat('employed_information.csv').st_size != 0:
                        with open('employed_information.csv') as employed:
                            reader = csv.reader(employed)
                            next(reader)
                            for row in reader:
                                if row[3] == new_email and new_email != self.old_email:
                                    self.new_email_info.config(text='*This new email is already in use', fg='red')
                                    return True
                    self.new_email_info.config(text='The new email is valid', fg='#00b300')
                    self.extension_validation = True
                    break
                else:
                    self.extension_validation = False
        if len(new_email) > 0 and self.extension_validation is False:
            self.new_email_info.config(text="*This new email isn't valid", fg='red')
        elif len(new_email) == 0:
            self.new_email_info.config(text="*The field cannot be let empty", fg='red')
            self.extension_validation = False

    #  This function checks if the new phone number is valid, in the next way:
    #  First, check if the number consists only from numbers, because a phone number cannot consist from characters.
    #  And also, checks if the length of the numbers == 10, because a romanian phone number has only 10 numbers. If the
    #  length of the numbers is == 10 and doesn't contain characters, checks if the new phone numbers is different from
    #  the old one, and if it's, checks in database, to see if the new phone number belongs to another employee.
    #  And if it doesn't belong to another employee, and has 10 numbers, and is different from the old one, it means
    #  that the new phone number is a valid one, and shows a green message.
    def check_new_phone_number(self):
        new_phone_number = self.phone_number_edit.get()
        if len(new_phone_number) > 0:
            for number in new_phone_number:
                if not number.isdigit():
                    self.new_phone_number_info.config(text='*Only numbers allowed', fg='red')
                    return True
        if len(new_phone_number) != 10 and len(new_phone_number) > 0:
            text = '*The new phone number must have 10 numbers'
            self.new_phone_number_info.config(text=text, fg='red')
        elif len(new_phone_number) == 10:
            if os.stat('employed_information.csv').st_size != 0:
                with open('employed_information.csv') as employed:
                    reader = csv.reader(employed)
                    next(reader)
                    for row in reader:
                        if row[4] == new_phone_number and new_phone_number != self.old_phone_number:
                            self.new_phone_number_info.config(text='*This new phone number belongs to another employee',
                                                              fg='red')
                            return True
            self.new_phone_number_info.config(text='Valid new phone number', fg='#00b300')
        else:
            self.new_phone_number_info.config(text='*The field cannot be let empty', fg='red')

    #  This function edits the employee details, only if an employee is found after a searching in search bar:
    #  makes visible the entry box for email and phone number, the option-menu widget for status and vehicle, and the
    #  SAVE button(because all of this five aren't visible implicitly), makes invisible the EDIT button, and makes
    #  disabled the search bar(because isn't allowed to search another employee while already edit an employee). And,
    #  for email and phone number, I must clear the information put in their entry box, because, if I check the first
    #  time, everything will be fine, but, at the second checking, the information from the first checking will be
    #  concatenating along with the information from the second checking and so on, and this isn't helpful at all.
    def edit_employee(self):
        self.email_edit.place(x=500, y=100)
        if len(self.email_edit.get()) > 0:
            self.email_edit.delete(0, 'end')
        self.email_edit.insert(0, self.email_employee['text'])
        self.email_edit.focus_set()
        self.old_email = self.email_employee['text']
        self.email_employee.config(text=' ')

        self.phone_number_edit.place(x=610, y=200)
        if len(self.phone_number_edit.get()) > 0:
            self.phone_number_edit.delete(0, 'end')
        self.phone_number_edit.insert(0, self.phone_number_employee['text'])
        self.old_phone_number = self.phone_number_employee['text']
        self.phone_number_employee.config(text=' ')

        self.select_status_button.place(x=530, y=300)
        self.old_status = self.status_employee['text']
        self.status_employee.config(text=' ')

        self.select_vehicle_button.place(x=353, y=401)
        self.old_vehicle = self.vehicle_employee['text']
        self.vehicle_employee.config(text=' ')

        self.edit_btn.place_forget()
        self.save_btn.place(x=450, y=460)
        self.search_bar_input.config(state='disabled')

    #  This function saves the information about the employee, after were edited:
    #  First, checks if the foreground color for both email and phone number is green(which means the information are
    #  valid), and if it's, makes invisible the entry box for email and phone number, the option-menu widget for status
    #  and vehicle, and the save button, and makes the search bar to be, again, interactive. Also makes the text label
    #  that corresponds to the email, phone number, status and vehicle, to be "", which means to be invisible. Because
    #  it isn't helpful to remain that text after we saved the information. And, at all, change the information about
    #  that employee in database(meaning updates the database) using pandas library.
    #  And if the color of email or phone number isn't green, which means the new information isn't valid, a messagebox
    #  will be displayed, showing that something went wrong.
    def save_changes(self):
        self.check_new_email()
        self.check_new_phone_number()
        if self.new_email_info['fg'] == '#00b300' and self.new_phone_number_info['fg'] == '#00b300':
            self.email_employee.config(text=self.email_edit.get())
            self.email_edit.place_forget()
            self.new_email_info.config(text=' ')

            self.phone_number_employee.config(text=self.phone_number_edit.get())
            self.phone_number_edit.place_forget()
            self.new_phone_number_info.config(text=' ')
            #  This one check the status of the employee, and if it's 'active', changes the color to green, and if it
            #  isn't 'active', it changes to red.
            if self.status_variable.get() == 'inactive' or self.status_variable.get() == 'fired':
                self.status_employee.config(fg='red')
            else:
                self.status_employee.config(fg='#00b300')
            self.status_employee.config(text=self.status_variable.get())
            self.select_status_button.place_forget()

            self.vehicle_employee.config(text=self.vehicle_variable.get())
            self.select_vehicle_button.place_forget()

            self.search_bar_input.config(state='normal')
            self.save_btn.place_forget()

            df = pd.read_csv('employed_information.csv', dtype='str')
            df = df.replace(to_replace=self.old_email, value=self.email_edit.get())
            df = df.replace(to_replace=self.old_phone_number, value=self.phone_number_edit.get())
            df = df.replace(to_replace=self.old_status, value=self.status_variable.get())
            df = df.replace(to_replace=self.old_vehicle, value=self.vehicle_variable.get())
            df.to_csv('employed_information.csv', index=False)
        else:
            messagebox.showerror('error', 'The fields must be filled with valid information!')
