from tkinter import *
import tkinter.font as font
open('color.txt','w+').write('red')
open('press.txt','w+').write('0')
root = Tk()
root.title('Chain Reaction By-Prakhar')
root.iconbitmap(None)
root.resizable(width = False, height = False)
root.geometry("400x500")
root.configure(bg = 'black')
def buttonOn0():
    m=open('press.txt','r').read()
    open('press.txt','w+').write(str(int(m)+1))
    for i in range(15):
        lst[i]['state'] = NORMAL
    q=open('color.txt','r').read()
    if q=='red':
        open('color.txt','w+').write('blue')
    elif q=='blue':
        open('color.txt','w+').write('red')
    a,c=[],[]
    for i in range(15):c.append(lst[i]['text'])
    lst[0].configure(text=str(int(lst[0]['text'])+1),bg=q)
    for i in range(15):a.append(lst[i]['text'])
    b=['2','3','2','3','4','3','3','4','3','3','4','3','2','3','2']
    for j in range(10):
        for i in range(15):
            if int(a[i])>=int(b[i]):
                if i==0:
                    a[i+1]=str(int(a[i+1])+1)
                    a[i+3]=str(int(a[i+3])+1)
                    a[i]='0'

                if i==2:
                    a[i-1]=str(int(a[i-1])+1)
                    a[i+3]=str(int(a[i+3])+1)
                    a[i]='0'

                if i==3 or i==6 or i==9:
                    a[i-3]=str(int(a[i-3])+1)
                    a[i+3]=str(int(a[i+3])+1)
                    a[i+1]=str(int(a[i+1])+1)
                    a[i]='0'

                if i==5 or i==8 or i==11:
                    a[i-3]=str(int(a[i-3])+1)
                    a[i+3]=str(int(a[i+3])+1)
                    a[i-1]=str(int(a[i-1])+1)
                    a[i]='0'

                if i==4 or i==7 or i==10:
                    a[i-3]=str(int(a[i-3])+1)
                    a[i+3]=str(int(a[i+3])+1)
                    a[i-1]=str(int(a[i-1])+1)
                    a[i+1] = str(int(a[i+1])+1)
                    a[i]='0'

                if i==1:
                    a[i+3]=str(int(a[i+3])+1)
                    a[i+1]=str(int(a[i+1])+1)
                    a[i-1]=str(int(a[i-1])+1)
                    a[i]='0'

                if i==12:
                    a[i+1]=str(int(a[i+1])+1)
                    a[i-3]=str(int(a[i-3])+1)
                    a[i]='0'

                if i==13:
                    a[i-3]=str(int(a[i-3])+1)
                    a[i+1]=str(int(a[i+1])+1)
                    a[i-1]=str(int(a[i-1])+1)
                    a[i]='0'

                if i==14:
                    a[i-3]=str(int(a[i-3])+1)
                    a[i-1]=str(int(a[i-1])+1)
                    a[i]='0'
    for i in range(15):
        lst[i]['text'] = a[i]
    d=[]
    for i in range(15):
        if a[i]!=c[i] and a[i]!='0':d.append(i)
    for i in range(len(d)):
        lst[d[i]]['bg']=q
    for i in range(15):
        if lst[i]['text']=='0':lst[i]['bg']='black'
    c=[]
    for i in range(15):c.append(lst[i]['bg'])
    for i in range(15):
        if q=='red':
            if c[i]=='red':
                lst[i]['state']=DISABLED
        if q=='blue':
            if c[i]=='blue':
                lst[i]['state']=DISABLED
    m=open('press.txt','r').read()
    if int(m)>2:
        if 'red'not in c:
            for i in range(15):lst[i]['state']=DISABLED
            label['text'] = 'P2'+label['text']
        if 'blue'not in c:
            for i in range(15):lst[i]['state']=DISABLED
            label['text'] = 'P1'+label['text']
    a=[]
    for i in range(15):a.append(lst[i]['text'])
    
    for i in range(15):
        if a[i]>b[i]:
            lst[i]['text']=b[i]
            for i in range(15):lst[i]['state']=DISABLED
            label['text'] = 'Draw'
                

def buttonOn1():
    m=open('press.txt','r').read()
    open('press.txt','w+').write(str(int(m)+1))
    for i in range(15):
        lst[i]['state'] = NORMAL
    q=open('color.txt','r').read()
    if q=='red':
        open('color.txt','w+').write('blue')
    elif q=='blue':
        open('color.txt','w+').write('red')
    a,c=[],[]
    for i in range(15):c.append(lst[i]['text'])
    lst[1].configure(text=str(int(lst[1]['text'])+1),bg=q)
    for i in range(15):a.append(lst[i]['text'])
    b=['2','3','2','3','4','3','3','4','3','3','4','3','2','3','2']
    for j in range(10):
        for i in range(15):
            if int(a[i])>=int(b[i]):
                if i==0:
                    a[i+1]=str(int(a[i+1])+1)
                    a[i+3]=str(int(a[i+3])+1)
                    a[i]='0'

                if i==2:
                    a[i-1]=str(int(a[i-1])+1)
                    a[i+3]=str(int(a[i+3])+1)
                    a[i]='0'

                if i==3 or i==6 or i==9:
                    a[i-3]=str(int(a[i-3])+1)
                    a[i+3]=str(int(a[i+3])+1)
                    a[i+1]=str(int(a[i+1])+1)
                    a[i]='0'

                if i==5 or i==8 or i==11:
                    a[i-3]=str(int(a[i-3])+1)
                    a[i+3]=str(int(a[i+3])+1)
                    a[i-1]=str(int(a[i-1])+1)
                    a[i]='0'

                if i==4 or i==7 or i==10:
                    a[i-3]=str(int(a[i-3])+1)
                    a[i+3]=str(int(a[i+3])+1)
                    a[i-1]=str(int(a[i-1])+1)
                    a[i+1] = str(int(a[i+1])+1)
                    a[i]='0'

                if i==1:
                    a[i+3]=str(int(a[i+3])+1)
                    a[i+1]=str(int(a[i+1])+1)
                    a[i-1]=str(int(a[i-1])+1)
                    a[i]='0'

                if i==12:
                    a[i+1]=str(int(a[i+1])+1)
                    a[i-3]=str(int(a[i-3])+1)
                    a[i]='0'

                if i==13:
                    a[i-3]=str(int(a[i-3])+1)
                    a[i+1]=str(int(a[i+1])+1)
                    a[i-1]=str(int(a[i-1])+1)
                    a[i]='0'

                if i==14:
                    a[i-3]=str(int(a[i-3])+1)
                    a[i-1]=str(int(a[i-1])+1)
                    a[i]='0'
    for i in range(15):
        lst[i]['text'] = a[i]
    d=[]
    for i in range(15):
        if a[i]!=c[i] and a[i]!='0':d.append(i)
    for i in range(len(d)):
        lst[d[i]]['bg']=q
    for i in range(15):
        if lst[i]['text']=='0':lst[i]['bg']='black'
    c=[]
    for i in range(15):c.append(lst[i]['bg'])
    for i in range(15):
        if q=='red':
            if c[i]=='red':
                lst[i]['state']=DISABLED
        if q=='blue':
            if c[i]=='blue':
                lst[i]['state']=DISABLED
    m=open('press.txt','r').read()
    if int(m)>2:
        if 'red'not in c:
            for i in range(15):lst[i]['state']=DISABLED
            label['text'] = 'P2'+label['text']
        if 'blue'not in c:
            for i in range(15):lst[i]['state']=DISABLED
            label['text'] = 'P1'+label['text']
    a=[]
    for i in range(15):a.append(lst[i]['text'])
    
    for i in range(15):
        if a[i]>b[i]:
            lst[i]['text']=b[i]
            for i in range(15):lst[i]['state']=DISABLED
            label['text'] = 'Draw'
        
