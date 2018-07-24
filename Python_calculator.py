#Special Calculator
#wrote by HAO PENG. ID:1780718

from tkinter import*
from math import*

num_reg=0                   #fot one-argument option, this variable store the number. for two-arguments option, it store the first argument
symbol_record=''            #this variable store the operational character
numtype_record=1            #if the vale of this variable is 0, it represents integer mode. if it is 1, it represent float mode    
angtype_record=0            #if the vale of this variable is 0, it represents degree mode. if it is 1, it represent radian mode 

def clean(event):                       #clean the entry text and initialize all variables
    global symbol_record
    global num_reg
    num_reg=0
    symbol_record=''
    display['text']=''
    numEntry.delete(0,'end')

def delete(event):                      #delect function
    global num_reg
    global symbol_record
    ind=numEntry.index('end')
    ind=ind-1
    if symbol_record=='':               #if there is no operational character, then it will delete last digit of num_reg                    
        numEntry.delete(ind)
        if ind>0:
            #if numtype_record==0:
            num_reg=numEntry.get()
            #else:
                #num_reg=float(numEntry.get())
            numEntry.delete(0,'end')
            numEntry.insert('end',num_reg)
        if ind==0:
            num_reg=0
    else:                               #if there is operational character, then it will delete last digit of second argument 
        if ind>0:
            numEntry.delete(ind)
            #if numtype_record==0:
            num=numEntry.get()
            #else:
                #num=float(numEntry.get())
            numEntry.delete(0,'end')
            numEntry.insert('end',num)
        if ind==0:
            numEntry.delete(ind)
        if ind<0:                       #or delect the operator
            symbol_record=''
            numEntry.delete(0,'end')
            numEntry.insert('end',num_reg)
    display['text']=str(num_reg)+symbol_record
     
def integers(event):                    #set mode as integer mode
    global numtype_record
    numtype_record=0
    label1['text']='Integer mood'

def floats(event):                      #set mode as float mode
    global numtype_record
    numtype_record=1
    label1['text']='Float   mood'

def degrees(event):                     #set mode as degree mode
    global angtype_record
    angtype_record=0
    label2['text']='Degree mood'

def radians(event):                     #set mode as radian mode
    global angtype_record
    angtype_record=1
    label2['text']='Radian mood'

def seven(event):                       #input 7
    numEntry.insert('end',7)
def eight(event):                       #input 8
    numEntry.insert('end',8)
def nine(event):                        #input 9
    numEntry.insert('end',9)
def four(event):                        #input 4
    numEntry.insert('end',4)
def five(event):                        #input 5
    numEntry.insert('end',5)
def six(event):                         #input 6
    numEntry.insert('end',6)
def one(event):                         #input 1
    numEntry.insert('end',1)
def two(event):                         #input 2
    numEntry.insert('end',2)
def three(event):                       #input 3
    numEntry.insert('end',3)
def zero(event):                        #input 0
    numEntry.insert('end',0)
def point(event):                       #input '.'
    numEntry.insert('end','.')
    
def subtract(event):                    #funvtion of subtraction and negative indication
    global num_reg
    global symbol_record
    global numtype_record
    ind=numEntry.index('end')
    if ind==0:                          #if there is no value,the '-' will represent negative indication
        numEntry.insert('end','-')
    else:                               #if there has value,the '-' will represent subtraction
        if numtype_record==0:
            num_reg=int(numEntry.get())
        else:
            num_reg=float(numEntry.get())
        display['text']=str(num_reg)+'-'
        numEntry.delete(0,'end')
        symbol_record='-'
def add(event):                         #funvtion of addition
    global num_reg
    global symbol_record
    global numtype_record
    ind=numEntry.index('end')
    if ind==0:
        numEntry.insert('end','+')
    else:
        if numtype_record==0:
            num_reg=int(numEntry.get())
        else:
            num_reg=float(numEntry.get())
        display['text']=str(num_reg)+'+'
        numEntry.delete(0,'end')
        symbol_record='+'
def mul(event):                         #funvtion of multipling
    global num_reg
    global symbol_record
    global numtype_record
    if numtype_record==0:
        num_reg=int(numEntry.get())
    else:
        num_reg=float(numEntry.get())
    display['text']=str(num_reg)+'*'
    numEntry.delete(0,'end')
    symbol_record='*'
def div(event):                         #funvtion of dividing
    global num_reg
    global symbol_record
    global numtype_record
    if numtype_record==0:
        num_reg=int(numEntry.get())
    else:
        num_reg=float(numEntry.get())
    display['text']=str(num_reg)+'/'
    numEntry.delete(0,'end')
    symbol_record='/'

