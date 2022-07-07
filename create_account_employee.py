from tkinter import*  # This imports everything from tkinter library
from tkinter import messagebox  # This imports only messagebox from tkinter library
import csv  # This import csv library(for database)
import os  # This import os library(for checking if a file is empty)
import generate_password  # Imports my libray, for generating a random password
import smtplib
import time


#  Here I created an "Account" class, where an object of this Class is created when the Create Account from
#  start_program library is clicked, and once it's created, we can create a new account for an employee
class Account:
    time_sec = 40
    check_code = False

    #  These variables I'll use for checking if the new email is valid
    extensions = ['gmail.com', 'yahoo.com', 'gmail.ro', 'yahoo.ro']
    extension_validation = False

    #  The main column for the csv file(our database)
    header = ['name', 'last_name', 'cnp', 'email', 'phone_number', 'password', 'status_contract', 'vehicle']

    #  Special characters for checking if the name or last name contains this special characters
    special_characters = [' ', '!', '?', '"', '#', '$', '%', '&', "'", '(', ')', '*', '+', ',', '`', '-', '.', '/',
                          ':', ';', '<', '>', '_', '?', '@', '[', ']', '{', '}', '|', '~', '^']

    validation_number = '279146358279'  # The validation number for checking if CNP is valid
    validation_numbers_cnp = []   # An empty list for using it later for checking CNP

    #  This lists I'll use later for button's options of the vehicles
    vehicles = ['Company scooter', 'Company bike', 'Company car', 'Personal car',
                'Personal scooter/moto', 'Personal electric scooter/bike']

    sender = 'bratumihai9797@gmail.com'
    sender_passwd = 'Chucknorris5599!'

    #  Name and Last Name variable for checking if the first letter is upper
    is_upper_name = False
    is_upper_last_name = False

    def __init__(self, frame):

        #  This is the window where the all widgets will be working with
        self.frame = frame

        #  NAME
        #  The next 7 lines create an entry box for name, where the user can type in something, creates a Button,
        #  and a label widget, with some specified arguments, and placed them depending on x and y-axis. All of these
        #  widgets belong to the frame
        self.name_input = Entry(frame, width=17, font=('Calibre', 12))
        self.name_input.place(x=269, y=42)
        self.name_btn = Button(frame, relief='ridge', text='Name', bg='#32dae6', font=('Calibre', 10, 'bold'), width=21,
                               disabledforeground='black', state='disabled', takefocus=0)
        self.name_btn.place(x=92, y=40)
        self.label_name_info = Label(frame, font=('Arial', 7, 'bold'), bg='#b3b3ff')
        self.label_name_info.place(x=269, y=67)
        self.count_name_length_info = Label(frame, font=('Calibre', 8, 'bold'), text='0/3', bg='#b3b3ff', fg='red')
        self.name_reg = self.frame.register(self.check_spelling_name)
        self.name_input.config(validate='key', validatecommand=(self.name_reg, "%P"))

        #  LAST NAME
        #  Same as above, but now for LAST NAME
        self.last_name_input = Entry(frame, width=17, font=('Calibre', 12))
        self.last_name_input.place(x=269, y=107)
        self.last_name_btn = Button(frame, relief='ridge', text='Last Name', bg='#32dae6', font=('Calibre', 10, 'bold'),
                                    width=21, state='disabled', disabledforeground='black', takefocus=0)
        self.last_name_btn.place(x=92, y=105)
        self.label_last_name_info = Label(frame, font=('Arial', 7, 'bold'), bg='#b3b3ff')
        self.label_last_name_info.place(x=269, y=132)
        self.count_last_name_length_info = Label(frame, font=('Calibre', 8, 'bold'), text='0/3', bg='#b3b3ff', fg='red')
        self.last_name_reg = self.frame.register(self.check_spelling_last_name)
        self.last_name_input.config(validate='key', validatecommand=(self.last_name_reg, "%P"))

        #  CNP
        #  Same as above, but now for CNP
        self.cnp_input = Entry(frame, width=17, font=('Calibre', 12))
        self.cnp_input.place(x=269, y=172)
        self.cnp_btn = Button(frame, relief='ridge', text='CNP', bg='#32dae6', font=('Calibre', 10, 'bold'), width=21,
                              disabledforeground='black', state='disabled', takefocus=0)
        self.cnp_btn.place(x=92, y=170)
        self.cnp_label_info = Label(frame, font=('Arial', 7, 'bold'), bg='#b3b3ff')
        self.cnp_label_info.place(x=269, y=197)
        self.count_cnp_digits_info = Label(frame, font=('Calibre', 8, 'bold'), text='0/13', bg='#b3b3ff', fg='red')
        self.cnp_reg = self.frame.register(self.check_spelling_cnp)
        self.cnp_input.config(validate='key', validatecommand=(self.cnp_reg, "%P"))

        #  EMAIL
        #  Same as above, but now for EMAIL
        self.email_input = Entry(frame, width=17, font=('Calibre', 12))
        self.email_input.place(x=269, y=237)
        self.email_btn = Button(frame, relief='ridge', text='Email', bg='#32dae6', font=('Calibre', 10, 'bold'),
                                width=21, state='disabled', disabledforeground='black', takefocus=0)
        self.email_btn.place(x=92, y=235)
        self.email_label_info = Label(frame, font=('Arial', 7, 'bold'), bg='#b3b3ff')
        self.email_label_info.place(x=269, y=262)

        #  PHONE NUMBER
        #  Same as above, but now for PHONE NUMBER
        self.phone_number_input = Entry(frame, width=17, font=('Calibre', 12))
        self.phone_number_input.place(x=269, y=302)
        self.phone_number_btn = Button(frame, relief='ridge', text='Phone Number', bg='#32dae6', width=21,
                                       font=('Calibre', 10, 'bold'), state='disabled', disabledforeground='black',
                                       takefocus=0)
        self.phone_number_btn.place(x=92, y=300)
        self.phone_number_label_info = Label(frame, font=('Arial', 7, 'bold'), bg='#b3b3ff')
        self.phone_number_label_info.place(x=269, y=327)
        self.count_phone_number_digits_info = Label(frame, font=('Calibre', 8, 'bold'), text='0/10', bg='#b3b3ff',
                                                    fg='red')
        self.phone_number_reg = self.frame.register(self.check_spelling_phone_number)
        self.phone_number_input.config(validate='key', validatecommand=(self.phone_number_reg, "%P"))

        #  VEHICLE
        #  The next five lines create an option-menu widget, for choosing the vehicle an employee will work on, with
        #  some specified arguments, and placed depending on x and y-axis. And the default text that will be displayed
        #  first time will be 'Select vehicle'.
        self.vehicle_variable = StringVar(frame)
        self.vehicle_variable.set('Select vehicle')
        self.select_vehicle_button = OptionMenu(frame, self.vehicle_variable, *self.vehicles)
        self.select_vehicle_button.config(bg='#32dae6', relief='groove', font=('Calibre', 10, 'bold'), width=38,
                                          highlightthickness=0, takefocus=0)
        self.select_vehicle_button.place(x=92, y=365)
        self.vehicle_label_info = Label(frame, font=('Arial', 7, 'bold'), bg='#b3b3ff')
        self.vehicle_label_info.place(x=92, y=395)

        #  ACCOUNT BUTTON
        #  The next 2 lines create a button widget, with some specified arguments, placed depending on x and y-axis.
        #  And executes a specified function once it's clicked.
        self.create_acc_btn = Button(frame, text='Create account', font=('Calibre', 16, 'bold'), relief='ridge',
                                     bg='#73fada', command=lambda: self.create_account(), takefocus=0, bd=3)
        self.create_acc_btn.place(x=420, y=440)

        # CLEAR DATA BUTTON
        self.clear_data_btn = Button(frame, text='Clear the information', font=('Calibre', 10, 'bold'), relief='ridge',
                                     bg='#7d68f7', takefocus=0, command=lambda: self.clear_data(), bd=2)
        self.clear_data_btn.place(x=600, y=300)

        # HELP BUTTON
        self.help_button = Button(frame, text='Help!', font=('Calibre', 10, 'bold'), relief='ridge',
                                  bg='#aefcbf', takefocus=0, command=lambda: help_message(), bd=2)
        self.help_button.place(x=700, y=30)

        #  This one calls the focus_defined function
        self.focus_defined()

        def help_message():
            message_name = '-A NAME must start with an upper letter, and cannot contain any more upper letter,' \
                           'number, or special characters, and must have a length of 3 characters!\n\n'
            message_last_name = '-A LAST NAME must start with an upper letter, and cannot contain any more upper ' \
                                'letter, number, or special characters, and must have a length of 3 characters!\n\n'
            message_cnp = '-A CNP contains only numbers, and must have 13 characters!\n\n'
            message_phone_number = '-A PHONE NUMBER contains only numbers, and must have 10 characters!'
            messagebox.showinfo('showinfo', message_name + message_last_name + message_cnp + message_phone_number)

    #  NAME
    #  This one it is executed once the name entry box is focused, and does the next thing:
    #  If the example text(in this case 'ex:Petrescu') is still there, it will delete it, change the foreground color,
    #  and at the end, it will change the background color. And the 'event' variable is there because this function is
    #  a bind function, and, without at least one argument, it won't work, and I will get an error. That's why is there,
    #  and I don't use it.
    def name_focusin(self, event):
        self.name_input.config(bg='#32dae6')
        self.count_name_length_info.place(x=430, y=45)

    #  This one it's executed once the name entry box loses the focus, and does the next thing:
    #  if the length of the input text from entry widget is == 0, inserts back the specified text, changes the
    #  foreground color of the entry box, and the background color of the button. And, at the end, changes the
    #  background color of the entry box
    def name_focusout(self, event):
        self.name_input.config(bg='white')
        self.count_name_length_info.place_forget()

    #  This function checks if the NAME is a valid one, and shows a specific message, depending on what was typed in.
    #  A valid NAME must have at least 3 letter, begins with a capital letter, and contains just letter, not numbers,
    #  not special characters, not another capital letters.
    def check_name(self):
        name = self.name_input.get()
        if len(name) >= 3:
            self.label_name_info.config(text='Valid', fg='#00b300')
            self.name_btn.config(bg='#00b300')
        elif 0 < len(name) < 3:
            self.label_name_info.config(text='*Invalid', fg='red')
            self.name_btn.config(bg='red')
        elif len(name) == 0:
            self.label_name_info.config(text='*This field cannot be let empty', fg='red')
            self.name_btn.config(bg='red')

    def check_spelling_name(self, name_input):
        text = str(len(name_input)) + '/3'
        if len(name_input) == 1:
            if name_input.isupper():
                self.is_upper_name = True
                self.count_name_length_info.config(text=text)
                return True
            else:
                self.is_upper_name = False
                return False
        elif len(name_input) > 1 and self.is_upper_name:
            count_upper_letter_name = 0
            for letter in name_input:
                if letter.isupper():
                    count_upper_letter_name += 1
                if letter.isdigit() or letter in self.special_characters or count_upper_letter_name > 1:
                    return False
            if len(name_input) >= 3:
                self.count_name_length_info.config(text=str(len(name_input)) + '/' + str(len(name_input)), fg='#00b300')
            else:
                self.count_name_length_info.config(text=text, fg='red')
            return True
        elif len(name_input) == 0:
            self.count_name_length_info.config(text=text)
            return True

    #  LAST NAME
    #  Same as above, but now for the LAST NAME
    def last_name_focusin(self, event):
        self.last_name_input.config(bg='#32dae6')
        self.count_last_name_length_info.place(x=430, y=106)

    #  Same as above, but now for the LAST NAME
    def last_name_focusout(self, event):
        self.last_name_input.config(bg='white')
        self.count_last_name_length_info.place_forget()

    # Same as above, but now for the LAST NAME
    def check_last_name(self):
        last_name = self.last_name_input.get()
        if len(last_name) >= 3:
            self.label_last_name_info.config(text='Valid', fg='#00b300')
            self.last_name_btn.config(bg='#00b300')
        elif 0 < len(last_name) < 3:
            self.label_last_name_info.config(text='*Invalid', fg='red')
            self.last_name_btn.config(bg='red')
        elif len(last_name) == 0:
            self.label_last_name_info.config(text='*This field cannot be let empty', fg='red')
            self.last_name_btn.config(bg='red')

    def check_spelling_last_name(self, last_name_input):
        text = str(len(last_name_input)) + '/3'
        if len(last_name_input) == 1:
            if last_name_input.isupper():
                self.is_upper_last_name = True
                self.count_last_name_length_info.config(text=text)
                return True
            else:
                self.is_upper_last_name = False
                return False
        elif len(last_name_input) > 1 and self.is_upper_last_name:
            count_upper_letter_last_name = 0
            for letter in last_name_input:
                if letter.isupper():
                    count_upper_letter_last_name += 1
                if letter.isdigit() or letter in self.special_characters or count_upper_letter_last_name > 1:
                    return False
            if len(last_name_input) >= 3:
                self.count_last_name_length_info.config(text=str(len(last_name_input)) + '/' + str(len(last_name_input))
                                                        , fg='#00b300')
            else:
                self.count_last_name_length_info.config(text=text, fg='red')
            return True
        elif len(last_name_input) == 0:
            self.count_last_name_length_info.config(text=text)
            return True

    #  CNP
    #  Same as above, but now for the CNP
    def cnp_focusin(self, event):
        self.cnp_input.config(bg='#32dae6')
        self.count_cnp_digits_info.place(x=430, y=173)

    #  Same as above, but now for the CNP
    def cnp_focusout(self, event):
        self.cnp_input.config(bg='white')
        self.count_cnp_digits_info.place_forget()

    #  This function checks if the CNP is a valid one, and shows a specific message, depending on what was typed in.
    #  A CNP must have 13 characters, doesn't contain letter or special characters, only numbers. It also checked if
    #  exist in database.
    def check_cnp(self):
        cnp = self.cnp_input.get()
        if len(cnp) == 13:
            for i in range(len(self.validation_number)):
                result_number = int(cnp[i]) * int(self.validation_number[i])
                self.validation_numbers_cnp.append(result_number)
            result = sum(self.validation_numbers_cnp)
            result %= 11
            if str(result) == cnp[-1]:
                if os.stat('employed_information.csv').st_size != 0:
                    with open('employed_information.csv') as employed:
                        reader = csv.reader(employed)
                        next(reader)
                        for row in reader:
                            if row[2] == cnp:
                                self.cnp_label_info.config(text='*This CNP belongs to another employee', fg='red')
                                self.cnp_btn.config(bg='red')
                                return True
                self.cnp_label_info.config(text='Valid', fg='#00b300')
                self.cnp_btn.config(bg='#00b300')
            else:
                self.cnp_label_info.config(text='Invalid', fg='red')
                self.cnp_btn.config(bg='red')
        else:
            self.cnp_label_info.config(text='*This field cannot be let empty', fg='red')
            self.cnp_btn.config(bg='red')
        self.validation_numbers_cnp = []

    def check_spelling_cnp(self, input_cnp):
        text = str(len(input_cnp)) + '/13'
        if len(input_cnp) > 0:
            if not input_cnp[-1].isdigit():
                return False
            if len(input_cnp) < 13:
                self.count_cnp_digits_info.config(text=text, fg='red')
            elif len(input_cnp) == 13:
                self.count_cnp_digits_info.config(text=text, fg='#00b300')
            elif len(input_cnp) > 13:
                return False
        elif len(input_cnp) == 0:
            self.count_cnp_digits_info.config(text=text)
        return True

    #  EMAIL
    #  Same as above, but now for EMAIL
    def email_focusin(self, event):
        self.email_input.config(bg='#32dae6')

    #  Same as above, but now for EMAIL
    def email_focusout(self, event):
        self.email_input.config(bg='white')

    #  This function checks if the EMAIL is a valid one, and shows a specified message, depending on what was typed in.
    #  A valid EMAIL must have '@' and a valid domain(gmail.com, gmail.ro etc...). It is also checked in database, if
    #  it exists.
    def check_email(self):
        email = self.email_input.get()
        if "@" in email:
            email_split = email.split('@')
            extension_email = email_split[1]
            for extension in self.extensions:
                if extension_email == extension:
                    if os.stat('employed_information.csv').st_size != 0:
                        with open('employed_information.csv') as employed:
                            reader = csv.reader(employed)
                            next(reader)
                            for row in reader:
                                if row[3] == email:
                                    self.email_label_info.config(text='*This email is already in use', fg='red')
                                    self.email_btn.config(bg='red')
                                    return True
                    self.email_label_info.config(text='Your email is valid', fg='#00b300')
                    self.email_btn.config(bg='#00b300')
                    self.extension_validation = True
                    break
                else:
                    self.extension_validation = False
        if len(email) > 0 and self.extension_validation is False:
            self.email_label_info.config(text="*Your email isn't valid", fg='red')
            self.email_btn.config(bg='red')
        elif len(email) == 0:
            self.email_label_info.config(text='*This field cannot be let empty', fg='red')
            self.email_btn.config(bg='red')
            self.extension_validation = False

    #  PHONE NUMBER
    #  Same as above, but now for the PHONE NUMBER
    def phone_number_focusin(self, event):
        self.phone_number_input.config(bg='#32dae6')
        self.count_phone_number_digits_info.place(x=430, y=303)

    #  Same as above, but now for the PHONE NUMBER
    def phone_number_focusout(self, event):
        self.phone_number_input.config(bg='white')
        self.count_phone_number_digits_info.place_forget()

    #  This function checks if the PHONE NUMBER is a valid one, and shows a specified message, depending on what was
    #  typed in. A valid PHONE NUMBER must have 10 numbers, and doesn't contain letters or special characters. It is
    #  also checked in database.
    def check_phone_number(self):
        phone_number = self.phone_number_input.get()
        if len(phone_number) == 10:
            if os.stat('employed_information.csv').st_size != 0:
                with open('employed_information.csv') as employed:
                    reader = csv.reader(employed)
                    next(reader)
                    for row in reader:
                        if row[4] == phone_number:
                            self.phone_number_label_info.config(text='*This phone number belongs to another employee',
                                                                fg='red')
                            self.phone_number_btn.config(bg='red')
                            return True
            self.phone_number_label_info.config(text='Valid phone number', fg='#00b300')
            self.phone_number_btn.config(bg='#00b300')
        else:
            self.phone_number_label_info.config(text='*This field cannot be let empty', fg='red')
            self.phone_number_btn.config(bg='red')

    def check_spelling_phone_number(self, input_phone):
        text = str(len(input_phone)) + '/10'
        if len(input_phone) > 0:
            if not input_phone[-1].isdigit():
                return False
            if len(input_phone) < 10:
                self.count_phone_number_digits_info.config(text=text, fg='red')
            elif len(input_phone) == 10:
                self.count_phone_number_digits_info.config(text=text, fg='#00b300')
            elif len(input_phone) > 10:
                return False
            return True
        elif len(input_phone) == 0:
            self.count_phone_number_digits_info.config(text=text)
            return True

    def check_chosen_vehicle(self):
        if self.vehicle_variable.get() == "Select vehicle":
            self.vehicle_label_info.config(text='*You must choose one of the available options', fg='red')
            self.select_vehicle_button.config(bg='red')
        else:
            self.vehicle_label_info.config(text='')
            self.select_vehicle_button.config(bg='#00b300')

    #  In this function, some functions are bound to do something at every time when an action happens over a widget(
    #  it is focused, a key is pressed etc...). In this case, when a specific widget loses the focus, or it's focused.
    def focus_defined(self):
        #  NAME
        self.name_input.bind("<FocusIn>", self.name_focusin)
        self.name_input.bind('<FocusOut>', self.name_focusout)

        #  LAST NAME
        self.last_name_input.bind("<FocusIn>", self.last_name_focusin)
        self.last_name_input.bind("<FocusOut>", self.last_name_focusout)

        #  CNP
        self.cnp_input.bind("<FocusIn>", self.cnp_focusin)
        self.cnp_input.bind("<FocusOut>", self.cnp_focusout)

        #  EMAIL
        self.email_input.bind("<FocusIn>", self.email_focusin)
        self.email_input.bind("<FocusOut>", self.email_focusout)

        #  PHONE NUMBER
        self.phone_number_input.bind("<FocusIn>", self.phone_number_focusin)
        self.phone_number_input.bind("<FocusOut>", self.phone_number_focusout)

    #  This function calls the functions that check the whole information(NAME, LAST NAME etc...), and if the foreground
    #  of the all label's messages that correspond to NAME, LAST NAME, are green(meaning the all information are valid),
    #  and if they do, creates that account, and put the information in the database. But, if the information aren't
    #  valid, a messagebox will be displayed, showing that something went wrong, and some information aren't valid.
    def create_account(self):
        self.check_name()
        self.check_last_name()
        self.check_cnp()
        self.check_email()
        self.check_phone_number()
        self.check_chosen_vehicle()
        if self.label_name_info['fg'] == '#00b300' and self.label_last_name_info['fg'] == '#00b300' \
                and self.email_label_info['fg'] == '#00b300' and self.cnp_label_info['fg'] == '#00b300' \
                and self.phone_number_label_info['fg'] == '#00b300' and self.vehicle_variable.get() != 'Select vehicle':
            messagebox.showinfo('Succes', 'The account has been created! An email with a verification code has been '
                                          'sent to ' + self.email_input.get())
            password = generate_password.generate_random_password()
            with open('employed_information.csv', 'a', newline='') as employed:
                if os.stat('employed_information.csv').st_size == 0:
                    dictwriter = csv.DictWriter(employed, delimiter=',', fieldnames=self.header)
                    dictwriter.writeheader()
                    writer = csv.writer(employed)
                    writer.writerow([self.name_input.get(), self.last_name_input.get(), self.cnp_input.get(),
                                    self.email_input.get(), self.phone_number_input.get(), password, 'active',
                                    self.vehicle_variable.get()])
                else:
                    writer = csv.writer(employed)
                    writer.writerow([self.name_input.get(), self.last_name_input.get(), self.cnp_input.get(),
                                    self.email_input.get(), self.phone_number_input.get(), password, 'active',
                                    self.vehicle_variable.get()])

        else:
            messagebox.showerror('error', 'The all fields must be filled with valid information!')

    def clear_data(self):
        self.name_input.delete(0, 'end')
        self.name_btn.config(bg='#32dae6')
        self.label_name_info.config(text='')
        self.count_name_length_info.config(fg='red')

        self.last_name_input.delete(0, 'end')
        self.last_name_btn.config(bg='#32dae6')
        self.label_last_name_info.config(text='')
        self.count_last_name_length_info.config(fg='red')

        self.cnp_input.delete(0, 'end')
        self.cnp_btn.config(bg='#32dae6')
        self.cnp_label_info.config(text='')
        self.count_cnp_digits_info.config(fg='red')

        self.email_input.delete(0, 'end')
        self.email_btn.config(bg='#32dae6')
        self.email_label_info.config(text='')

        self.phone_number_input.delete(0, 'end')
        self.phone_number_btn.config(bg='#32dae6')
        self.phone_number_label_info.config(text='')
        self.count_phone_number_digits_info.config(fg='red')

        self.vehicle_variable.set('Select vehicle')
        self.vehicle_label_info.config(text='')
        self.select_vehicle_button.config(bg='#32dae6')

        self.name_input.focus_set()

    def send_email(self):
        email_employee = self.email_input.get()
        number_code = generate_password.generate_random_num()
        message = """From:Voiniceii <voiniceii@recruitment-team.com>
To: bratumihai97@gmail.com
Subject: Verify Account

This is an automatic email! This is the number you have to type in for verifying email address: {number}

_ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _


Best regards, Voiniceii Team!
""".format(number=number_code)
        s = smtplib.SMTP('smtp.gmail.com', 587)

        s.starttls()

        # Authentication
        s.login(self.sender, self.sender_passwd)

        # sending the mail
        s.sendmail(self.sender, email_employee, message)

        # terminating the session
        s.quit()
        return number_code

    def verify_email_address(self):
        number_code = self.send_email()

        def countdown():
            if self.check_code:
                label_countdown.destroy()
                time.sleep(1)
                verify_window.destroy()
                return True
            elif self.time_sec >= 0:
                mins, secs = divmod(self.time_sec, 60)
                if secs < 10:
                    secs = '0' + str(secs)
                if secs == 29 and mins == 0:
                    label_countdown.config(fg='red')
                label_countdown.config(text=str(mins) + ":" + str(secs))
                self.time_sec -= 1
            else:
                del number_code
                verify_window.destroy()
                return True
            verify_window.after(1000, countdown)

        def check_is_number(input_number):
            if len(input_number) > 0:
                if not input_number[-1].isdigit():
                    return False
                if len(input_number) > 6:
                    return False
            return True

        def check_key_and_code():
            if verification_code_entry.get() == number_code and key_entry.get() == '1X9be1?UI6hmi_bjyp&A,Dv4_#eq1f':
                self.check_code = True
                verification_code_info.config(text='Valid', fg='green')
                key_info.config(text='Valid', fg='green')
            else:
                verification_code_info.config(text='Invalid', fg='red')
                key_info.config(text='Invalid', fg='red')

        verify_window = Toplevel(self.frame)

        verification_code_entry = Entry(verify_window, font=('Calibre', 10), show="*")
        verification_code_entry.place(x=120, y=30)
        verification_entry_reg = verify_window.register(check_is_number)
        verification_code_entry.config(validate='key', validatecommand=(verification_entry_reg, '%P'))
        verification_code_label = Label(verify_window, text='The code \nnumber', font=('Calibre', 12, 'bold'))
        verification_code_label.place(x=30, y=18)
        verification_code_info = Label(verify_window, font=('Calibre', 8, 'bold'))
        verification_code_info.place(x=120, y=50)

        key_entry = Entry(verify_window, font=('Calibre', 10))
        key_entry.place(x=120, y=100)
        key_label = Label(verify_window, text='The key', font=('Calibre', 12, 'bold'))
        key_label.place(x=40, y=98)
        key_info = Label(verify_window, font=('Calibre', 8, 'bold'))
        key_info.place(x=120, y=120)

        check_btn = Button(verify_window, text='Check', font=('Times New Roman', 10, 'bold'), relief='solid',
                           bg='#7832fa',
                           fg='white', command=lambda: check_key_and_code())
        check_btn.place(x=230, y=170)

        label_countdown = Label(verify_window, font=('Times New Roman', 14, 'bold'), fg='green')
        if self.time_sec < 30:
            label_countdown.config(fg='red')
        label_countdown.place(x=40, y=160)
        countdown()

        verify_window.title('Verify email address for employee')
        verify_window.geometry('300x200')
        verify_window.resizable(False, False)
        verify_window.mainloop()