def buttonOn2():
    m=open('press.txt','r').read()
    open('press.txt','w+').write(str(int(m)+1))
    for i in range(15):
        lst[i]['state'] = NORMAL
    q=open('color.txt','r').read()
    if q=='red':
        open('color.txt','w+').write('blue')
    elif q=='blue':
        open('color.txt','w+').write('red')
    a,c=[],[]
    for i in range(15):c.append(lst[i]['text'])
    lst[2].configure(text=str(int(lst[2]['text'])+1),bg=q)
    for i in range(15):a.append(lst[i]['text'])
    b=['2','3','2','3','4','3','3','4','3','3','4','3','2','3','2']
    for j in range(10):
        for i in range(15):
            if int(a[i])>=int(b[i]):
                if i==0:
                    a[i+1]=str(int(a[i+1])+1)
                    a[i+3]=str(int(a[i+3])+1)
                    a[i]='0'

                if i==2:
                    a[i-1]=str(int(a[i-1])+1)
                    a[i+3]=str(int(a[i+3])+1)
                    a[i]='0'

                if i==3 or i==6 or i==9:
                    a[i-3]=str(int(a[i-3])+1)
                    a[i+3]=str(int(a[i+3])+1)
                    a[i+1]=str(int(a[i+1])+1)
                    a[i]='0'

                if i==5 or i==8 or i==11:
                    a[i-3]=str(int(a[i-3])+1)
                    a[i+3]=str(int(a[i+3])+1)
                    a[i-1]=str(int(a[i-1])+1)
                    a[i]='0'

                if i==4 or i==7 or i==10:
                    a[i-3]=str(int(a[i-3])+1)
                    a[i+3]=str(int(a[i+3])+1)
                    a[i-1]=str(int(a[i-1])+1)
                    a[i+1] = str(int(a[i+1])+1)
                    a[i]='0'

                if i==1:
                    a[i+3]=str(int(a[i+3])+1)
                    a[i+1]=str(int(a[i+1])+1)
                    a[i-1]=str(int(a[i-1])+1)
                    a[i]='0'

                if i==12:
                    a[i+1]=str(int(a[i+1])+1)
                    a[i-3]=str(int(a[i-3])+1)
                    a[i]='0'

                if i==13:
                    a[i-3]=str(int(a[i-3])+1)
                    a[i+1]=str(int(a[i+1])+1)
                    a[i-1]=str(int(a[i-1])+1)
                    a[i]='0'

                if i==14:
                    a[i-3]=str(int(a[i-3])+1)
                    a[i-1]=str(int(a[i-1])+1)
                    a[i]='0'
    for i in range(15):
        lst[i]['text'] = a[i]
    d=[]
    for i in range(15):
        if a[i]!=c[i] and a[i]!='0':d.append(i)
    for i in range(len(d)):
        lst[d[i]]['bg']=q
    for i in range(15):
        if lst[i]['text']=='0':lst[i]['bg']='black'
    c=[]
    for i in range(15):c.append(lst[i]['bg'])
    for i in range(15):
        if q=='red':
            if c[i]=='red':
                lst[i]['state']=DISABLED
        if q=='blue':
            if c[i]=='blue':
                lst[i]['state']=DISABLED
    m=open('press.txt','r').read()
    if int(m)>2:
        if 'red'not in c:
            for i in range(15):lst[i]['state']=DISABLED
            label['text'] = 'P2'+label['text']
        if 'blue'not in c:
            for i in range(15):lst[i]['state']=DISABLED
            label['text'] = 'P1'+label['text']
    a=[]
    for i in range(15):a.append(lst[i]['text'])
    
    for i in range(15):
        if a[i]>b[i]:
            lst[i]['text']=b[i]
            for i in range(15):lst[i]['state']=DISABLED
            label['text'] = 'Draw'
        
def buttonOn3():
    m=open('press.txt','r').read()
    open('press.txt','w+').write(str(int(m)+1))
    for i in range(15):
        lst[i]['state'] = NORMAL
    q=open('color.txt','r').read()
    if q=='red':
        open('color.txt','w+').write('blue')
    elif q=='blue':
        open('color.txt','w+').write('red')
    a,c=[],[]
    for i in range(15):c.append(lst[i]['text'])
    lst[3].configure(text=str(int(lst[3]['text'])+1),bg=q)
    for i in range(15):a.append(lst[i]['text'])
    b=['2','3','2','3','4','3','3','4','3','3','4','3','2','3','2']
    for j in range(10):
        for i in range(15):
            if int(a[i])>=int(b[i]):
                if i==0:
                    a[i+1]=str(int(a[i+1])+1)
                    a[i+3]=str(int(a[i+3])+1)
                    a[i]='0'

                if i==2:
                    a[i-1]=str(int(a[i-1])+1)
                    a[i+3]=str(int(a[i+3])+1)
                    a[i]='0'

                if i==3 or i==6 or i==9:
                    a[i-3]=str(int(a[i-3])+1)
                    a[i+3]=str(int(a[i+3])+1)
                    a[i+1]=str(int(a[i+1])+1)
                    a[i]='0'

                if i==5 or i==8 or i==11:
                    a[i-3]=str(int(a[i-3])+1)
                    a[i+3]=str(int(a[i+3])+1)
                    a[i-1]=str(int(a[i-1])+1)
                    a[i]='0'

                if i==4 or i==7 or i==10:
                    a[i-3]=str(int(a[i-3])+1)
                    a[i+3]=str(int(a[i+3])+1)
                    a[i-1]=str(int(a[i-1])+1)
                    a[i+1] = str(int(a[i+1])+1)
                    a[i]='0'

                if i==1:
                    a[i+3]=str(int(a[i+3])+1)
                    a[i+1]=str(int(a[i+1])+1)
                    a[i-1]=str(int(a[i-1])+1)
                    a[i]='0'

                if i==12:
                    a[i+1]=str(int(a[i+1])+1)
                    a[i-3]=str(int(a[i-3])+1)
                    a[i]='0'

                if i==13:
                    a[i-3]=str(int(a[i-3])+1)
                    a[i+1]=str(int(a[i+1])+1)
                    a[i-1]=str(int(a[i-1])+1)
                    a[i]='0'

                if i==14:
                    a[i-3]=str(int(a[i-3])+1)
                    a[i-1]=str(int(a[i-1])+1)
                    a[i]='0'
    for i in range(15):
        lst[i]['text'] = a[i]
    d=[]
    for i in range(15):
        if a[i]!=c[i] and a[i]!='0':d.append(i)
    for i in range(len(d)):
        lst[d[i]]['bg']=q
    for i in range(15):
        if lst[i]['text']=='0':lst[i]['bg']='black'
    c=[]
    for i in range(15):c.append(lst[i]['bg'])
    for i in range(15):
        if q=='red':
            if c[i]=='red':
                lst[i]['state']=DISABLED
        if q=='blue':
            if c[i]=='blue':
                lst[i]['state']=DISABLED
    m=open('press.txt','r').read()
    if int(m)>2:
        if 'red'not in c:
            for i in range(15):lst[i]['state']=DISABLED
            label['text'] = 'P2'+label['text']
        if 'blue'not in c:
            for i in range(15):lst[i]['state']=DISABLED
            label['text'] = 'P1'+label['text']
    a=[]
    for i in range(15):a.append(lst[i]['text'])
    
    for i in range(15):
        if a[i]>b[i]:
            lst[i]['text']=b[i]
            for i in range(15):lst[i]['state']=DISABLED
            label['text'] = 'Draw'
        
