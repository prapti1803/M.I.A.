import webbrowser
from twilio.rest import Client
import smtplib, ssl
from tkinter import *
from tkinter import messagebox
import mysql.connector
from datetime import date
from newsapi.newsapi_client import NewsApiClient
from PIL import ImageTk,Image
mydb = mysql.connector.connect(
        host="localhost",
        user="root",
        passwd="pr@1803",
        database="m.i.a."

    )

mycursor = mydb.cursor()
mycursor.execute("SELECT *  FROM PERSONNEL")
myresult = mycursor.fetchall()
IDS=[]
NAMES=[]
UNITS=[]
POSTINGS=[]
DOJ=[]
DESIGNATION=[]
YRS_IN_SERVICE=[]
PHOTOS=[]
NEW_POSTING=[]
OPERATIONS=[]
EMAILS=[]
PH_NOS=[]
JN_DATE=[]
AWARDS=[]
PASSWORD=[]
for x in myresult:
    IDS.append(x[0])
    NAMES.append(x[1])
    UNITS.append(x[2])
    POSTINGS.append(x[3])
    DOJ.append(x[4])
    DESIGNATION.append(x[5])
    YRS_IN_SERVICE.append(x[6])
    PHOTOS.append(x[7])
    NEW_POSTING.append(x[8])
    OPERATIONS.append(x[9])
    EMAILS.append(x[10])
    PH_NOS.append(x[11])
    JN_DATE.append(x[12])
    AWARDS.append(x[14])
    PASSWORD.append(x[15])
print(IDS,NAMES)
mycursor1 = mydb.cursor()
mycursor1.execute("SELECT *  FROM WEAPON_SYSTEM")
myresult1 = mycursor1.fetchall()
NAME=[]
IMG=[]
TYPE=[]
CATEGORY=[]
SECTION=[]
CALIBER=[]
ORIGIN=[]
DESCRIPTION=[]
STATUS=[]
QUANTITY=[]
for x in myresult1:
    NAME.append(x[0])
    IMG.append(x[1])
    TYPE.append(x[2])
    CATEGORY.append(x[3])
    SECTION.append(x[4])
    CALIBER.append(x[5])
    ORIGIN.append(x[6])
    DESCRIPTION.append(x[7])
    STATUS.append(x[8])
    QUANTITY.append(x[9])

print(NAME,SECTION,QUANTITY)


