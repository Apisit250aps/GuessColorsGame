from pygame import *
from math import *
from tkinter import *
from tkinter import colorchooser
from tkinter import messagebox
from datetime import datetime
import random as rd
import matplotlib.pyplot as plt
import sqlite3

plt.style.use('seaborn')

mixer.init()

times = datetime.now()

def dms():
    mixer.music.load('assets\DMS_piano.mp3')
    for i in range(10):
        mixer.music.play()

def music():
    mixer.music.load('assets\music.mp3')
    for i in range(10):
        mixer.music.play()

def cmm1():
    mixer.music.load('assets\comm1.mp3')
    mixer.music.play()

def cmm2():
    mixer.music.load('assets\comm2.mp3')
    mixer.music.play()

def cmm3():
    mixer.music.load('assets\comm3.mp3')
    mixer.music.play()

def cmm4():
    mixer.music.load('assets\comm4.mp3')
    mixer.music.play()

def cmm5():
    mixer.music.load('assets\comm5.mp3')
    mixer.music.play()

def cmm6():
    mixer.music.load('assets\comm6.mp3')
    mixer.music.play()

def cmm7():
    mixer.music.load('assets\comm7.mp3')
    mixer.music.play()

def cmm8():
    mixer.music.load('assets\comm8.mp3')
    mixer.music.play()

def kuen():
    mixer.music.load('assets\kuen.mp3')
    mixer.music.play()

def hit():
    mixer.music.load('assets\hit.mp3')
    mixer.music.play()

def fishstop():
    mixer.music.stop()

dms()

ColorLists = [
    '#ff0000',
    '#ffff00',
    '#80ff00',
    '#00ff40',
    '#00ffff',
    '#0080c0',
    '#8080c0',
    '#ff00ff'
]

class MainGame:
    def __init__(self):
        self.awsList = []
        self.correct = []
        self.nearrie = []
        self.roundid = 0
        self.bonus = 10

    def randomcolor(self):
        self.rl = []
        for i in range(5):
            self.rdc = rd.choice(ColorLists)
            self.rl.append(self.rdc)
        print(f'Game has begun\n{self.rl}')

    def scorecal(self):
        global score
        sn = sum(self.nearrie)
        sc = sum(self.correct)
        score = ((sn+sc)+(self.roundid-10))*self.bonus
        scoreVar = f'You score is {score} points'

        messagebox.showinfo('Score!', scoreVar)
        text_msg.insert(END, f'\n{scoreVar}')
        con()

    def checker(self):
        self.roundid += 1
        c = 0
        n = 0
        print(f'Round :{self.roundid}')
        if self.awsList == self.rl:
            self.correct.append(5)
            self.nearrie.append(0)
            if self.roundid == 1:
                self.bonus += 10
                messagebox.showinfo('Win', 'You guessed very well')
                cmm7()
                answer()
                Main.scorecal()
            else:
                messagebox.showinfo('Win', 'Congratulations')
                cmm7()
                answer()
                Gplot()
                Main.scorecal()
        else:
            for i in range(5):
                if self.awsList[i] in self.rl:
                    if self.awsList[i] == self.rl[i]:
                        c += 1
                    else :
                        n += 1
            
            self.awsList.clear()
            self.correct.append(c)
            self.nearrie.append(n)
            self.bonus -= 1
            troll = ''
            if c == 0 and n == 0:
                troll += 'Can you only think of this?'
                cmm5()
            elif c == 0 and n == 1 or c == 1 and n == 0:
                troll += 'Are you kidding me?'
                cmm4()
            elif c == 3:
                troll = 'Not Bad!'
                cmm3()
            elif c == 4:
                troll += 'close to the truth'
                kuen()
            elif n == 4:
                troll = 'Hey'
                cmm6()
            else:
                troll += "I'm cheering for you."
                cmm8()
            cm = 'o'*c
            nm = '*'*n
            
            text = f'\nround :{self.roundid}\nCorrect >    {cm} \nResemble     >    {nm}\n{troll}'
            text_msg.insert(END, text)
            self.awsList.clear()
            c and n == 0
        if self.roundid == 9 and self.awsList != self.rl:
            cmm2()
            answer()
            Gplot()
            Main.scorecal()

Main = MainGame()
Main.randomcolor()

def choosecolor(button):
    c = colorchooser.askcolor()
    if c[1] not in ColorLists:
        cmm4()
        messagebox.showwarning('No this color in list',
                               'Please check the answer.')
    else:
        if c[1] != None:
            hit()
            button.config(bg=c[1], state=DISABLED)
            Main.awsList.append(c[1])
            print(f'add {c[1]}')
            if len(Main.awsList) > 4:
                Main.checker()
    return