def buttonOn4():
    m=open('press.txt','r').read()
    open('press.txt','w+').write(str(int(m)+1))
    for i in range(15):
        lst[i]['state'] = NORMAL
    q=open('color.txt','r').read()
    if q=='red':
        open('color.txt','w+').write('blue')
    elif q=='blue':
        open('color.txt','w+').write('red')
    a,c=[],[]
    for i in range(15):c.append(lst[i]['text'])
    lst[4].configure(text=str(int(lst[4]['text'])+1),bg=q)
    for i in range(15):a.append(lst[i]['text'])
    b=['2','3','2','3','4','3','3','4','3','3','4','3','2','3','2']
    for j in range(10):
        for i in range(15):
            if int(a[i])>=int(b[i]):
                if i==0:
                    a[i+1]=str(int(a[i+1])+1)
                    a[i+3]=str(int(a[i+3])+1)
                    a[i]='0'

                if i==2:
                    a[i-1]=str(int(a[i-1])+1)
                    a[i+3]=str(int(a[i+3])+1)
                    a[i]='0'

                if i==3 or i==6 or i==9:
                    a[i-3]=str(int(a[i-3])+1)
                    a[i+3]=str(int(a[i+3])+1)
                    a[i+1]=str(int(a[i+1])+1)
                    a[i]='0'

                if i==5 or i==8 or i==11:
                    a[i-3]=str(int(a[i-3])+1)
                    a[i+3]=str(int(a[i+3])+1)
                    a[i-1]=str(int(a[i-1])+1)
                    a[i]='0'

                if i==4 or i==7 or i==10:
                    a[i-3]=str(int(a[i-3])+1)
                    a[i+3]=str(int(a[i+3])+1)
                    a[i-1]=str(int(a[i-1])+1)
                    a[i+1] = str(int(a[i+1])+1)
                    a[i]='0'

                if i==1:
                    a[i+3]=str(int(a[i+3])+1)
                    a[i+1]=str(int(a[i+1])+1)
                    a[i-1]=str(int(a[i-1])+1)
                    a[i]='0'

                if i==12:
                    a[i+1]=str(int(a[i+1])+1)
                    a[i-3]=str(int(a[i-3])+1)
                    a[i]='0'

                if i==13:
                    a[i-3]=str(int(a[i-3])+1)
                    a[i+1]=str(int(a[i+1])+1)
                    a[i-1]=str(int(a[i-1])+1)
                    a[i]='0'

                if i==14:
                    a[i-3]=str(int(a[i-3])+1)
                    a[i-1]=str(int(a[i-1])+1)
                    a[i]='0'
    for i in range(15):
        lst[i]['text'] = a[i]
    d=[]
    for i in range(15):
        if a[i]!=c[i] and a[i]!='0':d.append(i)
    for i in range(len(d)):
        lst[d[i]]['bg']=q
    for i in range(15):
        if lst[i]['text']=='0':lst[i]['bg']='black'
    c=[]
    for i in range(15):c.append(lst[i]['bg'])
    for i in range(15):
        if q=='red':
            if c[i]=='red':
                lst[i]['state']=DISABLED
        if q=='blue':
            if c[i]=='blue':
                lst[i]['state']=DISABLED
    m=open('press.txt','r').read()
    if int(m)>2:
        if 'red'not in c:
            for i in range(15):lst[i]['state']=DISABLED
            label['text'] = 'P2'+label['text']
        if 'blue'not in c:
            for i in range(15):lst[i]['state']=DISABLED
            label['text'] = 'P1'+label['text']
    a=[]
    for i in range(15):a.append(lst[i]['text'])
    
    for i in range(15):
        if a[i]>b[i]:
            lst[i]['text']=b[i]
            for i in range(15):lst[i]['state']=DISABLED
            label['text'] = 'Draw'
        
def buttonOn5():
    m=open('press.txt','r').read()
    open('press.txt','w+').write(str(int(m)+1))
    for i in range(15):
        lst[i]['state'] = NORMAL
    q=open('color.txt','r').read()
    if q=='red':
        open('color.txt','w+').write('blue')
    elif q=='blue':
        open('color.txt','w+').write('red')
    a,c=[],[]
    for i in range(15):c.append(lst[i]['text'])
    lst[5].configure(text=str(int(lst[5]['text'])+1),bg=q)
    for i in range(15):a.append(lst[i]['text'])
    b=['2','3','2','3','4','3','3','4','3','3','4','3','2','3','2']
    for j in range(10):
        for i in range(15):
            if int(a[i])>=int(b[i]):
                if i==0:
                    a[i+1]=str(int(a[i+1])+1)
                    a[i+3]=str(int(a[i+3])+1)
                    a[i]='0'

                if i==2:
                    a[i-1]=str(int(a[i-1])+1)
                    a[i+3]=str(int(a[i+3])+1)
                    a[i]='0'

                if i==3 or i==6 or i==9:
                    a[i-3]=str(int(a[i-3])+1)
                    a[i+3]=str(int(a[i+3])+1)
                    a[i+1]=str(int(a[i+1])+1)
                    a[i]='0'

                if i==5 or i==8 or i==11:
                    a[i-3]=str(int(a[i-3])+1)
                    a[i+3]=str(int(a[i+3])+1)
                    a[i-1]=str(int(a[i-1])+1)
                    a[i]='0'

                if i==4 or i==7 or i==10:
                    a[i-3]=str(int(a[i-3])+1)
                    a[i+3]=str(int(a[i+3])+1)
                    a[i-1]=str(int(a[i-1])+1)
                    a[i+1] = str(int(a[i+1])+1)
                    a[i]='0'

                if i==1:
                    a[i+3]=str(int(a[i+3])+1)
                    a[i+1]=str(int(a[i+1])+1)
                    a[i-1]=str(int(a[i-1])+1)
                    a[i]='0'

                if i==12:
                    a[i+1]=str(int(a[i+1])+1)
                    a[i-3]=str(int(a[i-3])+1)
                    a[i]='0'

                if i==13:
                    a[i-3]=str(int(a[i-3])+1)
                    a[i+1]=str(int(a[i+1])+1)
                    a[i-1]=str(int(a[i-1])+1)
                    a[i]='0'

                if i==14:
                    a[i-3]=str(int(a[i-3])+1)
                    a[i-1]=str(int(a[i-1])+1)
                    a[i]='0'
    for i in range(15):
        lst[i]['text'] = a[i]
    d=[]
    for i in range(15):
        if a[i]!=c[i] and a[i]!='0':d.append(i)
    for i in range(len(d)):
        lst[d[i]]['bg']=q
    for i in range(15):
        if lst[i]['text']=='0':lst[i]['bg']='black'
    c=[]
    for i in range(15):c.append(lst[i]['bg'])
    for i in range(15):
        if q=='red':
            if c[i]=='red':
                lst[i]['state']=DISABLED
        if q=='blue':
            if c[i]=='blue':
                lst[i]['state']=DISABLED
    m=open('press.txt','r').read()
    if int(m)>2:
        if 'red'not in c:
            for i in range(15):lst[i]['state']=DISABLED
            label['text'] = 'P2'+label['text']
        if 'blue'not in c:
            for i in range(15):lst[i]['state']=DISABLED
            label['text'] = 'P1'+label['text']
    a=[]
    for i in range(15):a.append(lst[i]['text'])
    
    for i in range(15):
        if a[i]>b[i]:
            lst[i]['text']=b[i]
            for i in range(15):lst[i]['state']=DISABLED
            label['text'] = 'Draw'
        
