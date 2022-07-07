from tkinter import *  # This one imports everything from tkinter library
import search_employee  # This one imports my library(search_employee)
import create_account_employee  # This one also imports my library
import datetime  # This import datetime library


#  Here I created a "Start" class with a window(a class from tkinter library) as argument,
#  where that windows it's created when I create an object of this class
class Start(Tk):
    #  Those variables I'll use it later for making some animation(the first four for account button)
    width_acc_animation = 0
    height_acc_animation = 50
    new_y_acc = 140
    count_acc_obj = 0

    #  and the last four for search button
    width_search_animation = 0
    height_search_animation = 50
    new_y_search = 50
    count_search_obj = 0

    new_width_calender_clock_widget = 153  # A variable for making a transition between calendar and clock

    def __init__(self):
        #  This line make my class to inherit everything from Tk class(which I put it as argument in my class)
        #  and I'll use self instead of Tk when I'll use something from that class
        super().__init__()

        #  This one sets the title of my window
        self.title('Voiniceii')
        #  This one sets the resolution of the window
        self.geometry('900x500')
        #  This one makes the window not to be resizable on both axes(x and y). If I want one of them to be resizable,
        #  instead of 'False', I use 'True'
        self.resizable(False, False)
        #  This one changes the background color of the window(that it's a hex color)
        self.config(bg='#ccffe6')

        #  In the next two lines I created a frame that belongs to the main window(self), which I'll use it for making
        #  an animation for create account, and I set its height and background color, and where to be placed
        self.frame_account = Frame(self, height=50, bg='#b3b3ff')
        self.frame_account.place(x=99, y=140)

        #  Same as above, but now for search button(but the background color it's different, and where I put it)
        self.frame_search = Frame(self, height=50, bg='#ffdd99')
        self.frame_search.place(x=99, y=50)

        #  Same as above, but this frame is placed on the left side of the window, and his height is the same as
        #  window's height and its background color is different
        self.left_frame = Frame(self, height=500, width=100, bg='#a5d9b7', relief='ridge', borderwidth=3)
        self.left_frame.place(x=0, y=0)

        #  The next two lines create a button(for searching details about employees) that belongs to the window,
        #  which, once it's clicked, calls a function that starts an animation, and at the end of that animation,
        #  a new window(which is a frame) appears, where you can search details about employees and edit them.
        #  And if you press that button again, start the animation but in the reverse way, and at the end the normal
        #  window shows. And ofc, I placed that button depending on x and y.
        self.search_btn = Button(self, text="Search for\nemployee\ndetails", font=('Calibre', 12, 'bold'),
                                 relief='flat', bg='#b3ffff', command=lambda: self.start_search_employee_animation1(),
                                 activebackground='black', activeforeground='#b3ffff', takefocus=0)
        self.search_btn.place(x=4, y=40)

        #  Same as above, but now for create account
        self.create_acc_employee_btn = Button(self, text='Create\naccount', font=('Calibre', 12, 'bold'), relief='flat',
                                              bg='#b3ffff', command=lambda: self.start_create_acc_animation1(),
                                              activebackground='black', activeforeground='#b3ffff', takefocus=0)
        self.create_acc_employee_btn.place(x=21, y=139)

        #  CLOCK

        self.clock_frame = Frame(self, width=153, height=77, relief='groove', bd=3, highlightthickness=3,
                                 highlightbackground='#666633', bg='#b3ffff')
        self.clock_frame.place(x=720, y=380)

        self.colon1_clock = Label(self.clock_frame, font=('ds-digital', 26), bg='white')
        self.colon1_clock.place(x=38, y=-1)

        self.red_color_clock = Label(self.clock_frame, bg='#e6322c', font=('ds-digital', 26), width=2)
        self.red_color_clock.place(x=-1, y=-1)
        self.red_color_clock_info = Label(self.clock_frame, bg='#e6322c', font=('ds-digital', 13), text='HOUR')
        self.red_color_clock_info.place(x=-1, y=42)

        self.colon2_clock = Label(self.clock_frame, font=('ds-digital', 26), bg='white')
        self.colon2_clock.place(x=88, y=-1)

        self.yellow_color_clock = Label(self.clock_frame, bg='#e7f03a', font=('ds-digital', 26), width=2)
        self.yellow_color_clock.place(x=49, y=-1)
        self.yellow_color_clock_info = Label(self.clock_frame, bg='#e7f03a', font=('ds-digital', 13), text='MIN',
                                             width=4)
        self.yellow_color_clock_info.place(x=49, y=42)

        self.blue_color_clock = Label(self.clock_frame, bg='#2041e3', font=('ds-digital', 26), width=2)
        self.blue_color_clock.place(x=99, y=-1)
        self.blue_color_clock_info = Label(self.clock_frame, bg='#2041e3', font=('ds-digital', 13), text='SEC', width=4)
        self.blue_color_clock_info.place(x=99, y=42)
        self.time()

        #  CALENDAR
        self.calendar_frame = Frame(self, width=153, height=77, relief='groove', bd=3, highlightthickness=3,
                                    highlightbackground='#666633', bg='#b3ffff')
        self.calendar_frame.place(x=720, y=380)

        self.red_color_calendar = Label(self.calendar_frame, bg='#e6322c', font=('ds-digital', 26), width=2)
        self.red_color_calendar.place(x=-1, y=-1)
        self.red_color_calendar_info = Label(self.calendar_frame, bg='#e6322c', font=('ds-digital', 13), text='DAY',
                                             width=4)
        self.red_color_calendar_info.place(x=-1, y=42)

        self.yellow_color_calendar = Label(self.calendar_frame, bg='#e7f03a', font=('ds-digital', 26), width=2)
        self.yellow_color_calendar.place(x=49, y=-1)
        self.yellow_color_calendar_info = Label(self.calendar_frame, bg='#e7f03a', font=('ds-digital', 13),
                                                text='MONTH', width=4)
        self.yellow_color_calendar_info.place(x=49, y=42)

        self.blue_color_calendar = Label(self.calendar_frame, bg='#2041e3', font=('ds-digital', 13), width=4)
        self.blue_color_calendar.place(x=99, y=-1)
        self.blue_color_calendar_info = Label(self.calendar_frame, bg='#2041e3', font=('ds-digital', 13), text='YEAR',
                                              width=4)
        self.blue_color_calendar_info.place(x=99, y=42)
        self.calendar()

        #  SWITCH BUTTON BETWEEN CALENDAR AND DATE TIME

        self.switch = Button(text='Switch to Date-time', font=('ds-digital', 9),
                             command=lambda: self.start_transition_calendar_clock(), relief='solid', width=23,
                             bg='#b3ffff', takefocus=0)
        self.switch.place(x=722, y=460)
        self.mainloop()

    #  START SEARCH ANIMATION FOR FRAME
    #  This one starts the animation for search button, and creates an object(which its window is a frame
    #  (frame_search)) only if the count_search_obj == 0 and width_search_animation == 100.
    #  That created object belongs to Search class, and is from search_employee library.
    #  Here's how this animation works: It contains 3 steps(increases the width of the frame to the right edge of the
    #  window, moves the frame up, to the top edge of the frame, and increases the frame's height to the bottom edge
    #  of the window):
    #  Step no.1: I used width_search_animation variable, which increments the width of the frame object with 10 pixels
    #  at every 3 milliseconds(this is what after method does: calls the specific function at every specific time)
    #  if width_search_animation <= 800. If width_search_animation == 800 it increments the width with 1 pixels(When
    #  width_search_animation == 800, the width of the frame will be 800, but, because I placed the frame at x=99,
    #  somehow the width will be 899, and I want to be 900. That's why I added that one pixel, to cover the window
    #  completely). And after that, changes the background and foreground color of search button, to see that button
    #  is clicked, calls the function of step no.2, and return True(for not continuing calling the actual function).

    def start_search_employee_animation1(self):
        if self.width_search_animation == 100 and self.count_search_obj == 0:
            search_employee.Search(self.frame_search)
            self.count_search_obj += 1
        if self.width_search_animation <= 800:
            self.width_search_animation += 10
        if self.width_search_animation == 800:
            self.width_search_animation += 1
            self.search_btn.config(bg='black', fg='#b3ffff')
            self.frame_search.config(width=self.width_search_animation)
            self.start_search_employee_animation2()
            return True
        self.frame_search.config(width=self.width_search_animation)
        self.frame_search.after(2, self.start_search_employee_animation1)

    #  Step no.2: I used new_y_search variable, for moving up the frame with 2 pixels at every 3 milliseconds, and once
    #  it's reached 0, calls the function of step no.3, and return True(for not continuing calling the actual function).
    def start_search_employee_animation2(self):
        if self.new_y_search >= 0:
            self.new_y_search -= 2
        if self.new_y_search == 0:
            self.frame_search.place(y=self.new_y_search)
            self.start_search_employee_animation3()
            return True
        self.frame_search.place(y=self.new_y_search)
        self.frame_search.after(2, self.start_search_employee_animation2)

    #  Step no.3: I used height_search_animation variable, for increasing the frame's height with 5 pixels at every 3
    #  milliseconds, and once it's reached 500, changes the function that search button will call when it's clicked,
    #  and return True(for not continuing calling the actual function).
    def start_search_employee_animation3(self):
        if self.height_search_animation <= 500:
            self.height_search_animation += 5
        if self.height_search_animation == 500:
            self.frame_search.config(height=self.height_search_animation)
            self.search_btn.config(command=lambda: self.reverse_search_employee_animation1())
            return True
        self.frame_search.config(height=self.height_search_animation)
        self.frame_search.after(2, self.start_search_employee_animation3)

    #  START REVERSE SEARCH ANIMATION FOR FRAME
    #  It's the same as above, but now in the reverse way. Here the 3 steps are: decreases the height till reach 50,
    #  move down the frame till reach 50 , and decreases the frame's width till reach 0(which will be the values of the
    #  variables I declared at the top of the class). And the rest of the code it's the same as above(changes the
    #  search button's foreground, background, and the function will call when it's clicked etc...)
    def reverse_search_employee_animation1(self):
        if self.height_search_animation >= 50:
            self.height_search_animation -= 5
        if self.height_search_animation == 50:
            self.search_btn.config(fg='black', bg='#b3ffff')
            self.frame_search.config(height=self.height_search_animation)
            self.reverse_search_employee_animation2()
            return True
        self.frame_search.config(height=self.height_search_animation)
        self.frame_search.after(2, self.reverse_search_employee_animation1)

    def reverse_search_employee_animation2(self):
        if self.new_y_search <= 50:
            self.new_y_search += 2
        if self.new_y_search == 50:
            self.frame_search.place(y=self.new_y_search)
            self.reverse_search_employee_animation3()
            return True
        self.frame_search.place(y=self.new_y_search)
        self.frame_search.after(2, self.reverse_search_employee_animation2)

    def reverse_search_employee_animation3(self):
        if self.width_search_animation > 1:
            self.width_search_animation -= 10
        if self.width_search_animation == 1:
            self.width_search_animation -= 1
            self.frame_search.config(width=self.width_search_animation)
            self.search_btn.config(command=lambda: self.start_search_employee_animation1())
            return True
        self.frame_search.config(width=self.width_search_animation)
        self.frame_search.after(2, self.reverse_search_employee_animation3)

    #  START CREATE ACCOUNT ANIMATION FOR FRAME
    #  Same as above, but now the window is the frame_account(here, the object created belongs to Account class(which
    #  is from create_account_employee library)) with a small differences(here, new_y_acc will be 140, instead of 50,
    #  because the create account button was placed at different y than search button).
    def start_create_acc_animation1(self):
        if self.width_acc_animation == 100 and self.count_acc_obj == 0:
            create_account_employee.Account(self.frame_account)
            self.count_acc_obj += 1
        if self.width_acc_animation <= 800:
            self.width_acc_animation += 10
        if self.width_acc_animation == 800:
            self.width_acc_animation += 1
            self.create_acc_employee_btn.config(bg='black', fg='#b3ffff')
            self.frame_account.config(width=self.width_acc_animation)
            self.start_create_acc_animation2()
            return True
        self.frame_account.config(width=self.width_acc_animation)
        self.frame_account.after(2, self.start_create_acc_animation1)

    def start_create_acc_animation2(self):
        if self.new_y_acc >= 0:
            self.new_y_acc -= 2
        if self.new_y_acc == 0:
            self.frame_account.place(y=self.new_y_acc)
            self.start_create_acc_animation3()
            return True
        self.frame_account.place(y=self.new_y_acc)
        self.frame_account.after(2, self.start_create_acc_animation2)

    def start_create_acc_animation3(self):
        if self.height_acc_animation <= 500:
            self.height_acc_animation += 5
        if self.height_acc_animation == 500:
            self.frame_account.config(height=self.height_acc_animation)
            self.create_acc_employee_btn.config(command=lambda: self.reverse_create_acc_animation1())
            return True
        self.frame_account.config(height=self.height_acc_animation)
        self.frame_account.after(2, self.start_create_acc_animation3)

    #  START REVERSE CREATE ACCOUNT ANIMATION FOR FRAME
    #  Same as above, but now in the reverse way for the create account frame
    def reverse_create_acc_animation1(self):
        if self.height_acc_animation >= 50:
            self.height_acc_animation -= 5
        if self.height_acc_animation == 50:
            self.create_acc_employee_btn.config(fg='black', bg='#b3ffff')
            self.frame_account.config(height=self.height_acc_animation)
            self.reverse_create_acc_animation2()
            return True
        self.frame_account.config(height=self.height_acc_animation)
        self.frame_account.after(2, self.reverse_create_acc_animation1)

    def reverse_create_acc_animation2(self):
        if self.new_y_acc <= 140:
            self.new_y_acc += 2
        if self.new_y_acc == 140:
            self.frame_account.place(y=self.new_y_acc)
            self.reverse_create_acc_animation3()
            return True
        self.frame_account.place(y=self.new_y_acc)
        self.frame_account.after(2, self.reverse_create_acc_animation2)

    def reverse_create_acc_animation3(self):
        if self.width_acc_animation > 1:
            self.width_acc_animation -= 10
        if self.width_acc_animation == 1:
            self.width_acc_animation -= 1
            self.frame_account.config(width=self.width_acc_animation)
            self.create_acc_employee_btn.config(command=lambda: self.start_create_acc_animation1())
            return True
        self.frame_account.config(width=self.width_acc_animation)
        self.frame_account.after(2, self.reverse_create_acc_animation3)

    def time(self):
        today = datetime.datetime.today()
        hour = today.hour
        minute = today.minute
        second = today.second
        if second % 2 == 0:
            self.colon1_clock.config(text=' ')
            self.colon2_clock.config(text=' ')
        else:
            self.colon1_clock.config(text=':')
            self.colon2_clock.config(text=':')
        self.red_color_clock.config(text=hour)
        self.yellow_color_clock.config(text=minute)
        self.blue_color_clock.config(text=second)
        self.clock_frame.after(1000, self.time)

    def calendar(self):
        today = datetime.datetime.today()
        year = today.year
        year = str(year)
        month = today.month
        day = today.day
        self.red_color_calendar.config(text=day)
        self.yellow_color_calendar.config(text=month)
        text = year[0:2] + '\n' + year[2:]
        self.blue_color_calendar.config(text=text)
        self.calendar_frame.after(1000, self.calendar)

    def start_transition_calendar_clock(self):
        if self.new_width_calender_clock_widget > 2:
            self.new_width_calender_clock_widget -= 2
            self.calendar_frame.config(width=self.new_width_calender_clock_widget)
        if self.new_width_calender_clock_widget == 1:
            self.new_width_calender_clock_widget -= 1
            self.calendar_frame.config(width=self.new_width_calender_clock_widget)
            self.switch.config(command=lambda: self.reverse_transition_calendar_clock(), text='Switch to Calendar-time')
            return True
        self.calendar_frame.after(4, self.start_transition_calendar_clock)

    def reverse_transition_calendar_clock(self):
        if self.new_width_calender_clock_widget < 151:
            self.new_width_calender_clock_widget += 2
            self.calendar_frame.config(width=self.new_width_calender_clock_widget)
        if self.new_width_calender_clock_widget == 152:
            self.new_width_calender_clock_widget += 1
            self.calendar_frame.config(width=self.new_width_calender_clock_widget)
            self.switch.config(command=lambda: self.start_transition_calendar_clock(), text='Switch to Date-time')
            return True
        self.calendar_frame.after(4, self.reverse_transition_calendar_clock)


#  Here the program starts
if __name__ == '__main__':
    app = Start()