def Gplot():
    x = []
    for r in range(1, Main.roundid+1):
        x.append(r)
    plt.title('End Game!')

    y = Main.correct
    plt.plot(x, y, ls='-', c='g', label='Correct')

    y = Main.nearrie
    plt.plot(x, y, ls='--', c='y', label='Resemble')

    plt.ylabel('Points', color='black')
    plt.xlabel('Rounds', color='black')
    plt.legend(loc=7)
    plt.show()

def createconnection():
    global conn, cursor
    conn = sqlite3.connect('game.db')
    cursor = conn.cursor()

def Mainwindow():
    root = Tk()
    root.title('Mastrer Logic')
    root.config(bg='#f7f7f7')
    root.geometry('720x810')
    root.rowconfigure((0, 1, 2, 3, 4, 5), weight=1)
    root.columnconfigure((0, 1, 2), weight=1)
    root.resizable(0, 0)
    root.option_add('*font', 'sans-serif 12 bold')

    return root

def newgame():
    Main.randomcolor()
    Main.awsList.clear()
    Main.correct.clear()
    Main.nearrie.clear()
    Main.roundid = 0
    Main.bonus = 10

    Gamewindows(userinfo.get())

def answer():
    root.title('Final')
    root.config(bg='#dfe3ee')
    f = 5
    slotLabel = Frame(games, bg='#dfe3ee')
    slotLabel.grid(row=1, column=0, sticky=NW, padx=5, pady=5)
    for r in range(9):
        colorbar = LabelFrame(
            slotLabel, text=f'Round {r+1}', bg='#dfe3ee', fg='#ffffff')
        colorbar.grid(row=r, ipadx=f, ipady=f, padx=f)
        for c in range(5):
            cl = Main.rl[c]
            add_button(Button(colorbar, state=DISABLED), 1, c, cl)

def loginlayout():
    global userentry
    global pwdentry
    global loginframe
    loginframe = Frame(root, bg='#FFFFFF')
    loginframe.rowconfigure((0, 1, 2, 3, 4, 5), weight=1)
    loginframe.columnconfigure((0, 1, 2, 3), weight=1)
    root.title("Sing-in")
    frame_lg = Frame(loginframe, bg='#ffffff')
    frame_lg.grid(row=2, column=2, columnspan=2, sticky='news')

    logo = Label(frame_lg, text='Masterlogic', bg='#ffffff',
                 fg='#3b5998', font='sans-serif 16 bold')
    logo.grid(row=1, column=1, columnspan=2, sticky='news', pady=50)

    user_lg = LabelFrame(frame_lg, text='Username',
                         bg='#ffffff', fg='#000000')
    user_lg.grid(row=2, column=1, columnspan=2)

    pass_lg = LabelFrame(frame_lg, text='Password',
                         bg='#ffffff', fg='#000000')
    pass_lg.grid(row=3, column=1, columnspan=2)

    userentry = Entry(user_lg, bg='#FFFFFF',
                      font=70, textvariable=userinfo)
    userentry.grid(row=1, column=1, sticky='n', padx=10, ipadx=10, ipady=5)
    pwdentry = Entry(pass_lg, bg='#FFFFFF',
                     show='*', font=70, textvariable=pwdinfo)
    pwdentry.grid(row=3, column=1, sticky='n', padx=10, ipadx=10, ipady=5)

    Button(frame_lg, text="Sign-in",
           command=loginclick, width=10, bg='#3b5998', fg='#ffffff', relief=GROOVE).grid(row=4, column=1, columnspan=2, pady=5)
    Button(frame_lg, text="Sign-up",
           command=singup, width=15, bg='#00a400', fg='#ffffff', relief=GROOVE).grid(row=5, column=1, columnspan=2, pady=5)

    loginframe.grid(row=1, column=0, columnspan=3, rowspan=3, sticky='news')
    userentry.focus_force()

def loginclick():
    if userinfo.get() == "":
        messagebox.showwarning("ADMIN:", "Please enter username")
        userentry.focus_force()
    else:
        sql = "select * from students where username=?"
        cursor.execute(sql, [userinfo.get()])
        result = cursor.fetchall()
        if result:
            if pwdinfo.get() == "":
                messagebox.showwarning("ADMIN", "Please enter password")
                pwdentry.focus_force()
            else:
                sql = "select * from students where username=? AND password=?"
                cursor.execute(sql, [userinfo.get(), pwdinfo.get()])
                result = cursor.fetchone()
                if result:
                    messagebox.showinfo("ADMIN", "Login successfully")
                    Gamewindows(userinfo.get())
                else:
                    messagebox.showwarning("ADMIN", "Incorrect Password")
                    pwdentry.select_range(0, END)
                    pwdentry.focus_force()
        else:
            messagebox.showwarning(
                "ADMIN", "Username not found\nPlease register before login")

