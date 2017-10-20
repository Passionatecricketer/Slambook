class slambook:
    def __init__(self,name="",hobby="",song="",gender="",ideal="",food="",friend="",aim="",motto="",colour="",ambition="",d=0,m=0,y=0):
        self.name=name
        self.hobby=hobby
        self.song=song
        self.gender=gender
        self.ideal=ideal
        self.food=food
        self.friend=friend
        self.aim=aim
        self.motto=motto
        self.colour=colour
        self.ambition=ambition
    def new_entry(self):
        print "\t"*4,
        print "All about"
        a=[]
        f=True
        while f:
            print "\t"*3,
            self.name=raw_input("You are:")
            s=self.name
            for i in range(len(self.name)):
                if s[i] in [0,1,2,3,4,5,6,7,8,9]:
                    print "\t"*3,
                    print "Name cannot contain numbers"
                    f=True
                    break
                else:
                    f=False
                    continue
        a.append(self.name+"\n")
        return a

    def new_entry1(self):
        print "\t"*3,
        self.gender=raw_input("Are you male/female:")
        print "\t"*3,
        self.hobby=raw_input("What is your hobby:")
        print "\t"*3,
        self.song=raw_input("What's your favourite song:")
        print "\t"*3,
        self.colour=raw_input("What is your favourite colour:")
        print "\t"*3,
        self.food=raw_input("Favourite delicacy of mom's hand:")
        print "\t"*3,
        self.friend=raw_input("Name of your bfl(bestie for life:")
        print "\t"*3,
        self.aim=raw_input("What is your aim in life:")
        print "\t"*3,
        self.ideal=raw_input("who is your idea:")
        print "\t"*3,
        self.motto=raw_input("Your motto of life:")
        print "\t"*3,
        self.ambition=raw_input("Your ambition in life:")
        print "\n"*3,
        s=[]
        s.append(self.hobby+"\n")
        s.append(self.song+"\n")
        s.append(self.gender+"\n")
        s.append(self.ideal+"\n")
        s.append(self.food+"\n")
        s.append(self.friend+"\n")
        s.append(self.aim+"\n")
        s.append(self.motto+"\n")
        s.append(self.colour+"\n")
        s.append(self.ambition+"\n")
        return s
    def dob(self):
        h=[]
        a=1
        while a==1:
            try:
                print "\t"*3,
                self.d=input("enter the day of your birth(1-31):")
                print "\t"*3,
                self.m=input("Enter the month of your birth(1-12):")
                print "\t"*3,
                self.y=input("Enter the year of your birth(1900-2017):")
                if self.d<1 or self.d>31:
                    raise ValueError,"Date is out of range"
                if self.m<1 or self.m>12:
                    raise ValueError,"Month is out of range"
                if self.y<1900 or self.y>2017:
                    raise ValueError,"year is out of range"
            except ValueError,e:
                print "\t"*3,
                print e.message
                a=1
            else:
                break
        h.append(str(self.d))
        h.append("/")
        h.append(str(self.m))
        h.append("/")
        h.append(str(self.y)+"\n")
        return h
    def dob1(self):
        print "Date of birth:",str(self.d)+"/"+str(self.m)+"/"+str(self.y) 
    def entry_display(self):
        print "\t"*3,
        print self.name,"'s details"
        print "\t"*3,
        slambook.dob1(self)
        print "\t"*3,
        print "Favouritr song:",self.song
        print "\t"*3,
        print "Hobby:",self.hobby
        print "\t"*3,
        print "Gender:",self.gender
        print "\t"*3,
        print "Ideal:",self.ideal
        print "\t"*3,
        print "Favourite food:",self.food
        print "\t"*3,
        print "Best friend's name:",self.friend
        print "\t"*3,
        print "Aim:",self.aim
        print "\t"*3,
        print "Motto:",self.motto
        print "\t"*3,
        print "Favourite colour:",self.colour
        print "\t"*3,
        print "Ambition:",self.ambition
        print "\t"*3,
        


b=[]
b.append("Name"+"\n")
b.append("Date of birth"+"\n")
b.append("Hobby"+"\n")
b.append("Favourite song"+"\n")
b.append("Gender"+"\n")
b.append("Ideal"+"\n")
b.append("Favourite food"+"\n")
b.append("Best friend's name"+"\n")
b.append("Aim"+"\n")
b.append("Motto"+"\n")
b.append("Favourite colour"+"\n")
b.append("Ambition"+"\n")
f=slambook()
g=open("slambook.txt","w+")
g.writelines(b)
g.close()

x=0
while x==0:
    f.new_entry()
    f.dob()
    f.new_entry1()
    f.entry_display()
    print "\t"*3,
    ch=raw_input("Want to enter more records(Y/N)?")
    if ch=="Y" or ch=="y":
        x=0
    else:
        x=1
        break
k=open("slambook2.txt","a+")
k.writelines(f.new_entry())
k.writelines(f.new_entry1())
k.writelines(f.dob())
k.writelines(f.add())
k.close()

g=open("slambook.txt","r+")
k=open("slambook.txt","r+")
y=g.readlines()
s=k.readlines()
m=0
while m==0:
    print "\t"*3,
    print "Menu"
    print "\t"*3,
    print "1.Want to search person having same name"
    print "\t"*3,
    print "2.Want to search person by date of birth"
    print "\t"*3,
    print "3.Exit"
    print "\n"
    print "\t"*3,
    c=raw_input("Enter the choice:")
    a=0
    while c=="1":
        print "\t"*3,
        d=raw_input("Enter the name to be searched:")
        for i in range(0,len(s),12):
            if s[i]==d+"\n":
                print "\n"*4,
                m=0
                while m<=11:
                    print b[m],":",s[i+m]
                    m+=1
                    a=0
            else:
                a+=1
                continue
        if len(s)/12==a-1:
            print "\n"
            print "\t"*2,
            print ".......Entered name is not found......"
            print "\n"*3
        print "\n"*3
        r=raw_input("Want to search more or not(Y/N):")
        if r=="Y" or r=="y":
            c="1"
        else:
            c=1

    while c=="2":
        f=0
        print "\t"*3,
        d=raw_input("Enter the day of birth:")
        print "\t"*3,
        m=raw_input("Enter the month of birth:")
        print "\t"*3,
        y=raw_input("Enter the year of birth:")
        for i in range(1,len(s),12):
            if s[i]==str(d)+"/"+str(m)+"/"+str(y)+"/n":
                print "\n"*4
                m=0
                while m<=11:
                    print b[m],s[i+(m-1)]
                    m+=1
                    f=0
            else:
                f+=1
                continue
        if len(s)/12==f-1:
            print "\n"
            print "\t"*2,
            print "......Entered date of birth is not found....."
            print "\n"*3
        print "\n"*3
        d=raw_input("Want to search more(Y/N):")
        if d=="Y" or d=="y":
            c="2"
        else:
            c=0
    else:
        print "\n"*3,"\t"
        print "......Thanks for running the program....."
    f=raw_input("want to again search(Y/N):")
    if f=="Y" or f=='y':
        m=0
    else:
        m=1