def buttonOn6():
    m=open('press.txt','r').read()
    open('press.txt','w+').write(str(int(m)+1))
    for i in range(15):
        lst[i]['state'] = NORMAL
    q=open('color.txt','r').read()
    if q=='red':
        open('color.txt','w+').write('blue')
    elif q=='blue':
        open('color.txt','w+').write('red')
    a,c=[],[]
    for i in range(15):c.append(lst[i]['text'])
    lst[6].configure(text=str(int(lst[6]['text'])+1),bg=q)
    for i in range(15):a.append(lst[i]['text'])
    b=['2','3','2','3','4','3','3','4','3','3','4','3','2','3','2']
    for j in range(10):
        for i in range(15):
            if int(a[i])>=int(b[i]):
                if i==0:
                    a[i+1]=str(int(a[i+1])+1)
                    a[i+3]=str(int(a[i+3])+1)
                    a[i]='0'

                if i==2:
                    a[i-1]=str(int(a[i-1])+1)
                    a[i+3]=str(int(a[i+3])+1)
                    a[i]='0'

                if i==3 or i==6 or i==9:
                    a[i-3]=str(int(a[i-3])+1)
                    a[i+3]=str(int(a[i+3])+1)
                    a[i+1]=str(int(a[i+1])+1)
                    a[i]='0'

                if i==5 or i==8 or i==11:
                    a[i-3]=str(int(a[i-3])+1)
                    a[i+3]=str(int(a[i+3])+1)
                    a[i-1]=str(int(a[i-1])+1)
                    a[i]='0'

                if i==4 or i==7 or i==10:
                    a[i-3]=str(int(a[i-3])+1)
                    a[i+3]=str(int(a[i+3])+1)
                    a[i-1]=str(int(a[i-1])+1)
                    a[i+1] = str(int(a[i+1])+1)
                    a[i]='0'

                if i==1:
                    a[i+3]=str(int(a[i+3])+1)
                    a[i+1]=str(int(a[i+1])+1)
                    a[i-1]=str(int(a[i-1])+1)
                    a[i]='0'

                if i==12:
                    a[i+1]=str(int(a[i+1])+1)
                    a[i-3]=str(int(a[i-3])+1)
                    a[i]='0'

                if i==13:
                    a[i-3]=str(int(a[i-3])+1)
                    a[i+1]=str(int(a[i+1])+1)
                    a[i-1]=str(int(a[i-1])+1)
                    a[i]='0'

                if i==14:
                    a[i-3]=str(int(a[i-3])+1)
                    a[i-1]=str(int(a[i-1])+1)
                    a[i]='0'
    for i in range(15):
        lst[i]['text'] = a[i]
    d=[]
    for i in range(15):
        if a[i]!=c[i] and a[i]!='0':d.append(i)
    for i in range(len(d)):
        lst[d[i]]['bg']=q
    for i in range(15):
        if lst[i]['text']=='0':lst[i]['bg']='black'
    c=[]
    for i in range(15):c.append(lst[i]['bg'])
    for i in range(15):
        if q=='red':
            if c[i]=='red':
                lst[i]['state']=DISABLED
        if q=='blue':
            if c[i]=='blue':
                lst[i]['state']=DISABLED
    m=open('press.txt','r').read()
    if int(m)>2:
        if 'red'not in c:
            for i in range(15):lst[i]['state']=DISABLED
            label['text'] = 'P2'+label['text']
        if 'blue'not in c:
            for i in range(15):lst[i]['state']=DISABLED
            label['text'] = 'P1'+label['text']
    a=[]
    for i in range(15):a.append(lst[i]['text'])
    
    for i in range(15):
        if a[i]>b[i]:
            lst[i]['text']=b[i]
            for i in range(15):lst[i]['state']=DISABLED
            label['text'] = 'Draw'
        
def buttonOn7():
    m=open('press.txt','r').read()
    open('press.txt','w+').write(str(int(m)+1))
    for i in range(15):
        lst[i]['state'] = NORMAL
    q=open('color.txt','r').read()
    if q=='red':
        open('color.txt','w+').write('blue')
    elif q=='blue':
        open('color.txt','w+').write('red')
    a,c=[],[]
    for i in range(15):c.append(lst[i]['text'])
    lst[7].configure(text=str(int(lst[7]['text'])+1),bg=q)
    for i in range(15):a.append(lst[i]['text'])
    b=['2','3','2','3','4','3','3','4','3','3','4','3','2','3','2']
    for j in range(10):
        for i in range(15):
            if int(a[i])>=int(b[i]):
                if i==0:
                    a[i+1]=str(int(a[i+1])+1)
                    a[i+3]=str(int(a[i+3])+1)
                    a[i]='0'

                if i==2:
                    a[i-1]=str(int(a[i-1])+1)
                    a[i+3]=str(int(a[i+3])+1)
                    a[i]='0'

                if i==3 or i==6 or i==9:
                    a[i-3]=str(int(a[i-3])+1)
                    a[i+3]=str(int(a[i+3])+1)
                    a[i+1]=str(int(a[i+1])+1)
                    a[i]='0'
                if i==5 or i==8 or i==11:
                    a[i-3]=str(int(a[i-3])+1)
                    a[i+3]=str(int(a[i+3])+1)
                    a[i-1]=str(int(a[i-1])+1)
                    a[i]='0'

                if i==4 or i==7 or i==10:
                    a[i-3]=str(int(a[i-3])+1)
                    a[i+3]=str(int(a[i+3])+1)
                    a[i-1]=str(int(a[i-1])+1)
                    a[i+1] = str(int(a[i+1])+1)
                    a[i]='0'

                if i==1:
                    a[i+3]=str(int(a[i+3])+1)
                    a[i+1]=str(int(a[i+1])+1)
                    a[i-1]=str(int(a[i-1])+1)
                    a[i]='0'

                if i==12:
                    a[i+1]=str(int(a[i+1])+1)
                    a[i-3]=str(int(a[i-3])+1)
                    a[i]='0'

                if i==13:
                    a[i-3]=str(int(a[i-3])+1)
                    a[i+1]=str(int(a[i+1])+1)
                    a[i-1]=str(int(a[i-1])+1)
                    a[i]='0'

                if i==14:
                    a[i-3]=str(int(a[i-3])+1)
                    a[i-1]=str(int(a[i-1])+1)
                    a[i]='0'
    for i in range(15):
        lst[i]['text'] = a[i]
    d=[]
    for i in range(15):
        if a[i]!=c[i] and a[i]!='0':d.append(i)
    for i in range(len(d)):
        lst[d[i]]['bg']=q
    for i in range(15):
        if lst[i]['text']=='0':lst[i]['bg']='black'
    c=[]
    for i in range(15):c.append(lst[i]['bg'])
    for i in range(15):
        if q=='red':
            if c[i]=='red':
                lst[i]['state']=DISABLED
        if q=='blue':
            if c[i]=='blue':
                lst[i]['state']=DISABLED
    m=open('press.txt','r').read()
    if int(m)>2:
        if 'red'not in c:
            for i in range(15):lst[i]['state']=DISABLED
            label['text'] = 'P2'+label['text']
        if 'blue'not in c:
            for i in range(15):lst[i]['state']=DISABLED
            label['text'] = 'P1'+label['text']
    a=[]
    for i in range(15):a.append(lst[i]['text'])
    
    for i in range(15):
        if a[i]>b[i]:
            lst[i]['text']=b[i]
            for i in range(15):lst[i]['state']=DISABLED
            label['text'] = 'Draw'
        