def square_root(event):                 #Founction of square_root
    global numtype_record
    global num_reg
    num=float(numEntry.get())
    if num<0:
        display['text']='√'+str(num)+' negative input'
    else:
        if numtype_record==0:
            num_reg=int(sqrt(num))
            num=int(num)
        else:
            num_reg=float(sqrt(num))
        display['text']='√'+str(num)+'='+str(num_reg)
        numEntry.delete(0,'end')
        numEntry.insert(0,num_reg)

def raise_to_power(event):              #Founction of power
    global num_reg
    global symbol_record
    global numtype_record
    if numtype_record==0:
        num_reg=int(numEntry.get())
    else:
        num_reg=float(numEntry.get())
    display['text']=str(num_reg)+'^'
    numEntry.delete(0,'end')
    symbol_record='^'

def log_ten(event):                     #Founction of log based on 10
    global numtype_record
    num=float(numEntry.get())
    if num<=0:
        display['text']='log'+str(num)+' input is unvaluable, error'
    else:
        if numtype_record==0:
            num_reg=int(log10(num))
            num=int(num)
        else:
            num_reg=float(log10(num))
        display['text']='log'+str(num)+'='+str(num_reg)
        numEntry.delete(0,'end')
        numEntry.insert(0,num_reg)

def sins(event):                        #Founction of sin
    global numtype_record
    global angtype_record
    num=float(numEntry.get())
    if angtype_record==0:
        if numtype_record==0:
            num_reg=int(sin(num*pi/180))     #in degree mode, it will transform degree to radian, then caculate the function
            num=int(num)
        else:
            num_reg=float(sin(num*pi/180))    
    else:
        if numtype_record==0:
            num_reg=int(sin(num))
            num=int(num)
        else:
            num_reg=float(sin(num))
    display['text']='sin'+str(num)+'='+str(num_reg)
    numEntry.delete(0,'end')
    numEntry.insert(0,num_reg)

def coss(event):                        #Founction of cos
    global numtype_record
    global angtype_record
    num=float(numEntry.get())
    if angtype_record==0:
        if numtype_record==0:
            num_reg=int(cos(num*pi/180))
            num=int(num)
        else:
            num_reg=float(cos(num*pi/180))    
    else:
        if numtype_record==0:
            num_reg=int(cos(num))
            num=int(num)
        else:
            num_reg=float(cos(num))
    display['text']='cos'+str(num)+'='+str(num_reg)
    numEntry.delete(0,'end')
    numEntry.insert(0,num_reg)

def tans(event):                        #Founction of tans
    global numtype_record
    global angtype_record
    num=float(numEntry.get())
    if angtype_record==0:
        if numtype_record==0:
            num_reg=int(tan(num*pi/180))
            num=int(num)
        else:
            num_reg=float(tan(num*pi/180))    
    else:
        if numtype_record==0:
            num_reg=int(tan(num))
            num=int(num)
        else:
            num_reg=float(tan(num))
    display['text']='tan'+str(num)+'='+str(num_reg)
    numEntry.delete(0,'end')
    numEntry.insert(0,num_reg)
    
def equal(event):                       #Founction of equality sign
    global num_reg
    global symbol_record
    global numtype_record
    if numtype_record==0:
        num=int(numEntry.get())
    else:
        num=float(numEntry.get())
    num2=num_reg
    if symbol_record=='^':              #for two-arguments operation, the function 'equal' will distinguish what operator has been inputed, then run different function. here it runs power function
        if numtype_record==0:
            num_reg=int(pow(num_reg,num))
        else:
            num_reg=float(pow(num_reg,num))
        display['text']=str(num2)+'^'+str(num)+'='+str(num_reg)
    if symbol_record=='-':              #here is subtraction
        num_reg=num_reg-num
        display['text']=str(num2)+'-'+str(num)+'='+str(num_reg)
    if symbol_record=='+':              #here is addition
        num_reg=num_reg+num
        display['text']=str(num2)+'+'+str(num)+'='+str(num_reg)
    if symbol_record=='*':              #here is multipling
        num_reg=num_reg*num
        display['text']=str(num2)+'*'+str(num)+'='+str(num_reg)
    if symbol_record=='/':              #here is dividing
        if num==0:
            display['text']=str(num2)+'/'+str(num)+' dividend is 0, error'
        else:
            if numtype_record==0:
                num_reg=int(num_reg/num)
            else:
                num_reg=float(num_reg/num)
            display['text']=str(num2)+'/'+str(num)+'='+str(num_reg)
    if symbol_record=='':               #here is just equal for one argument
        num_reg=num
        display['text']=str(num_reg)
    numEntry.delete(0,'end')
    numEntry.insert(0,num_reg)
    symbol_record=''
    

root=Tk()                               #definition of GUI interface
root.title('Special Calculatro')
root.geometry("350x230+200+20")