def singup():  # สมัคร
    global fname, lname, newuser, newuser, newpwd, cpwd
    global frame_lg
    kitt = Frame(root, bg='#FFFFFF')
    kitt.rowconfigure((0, 1, 2, 3, 4, 5, 6, 7, 8), weight=1)
    kitt.columnconfigure((0, 1, 2, 3), weight=1)
    root.title("Sing-up")

    frame_lg = Frame(kitt, bg='#ffffff')
    frame_lg.grid(row=2, column=2, columnspan=2, sticky='news')

    logo = Label(frame_lg, text='Masterlogic', bg='#3b5998', fg='#ffffff')
    logo.grid(row=1, column=1, columnspan=2, sticky='news', pady=50)

    firstname = LabelFrame(frame_lg, text='First name',
                           bg='#ffffff', fg='#000000')
    firstname.grid(row=2, column=1, columnspan=2)

    lastname = LabelFrame(frame_lg, text='Last name',
                          bg='#ffffff', fg='#000000')
    lastname.grid(row=3, column=1, columnspan=2)

    newuser = LabelFrame(frame_lg, text='Username',
                         bg='#ffffff', fg='#000000')
    newuser.grid(row=4, column=1, columnspan=2)

    newpwd = LabelFrame(frame_lg, text='Password',
                        bg='#ffffff', fg='#000000')
    newpwd.grid(row=5, column=1, columnspan=2)

    cfpwd = LabelFrame(frame_lg, text='Confirm Password',
                       bg='#ffffff', fg='#000000')
    cfpwd.grid(row=6, column=1, columnspan=2)

    fname = Entry(firstname, bg='#FFFFFF',
                  font=70)
    fname.grid(row=1, column=1, sticky='n', padx=10, ipadx=10, ipady=5)
    lname = Entry(lastname, bg='#FFFFFF',
                  font=70)
    lname.grid(row=3, column=1, sticky='n', padx=10, ipadx=10, ipady=5)

    newuser = Entry(newuser, bg='#FFFFFF',
                    font=70)
    newuser.grid(row=4, column=1, sticky='n', padx=10, ipadx=10, ipady=5)

    newpwd = Entry(newpwd, bg='#FFFFFF',
                   show='*', font=70)
    newpwd.grid(row=5, column=1, sticky='n', padx=10, ipadx=10, ipady=5)

    cpwd = Entry(cfpwd, bg='#FFFFFF',
                 show='*', font=70)
    cpwd.grid(row=6, column=1, sticky='n', padx=10, ipadx=10, ipady=5)

    Button(frame_lg, text="Sign-up", command=singupclick, width=10, bg='#3b5998', fg='#ffffff',
           relief=GROOVE).grid(row=7, column=1, columnspan=2, pady=5)

    Button(frame_lg, text="Back",
           command=loginlayout, width=15, bg='#dfe3ee', fg='#ffffff', relief=GROOVE).grid(row=8, column=1, columnspan=2, pady=5)

    kitt.grid(row=1, column=0, columnspan=3, rowspan=3, sticky='news')
    userentry.focus_force()

def singupclick():
    if fname.get() == "":
        messagebox.showwarning("Admin: ", "Please enter firstname")
        fname.focus_force()
    elif lname.get() == "":
        messagebox.showwarning("Admin: ", "Pleasse enter lastname")
        lname.focus_force()
    elif newuser.get() == "":
        messagebox.showwarning("Admin: ", "Please enter a new username")
        newuser.focus_force()
    elif newpwd.get() == "":
        messagebox.showwarning("Admin: ", "Please enter a password")
        newpwd.focus_force()
    elif cpwd.get() == "":
        messagebox.showwarning("Admin: ", "Please enter a confirm password")
        cpwd.focus_force()
    else:
        sql = "select * from students where username=?"
        cursor.execute(sql, [newuser.get()])
        result = cursor.fetchall()
        if result:
            messagebox.showerror("Admin:", "The username is already exists")
            newuser.select_range(0, END)
            newuser.focus_force()
        else:
            if newpwd.get() == cpwd.get():
                sql = "insert into students values (?,?,?,?)"
                param = [fname.get(), lname.get(), newuser.get(), newpwd.get()]
                cursor.execute(sql, param)
                conn.commit()
                # retrivedata()
                messagebox.showinfo("Admin:", "Registration Successfully")
                exitRegistClick()
                fname.delete(0, END)
                lname.delete(0, END)
                newuser.delete(0, END)
                newpwd.delete(0, END)
                cpwd.delete(0, END)
            else:
                messagebox.showwarning(
                    "Admin: ", "Incorrect a confirm password\n Try again")
                cpwd.selection_range(0, END)
                cpwd.focus_force()