def buttonOn8():
    m=open('press.txt','r').read()
    open('press.txt','w+').write(str(int(m)+1))
    for i in range(15):
        lst[i]['state'] = NORMAL
    q=open('color.txt','r').read()
    if q=='red':
        open('color.txt','w+').write('blue')
    elif q=='blue':
        open('color.txt','w+').write('red')
    a,c=[],[]
    for i in range(15):c.append(lst[i]['text'])
    lst[8].configure(text=str(int(lst[8]['text'])+1),bg=q)
    for i in range(15):a.append(lst[i]['text'])
    b=['2','3','2','3','4','3','3','4','3','3','4','3','2','3','2']
    for j in range(10):
        for i in range(15):
            if int(a[i])>=int(b[i]):
                if i==0:
                    a[i+1]=str(int(a[i+1])+1)
                    a[i+3]=str(int(a[i+3])+1)
                    a[i]='0'

                if i==2:
                    a[i-1]=str(int(a[i-1])+1)
                    a[i+3]=str(int(a[i+3])+1)
                    a[i]='0'

                if i==3 or i==6 or i==9:
                    a[i-3]=str(int(a[i-3])+1)
                    a[i+3]=str(int(a[i+3])+1)
                    a[i+1]=str(int(a[i+1])+1)
                    a[i]='0'

                if i==5 or i==8 or i==11:
                    a[i-3]=str(int(a[i-3])+1)
                    a[i+3]=str(int(a[i+3])+1)
                    a[i-1]=str(int(a[i-1])+1)
                    a[i]='0'

                if i==4 or i==7 or i==10:
                    a[i-3]=str(int(a[i-3])+1)
                    a[i+3]=str(int(a[i+3])+1)
                    a[i-1]=str(int(a[i-1])+1)
                    a[i+1] = str(int(a[i+1])+1)
                    a[i]='0'

                if i==1:
                    a[i+3]=str(int(a[i+3])+1)
                    a[i+1]=str(int(a[i+1])+1)
                    a[i-1]=str(int(a[i-1])+1)
                    a[i]='0'

                if i==12:
                    a[i+1]=str(int(a[i+1])+1)
                    a[i-3]=str(int(a[i-3])+1)
                    a[i]='0'

                if i==13:
                    a[i-3]=str(int(a[i-3])+1)
                    a[i+1]=str(int(a[i+1])+1)
                    a[i-1]=str(int(a[i-1])+1)
                    a[i]='0'

                if i==14:
                    a[i-3]=str(int(a[i-3])+1)
                    a[i-1]=str(int(a[i-1])+1)
                    a[i]='0'
    for i in range(15):
        lst[i]['text'] = a[i]
    d=[]
    for i in range(15):
        if a[i]!=c[i] and a[i]!='0':d.append(i)
    for i in range(len(d)):
        lst[d[i]]['bg']=q
    for i in range(15):
        if lst[i]['text']=='0':lst[i]['bg']='black'
    c=[]
    for i in range(15):c.append(lst[i]['bg'])
    for i in range(15):
        if q=='red':
            if c[i]=='red':
                lst[i]['state']=DISABLED
        if q=='blue':
            if c[i]=='blue':
                lst[i]['state']=DISABLED
    m=open('press.txt','r').read()
    if int(m)>2:
        if 'red'not in c:
            for i in range(15):lst[i]['state']=DISABLED
            label['text'] = 'P2'+label['text']
        if 'blue'not in c:
            for i in range(15):lst[i]['state']=DISABLED
            label['text'] = 'P1'+label['text']
    a=[]
    for i in range(15):a.append(lst[i]['text'])
    
    for i in range(15):
        if a[i]>b[i]:
            lst[i]['text']=b[i]
            for i in range(15):lst[i]['state']=DISABLED
            label['text'] = 'Draw'
        
def buttonOn9():
    m=open('press.txt','r').read()
    open('press.txt','w+').write(str(int(m)+1))
    for i in range(15):
        lst[i]['state'] = NORMAL
    q=open('color.txt','r').read()
    if q=='red':
        open('color.txt','w+').write('blue')
    elif q=='blue':
        open('color.txt','w+').write('red')
    a,c=[],[]
    for i in range(15):c.append(lst[i]['text'])
    lst[9].configure(text=str(int(lst[9]['text'])+1),bg=q)
    for i in range(15):a.append(lst[i]['text'])
    b=['2','3','2','3','4','3','3','4','3','3','4','3','2','3','2']
    for j in range(10):
        for i in range(15):
            if int(a[i])>=int(b[i]):
                if i==0:
                    a[i+1]=str(int(a[i+1])+1)
                    a[i+3]=str(int(a[i+3])+1)
                    a[i]='0'

                if i==2:
                    a[i-1]=str(int(a[i-1])+1)
                    a[i+3]=str(int(a[i+3])+1)
                    a[i]='0'

                if i==3 or i==6 or i==9:
                    a[i-3]=str(int(a[i-3])+1)
                    a[i+3]=str(int(a[i+3])+1)
                    a[i+1]=str(int(a[i+1])+1)
                    a[i]='0'

                if i==5 or i==8 or i==11:
                    a[i-3]=str(int(a[i-3])+1)
                    a[i+3]=str(int(a[i+3])+1)
                    a[i-1]=str(int(a[i-1])+1)
                    a[i]='0'

                if i==4 or i==7 or i==10:
                    a[i-3]=str(int(a[i-3])+1)
                    a[i+3]=str(int(a[i+3])+1)
                    a[i-1]=str(int(a[i-1])+1)
                    a[i+1] = str(int(a[i+1])+1)
                    a[i]='0'

                if i==1:
                    a[i+3]=str(int(a[i+3])+1)
                    a[i+1]=str(int(a[i+1])+1)
                    a[i-1]=str(int(a[i-1])+1)
                    a[i]='0'

                if i==12:
                    a[i+1]=str(int(a[i+1])+1)
                    a[i-3]=str(int(a[i-3])+1)
                    a[i]='0'

                if i==13:
                    a[i-3]=str(int(a[i-3])+1)
                    a[i+1]=str(int(a[i+1])+1)
                    a[i-1]=str(int(a[i-1])+1)
                    a[i]='0'

                if i==14:
                    a[i-3]=str(int(a[i-3])+1)
                    a[i-1]=str(int(a[i-1])+1)
                    a[i]='0'
    for i in range(15):
        lst[i]['text'] = a[i]
    d=[]
    for i in range(15):
        if a[i]!=c[i] and a[i]!='0':d.append(i)
    for i in range(len(d)):
        lst[d[i]]['bg']=q
    for i in range(15):
        if lst[i]['text']=='0':lst[i]['bg']='black'
    c=[]
    for i in range(15):c.append(lst[i]['bg'])
    for i in range(15):
        if q=='red':
            if c[i]=='red':
                lst[i]['state']=DISABLED
        if q=='blue':
            if c[i]=='blue':
                lst[i]['state']=DISABLED
    m=open('press.txt','r').read()
    if int(m)>2:
        if 'red'not in c:
            for i in range(15):lst[i]['state']=DISABLED
            label['text'] = 'P2'+label['text']
        if 'blue'not in c:
            for i in range(15):lst[i]['state']=DISABLED
            label['text'] = 'P1'+label['text']
    a=[]
    for i in range(15):a.append(lst[i]['text'])
    
    for i in range(15):
        if a[i]>b[i]:
            lst[i]['text']=b[i]
            for i in range(15):lst[i]['state']=DISABLED
            label['text'] = 'Draw'
        