frame0=Frame(root,bg='black',width=350)                      #I has definded 4 frame. the first is used to displaying. the second is used to select mode. the third is use to input and output. the last one is used to construct function buttons.
frame0.grid(row=0,column=0,sticky=W,padx=0,pady=0,ipadx=50)

display=Label(frame0,text='',anchor='nw',bg='black',fg='white',width=35,justify='left')
display.pack(fill=X)

frame1=Frame(root,bg='black',width=350)
frame1.grid(row=1,column=0,sticky=W,padx=0,pady=0,ipadx=3)

label1=Label(frame1,text='Float   mood',bg='#272727',fg='white',anchor='center',justify='center',width=12)   # display laber
label1.grid(row=0,column=0,sticky=W+E+N+S,padx=1,pady=2,ipadx=40)

label2=Label(frame1,text='Degree mood',bg='#272727',fg='white',anchor='center',justify='center',width=12)
label2.grid(row=0,column=1,sticky=W+E+N+S,padx=1,pady=2,ipadx=40)

frame2=Frame(root,bg="black",width=350)
frame2.grid(row=2,column=0,sticky=W,padx=0,pady=0,ipadx=2)

intButton=Button(frame2,text='Integer',width=8,bg='#adadad',fg='white')                         # mode select button
intButton.bind("<Button-1>",integers)
intButton.grid(row=0,column=0,sticky=W+E+N+S,padx=1,pady=2,ipadx=11)

floButton=Button(frame2,text='Float',width=7,bg='#adadad',fg='white')
floButton.bind("<Button-1>",floats)
floButton.grid(row=0,column=1,sticky=W+E+N+S,padx=1,pady=2,ipadx=11)

degButton=Button(frame2,text='Degree',width=8,bg='#adadad',fg='white')
degButton.bind("<Button-1>",degrees)
degButton.grid(row=0,column=2,sticky=W+E+N+S,padx=1,pady=2,ipadx=11)

radButton=Button(frame2,text='Radian',width=7,bg='#adadad',fg='white')
radButton.bind("<Button-1>",radians)
radButton.grid(row=0,column=3,sticky=W+E+N+S,padx=1,pady=2,ipadx=11)

frame3=Frame(root,bg='black',width=350)
frame3.grid(row=4,column=0,sticky=W,padx=0,pady=0,ipadx=3)

numEntry=Entry(frame3,bg='black',fg='white')                #entry type which achieve the inputing and outputing of number
numEntry.pack(side=LEFT,padx=1,pady=2,ipadx=40)

DButton=Button(frame3,text='Delete',fg='white',bg='red')    #delect button
DButton.bind("<Button-1>",delete)
DButton.pack(side=LEFT,padx=1,pady=2,ipadx=13)

cButton=Button(frame3,text='Clear',fg='white',bg='orange')  #clean button
cButton.bind("<Button-1>",clean)
cButton.pack(side=LEFT,padx=1,pady=2,ipadx=13)

frame4=Frame(root,bg="black",width=350)                     #in this frame, all the elements using grid to construct.
frame4.grid(row=5,column=0,sticky=W,padx=0,pady=0,ipadx=4)