class EMPLOYEES:
    def search(self,name,id):
        window.title("                                                                     SEARCH")
        window.geometry("800x600")
        Canvas(window, bg="blue", height=600, width=800).pack()
        filename = PhotoImage(file="C:\\Users\\prapti\\PycharmProjects\\M.I.A\\Resource\\eagle5.png")
        background_label = Label(window, image=filename)
        background_label.place(x=0, y=0, relwidth=1, relheight=1)
        for i in range(len(NAMES)):
            if NAMES[i]== name.upper() and IDS[i]==id.upper():
                load = Image.open(PHOTOS[i])
                load = load.resize((250, 300), Image.ANTIALIAS)
                render = ImageTk.PhotoImage(load)
                img = Label(window, image=render)
                if len(DESIGNATION[i]+NAMES[i])<30:
                    Label(window,text=DESIGNATION[i]+" "+NAMES[i],bg='#D8D8D8',fg='black',font=('impact',15)).place(x=20,y=350)
                else:
                    Label(window, text=DESIGNATION[i] + " " + NAMES[i], bg='#D8D8D8', fg='black',
                          font=('impact', 13)).place(x=20, y=350)
                img.image = render
                img.place(x=20, y=50)
                frame=Frame(window,bg="black",borderwidth=4,relief=RIDGE)
                frame.place(x=300,y=50,height=520,width=480)
                Label(frame,text="PROFILE",fg='#787878',bg="black",font=("impact",20)).place(relx=.4,rely=.01)
                Label(frame,text="SERVICE NO.",fg='#787878',bg='black',font=("impact", 15)).place(x=50, y=50)
                Label(frame, text=IDS[i],fg='white',bg='black',font=("impact", 15)).place(x=260, y=50)
                Label(frame, text="RANK                   ",fg='#787878',bg='black',font=("impact", 15)).place(x=50, y=90)
                Label(frame, text=DESIGNATION[i],fg='white',bg='black',font=("impact", 15)).place(x=260, y=90)
                Label(frame, text="NAME                   ",fg='#787878',bg='black',font=("impact", 15)).place(x=50, y=130)

                Label(frame, text=NAMES[i],fg='white',bg='black',font=("impact", 15)).place(x=260, y=130)
                Label(frame, text="MEDALS ", fg='#787878', bg='black', font=("impact", 15)).place(x=50,
                                                                                                  y=170)
                Label(frame, text=AWARDS[i].upper(), fg='white', bg='black', font=("impact", 15)).place(x=260, y=170)
                Label(frame, text="UNIT                   ",fg='#787878',bg='black',font=("impact", 15)).place(x=50, y=210)
                if len(UNITS[i])<20:
                    Label(frame, text=UNITS[i],fg='white',bg='black',font=("impact", 15)).place(x=260, y=210)
                else :
                    Label(frame, text=UNITS[i], fg='white', bg='black', font=("impact", 13)).place(x=260, y=210)
                Label(frame, text="POSTING                ",fg='#787878',bg='black',font=("impact", 15)).place(x=50, y=250)
                Label(frame, text=POSTINGS[i],fg='white',bg='black',font=("impact", 15)).place(x=260, y=250)
                Label(frame, text="DATE OF COMMISSIONING  ",fg='#787878',bg='black',font=("impact", 15)).place(x=50, y=290)
                Label(frame, text=DOJ[i],fg='white',bg='black',font=("impact", 15)).place(x=260, y=290)
                Label(frame, text="YEARS IN SERVICE ",fg='#787878',bg='black',font=("impact", 15)).place(x=50, y=330)
                Label(frame, text=YRS_IN_SERVICE[i],fg='white',bg='black',font=("impact", 15)).place(x=260, y=330)
                Label(frame, text="RECENT TRANSFER ", fg='#787878', bg='black', font=("impact", 15)).place(x=50,
                                                                                                                  y=370)
                Label(frame, text=NEW_POSTING[i].upper(), fg='white', bg='black', font=("impact", 15)).place(x=260, y=370)
                Label(frame, text="JOINING DATE ", fg='#787878', bg='black', font=("impact", 15)).place(x=50,
                                                                                                                  y=410)
                Label(frame, text=JN_DATE[i].upper(), fg='white', bg='black', font=("impact", 15)).place(x=260, y=410)

                break



        window.mainloop()

    def find_arm(self, weapon, arm):

        window.title("                                                                   ")
        window.geometry("800x600")
        Canvas(window, bg="blue", height=600, width=800).pack()
        filename = PhotoImage(file="C:\\Users\\prapti\\PycharmProjects\\M.I.A\\Resource\\eagle5.png")
        background_label = Label(window, image=filename)
        background_label.place(x=0, y=0, relwidth=1, relheight=1)
        for i in range(len(NAME)):
            if NAME[i].upper() == weapon.upper() and SECTION[i].upper() == arm.upper():
                load = Image.open(IMG[i])
                load = load.resize((250, 300), Image.ANTIALIAS)
                render = ImageTk.PhotoImage(load)
                img = Label(window, image=render)
                if len(NAME[i]) < 30:
                    Label(window, text=NAME[i], bg='#787878', fg='black',
                          font=('impact', 15)).place(x=40, y=340)
                else:
                    Label(window, NAME[i], bg='#787878', fg='black',
                          font=('impact', 13)).place(x=40, y=340)
                img.image = render
                img.place(x=40, y=30)
                frame = Frame(window, bg="black", borderwidth=4, relief=RAISED)
                frame.place(x=300, y=30, height=550, width=500)
                Label(frame, text=NAME[i], fg='#787878', bg="black", font=("impact", 20)).place(x=100, y=10)
                Label(frame, text="NAME         ", fg='#787878', bg='black', font=("impact", 15)).place(x=50, y=50)
                Label(frame, text=NAME[i], fg='white', bg='black', font=("impact", 15)).place(x=260, y=50)
                Label(frame, text="TYPE         ", fg='#787878', bg='black', font=("impact", 15)).place(
                    x=50, y=100)
                Label(frame, text=TYPE[i], fg='white', bg='black', font=("impact", 15)).place(x=260,
                                                                                                  y=100)
                Label(frame, text="CATEGORY                   ", fg='#787878', bg='black', font=("impact", 15)).place(
                    x=50, y=150)
                Label(frame, text=CATEGORY[i], fg='white', bg='black', font=("impact", 15)).place(x=260, y=150)
                Label(frame, text="ARM                   ", fg='#787878', bg='black', font=("impact", 15)).place(
                    x=50, y=200)
                Label(frame, text=SECTION[i], fg='white', bg='black', font=("impact", 15)).place(x=260, y=200)

                Label(frame, text="DESCRIPTION    ", fg="#787878", bg='black', font=("impact", 15)).place(x=50, y=200)
                T = Text(frame, height=6, width=20,bg="black",fg='white',font=("impact", 14),relief=FLAT)
                T.place(x=260,y=200)
                T.insert(INSERT,DESCRIPTION[i])
                Label(frame, text="CALIBER                ", fg='#787878', bg='black', font=("impact", 15)).place(
                    x=50, y=350)
                Label(frame, text=CALIBER[i], fg='white', bg='black', font=("impact", 15)).place(x=260, y=350)
                Label(frame, text="STATUS    ", fg='#787878', bg='black', font=("impact", 15)).place(x=50, y=400)
                T = Text(frame, height=2, width=20, bg="black", fg='white', font=("impact", 15), relief=FLAT)
                T.place(x=260, y=400)
                T.insert(INSERT, STATUS[i])
                Label(frame, text="QUANTITY       ", fg='#787878', bg='black', font=("impact", 15)).place(
                    x=50, y=500)
                Label(frame, text=QUANTITY[i], fg='white', bg='black', font=("impact", 15)).place(x=260,y=500)

                break
        window.mainloop()
    def Weapon_System(self):
        window.title("                                                                     SEARCH")
        window.geometry("600x315")
        Canvas(window, bg="blue", height=315, width=600).pack()
        filename = PhotoImage(file="C:\\Users\\prapti\\PycharmProjects\\M.I.A\\Resource\\indian-army.png")
        background_label = Label(window, image=filename)
        background_label.place(x=0, y=0, relwidth=1, relheight=1)

        WEAPON = Label(window, text="WEAPON NAME:",fg='#787878',bg='black', font=("IMPACT", 15))
        WEAPON.place(relx=.35, rely=.40, anchor=CENTER)
        weapon = Entry(window, width=30)
        weapon.place(relx=.80, rely=.40, anchor=CENTER)
        ARM = Label(window, text="ARMS:",fg='#787878',bg='black', font=("IMPACT", 15))
        ARM.place(relx=.35, rely=.60, anchor=CENTER)
        arm = Entry(window, width=30)
        arm.place(relx=.80, rely=.60, anchor=CENTER)

        Button(window, text="FIND", font=("IMPACT", 15), bg="#787878", fg="black",borderwidth=3,relief=RIDGE,
               command=lambda: self.find_arm(weapon.get(), arm.get())).place(relx=.5, rely=.85,
                                                                       anchor=CENTER)
        window.mainloop()
    def data(self):
        window.title("                                            SEARCH")
        window.geometry("450x450")
        Canvas(window, bg="blue", height=450, width=450).pack()
        filename = PhotoImage(file="C:\\Users\\prapti\\PycharmProjects\\M.I.A\\Resource\\eagle2.png")
        background_label = Label(window, image=filename)
        background_label.place(x=0, y=0, relwidth=1, relheight=1)
        Label(window, text="SEARCH FOR A PROFILE", fg='#D8D8D8', bg="black", font=("impact", 15)).place(relx=.25,rely=.05)
        ID = Label(window, text="ID:",fg='#D8D8D8', bg="black", font=("impact", 15))
        ID.place(relx=.20, rely=.15, anchor=CENTER)
        id = Entry(window, width=30)
        id.place(relx=.50, rely=.15, anchor=CENTER)
        NAME = Label(window, text="NAME:", fg='#D8D8D8', bg="black", font=("impact", 15))
        NAME.place(relx=.20, rely=.25, anchor=CENTER)
        name = Entry(window, width=30)
        name.place(relx=.50, rely=.25, anchor=CENTER)
        Button(window, text="SEARCH", font=("impact", 15), bg="#D8D8D8", fg="black",
               command=lambda: self.search(name.get(),id.get())).place(relx=.5, rely=.4,
                                                                                            anchor=CENTER)
        window.mainloop()

    def map_kargil(self):

        webbrowser.open("C://Users/prapti/PycharmProjects/M.I.A/kargil.html")

    def kargil(self):
        window.title("KARGIL")
        window.geometry("900x600")
        Canvas(window, bg="grey", height=600, width=900).pack()
        filename = PhotoImage(file="C:\\Users\\prapti\\PycharmProjects\\M.I.A\\Resource\\eagle7.png")
        background_label = Label(window, image=filename)
        background_label.place(x=0, y=0, relwidth=1, relheight=1)
        load = Image.open("C:/Users/prapti/PycharmProjects/M.I.A/Resource/kargi1.jpg")
        load = load.resize((400, 200), Image.ANTIALIAS)
        render = ImageTk.PhotoImage(load)
        img = Label(window, image=render)
        img.image = render
        img.place(x=20, y=10)
        str = '''The Kargil War, also known as the Kargil conflict, [note (I)] was an armed conflict between India and Pakistan that took place between May and July 1999 in the Kargil district of Kashmir  and   elsewhere along the Line of Control (LOC).The cause of the war was the infiltration of Pakistani soldiers  disguised as Kashmiri militants into positions on the Indian side of the LOC,   which serves as the de  facto border between the two states. During the initial stages of the war, Pakistan blamed the fighting   entirely   on independent Kashmiri insurgents,but documents left behind by casualties and later statements by Pakistan's Prime    Minister   and   Chief  of Army Staff showed involvement of Pakistani paramilitary forces, led by General Ashraf Rashid.
        '''
        Label(window, text="THE KARGIL WAR OF 1999", fg='black', bg='#696969', font=("impact", 15)).place(
            x=20, y=200)
        T = Text(window, height=10, width=90, bg="black", fg='#A9A9A9', font=("impact", 13), relief=FLAT)
        T.place(x=20, y=230)
        T.insert(INSERT, str)
        Label(window, text="DATE:", fg='#696969', bg='black', font=("impact", 13)).place(
            x=20, y=400)
        Label(window, text="3 May – 26 July 1999", fg='#A9A9A9', bg='black', font=("impact", 13)).place(
           x=100, y=400)
        Label(window, text="RESULT:", fg='#696969', bg='black', font=("impact", 13)).place(
            x=20, y=450)
        Label(window,text='''Indian victory India regains possession of Kargil Return to the status quo ante bellum''',
             fg='#A9A9A9', bg='black', font=("impact", 13),wraplength=800,justify=LEFT).place(
            x=100, y=450)
        Label(window,
             text="CASUALITY:",
              fg='#696969', bg='black', font=("impact", 13)).place(
            x=20, y=500)

        Label(window, text='''Indian official figures:527 killed ,1,363 wounded \nPakistani figures :737-1,200 casualties , 1,000+ wounded''', fg='#A9A9A9', bg='black', font=("impact", 13),wraplength=800,justify=LEFT).place(
            x=100, y=500)

        Button(window, text="MAP",width=43, font=("impact", 14), bg="#A9A9A9", fg="black",
               command= lambda: self.map_kargil(),borderwidth=3,relief=RIDGE).place(x=450, y=170,
                                                  )

        window.mainloop()
    def map_1947(self):

        webbrowser.open("C://Users/prapti/PycharmProjects/M.I.A/1947.html")

    def War_1947(self):
        window.title("INDO-PAK WAR OF 1947")
        window.geometry("900x600")
        Canvas(window, bg="grey", height=600, width=900).pack()
        filename = PhotoImage(file="C:\\Users\\prapti\\PycharmProjects\\M.I.A\\Resource\\eagle7.png")
        background_label = Label(window, image=filename)
        background_label.place(x=0, y=0, relwidth=1, relheight=1)
        load = Image.open("C:/Users/prapti/PycharmProjects/M.I.A/Resource/War1947.jpg")
        load = load.resize((400, 200), Image.ANTIALIAS)
        render = ImageTk.PhotoImage(load)
        img = Label(window, image=render)
        img.image = render
        img.place(x=20, y=10)
        str = '''The Indo-Pakistani War of 1947–1948, sometimes known as the First Kashmir War, was an armed conflict that was fought between India and Pakistan over the princely state of Jammu and Kashmir from 1947 to 1948. It was the first of four Indo-Pakistani wars that was fought between the two newly-independent nations. Pakistan precipitated the war a few weeks after its independence by launching tribal lashkar (militias) from Waziristan, in an effort to capture Kashmir, the future of which hung in the balance. The inconclusive result of the war still affects the geopolitics of both countries.'''
        Label(window, text="INDO PAK OF 1947", fg='black', bg='#696969', font=("impact", 15)).place(
            x=20, y=200)
        T = Text(window, height=10, width=90, bg="black", fg='#A9A9A9', font=("impact", 13), relief=FLAT)
        T.place(x=20, y=230)
        T.insert(INSERT, str)
        Label(window, text="DATE:", fg='#696969', bg='black', font=("impact", 13)).place(
            x=20, y=400)
        Label(window, text="22 October 1947 – 5 January 1949", fg='#A9A9A9', bg='black', font=("impact", 13)).place(
           x=100, y=400)
        Label(window, text="RESULT:", fg='#696969', bg='black', font=("impact", 13)).place(
            x=20, y=450)
        Label(window,text='''United Nations-mandated ceasefire''',
             fg='#A9A9A9', bg='black', font=("impact", 13),wraplength=800,justify=LEFT).place(
            x=100, y=450)
        Label(window,
             text="CASUALITY:",
              fg='#696969', bg='black', font=("impact", 13)).place(
            x=20, y=500)

        Label(window, text='''Indian official figures:1,104 killed ,3,154 wounded \nPakistani figures :6,000 killed ,~14,000 wounded''', fg='#A9A9A9', bg='black', font=("impact", 13),wraplength=800,justify=LEFT).place(
            x=100, y=500)

        Button(window, text="MAP",width=43, font=("impact", 14), bg="#A9A9A9", fg="black",
               command= lambda: self.map_1947(),borderwidth=3,relief=RIDGE).place(x=450, y=170,
                                                  )

        window.mainloop()

    def map_1962(self):

        webbrowser.open("C://Users/prapti/PycharmProjects/M.I.A/1962.html")

    def War_1962(self):
        window.title("INDO-CHINA WAR OF 1962")
        window.geometry("900x600")
        Canvas(window, bg="grey", height=600, width=900).pack()
        filename = PhotoImage(file="C:\\Users\\prapti\\PycharmProjects\\M.I.A\\Resource\\eagle7.png")
        background_label = Label(window, image=filename)
        background_label.place(x=0, y=0, relwidth=1, relheight=1)
        load = Image.open("C:/Users/prapti/PycharmProjects/M.I.A/Resource/War1962.jpg")
        load = load.resize((400, 200), Image.ANTIALIAS)
        render = ImageTk.PhotoImage(load)
        img = Label(window, image=render)
        img.image = render
        img.place(x=20, y=10)
        str = '''The Sino-Indian War, also known as the Indo-China War and Sino-Indian Border Conflict, was a war between China and India that occurred in 1962. A Chinese disputed Himalayan border was the main cause of the war. There had been a series of violent border skirmishes between the two countries after the 1959 Tibetan uprising, when India granted asylum to the Dalai Lama. India initiated a defensive Forward Policy from 1960 to hinder Chinese military patrols and logistics, in which it placed outposts along the border, including several north of the McMahon Line, the eastern portion of the Line of Actual Control proclaimed by Chinese Premier Zhou Enlai in 1959.'''
        Label(window, text="SINO-INDIAN WAR OF 1962", fg='black', bg='#696969', font=("impact", 15)).place(
            x=20, y=200)
        T = Text(window, height=10, width=90, bg="black", fg='#A9A9A9', font=("impact", 13), relief=FLAT)
        T.place(x=20, y=230)
        T.insert(INSERT, str)
        Label(window, text="DATE:", fg='#696969', bg='black', font=("impact", 13)).place(
            x=20, y=400)
        Label(window, text="20 October – 21 November 1962", fg='#A9A9A9', bg='black', font=("impact", 13)).place(
           x=100, y=400)
        Label(window, text="RESULT:", fg='#696969', bg='black', font=("impact", 13)).place(
            x=20, y=450)
        Label(window,text='''Chinese victory
China took control of Aksai Chin''',
             fg='#A9A9A9', bg='black', font=("impact", 13),wraplength=800,justify=LEFT).place(
            x=100, y=450)
        Label(window,
             text="CASUALITY:",
              fg='#696969', bg='black', font=("impact", 13)).place(
            x=20, y=500)

        Label(window, text='''Indian official figures:1,383 killed, 1,696 missing, 548–1,047 wounded, 3,968 captured \nChinese figures :722 killed, 1,697 wounded''', fg='#A9A9A9', bg='black', font=("impact", 13),wraplength=800,justify=LEFT).place(
            x=100, y=500)

        Button(window, text="MAP",width=43, font=("impact", 14), bg="#A9A9A9", fg="black",
               command= lambda: self.map_1962(),borderwidth=3,relief=RIDGE).place(x=450, y=170,
                                                  )

        window.mainloop()

    def map_1965(self):

        webbrowser.open("C://Users/prapti/PycharmProjects/M.I.A/1965.html")

    def War_1965(self):
        window.title("INDO-PAK WAR OF 1965")
        window.geometry("900x600")
        Canvas(window, bg="grey", height=600, width=900).pack()
        filename = PhotoImage(file="C:\\Users\\prapti\\PycharmProjects\\M.I.A\\Resource\\eagle7.png")
        background_label = Label(window, image=filename)
        background_label.place(x=0, y=0, relwidth=1, relheight=1)
        load = Image.open("C:/Users/prapti/PycharmProjects/M.I.A/Resource/War1965.jpg")
        load = load.resize((400, 200), Image.ANTIALIAS)
        render = ImageTk.PhotoImage(load)
        img = Label(window, image=render)
        img.image = render
        img.place(x=20, y=10)
        str = '''The Indo-Pakistani War of 1965 was a culmination of skirmishes that took place between April 1965 and September 1965 between Pakistan and India. The conflict began following Pakistan's Operation Gibraltar, which was designed to infiltrate forces into Jammu and Kashmir to precipitate an insurgency against Indian rule. India retaliated by launching a full-scale military attack on West Pakistan. The seventeen-day war caused thousands of casualties on both sides and witnessed the largest engagement of armored vehicles and the largest tank battle since World War II.'''
        Label(window, text="INDO-PAK WAR OF 1965", fg='black', bg='#696969', font=("impact", 15)).place(
            x=20, y=200)
        T = Text(window, height=10, width=90, bg="black", fg='#A9A9A9', font=("impact", 13), relief=FLAT)
        T.place(x=20, y=230)
        T.insert(INSERT, str)
        Label(window, text="DATE:", fg='#696969', bg='black', font=("impact", 13)).place(
            x=20, y=400)
        Label(window, text="August – 23 September 1965", fg='#A9A9A9', bg='black', font=("impact", 13)).place(
            x=100, y=400)
        Label(window, text="RESULT:", fg='#696969', bg='black', font=("impact", 13)).place(
            x=20, y=450)
        Label(window, text='''Return to the status quo ante bellum
    Ceasefire through UNSC Resolution 211 , No permanent territorial changes''',
              fg='#A9A9A9', bg='black', font=("impact", 13), wraplength=800, justify=LEFT).place(
            x=100, y=450)
        Label(window,
              text="CASUALITY:",
              fg='#696969', bg='black', font=("impact", 13)).place(
            x=20, y=500)

        Label(window,
              text='''Indian official figures:3,000 men, 150–190 tanks, 60–75 aircraft
540 km2 (210 mi2) of territory lost (primarily in Kashmir), 548–1,047 wounded, 3,968 captured \nPakistani figures :3,800 men, 200-300 Tanks, 20 aircraft
Over 1,840 km2 (710 mi2) of territory lost (in Sindh, Lahore, Sialkot, and Kashmir sectors)''',
              fg='#A9A9A9', bg='black', font=("impact", 13), wraplength=800, justify=LEFT).place(
            x=100, y=500)

        Button(window, text="MAP", width=43, font=("impact", 14), bg="#A9A9A9", fg="black",
               command=lambda: self.map_1965(), borderwidth=3, relief=RIDGE).place(x=450, y=170,
                                                                                   )

        window.mainloop()

    def map_1971(self):
        webbrowser.open("C://Users/prapti/PycharmProjects/M.I.A/1971.html")

    def War_1971(self):
        window.title("INDO-PAK WAR OF 1971")
        window.geometry("900x600")
        Canvas(window, bg="grey", height=600, width=900).pack()
        filename = PhotoImage(file="C:\\Users\\prapti\\PycharmProjects\\M.I.A\\Resource\\eagle7.png")
        background_label = Label(window, image=filename)
        background_label.place(x=0, y=0, relwidth=1, relheight=1)
        load = Image.open("C:/Users/prapti/PycharmProjects/M.I.A/Resource/1971.jpg")
        load = load.resize((400, 200), Image.ANTIALIAS)
        render = ImageTk.PhotoImage(load)
        img = Label(window, image=render)
        img.image = render
        img.place(x=20, y=10)
        str = ''' The Indo-Pakistani War of 1971 was a military confrontation between India's Mitro bahini forces and Pakistan that occurred during the liberation war in East Pakistan from 3 December 1971 to the fall of Dacca (Dhaka) on 16 December 1971. The war began with Operation Chengiz Khan's preemptive aerial strikes on 11 Indian air stations, which led to the commencement of hostilities with Pakistan and Indian entry into the war for independence in East Pakistan on the side of Bengali nationalist forces. Lasting just 13 days, it is one of the shortest wars in history.'''
        Label(window, text="INDO-PAK WAR OF 1971", fg='black', bg='#696969', font=("impact", 15)).place(
              x=20, y=200)
        T = Text(window, height=10, width=90, bg="black", fg='#A9A9A9', font=("impact", 13), relief=FLAT)
        T.place(x=20, y=230)
        T.insert(INSERT, str)
        Label(window, text="DATE:", fg='#696969', bg='black', font=("impact", 13)).place(
                x=20, y=400)
        Label(window, text="3–16 December 1971 (13 days)", fg='#A9A9A9', bg='black', font=("impact", 13)).place(
                x=100, y=400)
        Label(window, text="RESULT:", fg='#696969', bg='black', font=("impact", 13)).place(
                x=20, y=450)
        Label(window, text='''Indian victory, Eastern front: Surrender of East Pakistan military command
Western front: Unilateral ceasefire''',
                  fg='#A9A9A9', bg='black', font=("impact", 13), wraplength=800, justify=LEFT).place(
                x=100, y=450)
        Label(window,
                  text="CASUALITY:",
                  fg='#696969', bg='black', font=("impact", 13)).place(
                x=20, y=500)

        Label(window,
                  text='''Indian official figures:2,500–3,843 killed
9,851–12,000 injured
       Pakistani figures :9,000 killed
25,000 wounded 93,000 captured)''',
                  fg='#A9A9A9', bg='black', font=("impact", 13), wraplength=800, justify=LEFT).place(
                x=100, y=500)

        Button(window, text="MAP", width=43, font=("impact", 14), bg="#A9A9A9", fg="black",
                   command=lambda: self.map_1971(), borderwidth=3, relief=RIDGE).place(x=450, y=170,
                                                                                       )

        window.mainloop()

    def war(self):
        window.title("                                                                     war")
        window.geometry("800x600")
        Canvas(window, bg="blue", height=600, width=800).pack()
        filename = PhotoImage(file="C:\\Users\\prapti\\PycharmProjects\\M.I.A\\Resource\\eagle4.png")
        background_label = Label(window, image=filename)
        background_label.place(x=0, y=0, relwidth=1, relheight=1)
        print("hello")
        Button(window, text="INDO-PAK WAR OF 1947",width=35, font=("impact", 15), bg="#A9A9A9", fg="black",relief=RIDGE,
               command=self.War_1947).place(relx=.26, rely=.1,
                                                                        )
        Button(window, text="INDO-CHINA WAR OF 1962",width=35, font=("impact", 15), bg="#A9A9A9", fg="black",relief=RIDGE,
               command=self.War_1962).place(relx=.26, rely=.2,
                                         )
        Button(window, text="INDO-PAK WAR OF 1965",width=35, font=("impact", 15), bg="#A9A9A9", fg="black",relief=RIDGE,
               command=self.War_1965).place(relx=.26, rely=.3,
                                          )
        Button(window, text="INDO-PAK WAR OF 1971",width=35, font=("impact", 15), bg="#A9A9A9", fg="black",relief=RIDGE,
               command=self.War_1971).place(relx=.26, rely=.4,
                                          )
        Button(window, text="KARGIL",width=35, font=("impact", 15), bg="#A9A9A9", fg="black",relief=RIDGE,
               command=self.kargil).place(relx=.26, rely=.5,
                                          )
        window.mainloop()
    def transfer(self,Ser_no,Trf_stn,Jn_date):
        j = 0
        for i in IDS:
            j += 1
            if i==Ser_no:

                mycursor.execute("UPDATE PERSONNEL SET NEW_POSTING = %s, JOINING_DATE = %s WHERE ID = %s ",(Trf_stn,Jn_date,i))
                mydb.commit()
                account_sid = 'AC12b491a5fe44951fbd3d8c722e59120b'
                auth_token = 'e3c11d1eb729c91625f028097c193837'


                client = Client(account_sid, auth_token)

                client.messages.create(body='You have been posted to '+Trf_stn+'. You are expected to report the station HQ  by '+Jn_date +',0000hrs . ', from_='+12058391325'
                                                 , to=PH_NOS[j-1])


                port = 465  # For SSL
                smtp_server = "smtp.gmail.com"
                sender_email = "prapti1803@gmail.com"  # Enter your address
                receiver_email = EMAILS[j-1]  # Enter receiver address
                password="1803prapti"
                message = """
                Subject: TRANSFER LETTER

                Hello sir/ma'am,
                You have been posted to %s . You are expected to reach the station Head Quarter by %s , 0000hrs. 
                Thank you"""%(Trf_stn,Jn_date)



                context = ssl.create_default_context()
                with smtplib.SMTP_SSL(smtp_server, port, context=context) as server:
                    server.login(sender_email, password)
                    server.sendmail(sender_email, receiver_email, message)
                break
    def operation(self,Ser_no,Trf_stn,Jn_date):
        j = 0
        for i in IDS:

            j += 1
            if i==Ser_no:

                mycursor.execute("UPDATE PERSONNEL SET OPERATIONS = %s, DATE_OP  = %s WHERE ID = %s ",(Trf_stn,Jn_date,i))
                mydb.commit()
                account_sid = 'AC12b491a5fe44951fbd3d8c722e59120b'
                auth_token = 'e3c11d1eb729c91625f028097c193837'


                client = Client(account_sid, auth_token)

                client.messages.create(body='You have been deployed in the operation '+Trf_stn+'. You are expected to report your CO  by '+Jn_date + '. ', from_='+12058391325'
                                                 , to=PH_NOS[j-1])


                port = 465  # For SSL
                smtp_server = "smtp.gmail.com"
                sender_email = "prapti1803@gmail.com"  # Enter your address
                receiver_email = EMAILS[j-1]  # Enter receiver address
                password="1803prapti"
                message = """
                Subject: OPERATION 

                Hello sir/ma'am,
                You have been deployed in operation %s . You are expected to contact your CO and Regiment HQ by %s , 0000hrs. 
                Thank you"""%(Trf_stn,Jn_date)



                context = ssl.create_default_context()
                with smtplib.SMTP_SSL(smtp_server, port, context=context) as server:
                    server.login(sender_email, password)
                    server.sendmail(sender_email, receiver_email, message)
                break

    def new_transfer(self):
        window.title("                                                                     ")
        window.geometry("800x600")
        Canvas(window, bg="blue", height=600, width=800).pack()
        filename = PhotoImage(file="C:\\Users\\prapti\\PycharmProjects\\M.I.A\\Resource\\eagle4.png")
        background_label = Label(window, image=filename)
        background_label.place(x=0, y=0, relwidth=1, relheight=1)
        Label(window, text="TRANSFER", bg="black", fg="#D8D8D8", font=("impact", 20)).place(relx=.25, rely=.05)
        name=Label(window, text="NAME:", bg="black", fg="#D8D8D8", font=("impact", 20))
        name.place(relx=.1, rely=.2)
        Name = Entry(window, width=30)
        Name.place(relx=.6,rely=.2,height=20)
        ser_no = Label(window, text="SERVICE NUMBER:", bg="black", fg="#D8D8D8", font=("impact", 20))
        ser_no.place(relx=.1, rely=.3)
        Ser_no = Entry(window, width=30)
        Ser_no.place(relx=.6, rely=.3,height=20)
        trf_stn = Label(window, text="TRANSFER STATION:", bg="black", fg="#D8D8D8", font=("impact", 20))
        trf_stn.place(relx=.1, rely=.4)
        Trf_stn = Entry(window, width=30)
        Trf_stn.place(relx=.6, rely=.4,height=20)
        jn_date = Label(window, text="JOINING DATE:", bg="black", fg="#D8D8D8", font=("impact", 20))
        jn_date.place(relx=.1, rely=.5)
        Jn_date = Entry(window, width=30)
        Jn_date.place(relx=.6, rely=.5,height=20)
        Button(window, text="ENTER", font=("impact", 15), bg="#D8D8D8", fg="black",
               height=1, width=15, command=lambda: self.transfer(Ser_no.get(),Trf_stn.get(),Jn_date.get()), borderwidth=3, relief=RIDGE).place(
            relx=.4, rely=0.6)
        window.mainloop()
    def new_operation(self):
        window.title("                                                                     ")
        window.geometry("800x600")
        Canvas(window, bg="blue", height=600, width=800).pack()
        filename = PhotoImage(file="C:\\Users\\prapti\\PycharmProjects\\M.I.A\\Resource\\eagle4.png")
        background_label = Label(window, image=filename)
        background_label.place(x=0, y=0, relwidth=1, relheight=1)
        Label(window, text="OPERATION", bg="black", fg="#D8D8D8", font=("impact", 20)).place(relx=.25, rely=.05)
        name = Label(window, text="NAME:", bg="black", fg="#D8D8D8", font=("impact", 20))
        name.place(relx=.1, rely=.2)
        Name = Entry(window, width=30)
        Name.place(relx=.6, rely=.2, height=20)
        ser_no = Label(window, text="SERVICE NUMBER:", bg="black", fg="#D8D8D8", font=("impact", 20))
        ser_no.place(relx=.1, rely=.3)
        Ser_no = Entry(window, width=30)
        Ser_no.place(relx=.6, rely=.3, height=20)
        trf_stn = Label(window, text="OPERATION NAME:", bg="black", fg="#D8D8D8", font=("impact", 20))
        trf_stn.place(relx=.1, rely=.4)
        Trf_stn = Entry(window, width=30)
        Trf_stn.place(relx=.6, rely=.4, height=20)
        jn_date = Label(window, text="DATE:", bg="black", fg="#D8D8D8", font=("impact", 20))
        jn_date.place(relx=.1, rely=.5)
        Jn_date = Entry(window, width=30)
        Jn_date.place(relx=.6, rely=.5, height=20)
        Button(window, text="ENTER", font=("impact", 15), bg="#D8D8D8", fg="black",
                   height=1, width=15, command=lambda: self.operation(Ser_no.get(), Trf_stn.get(), Jn_date.get()),
                   borderwidth=3, relief=RIDGE).place(
                relx=.4, rely=0.6)



        window.mainloop()
    def weapon(self,name,count):
        j = -1
        for i in NAME:

            j += 1
            if i.upper()==name.upper():
                mycursor1.execute("UPDATE WEAPON_SYSTEM SET QUANTITY = %s WHERE NAME= %s ",(QUANTITY[j]+count,i))
                mydb.commit()
                break
    def weapon_procurement(self):
        window.title("                                                                     ")
        window.geometry("800x600")
        Canvas(window, bg="blue", height=600, width=800).pack()
        filename = PhotoImage(file="C:\\Users\\prapti\\PycharmProjects\\M.I.A\\Resource\\eagle4.png")
        background_label = Label(window, image=filename)
        background_label.place(x=0, y=0, relwidth=1, relheight=1)
        Label(window, text="WEAPON PROCUREMENT", bg="black", fg="#D8D8D8", font=("impact", 20)).place(relx=.25, rely=.05)
        name = Label(window, text="WEAPON NAME:", bg="black", fg="#D8D8D8", font=("impact", 20))
        name.place(relx=.1, rely=.2)
        Name = Entry(window, width=30)
        Name.place(relx=.6, rely=.2, height=20)
        wep_name = Label(window, text="WEAPON TYPE:", bg="black", fg="#D8D8D8", font=("impact", 20))
        wep_name.place(relx=.1, rely=.3)
        Wep_name = Entry(window, width=30)
        Wep_name.place(relx=.6, rely=.3, height=20)
        count = Label(window, text="WEAPON INDUCTION:", bg="black", fg="#D8D8D8", font=("impact", 20))
        count.place(relx=.1, rely=.4)
        Count = Entry(window, width=30)
        Count.place(relx=.6, rely=.4, height=20)

        Button(window, text="ENTER", font=("impact", 15), bg="#D8D8D8", fg="black",
               height=1, width=15, command=lambda: self.weapon(Name.get(), int(Count.get())),
               borderwidth=3, relief=RIDGE).place(
            relx=.4, rely=0.7)
        window.mainloop()
    def medal(self,ser_no,award):
        j = -1

        for i in IDS:

            j += 1
            if i.upper() == ser_no.upper():
                if AWARDS[j]=='none':
                    mycursor.execute("UPDATE PERSONNEL SET AWARDS = %s WHERE ID= %s ", (award, i))
                    mydb.commit()
                else:
                    mycursor.execute("UPDATE PERSONNEL SET AWARDS = %s WHERE ID= %s ", (AWARDS[j]+','+award, i))
                    mydb.commit()

                break
    def gallantry_award(self):
        window.title("                                                                     ")
        window.geometry("800x600")
        Canvas(window, bg="blue", height=600, width=800).pack()
        filename = PhotoImage(file="C:\\Users\\prapti\\PycharmProjects\\M.I.A\\Resource\\eagle4.png")
        background_label = Label(window, image=filename)
        background_label.place(x=0, y=0, relwidth=1, relheight=1)
        Label(window, text="AWARDS AND DECORATIONS", bg="black", fg="#D8D8D8", font=("impact", 20)).place(relx=.25,
                                                                                                      rely=.05)
        name = Label(window, text="NAME:", bg="black", fg="#D8D8D8", font=("impact", 20))
        name.place(relx=.1, rely=.2)
        Name = Entry(window, width=30)
        Name.place(relx=.6, rely=.2, height=20)
        ser_no = Label(window, text="SERVICE NUMBER:", bg="black", fg="#D8D8D8", font=("impact", 20))
        ser_no.place(relx=.1, rely=.3)
        Ser_no = Entry(window, width=30)
        Ser_no.place(relx=.6, rely=.3, height=20)
        award = Label(window, text="AWARD:", bg="black", fg="#D8D8D8", font=("impact", 20))
        award.place(relx=.1, rely=.4)
        Award = Entry(window, width=30)
        Award.place(relx=.6, rely=.4, height=20)
        Button(window, text="ENTER", font=("impact", 15), bg="#D8D8D8", fg="black",
               height=1, width=15, command=lambda: self.medal(Ser_no.get(), Award.get()),
               borderwidth=3, relief=RIDGE).place(
            relx=.4, rely=0.6)
        window.mainloop()
    def recruit(self,name,ser_no,unit,jn_date,posting,img,email,ph_no,DESGN):
        if ser_no not in IDS:
            mycursor.execute("INSERT INTO PERSONNEL(NAME,ID,UNIT,DOJ,POSTINGS,images,EMAIL,PH_NO,DESIGNATION) VALUES(%s,%s,%s,%s,%s,%s,%s,%s) ", (name,ser_no,unit,jn_date,posting,img,email,ph_no,DESGN))
            mydb.commit()



    def new_recruit(self):
        window.title("                                                                     ")
        window.geometry("900x600")
        Canvas(window, bg="blue", height=600, width=900).pack()
        filename = PhotoImage(file="C:\\Users\\prapti\\PycharmProjects\\M.I.A\\Resource\\eagle7.png")
        background_label = Label(window, image=filename)
        background_label.place(x=0, y=0, relwidth=1, relheight=1)

        name = Label(window, text="NAME:", bg="black", fg="#D8D8D8", font=("impact", 20))
        name.place(relx=.1, rely=.1)
        Name = Entry(window, width=30)
        Name.place(relx=.6, rely=.1, height=20)
        ser_no = Label(window, text="SERVICE NUMBER:", bg="black", fg="#D8D8D8", font=("impact", 20))
        ser_no.place(relx=.1, rely=.2)
        Ser_no = Entry(window, width=30)
        Ser_no.place(relx=.6, rely=.2, height=20)
        unit = Label(window, text="UNIT:", bg="black", fg="#D8D8D8", font=("impact", 20))
        unit.place(relx=.1, rely=.3)
        Unit = Entry(window, width=30)
        Unit.place(relx=.6, rely=.3, height=20)
        jn_date = Label(window, text="DATE:", bg="black", fg="#D8D8D8", font=("impact", 20))
        jn_date.place(relx=.1, rely=.4)
        Jn_date = Entry(window, width=30)
        Jn_date.place(relx=.6, rely=.4, height=20)
        posting=Label(window,text='POSTING:',bg='black',fg='#D8D8D8',font=('impact',20))
        posting.place(relx=.1,rely=.5)
        Posting = Entry(window, width=30)
        Posting.place(relx=.6, rely=.5, height=20)
        img = Label(window, text='IMAGE ADDRESS:', bg='black', fg='#D8D8D8', font=('impact', 20))
        img.place(relx=.1, rely=.6)
        Img = Entry(window, width=30)
        Img.place(relx=.6, rely=.6, height=20)
        email = Label(window, text='EMAIL ID:', bg='black', fg='#D8D8D8', font=('impact', 20))
        email.place(relx=.1, rely=.7)
        Email = Entry(window, width=30)
        Email.place(relx=.6, rely=.7, height=20)
        ph_no = Label(window, text='PHONE NUMBER:', bg='black', fg='#D8D8D8', font=('impact', 20))
        ph_no.place(relx=.1, rely=.8)
        Ph_no = Entry(window, width=30)
        Ph_no.place(relx=.6, rely=.8, height=20)
        desgn = Label(window, text='DESIGNATION:', bg='black', fg='#D8D8D8', font=('impact', 20))
        desgn.place(relx=.1, rely=.9)
        Desgn = Entry(window, width=30)
        Desgn.place(relx=.6, rely=.9, height=20)
        Button(window, text="ENTER", font=("impact", 15), bg="#D8D8D8", fg="black",
               height=1, width=15, command=lambda: self.recruit(Name.get(),Ser_no.get(),Unit.get(),Jn_date.get(),Posting.get(),Img.get(),Email.get(),Ph_no.get()),
               borderwidth=3, relief=RIDGE).place(
            relx=.4, rely=0.9)

        window.mainloop()
    def wep(self,Name,Type,Category,Section,Caliber,Origin,Desc,Status,Quantity,Wep_img):
        if Name not in NAME:
            mycursor1.execute("INSERT INTO WEAPON_SYSTEM(Name,Type,Category,Section,Caliber,Origin,Description,Status,Quantity,weaponimg) VALUES(%s,%s,%s,%s,%s,%s,%s,%s,%s,%s) ", (Name,Type,Category,Section,Caliber,Origin,Desc,Status,int(Quantity),Wep_img))
            mydb.commit()
    def new_weapon(self):
        window.title("                                                                     ")
        window.geometry("800x600")
        Canvas(window, bg="blue", height=600, width=800).pack()
        filename = PhotoImage(file="C:\\Users\\prapti\\PycharmProjects\\M.I.A\\Resource\\eagle6.png")
        background_label = Label(window, image=filename)
        background_label.place(x=0, y=0, relwidth=1, relheight=1)
        Label(window, text='WEAPON INDUCTION', bg="black", fg="#D8D8D8", font=("impact", 20)).place(relx=.3,
                                                                                                          rely=.05)
        name = Label(window, text="NAME:", bg="black", fg="#D8D8D8", font=("impact", 14))
        name.place(relx=.2, rely=.1)
        Name = Entry(window, width=30)
        Name.place(relx=.6, rely=.1, height=20)
        type = Label(window, text="TYPE:", bg="black", fg="#D8D8D8", font=("impact", 14))
        type.place(relx=.2, rely=.15)
        Type = Entry(window, width=30)
        Type.place(relx=.6, rely=.15, height=20)
        category = Label(window, text="CATEGORY:", bg="black", fg="#D8D8D8", font=("impact", 14))
        category.place(relx=.2, rely=.2)
        Category = Entry(window, width=30)
        Category.place(relx=.6, rely=.2, height=20)
        section = Label(window, text="ARM:", bg="black", fg="#D8D8D8", font=("impact", 14))
        section.place(relx=.2, rely=.25)
        Section = Entry(window, width=30)
        Section.place(relx=.6, rely=.25, height=20)
        caliber = Label(window, text='CALIBER:', bg='black', fg='#D8D8D8', font=('impact', 14))
        caliber.place(relx=.2, rely=.3)
        Caliber = Entry(window, width=30)
        Caliber.place(relx=.6, rely=.3, height=20)
        origin = Label(window, text='ORIGIN:', bg='black', fg='#D8D8D8', font=('impact', 14))
        origin.place(relx=.2, rely=.35)
        Origin = Entry(window, width=30)
        Origin.place(relx=.6, rely=.35, height=20)
        desc = Label(window, text='DESCRIPTION:', bg='black', fg='#D8D8D8', font=('impact', 14))
        desc.place(relx=.2, rely=.4)
        Desc = Text(window, width=30,height=5)
        Desc.place(relx=.6, rely=.4)
        status = Label(window, text='STATUS:', bg='black', fg='#D8D8D8', font=('impact', 14))
        status.place(relx=.2, rely=.6)
        Status = Entry(window, width=30)
        Status.place(relx=.6, rely=.6, height=20)
        quantity = Label(window, text='QUANTITY:', bg='black', fg='#D8D8D8', font=('impact', 14))
        quantity.place(relx=.2, rely=.65)
        Quantity = Entry(window, width=30)
        Quantity.place(relx=.6, rely=.65, height=20)
        wep_img = Label(window, text="WEAPON IMAGE:", bg="black", fg="#D8D8D8", font=("impact", 14))
        wep_img.place(relx=.2, rely=.7)
        Wep_img = Entry(window, width=30)
        Wep_img.place(relx=.6, rely=.7, height=20)
        Button(window, text="ENTER", font=("impact", 15), bg="#D8D8D8", fg="black",
               height=1, width=15, command=lambda: self.wep(Name.get(),Type.get(),Category.get(),Section.get(),Caliber.get(),Origin.get(),Desc.get('1.0','end'),Status.get(),Quantity.get(),Wep_img.get()),
               borderwidth=3, relief=RIDGE).place(
            relx=.4, rely=0.75)
        window.mainloop()

    def update_data(self,userid):
        if userid[0:2].upper()!='sc'.upper():
            messagebox.showerror("RESTRICTED ACCESS", "Please enter all the details", parent=window)
        else:
            window.title("                                                                     ")
            window.geometry("800x600")
            Canvas(window, bg="blue", height=600, width=800).pack()
            filename = PhotoImage(file="C:\\Users\\prapti\\PycharmProjects\\M.I.A\\Resource\\eagle4.png")
            background_label = Label(window, image=filename)
            background_label.place(x=0, y=0, relwidth=1, relheight=1)
            Label(window, text="MILITARY INTELLIGENCE AGENCY", bg="black", fg="#D8D8D8", font=("impact", 25)).place(relx=.25, rely=.05)
            Button(window, text="WEAPON PROCUREMENT", font=("impact", 15), bg="#D8D8D8", fg="black",
                   activebackground="#679267", height=2, width=25, borderwidth=3, relief=RIDGE,
                   command=self.weapon_procurement).place(
                relx=0.1, rely=.15)
            Button(window, text="AWARDS AND DECORATIONS ", font=("impact", 15), bg="#D8D8D8", fg="black",
                   activebackground="#679267", height=2, width=25, borderwidth=3, relief=RIDGE,
                   command=self.gallantry_award).place(
                relx=0.1, rely=.3)
            Button(window, text="TRANSFERS", font=("impact", 15), bg="#D8D8D8",fg="black",
                   activebackground="#679267", height=2, width=25,borderwidth=3,relief=RIDGE, command=self.new_transfer).place(
                relx=0.1, rely=.45)
            Button(window, text="OPERATION DEPLOYMENT", font=("impact", 15), bg="#D8D8D8", fg="black",
                   height=2, width=25,borderwidth=3,relief=RIDGE,command=self.new_operation).place(
                relx=.6, rely=.15)
            Button(window, text="NEW RECRUITMENTS", font=("impact", 15), bg="#D8D8D8", fg="black",
                   height=2, width=25, borderwidth=3, relief=RIDGE, command=self.new_recruit).place(
                relx=.6, rely=.3)
            Button(window, text="NEW WEAPON INDUCTION", font=("impact", 15), bg="#D8D8D8", fg="black",
                   height=2, width=25, borderwidth=3, relief=RIDGE, command=self.new_weapon).place(
                relx=.6, rely=.45)
            window.mainloop()

    def update(self):
        window.title("                                                                     ")
        window.geometry("450x450")
        Canvas(window, bg="blue", height=450, width=450).pack()
        filename = PhotoImage(file="C:\\Users\\prapti\\PycharmProjects\\M.I.A\\Resource\\eagle2.png")
        background_label = Label(window, image=filename)
        background_label.place(x=0, y=0, relwidth=1, relheight=1)


        Label(window, text="AUTHORIZED ACCESS ONLY", bg="black",fg="#D8D8D8",font=("impact", 20)).place(relx=.25,rely=.05)
        username = Label(window, text="NAME:", bg="black",fg="#D8D8D8", font=("impact", 15))
        username.place(relx=.30, rely=.20, anchor=CENTER)
        usrname = Entry(window, width=30)
        usrname.place(relx=.70, rely=.20, anchor=CENTER)
        userid = Label(window, text="SERVICE NUMBER:", bg="black",fg="#D8D8D8", font=("impact", 15))
        userid.place(relx=.30, rely=.30, anchor=CENTER)
        usrid = Entry(window, width=30)
        usrid.place(relx=.70, rely=.30, anchor=CENTER)
        Button(window, text="UPDATE", font=("impact", 15), bg="#D8D8D8", fg="black",borderwidth=2, relief=RAISED,
               command=lambda: self.update_data(usrid.get())).place(relx=.5, rely=.40,anchor=CENTER)



        window.mainloop()
    def pak(self):
        window.title("                                                                     ")
        window.geometry("800x600")
        Canvas(window, bg="blue", height=600, width=800).pack()
        filename = PhotoImage(file="C:\\Users\\prapti\\PycharmProjects\\M.I.A\\Resource\\eagle6.png")
        background_label = Label(window, image=filename)
        background_label.place(x=0, y=0, relwidth=1, relheight=1)
        newsapi = NewsApiClient(api_key='168cd764270d47e2b8c86176e49b7346')

        all_articles = newsapi.get_everything(
            sources='google-news-in,the-hindu,the-times-of-india',
            q='Pakistan',
            language='en',
            from_param=date.today(),

        )
        Source = []
        Title = []
        Description = []
        for article in all_articles['articles']:
            Source.append(article['source']['name'])
            Title.append(article['title'])
            Description.append(article['description'])
        if len(Title)==0:
           Label(window, text="No News Today", bg="black", fg="#D8D8D8", font=("impact", 20)).place(relx=.3,
                                                                                             rely=.5)
        elif len(Title)==1:
            Label(window, text=Title[0], bg="black", fg="#696969", font=("impact", 20),wraplength=750,justify=LEFT).place(relx=.05,
                                                                                              rely=.1)
            Label(window, text=Description[0], bg="black", fg="#A9A9A9", font=("impact", 15),wraplength=750,justify=LEFT).place(relx=.05,
                                                                                                    rely=.25)
            Label(window, text=Source[0], bg="black", fg="#A9A9A9", font=("impact", 15)).place(relx=.8,
                                                                                               rely=.4)

        elif len(Title)>=2:
            Label(window, text=Title[0], bg="black", fg="#696969", font=("impact", 20),wraplength=750,justify=LEFT).place(relx=.05,
                                                                                                              rely=.1)
            Label(window, text=Description[0], bg="black", fg="#A9A9A9", font=("impact", 15),wraplength=750,justify=LEFT).place(relx=.05,
                                                                                              rely=.25)
            Label(window, text=Source[0], bg="black", fg="#A9A9A9", font=("impact", 15)).place(relx=.8,
                                                                                              rely=.4)
            Label(window, text=Title[1], bg="black", fg="#696969", font=("impact", 20,),wraplength=750,justify=LEFT).place(relx=.05,
                                                                                              rely=.45)
            Label(window, text=Description[1], bg="black", fg="#A9A9A9", font=("impact", 15),wraplength=750,justify=LEFT).place(relx=.05,
                                                                                                    rely=.6)
            Label(window, text=Source[1], bg="black", fg="#A9A9A9", font=("impact", 15)).place(relx=.8,
                                                                                               rely=.75)
        window.mainloop()
    def china(self):
        window.title("                                                                     ")
        window.geometry("800x600")
        Canvas(window, bg="blue", height=600, width=800).pack()
        filename = PhotoImage(file="C:\\Users\\prapti\\PycharmProjects\\M.I.A\\Resource\\eagle6.png")
        background_label = Label(window, image=filename)
        background_label.place(x=0, y=0, relwidth=1, relheight=1)
        newsapi = NewsApiClient(api_key='168cd764270d47e2b8c86176e49b7346')

        all_articles = newsapi.get_everything(
            sources='google-news-in,the-hindu,the-times-of-india',
            q='China',
            language='en',
            from_param=date.today(),

        )
        Source = []
        Title = []
        Description = []
        for article in all_articles['articles']:
            Source.append(article['source']['name'])
            Title.append(article['title'])
            Description.append(article['description'])
        if len(Title)==0:
           Label(window, text="No News Today", bg="black", fg="#D8D8D8", font=("impact", 20)).place(relx=.3,
                                                                                             rely=.5)
        elif len(Title)==1:
            Label(window, text=Title[0], bg="black", fg="#696969", font=("impact", 20),wraplength=750,justify=LEFT).place(relx=.05,
                                                                                              rely=.1)
            Label(window, text=Description[0], bg="black", fg="#A9A9A9", font=("impact", 15),wraplength=750,justify=LEFT).place(relx=.05,
                                                                                                    rely=.25)
            Label(window, text=Source[0], bg="black", fg="#A9A9A9", font=("impact", 15)).place(relx=.8,
                                                                                               rely=.4)

        elif len(Title)>=2:
            Label(window, text=Title[0], bg="black", fg="#696969", font=("impact", 20),wraplength=750,justify=LEFT).place(relx=.05,
                                                                                                              rely=.1)
            Label(window, text=Description[0], bg="black", fg="#A9A9A9", font=("impact", 15),wraplength=750,justify=LEFT).place(relx=.05,
                                                                                              rely=.25)
            Label(window, text=Source[0], bg="black", fg="#A9A9A9", font=("impact", 15)).place(relx=.8,
                                                                                              rely=.4)
            Label(window, text=Title[1], bg="black", fg="#696969", font=("impact", 20,),wraplength=750,justify=LEFT).place(relx=.05,
                                                                                              rely=.45)
            Label(window, text=Description[1], bg="black", fg="#A9A9A9", font=("impact", 15),wraplength=750,justify=LEFT).place(relx=.05,
                                                                                                    rely=.6)
            Label(window, text=Source[1], bg="black", fg="#A9A9A9", font=("impact", 15)).place(relx=.8,
                                                                                               rely=.75)
        window.mainloop()
    def northeast(self):
        window.title("                                                                     ")
        window.geometry("800x600")
        Canvas(window, bg="blue", height=600, width=800).pack()
        filename = PhotoImage(file="C:\\Users\\prapti\\PycharmProjects\\M.I.A\\Resource\\eagle6.png")
        background_label = Label(window, image=filename)
        background_label.place(x=0, y=0, relwidth=1, relheight=1)
        newsapi = NewsApiClient(api_key='168cd764270d47e2b8c86176e49b7346')

        all_articles = newsapi.get_everything(
            sources='google-news-in,the-hindu,the-times-of-india',
            q='afspa',
            language='en',
            from_param=date.today(),

        )
        Source = []
        Title = []
        Description = []
        for article in all_articles['articles']:
            Source.append(article['source']['name'])
            Title.append(article['title'])
            Description.append(article['description'])
        if len(Title)==0:
           Label(window, text="No News Today", bg="black", fg="#D8D8D8", font=("impact", 20)).place(relx=.3,
                                                                                             rely=.5)
        elif len(Title)==1:
            Label(window, text=Title[0], bg="black", fg="#696969", font=("impact", 20),wraplength=750,justify=LEFT).place(relx=.05,
                                                                                              rely=.1)
            Label(window, text=Description[0], bg="black", fg="#A9A9A9", font=("impact", 15),wraplength=750,justify=LEFT).place(relx=.05,
                                                                                                    rely=.25)
            Label(window, text=Source[0], bg="black", fg="#A9A9A9", font=("impact", 15)).place(relx=.8,
                                                                                               rely=.4)

        elif len(Title)>=2:
            Label(window, text=Title[0], bg="black", fg="#696969", font=("impact", 20),wraplength=750,justify=LEFT).place(relx=.05,
                                                                                                              rely=.1)
            Label(window, text=Description[0], bg="black", fg="#A9A9A9", font=("impact", 15),wraplength=750,justify=LEFT).place(relx=.05,
                                                                                              rely=.25)
            Label(window, text=Source[0], bg="black", fg="#A9A9A9", font=("impact", 15)).place(relx=.8,
                                                                                              rely=.4)
            Label(window, text=Title[1], bg="black", fg="#696969", font=("impact", 20,),wraplength=750,justify=LEFT).place(relx=.05,
                                                                                              rely=.45)
            Label(window, text=Description[1], bg="black", fg="#A9A9A9", font=("impact", 15),wraplength=750,justify=LEFT).place(relx=.05,
                                                                                                    rely=.6)
            Label(window, text=Source[1], bg="black", fg="#A9A9A9", font=("impact", 15)).place(relx=.8,
                                                                                               rely=.75)
        window.mainloop()
    def kashmir(self):
        window.title("                                                                     ")
        window.geometry("800x600")
        Canvas(window, bg="blue", height=600, width=800).pack()
        filename = PhotoImage(file="C:\\Users\\prapti\\PycharmProjects\\M.I.A\\Resource\\eagle6.png")
        background_label = Label(window, image=filename)
        background_label.place(x=0, y=0, relwidth=1, relheight=1)
        newsapi = NewsApiClient(api_key='168cd764270d47e2b8c86176e49b7346')

        all_articles = newsapi.get_everything(
            sources='google-news-in,the-hindu,the-times-of-india',
            q='kashmir',
            language='en',
            from_param=date.today(),

        )
        Source = []
        Title = []
        Description = []
        for article in all_articles['articles']:
            Source.append(article['source']['name'])
            Title.append(article['title'])
            Description.append(article['description'])
        if len(Title)==0:
           Label(window, text="No News Today", bg="black", fg="#D8D8D8", font=("impact", 20)).place(relx=.3,
                                                                                             rely=.5)
        elif len(Title)==1:
            Label(window, text=Title[0], bg="black", fg="#696969", font=("impact", 20),wraplength=750,justify=LEFT).place(relx=.05,
                                                                                              rely=.1)
            Label(window, text=Description[0], bg="black", fg="#A9A9A9", font=("impact", 15),wraplength=750,justify=LEFT).place(relx=.05,
                                                                                                    rely=.25)
            Label(window, text=Source[0], bg="black", fg="#A9A9A9", font=("impact", 15)).place(relx=.8,
                                                                                               rely=.4)

        elif len(Title)>=2:
            Label(window, text=Title[0], bg="black", fg="#696969", font=("impact", 20),wraplength=750,justify=LEFT).place(relx=.05,
                                                                                                              rely=.1)
            Label(window, text=Description[0], bg="black", fg="#A9A9A9", font=("impact", 15),wraplength=750,justify=LEFT).place(relx=.05,
                                                                                              rely=.25)
            Label(window, text=Source[0], bg="black", fg="#A9A9A9", font=("impact", 15)).place(relx=.8,
                                                                                              rely=.4)
            Label(window, text=Title[1], bg="black", fg="#696969", font=("impact", 20,),wraplength=750,justify=LEFT).place(relx=.05,
                                                                                              rely=.45)
            Label(window, text=Description[1], bg="black", fg="#A9A9A9", font=("impact", 15),wraplength=750,justify=LEFT).place(relx=.05,
                                                                                                    rely=.6)
            Label(window, text=Source[1], bg="black", fg="#A9A9A9", font=("impact", 15)).place(relx=.8,
                                                                                               rely=.75)
        window.mainloop()
    def terror(self):
        window.title("                                                                     ")
        window.geometry("800x600")
        Canvas(window, bg="blue", height=600, width=800).pack()
        filename = PhotoImage(file="C:\\Users\\prapti\\PycharmProjects\\M.I.A\\Resource\\eagle6.png")
        background_label = Label(window, image=filename)
        background_label.place(x=0, y=0, relwidth=1, relheight=1)
        newsapi = NewsApiClient(api_key='168cd764270d47e2b8c86176e49b7346')

        all_articles = newsapi.get_everything(
            sources='google-news-in,the-hindu,the-times-of-india',
            q='terrorism',
            language='en',
            from_param=date.today(),

        )
        Source = []
        Title = []
        Description = []
        for article in all_articles['articles']:
            Source.append(article['source']['name'])
            Title.append(article['title'])
            Description.append(article['description'])
        if len(Title)==0:
           Label(window, text="No News Today", bg="black", fg="#D8D8D8", font=("impact", 20)).place(relx=.3,
                                                                                             rely=.5)
        elif len(Title)==1:
            Label(window, text=Title[0], bg="black", fg="#696969", font=("impact", 20),wraplength=750,justify=LEFT).place(relx=.05,
                                                                                              rely=.1)
            Label(window, text=Description[0], bg="black", fg="#A9A9A9", font=("impact", 15),wraplength=750,justify=LEFT).place(relx=.05,
                                                                                                    rely=.25)
            Label(window, text=Source[0], bg="black", fg="#A9A9A9", font=("impact", 15)).place(relx=.8,
                                                                                               rely=.4)

        elif len(Title)>=2:
            Label(window, text=Title[0], bg="black", fg="#696969", font=("impact", 20),wraplength=750,justify=LEFT).place(relx=.05,
                                                                                                              rely=.1)
            Label(window, text=Description[0], bg="black", fg="#A9A9A9", font=("impact", 15),wraplength=750,justify=LEFT).place(relx=.05,
                                                                                              rely=.25)
            Label(window, text=Source[0], bg="black", fg="#A9A9A9", font=("impact", 15)).place(relx=.8,
                                                                                              rely=.4)
            Label(window, text=Title[1], bg="black", fg="#696969", font=("impact", 20,),wraplength=750,justify=LEFT).place(relx=.05,
                                                                                              rely=.45)
            Label(window, text=Description[1], bg="black", fg="#A9A9A9", font=("impact", 15),wraplength=750,justify=LEFT).place(relx=.05,
                                                                                                    rely=.6)
            Label(window, text=Source[1], bg="black", fg="#A9A9A9", font=("impact", 15)).place(relx=.8,
                                                                                               rely=.75)
        window.mainloop()

    def news(self):
        window.title("                                                                     ")
        window.geometry("800x600")
        Canvas(window, bg="blue", height=600, width=800).pack()
        filename = PhotoImage(file="C:\\Users\\prapti\\PycharmProjects\\M.I.A\\Resource\\eagle4.png")
        background_label = Label(window, image=filename)
        background_label.place(x=0, y=0, relwidth=1, relheight=1)
        Label(window, text="TODAYS NEWS", bg="black", fg="#D8D8D8", font=("impact", 25)).place(
            relx=.4, rely=.05)
        Button(window, text="NEWS FROM PAKISTAN", font=("impact", 15), bg="#D8D8D8", fg="black",
               activebackground="#679267", height=2, width=25, borderwidth=3, relief=RIDGE,
               command=self.pak).place(
            x=60, y=100)
        Button(window, text="NEWS FROM NORTH EAST", font=("impact", 15), bg="#D8D8D8", fg="black",
               activebackground="#679267", height=2, width=25, borderwidth=3, relief=RIDGE
               ,command=self.northeast).place(
            x=500, y=100)
        Button(window, text="NEWS FROM KASHMIR", font=("impact", 15), bg="#D8D8D8", fg="black",
               activebackground="#679267", height=2, width=25, borderwidth=3, relief=RIDGE,command=self.kashmir
              ).place(
            x=60, y=200)
        Button(window, text="NEWS FROM CHINA", font=("impact", 15), bg="#D8D8D8", fg="black",
               height=2, width=25, borderwidth=3, relief=RIDGE,command=self.china).place(
            x=500, y=200)
        Button(window, text="Terrorism", font=("impact", 15), bg="#D8D8D8", fg="black",
               height=2, width=25, borderwidth=3, relief=RIDGE,command=self.terror).place(
            x=270, y=300)
        window.mainloop()



    def home(self,password='pr@1803', uid='123', uname='NONE'):
        for i in range(len(NAMES)):
            if password == "" or uname == "" or uid == "":
                messagebox.showerror("                       ERROR", "Please enter all the details", parent=window)
            elif password !=PASSWORD[i]:
                messagebox.showerror("                ERROR", "Wrong password", parent=window)
            elif uname.upper() == NAMES[i] and uid.upper()!=IDS[i]:
                messagebox.showerror("                  ERROR", "Wrong service ID", parent=window)


            elif uname.upper() not in NAMES:
                messagebox.showerror("                  ERROR", "Person not in database", parent=window)
            elif uname.upper() == NAMES[i] and uid.upper() == IDS[i]:
                def goback():
                    self.home()

                menubar = Menu(window)
                menubar.add_command(label="HOME", command=goback)
                window.config(menu=menubar)

        # display the menu

                window.title("                                                                      HOME")

                window.geometry("800x600")

                Canvas(window, bg="blue", height=600, width=800).pack()

                filename = PhotoImage(file="C:\\Users\\prapti\\PycharmProjects\\M.I.A\\Resource\\eagle4.png")
                background_label = Label(window, image=filename)
                background_label.place(x=0, y=0, relwidth=1, relheight=1)

                Button(window, text="PERSONNEL INFORMATION", font=("impact", 15), bg="#D8D8D8", fg="black", height=1, width=40, command= self.data,borderwidth=2,relief=RIDGE).place(
            relx=.25, rely=.1)
                Button(window, text="NEWS", font=("impact", 15), bg="#D8D8D8", fg="black", height=1, width=40,borderwidth=2,relief=RIDGE,command=self.news).place(
            relx=.25, rely=.2)
                Button(window, text="WARS FOUGHT POST INDEPENDENCE", font=("impact", 15), bg="#D8D8D8", fg="black", height=1, width=40,command=self.war,borderwidth=2,relief=RIDGE).place(relx=.25, rely=.3)
                Button(window, text="WEAPON SYSTEM", font=("impact", 15), bg="#D8D8D8", fg="black", height=1, width=40,command= self.Weapon_System,borderwidth=2,relief=RIDGE).place(relx=.25, rely=.4)
                Button(window, text="UPDATE", font=("impact", 15), bg="#D8D8D8", fg="black", height=1, width=40, command=self.update,borderwidth=2,relief=RIDGE).place(relx=.25, rely=.5)

                window.mainloop()


    def login(self):
        window.title("                                                                     LOGIN")
        window.geometry("450x450")
        Canvas(window, bg="blue", height=450, width=450).pack()
        filename = PhotoImage(file="C:\\Users\\prapti\\PycharmProjects\\M.I.A\\Resource\\eagle2.png")
        background_label = Label(window, image=filename)
        background_label.place(x=0, y=0, relwidth=1, relheight=1)
        username = Label(window, text="USER NAME:", bg="black",fg="#D8D8D8", font=("impact", 15))
        username.place(relx=.30, rely=.10, anchor=CENTER)
        usrname = Entry(window, width=30)
        usrname.place(relx=.70, rely=.10, anchor=CENTER)
        userid = Label(window, text="SERVICE NUMBER:", bg="black",fg="#D8D8D8", font=("impact", 15))
        userid.place(relx=.30, rely=.20, anchor=CENTER)
        usrid = Entry(window, width=30)
        usrid.place(relx=.70, rely=.20, anchor=CENTER)
        pssword = Label(window, text="PASSWORD:", bg="black",fg="#D8D8D8", font=("impact", 15))
        pssword.place(relx=.30, rely=.30, anchor=CENTER)
        password = Entry(window, show="*", width=30)
        password.place(relx=.70, rely=.30, anchor=CENTER)
        print(password.get(), usrname.get(), usrid.get())
        Button(window, text="LOGIN", font=("impact", 15), bg="#D8D8D8",fg="black",relief=RAISED,
           command=lambda: self.home(password.get(), usrid.get(), usrname.get())).place(relx=.5, rely=.40, anchor=CENTER)

        window.mainloop()


window = Tk()
x=EMPLOYEES()
window.title("                                                           M.I.A.: Military Intelligence Agency")
Canvas(window, bg="blue", height=500, width=600).pack()
filename = PhotoImage(file="C:\\Users\\prapti\\PycharmProjects\\M.I.A\\Resource\\cami1.png")
background_label = Label(window, image=filename).place(x=0, y=0, relwidth=1, relheight=1)
Button(window, text="LOGIN", font=("Helvetica", 15), bg="dark green", fg="black", command=lambda: EMPLOYEES.login(x)).place(
    relx=.5, rely=.65, anchor=CENTER)

window.mainloop()