def buttonOn10():
    m=open('press.txt','r').read()
    open('press.txt','w+').write(str(int(m)+1))
    for i in range(15):
        lst[i]['state'] = NORMAL
    q=open('color.txt','r').read()
    if q=='red':
        open('color.txt','w+').write('blue')
    elif q=='blue':
        open('color.txt','w+').write('red')
    a,c=[],[]
    for i in range(15):c.append(lst[i]['text'])
    lst[10].configure(text=str(int(lst[10]['text'])+1),bg=q)
    for i in range(15):a.append(lst[i]['text'])
    b=['2','3','2','3','4','3','3','4','3','3','4','3','2','3','2']
    for j in range(10):
        for i in range(15):
            if int(a[i])>=int(b[i]):
                if i==0:
                    a[i+1]=str(int(a[i+1])+1)
                    a[i+3]=str(int(a[i+3])+1)
                    a[i]='0'

                if i==2:
                    a[i-1]=str(int(a[i-1])+1)
                    a[i+3]=str(int(a[i+3])+1)
                    a[i]='0'

                if i==3 or i==6 or i==9:
                    a[i-3]=str(int(a[i-3])+1)
                    a[i+3]=str(int(a[i+3])+1)
                    a[i+1]=str(int(a[i+1])+1)
                    a[i]='0'

                if i==5 or i==8 or i==11:
                    a[i-3]=str(int(a[i-3])+1)
                    a[i+3]=str(int(a[i+3])+1)
                    a[i-1]=str(int(a[i-1])+1)
                    a[i]='0'

                if i==4 or i==7 or i==10:
                    a[i-3]=str(int(a[i-3])+1)
                    a[i+3]=str(int(a[i+3])+1)
                    a[i-1]=str(int(a[i-1])+1)
                    a[i+1] = str(int(a[i+1])+1)
                    a[i]='0'

                if i==1:
                    a[i+3]=str(int(a[i+3])+1)
                    a[i+1]=str(int(a[i+1])+1)
                    a[i-1]=str(int(a[i-1])+1)
                    a[i]='0'

                if i==12:
                    a[i+1]=str(int(a[i+1])+1)
                    a[i-3]=str(int(a[i-3])+1)
                    a[i]='0'

                if i==13:
                    a[i-3]=str(int(a[i-3])+1)
                    a[i+1]=str(int(a[i+1])+1)
                    a[i-1]=str(int(a[i-1])+1)
                    a[i]='0'

                if i==14:
                    a[i-3]=str(int(a[i-3])+1)
                    a[i-1]=str(int(a[i-1])+1)
                    a[i]='0'
    for i in range(15):
        lst[i]['text'] = a[i]
    d=[]
    for i in range(15):
        if a[i]!=c[i] and a[i]!='0':d.append(i)
    for i in range(len(d)):
        lst[d[i]]['bg']=q
    for i in range(15):
        if lst[i]['text']=='0':lst[i]['bg']='black'
    c=[]
    for i in range(15):c.append(lst[i]['bg'])
    for i in range(15):
        if q=='red':
            if c[i]=='red':
                lst[i]['state']=DISABLED
        if q=='blue':
            if c[i]=='blue':
                lst[i]['state']=DISABLED
    m=open('press.txt','r').read()
    if int(m)>2:
        if 'red'not in c:
            for i in range(15):lst[i]['state']=DISABLED
            label['text'] = 'P2'+label['text']
        if 'blue'not in c:
            for i in range(15):lst[i]['state']=DISABLED
            label['text'] = 'P1'+label['text']
    a=[]
    for i in range(15):a.append(lst[i]['text'])
    
    for i in range(15):
        if a[i]>b[i]:
            lst[i]['text']=b[i]
            for i in range(15):lst[i]['state']=DISABLED
            label['text'] = 'Draw'
        
def buttonOn11():
    m=open('press.txt','r').read()
    open('press.txt','w+').write(str(int(m)+1))
    for i in range(15):
        lst[i]['state'] = NORMAL
    q=open('color.txt','r').read()
    if q=='red':
        open('color.txt','w+').write('blue')
    elif q=='blue':
        open('color.txt','w+').write('red')
    a,c=[],[]
    for i in range(15):c.append(lst[i]['text'])
    lst[11].configure(text=str(int(lst[11]['text'])+1),bg=q)
    for i in range(15):a.append(lst[i]['text'])
    b=['2','3','2','3','4','3','3','4','3','3','4','3','2','3','2']
    for j in range(10):
        for i in range(15):
            if int(a[i])>=int(b[i]):
                if i==0:
                    a[i+1]=str(int(a[i+1])+1)
                    a[i+3]=str(int(a[i+3])+1)
                    a[i]='0'

                if i==2:
                    a[i-1]=str(int(a[i-1])+1)
                    a[i+3]=str(int(a[i+3])+1)
                    a[i]='0'

                if i==3 or i==6 or i==9:
                    a[i-3]=str(int(a[i-3])+1)
                    a[i+3]=str(int(a[i+3])+1)
                    a[i+1]=str(int(a[i+1])+1)
                    a[i]='0'

                if i==5 or i==8 or i==11:
                    a[i-3]=str(int(a[i-3])+1)
                    a[i+3]=str(int(a[i+3])+1)
                    a[i-1]=str(int(a[i-1])+1)
                    a[i]='0'

                if i==4 or i==7 or i==10:
                    a[i-3]=str(int(a[i-3])+1)
                    a[i+3]=str(int(a[i+3])+1)
                    a[i-1]=str(int(a[i-1])+1)
                    a[i+1] = str(int(a[i+1])+1)
                    a[i]='0'

                if i==1:
                    a[i+3]=str(int(a[i+3])+1)
                    a[i+1]=str(int(a[i+1])+1)
                    a[i-1]=str(int(a[i-1])+1)
                    a[i]='0'

                if i==12:
                    a[i+1]=str(int(a[i+1])+1)
                    a[i-3]=str(int(a[i-3])+1)
                    a[i]='0'

                if i==13:
                    a[i-3]=str(int(a[i-3])+1)
                    a[i+1]=str(int(a[i+1])+1)
                    a[i-1]=str(int(a[i-1])+1)
                    a[i]='0'

                if i==14:
                    a[i-3]=str(int(a[i-3])+1)
                    a[i-1]=str(int(a[i-1])+1)
                    a[i]='0'
    for i in range(15):
        lst[i]['text'] = a[i]
    d=[]
    for i in range(15):
        if a[i]!=c[i] and a[i]!='0':d.append(i)
    for i in range(len(d)):
        lst[d[i]]['bg']=q
    for i in range(15):
        if lst[i]['text']=='0':lst[i]['bg']='black'
    c=[]
    for i in range(15):c.append(lst[i]['bg'])
    for i in range(15):
        if q=='red':
            if c[i]=='red':
                lst[i]['state']=DISABLED
        if q=='blue':
            if c[i]=='blue':
                lst[i]['state']=DISABLED
    m=open('press.txt','r').read()
    if int(m)>2:
        if 'red'not in c:
            for i in range(15):lst[i]['state']=DISABLED
            label['text'] = 'P2'+label['text']
        if 'blue'not in c:
            for i in range(15):lst[i]['state']=DISABLED
            label['text'] = 'P1'+label['text']
    a=[]
    for i in range(15):a.append(lst[i]['text'])
    
    for i in range(15):
        if a[i]>b[i]:
            lst[i]['text']=b[i]
            for i in range(15):lst[i]['state']=DISABLED
            label['text'] = 'Draw'
        