sevenButton=Button(frame4,text='7',bg='#3c3c3c',fg='white',width=3)         #here are numbers button for 0 to 9
sevenButton.bind("<Button-1>",seven)
sevenButton.grid(row=0,column=0,sticky=W+E+N+S,padx=1,pady=2,ipadx=12)
eightButton=Button(frame4,text='8',bg='#3c3c3c',fg='white',width=3)
eightButton.bind("<Button-1>",eight)
eightButton.grid(row=0,column=1,sticky=W+E+N+S,padx=1,pady=2,ipadx=12)
nineButton=Button(frame4,text='9',bg='#3c3c3c',fg='white',width=3)
nineButton.bind("<Button-1>",nine)
nineButton.grid(row=0,column=2,sticky=W+E+N+S,padx=1,pady=2,ipadx=12)
fourButton=Button(frame4,text='4',bg='#3c3c3c',fg='white',width=3)
fourButton.bind("<Button-1>",four)
fourButton.grid(row=1,column=0,sticky=W+E+N+S,padx=1,pady=2,ipadx=12)
fiveButton=Button(frame4,text='5',bg='#3c3c3c',fg='white',width=3)
fiveButton.bind("<Button-1>",five)
fiveButton.grid(row=1,column=1,sticky=W+E+N+S,padx=1,pady=2,ipadx=12)
sixButton=Button(frame4,text='6',bg='#3c3c3c',fg='white',width=3)
sixButton.bind("<Button-1>",six)
sixButton.grid(row=1,column=2,sticky=W+E+N+S,padx=1,pady=2,ipadx=12)
oneButton=Button(frame4,text='1',bg='#3c3c3c',fg='white',width=3)
oneButton.bind("<Button-1>",one)
oneButton.grid(row=2,column=0,sticky=W+E+N+S,padx=1,pady=2,ipadx=12)
twoButton=Button(frame4,text='2',bg='#3c3c3c',fg='white',width=3)
twoButton.bind("<Button-1>",two)
twoButton.grid(row=2,column=1,sticky=W+E+N+S,padx=1,pady=2,ipadx=12)
threeButton=Button(frame4,text='3',bg='#3c3c3c',fg='white',width=3)
threeButton.bind("<Button-1>",three)
threeButton.grid(row=2,column=2,sticky=W+E+N+S,padx=1,pady=2,ipadx=12)
addButton=Button(frame4,text='+',bg='orange',fg='black',width=3)            #'+'button
addButton.bind("<Button-1>",add)
addButton.grid(row=2,column=3,sticky=W+E+N+S,padx=1,pady=2,ipadx=12)
mulButton=Button(frame4,text='*',bg='orange',fg='black',width=3)            #'*'button
mulButton.bind("<Button-1>",mul)
mulButton.grid(row=2,column=4,sticky=W+E+N+S,padx=1,pady=2,ipadx=12)
name1=Label(frame4,text='Designer:',bg='black',fg='white',anchor='center',justify='center',width=3)
name1.grid(row=2,column=5,sticky=W+E+N+S,padx=1,pady=2,ipadx=4)
zeroButton=Button(frame4,text='0',bg='#3c3c3c',fg='white',width=3)
zeroButton.bind("<Button-1>",zero)
zeroButton.grid(row=3,column=0,sticky=W+E+N+S,padx=1,pady=2,ipadx=12)
pointButton=Button(frame4,text='.',bg='#3c3c3c',fg='white',width=3)         #here is '.' button
pointButton.bind("<Button-1>",point)
pointButton.grid(row=3,column=1,sticky=W+E+N+S,padx=1,pady=2,ipadx=12)
equButton=Button(frame4,text='=',width=3)                                   # here is "euqal" button
equButton.bind("<Button-1>",equal)
equButton.grid(row=3,column=2,sticky=W+E+N+S,padx=1,pady=2,ipadx=12)
subButton=Button(frame4,text='-',bg='orange',fg='black')                    #'-'button
subButton.bind("<Button-1>",subtract)
subButton.grid(row=3,column=3,sticky=W+E+N+S,padx=1,pady=2,ipadx=12)
divButton=Button(frame4,text='/',bg='orange',fg='black')                    #'/'button
divButton.bind("<Button-1>",div)
divButton.grid(row=3,column=4,sticky=W+E+N+S,padx=1,pady=2,ipadx=12)
name2=Label(frame4,text='HAO',bg='black',fg='white',anchor='center',justify='center',width=3)
name2.grid(row=3,column=5,sticky=W+E+N+S,padx=1,pady=2,ipadx=4)

powButton=Button(frame4,text='√ sqr',bg='#7b7b7b',fg='white',width=3)       #'√'button
powButton.bind("<Button-1>",square_root)
powButton.grid(row=0,column=3,sticky=W+E+N+S,padx=1,pady=2,ipadx=12)

powButton=Button(frame4,text='^ pow',bg='#7b7b7b',fg='white',width=3)       #'^'button
powButton.bind("<Button-1>",raise_to_power)
powButton.grid(row=0,column=4,sticky=W+E+N+S,padx=1,pady=2,ipadx=12)

logButton=Button(frame4,text='log10',bg='#7b7b7b',fg='white',width=3)       #'log'button
logButton.bind("<Button-1>",log_ten)
logButton.grid(row=0,column=5,sticky=W+E+N+S,padx=1,pady=2,ipadx=12)

sinButton=Button(frame4,text='sin',bg='#7b7b7b',fg='white',width=3)         #'sin'button
sinButton.bind("<Button-1>",sins)
sinButton.grid(row=1,column=3,sticky=W+E+N+S,padx=1,pady=2,ipadx=12)

cosButton=Button(frame4,text='cos',bg='#7b7b7b',fg='white',width=3)         #'cos'button
cosButton.bind("<Button-1>",coss)
cosButton.grid(row=1,column=4,sticky=W+E+N+S,padx=1,pady=2,ipadx=12)

tanButton=Button(frame4,text='tan',bg='#7b7b7b',fg='white',width=3)         #'tan'button
tanButton.bind("<Button-1>",tans)
tanButton.grid(row=1,column=5,sticky=W+E+N+S,padx=1,pady=2,ipadx=12)

frame4=Frame(root,bg="black",width=350,height=10)                           #in this frame, all the elements using grid to construct.
frame4.grid(row=6,column=0,sticky=W,padx=0,pady=0,ipadx=0)

root.mainloop()
    