def con():
    music()
    cls = Frame(root, bg='#FFFFFF')
    cls.rowconfigure((0, 1, 2, 3, 4, 5, 6, 7, 8), weight=1)
    cls.columnconfigure((0, 1, 2, 3), weight=1)
    root.title(f"Master Logic : User : {name}")

    frame_cls = Frame(cls, bg='#ffffff')
    frame_cls.grid(row=2, column=2, columnspan=2, sticky='news')

    logo = Label(frame_cls, text='Masterlogic', bg='#ffffff',
                 fg='#3b5998', font='sans-serif 16 bold')
    logo.grid(row=1, column=1, columnspan=2, sticky='news',)

    congratulations = Label(frame_cls, text='congratulations :',
                            bg='#ffffff', fg='#3b5998', font='sans-serif 16 bold')
    congratulations.grid(row=2, column=1, columnspan=1, sticky='news', pady=30)

    user = Label(frame_cls, text='user : '+name, bg='#ffffff', fg='#3b5998')
    user.grid(row=2, column=2, columnspan=1, sticky='news', pady=30)

    points = Label(frame_cls, text='the points you get : ' +
                   str(score), bg='#ffffff', fg='#3b5998')
    points.grid(row=3, column=1, columnspan=2, sticky='news', pady=30)

    Button(frame_cls, text="New game",
           command=newgame, width=10, bg='#3b5998', fg='#ffffff', relief=GROOVE).grid(row=6, column=1, columnspan=2, pady=5)
    Button(frame_cls, text="Exit",
           command=exit, width=15, bg='#00a400', fg='#ffffff', relief=GROOVE).grid(row=7, column=1, columnspan=2, pady=5)

    cls.grid(row=1, column=0, columnspan=3, rowspan=3, sticky='news')
    userentry.focus_force()

def exitRegistClick():
    frame_lg.destroy()
    loginlayout()

def Gamewindows(username):
    global name
    cmm1()
    # load user login data by username
    sql_student = "SELECT * FROM students WHERE username=?"
    cursor.execute(sql_student, [username])
    result_stu = cursor.fetchone()
    name = result_stu[0]+result_stu[1]
    root.title(f"Master Logic : User : "+name)
    global games
    global text_msg
    games = Frame(root, bg='#FFFFFF')
    games.grid(row=1, column=1, columnspan=2, rowspan=2, sticky=W)

    f = 5
    cl = 'white'
    slotLabel = Frame(games, bg='#dfe3ee')
    slotLabel.grid(row=1, column=0, sticky=NW, padx=5, pady=5)

    for r in range(9):
        colorbar = LabelFrame(
            slotLabel, text=f'Round {r+1}', bg='#8b9dc3', fg='#FFFFFF')
        colorbar.grid(row=r, ipadx=f, ipady=f, padx=f)
        for c in range(5):
            add_button(Button(colorbar), 1, c, cl)

    textL = Frame(games, bg='#ffffff')
    textL.grid(row=1, column=1, sticky=NE, padx=5, pady=5)

    text_msg = Text(textL, width=35, height=50,
                    bg='#dfe3ee', fg='#000000', font='tahoma 10')
    v_scrollbar = Scrollbar(textL, command=text_msg.yview)
    v_scrollbar.pack(side=RIGHT, fill=Y)
    text_msg.pack(side=LEFT, fill=Y, expand=YES)
    text_msg.bind('<Key>', lambda e: 'break')
    menu_bar = Menu(root, bg='#f7f7f7', fg='#3b5998')
    root.config(menu=menu_bar)
    menu_ls = Menu(menu_bar, tearoff=False,
                   bg='#f7f7f7', fg='#3b5998', font='Cursive 8 bold')
    menu_op = Menu(menu_bar, tearoff=False,
                   bg='#f7f7f7', fg='#3b5998', font='Cursive 8 bold')
    menu_bar.add_cascade(menu=menu_ls, label='Game')
    menu_bar.add_cascade(menu=menu_op, label='Musics')

    menu_ls.add_command(label='New Game', command=lambda: newgame())
    menu_ls.add_command(label='Exit', command=lambda: quit())

    menu_op.add_command(label='DMS', command=dms)
    menu_op.add_command(label='Music', command=music)
    menu_op.add_command(label='stop', command=fishstop)

    return text_msg

def add_button(bt, r, c, cl):
    bt.config(width=5, bg=cl,
              relief=GROOVE, state=NORMAL, command=lambda: choosecolor(bt))
    bt.grid(row=r, column=c, padx=10, pady=12)

root = Mainwindow()

userinfo = StringVar()
pwdinfo = StringVar()

createconnection()
loginlayout()
mainloop()
cursor.close()
conn.close()