def buttonOn12():
    m=open('press.txt','r').read()
    open('press.txt','w+').write(str(int(m)+1))
    for i in range(15):
        lst[i]['state'] = NORMAL
    q=open('color.txt','r').read()
    if q=='red':
        open('color.txt','w+').write('blue')
    elif q=='blue':
        open('color.txt','w+').write('red')
    a,c=[],[]
    for i in range(15):c.append(lst[i]['text'])
    lst[12].configure(text=str(int(lst[12]['text'])+1),bg=q)
    for i in range(15):a.append(lst[i]['text'])
    b=['2','3','2','3','4','3','3','4','3','3','4','3','2','3','2']
    for j in range(10):
        for i in range(15):
            if int(a[i])>=int(b[i]):
                if i==0:
                    a[i+1]=str(int(a[i+1])+1)
                    a[i+3]=str(int(a[i+3])+1)
                    a[i]='0'

                if i==2:
                    a[i-1]=str(int(a[i-1])+1)
                    a[i+3]=str(int(a[i+3])+1)
                    a[i]='0'

                if i==3 or i==6 or i==9:
                    a[i-3]=str(int(a[i-3])+1)
                    a[i+3]=str(int(a[i+3])+1)
                    a[i+1]=str(int(a[i+1])+1)
                    a[i]='0'

                if i==5 or i==8 or i==11:
                    a[i-3]=str(int(a[i-3])+1)
                    a[i+3]=str(int(a[i+3])+1)
                    a[i-1]=str(int(a[i-1])+1)
                    a[i]='0'

                if i==4 or i==7 or i==10:
                    a[i-3]=str(int(a[i-3])+1)
                    a[i+3]=str(int(a[i+3])+1)
                    a[i-1]=str(int(a[i-1])+1)
                    a[i+1] = str(int(a[i+1])+1)
                    a[i]='0'

                if i==1:
                    a[i+3]=str(int(a[i+3])+1)
                    a[i+1]=str(int(a[i+1])+1)
                    a[i-1]=str(int(a[i-1])+1)
                    a[i]='0'
                if i==12:
                    a[i+1]=str(int(a[i+1])+1)
                    a[i-3]=str(int(a[i-3])+1)
                    a[i]='0'

                if i==13:
                    a[i-3]=str(int(a[i-3])+1)
                    a[i+1]=str(int(a[i+1])+1)
                    a[i-1]=str(int(a[i-1])+1)
                    a[i]='0'

                if i==14:
                    a[i-3]=str(int(a[i-3])+1)
                    a[i-1]=str(int(a[i-1])+1)
                    a[i]='0'
    for i in range(15):
        lst[i]['text'] = a[i]
    d=[]
    for i in range(15):
        if a[i]!=c[i] and a[i]!='0':d.append(i)
    for i in range(len(d)):
        lst[d[i]]['bg']=q
    for i in range(15):
        if lst[i]['text']=='0':lst[i]['bg']='black'
    c=[]
    for i in range(15):c.append(lst[i]['bg'])
    for i in range(15):
        if q=='red':
            if c[i]=='red':
                lst[i]['state']=DISABLED
        if q=='blue':
            if c[i]=='blue':
                lst[i]['state']=DISABLED
    m=open('press.txt','r').read()
    if int(m)>2:
        if 'red'not in c:
            for i in range(15):lst[i]['state']=DISABLED
            label['text'] = 'P2'+label['text']
        if 'blue'not in c:
            for i in range(15):lst[i]['state']=DISABLED
            label['text'] = 'P1'+label['text']
    a=[]
    for i in range(15):a.append(lst[i]['text'])
    
    for i in range(15):
        if a[i]>b[i]:
            lst[i]['text']=b[i]
            for i in range(15):lst[i]['state']=DISABLED
            label['text'] = 'Draw'
        
def buttonOn13():
    m=open('press.txt','r').read()
    open('press.txt','w+').write(str(int(m)+1))
    for i in range(15):
        lst[i]['state'] = NORMAL
    q=open('color.txt','r').read()
    if q=='red':
        open('color.txt','w+').write('blue')
    elif q=='blue':
        open('color.txt','w+').write('red')
    a,c=[],[]
    for i in range(15):c.append(lst[i]['text'])
    lst[13].configure(text=str(int(lst[13]['text'])+1),bg=q)
    for i in range(15):a.append(lst[i]['text'])
    b=['2','3','2','3','4','3','3','4','3','3','4','3','2','3','2']
    for j in range(10):
        for i in range(15):
            if int(a[i])>=int(b[i]):
                if i==0:
                    a[i+1]=str(int(a[i+1])+1)
                    a[i+3]=str(int(a[i+3])+1)
                    a[i]='0'

                if i==2:
                    a[i-1]=str(int(a[i-1])+1)
                    a[i+3]=str(int(a[i+3])+1)
                    a[i]='0'

                if i==3 or i==6 or i==9:
                    a[i-3]=str(int(a[i-3])+1)
                    a[i+3]=str(int(a[i+3])+1)
                    a[i+1]=str(int(a[i+1])+1)
                    a[i]='0'

                if i==5 or i==8 or i==11:
                    a[i-3]=str(int(a[i-3])+1)
                    a[i+3]=str(int(a[i+3])+1)
                    a[i-1]=str(int(a[i-1])+1)
                    a[i]='0'

                if i==4 or i==7 or i==10:
                    a[i-3]=str(int(a[i-3])+1)
                    a[i+3]=str(int(a[i+3])+1)
                    a[i-1]=str(int(a[i-1])+1)
                    a[i+1] = str(int(a[i+1])+1)
                    a[i]='0'

                if i==1:
                    a[i+3]=str(int(a[i+3])+1)
                    a[i+1]=str(int(a[i+1])+1)
                    a[i-1]=str(int(a[i-1])+1)
                    a[i]='0'

                if i==12:
                    a[i+1]=str(int(a[i+1])+1)
                    a[i-3]=str(int(a[i-3])+1)
                    a[i]='0'

                if i==13:
                    a[i-3]=str(int(a[i-3])+1)
                    a[i+1]=str(int(a[i+1])+1)
                    a[i-1]=str(int(a[i-1])+1)
                    a[i]='0'

                if i==14:
                    a[i-3]=str(int(a[i-3])+1)
                    a[i-1]=str(int(a[i-1])+1)
                    a[i]='0'
    for i in range(15):
        lst[i]['text'] = a[i]
    d=[]
    for i in range(15):
        if a[i]!=c[i] and a[i]!='0':d.append(i)
    for i in range(len(d)):
        lst[d[i]]['bg']=q
    for i in range(15):
        if lst[i]['text']=='0':lst[i]['bg']='black'
    c=[]
    for i in range(15):c.append(lst[i]['bg'])
    for i in range(15):
        if q=='red':
            if c[i]=='red':
                lst[i]['state']=DISABLED
        if q=='blue':
            if c[i]=='blue':
                lst[i]['state']=DISABLED
    m=open('press.txt','r').read()
    if int(m)>2:
        if 'red'not in c:
            for i in range(15):lst[i]['state']=DISABLED
            label['text'] = 'P2'+label['text']
        if 'blue'not in c:
            for i in range(15):lst[i]['state']=DISABLED
            label['text'] = 'P1'+label['text']
    a=[]
    for i in range(15):a.append(lst[i]['text'])
    
    for i in range(15):
        if a[i]>b[i]:
            lst[i]['text']=b[i]
            for i in range(15):lst[i]['state']=DISABLED
            label['text'] = 'Draw'
        
def buttonOn14():
    m=open('press.txt','r').read()
    open('press.txt','w+').write(str(int(m)+1))
    for i in range(15):
        lst[i]['state'] = NORMAL
    q=open('color.txt','r').read()
    if q=='red':
        open('color.txt','w+').write('blue')
    elif q=='blue':
        open('color.txt','w+').write('red')
    a,c=[],[]
    for i in range(15):c.append(lst[i]['text'])
    lst[14].configure(text=str(int(lst[14]['text'])+1),bg=q)
    for i in range(15):a.append(lst[i]['text'])
    b=['2','3','2','3','4','3','3','4','3','3','4','3','2','3','2']
    for j in range(10):
        for i in range(15):
            if int(a[i])>=int(b[i]):
                if i==0:
                    a[i+1]=str(int(a[i+1])+1)
                    a[i+3]=str(int(a[i+3])+1)
                    a[i]='0'

                if i==2:
                    a[i-1]=str(int(a[i-1])+1)
                    a[i+3]=str(int(a[i+3])+1)
                    a[i]='0'

                if i==3 or i==6 or i==9:
                    a[i-3]=str(int(a[i-3])+1)
                    a[i+3]=str(int(a[i+3])+1)
                    a[i+1]=str(int(a[i+1])+1)
                    a[i]='0'

                if i==5 or i==8 or i==11:
                    a[i-3]=str(int(a[i-3])+1)
                    a[i+3]=str(int(a[i+3])+1)
                    a[i-1]=str(int(a[i-1])+1)
                    a[i]='0'

                if i==4 or i==7 or i==10:
                    a[i-3]=str(int(a[i-3])+1)
                    a[i+3]=str(int(a[i+3])+1)
                    a[i-1]=str(int(a[i-1])+1)
                    a[i+1] = str(int(a[i+1])+1)
                    a[i]='0'

                if i==1:
                    a[i+3]=str(int(a[i+3])+1)
                    a[i+1]=str(int(a[i+1])+1)
                    a[i-1]=str(int(a[i-1])+1)
                    a[i]='0'

                if i==12:
                    a[i+1]=str(int(a[i+1])+1)
                    a[i-3]=str(int(a[i-3])+1)
                    a[i]='0'

                if i==13:
                    a[i-3]=str(int(a[i-3])+1)
                    a[i+1]=str(int(a[i+1])+1)
                    a[i-1]=str(int(a[i-1])+1)
                    a[i]='0'

                if i==14:
                    a[i-3]=str(int(a[i-3])+1)
                    a[i-1]=str(int(a[i-1])+1)
                    a[i]='0'
    for i in range(15):
        lst[i]['text'] = a[i]
    d=[]
    for i in range(15):
        if a[i]!=c[i] and a[i]!='0':d.append(i)
    for i in range(len(d)):
        lst[d[i]]['bg']=q
    for i in range(15):
        if lst[i]['text']=='0':lst[i]['bg']='black'
    c=[]
    for i in range(15):c.append(lst[i]['bg'])
    for i in range(15):
        if q=='red':
            if c[i]=='red':
                lst[i]['state']=DISABLED
        if q=='blue':
            if c[i]=='blue':
                lst[i]['state']=DISABLED
    m=open('press.txt','r').read()
    if int(m)>2:
        if 'red'not in c:
            for i in range(15):lst[i]['state']=DISABLED
            label['text'] = 'P2'+label['text']
        if 'blue'not in c:
            for i in range(15):lst[i]['state']=DISABLED
            label['text'] = 'P1'+label['text']
    a=[]
    for i in range(15):a.append(lst[i]['text'])
    
    for i in range(15):
        if a[i]>b[i]:
            lst[i]['text']=b[i]
            for i in range(15):lst[i]['state']=DISABLED
            label['text'] = 'Draw'
#Buttons
lst=[None,None,None,None,None,None,None,None,None,None,None,None,None,None,None]
lst[0] = Button(root, text = "0", fg='white', bg = 'black', command=buttonOn0)
lst[0].place(x = 0, y = 0,width=100, height=100)
lst[0]['font'] = font.Font(size=50)
lst[1] = Button(root, text = "0", fg='white', bg = 'black', command=buttonOn1)
lst[1].place(x = 100, y = 0,width=100, height=100)
lst[1]['font'] = font.Font(size=50)
lst[2] = Button(root, text = "0", fg='white', bg = 'black', command=buttonOn2)
lst[2].place(x = 200, y = 0,width=100, height=100)
lst[2]['font'] = font.Font(size=50)

lst[3] = Button(root, text = "0", fg='white', bg = 'black', command=buttonOn3)
lst[3].place(x = 0, y = 100,width=100, height=100)
lst[3]['font'] = font.Font(size=50)
lst[4] = Button(root, text = "0", fg='white', bg = 'black', command=buttonOn4)
lst[4].place(x = 100, y = 100,width=100, height=100)
lst[4]['font'] = font.Font(size=50)
lst[5] = Button(root, text = "0", fg='white', bg = 'black', command=buttonOn5)
lst[5].place(x = 200, y = 100,width=100, height=100)
lst[5]['font'] = font.Font(size=50)

lst[6] = Button(root, text = "0", fg='white', bg = 'black', command=buttonOn6)
lst[6].place(x = 0, y = 200,width=100, height=100)
lst[6]['font'] = font.Font(size=50)
lst[7] = Button(root, text = "0", fg='white', bg = 'black', command=buttonOn7)
lst[7].place(x = 100, y = 200,width=100, height=100)
lst[7]['font'] = font.Font(size=50)
lst[8] = Button(root, text = "0", fg='white', bg = 'black', command=buttonOn8)
lst[8].place(x = 200, y = 200,width=100, height=100)
lst[8]['font'] = font.Font(size=50)

lst[9] = Button(root, text = "0", fg='white', bg = 'black', command=buttonOn9)
lst[9].place(x = 0, y = 300,width=100, height=100)
lst[9]['font'] = font.Font(size=50)
lst[10] = Button(root, text = "0", fg='white', bg = 'black', command=buttonOn10)
lst[10].place(x = 100, y = 300,width=100, height=100)
lst[10]['font'] = font.Font(size=50)
lst[11] = Button(root, text = "0", fg='white', bg = 'black', command=buttonOn11)
lst[11].place(x = 200, y = 300,width=100, height=100)
lst[11]['font'] = font.Font(size=50)

lst[12] = Button(root, text = "0", fg='white', bg = 'black', command=buttonOn12)
lst[12].place(x = 0, y = 400,width=100, height=100)
lst[12]['font'] = font.Font(size=50)
lst[13] = Button(root, text = "0", fg='white', bg = 'black', command=buttonOn13)
lst[13].place(x = 100, y = 400,width=100, height=100)
lst[13]['font'] = font.Font(size=50)
lst[14] = Button(root, text = "0", fg='white', bg = 'black', command=buttonOn14)
lst[14].place(x = 200, y = 400,width=100, height=100)
lst[14]['font'] = font.Font(size=50)
#Label
label1 = Label(root, text = "P1", fg='white', bg = 'black')
label1.place(x = 300, y = 0,width=100, height=100)
label1['font'] = font.Font(size=50)
label1 = Label(root, text = "P1", fg='red', bg = 'red')
label1.place(x = 300, y = 100,width=100, height=100)
label1['font'] = font.Font(size=50)
label1 = Label(root, text = "P1", fg='blue', bg = 'blue')
label1.place(x = 300, y = 300,width=100, height=100)
label1['font'] = font.Font(size=50)
label1 = Label(root, text = "P2", fg='white', bg = 'black')
label1.place(x = 300, y = 400,width=100, height=100)
label1['font'] = font.Font(size=50)

label = Label(root, text = "\nWins", fg='white', bg = 'black')
label.place(x = 300, y = 200,width=100, height=100)
label['font'] = font.Font(size=30)

root.mainloop()
