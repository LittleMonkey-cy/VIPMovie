import requests,webbrowser,re
#创建界面
from tkinter import*
url = "https://www.kivi8.top/"
headers = {"User-Agent":
               "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/84.0.4147.125 Safari/537.36 Edg/84.0.522.61"}
response = requests.get(url, headers=headers, timeout=30)
response.encoding = response.apparent_encoding
html = response.text
# print(html)
# res = re.compile(r'value="(.*?)">')
res = re.compile(r'value="(.*?)">')
reg = re.findall(res, html)
# print(len(reg))
# print(reg)
one = reg[0]
two = reg[1]
three = reg[2]
four = reg[3]
five = reg[4]
six = reg[5]
seven = reg[6]
eight = reg[7]
nine = reg[8]
ten = reg[9]
eleven = reg[10]
twelve = reg[11]
thirteen = reg[12]
fourteen = reg[14]
fifteen = reg[15]
sixteen = reg[16]
seventeen = reg[17]
eighteen = reg[18]
nineteen = reg[19]
twenty = reg[20]
TwentyOne = reg[21]
TwentyTwo = reg[22]
TwentyThree = reg[23]
TwentyFour = reg[24]
TwentyFive = reg[25]
TwentySix = reg[26]
TwentySeven = reg[27]
# TwentyEight = reg[28]
# 创建界面
window = Tk()
#窗口标题
window.title("VIP影视---陈钰")
#窗口界面大小
window.geometry("1000x700")
# 防止用户调整尺寸
window.resizable(0,0)
# 添加背景图片
im = PhotoImage(file="bg.png")
bj = Label(window, image=im)
bj.pack()
#创建界面上的控件
lb1 = Label(window,text = 'VIP电影解析',fg = "red",bg = "black",font = ("楷体",30))
lb1.place(x=380,y=0,width=300,height=45)
lb2 = Label(window,text = "请输入视频或电影的网址链接")
lb2.place(x=20,y=600,width=250,height=25)
#连接输入区
inp = Entry(window)
inp.place(x=290,y=600,width=500,height=25)
# 信息提示区
lb3 = Label(window,text = "成\r\n由\r\n奋\r\n发\r\n败\r\n由\r\n奢",fg="red",bg="black",font=("华文行楷",20))
lb3.place(x=0,y=0,width=180,height=600)
lb4 = Label(window,text = "富\r\n在\r\n勤\r\n劳\r\n穷\r\n在\r\n惰",fg="red",bg="black",font=("华文行楷",20))
lb4.place(x=820,y=0,width=180,height=600)
#单选按钮
var = StringVar()
var.set(1)
radio = Radiobutton(window,text="连接一",variable=var,value=one)
radio.place(x=230,y=100,width=150,height=20)
r1 = Radiobutton(window,text="连接二",variable=var,value=two)
r1.place(x=230,y=150,width=150,height=20)
r2 = Radiobutton(window,text='连接三',variable=var,value=three)
r2.place(x=230,y=200,width=150,height=20)
r3 = Radiobutton(window,text='连接四',variable=var,value=four)
r3.place(x=230,y=250,width=150,height=20)
r4 = Radiobutton(window,text='连接五',variable=var,value=five)
r4.place(x=230,y=300,width=150,height=20)
r5 = Radiobutton(window,text='连接六',variable=var,value=six)
r5.place(x=230,y=350,width=150,height=20)
r6 = Radiobutton(window,text='连接七',variable=var,value=seven)
r6.place(x=230,y=400,width=150,height=20)
r7 = Radiobutton(window,text='连接八',variable=var,value=eight)
r7.place(x=230,y=450,width=150,height=20)
r8 = Radiobutton(window,text='连接九',variable=var,value=nine)
r8.place(x=230,y=500,width=150,height=20)
r9 = Radiobutton(window,text='连接十',variable=var,value=ten)
r9.place(x=230,y=550,width=150,height=20)
r10 = Radiobutton(window,text='连接十一',variable=var,value=eleven)
r10.place(x=420,y=100,width=150,height=20)
r11 = Radiobutton(window,text='连接十二',variable=var,value=twelve)
r11.place(x=420,y=150,width=150,height=20)
r12 = Radiobutton(window,text='连接十三',variable=var,value=thirteen)
r12.place(x=420,y=200,width=150,height=20)
r13 = Radiobutton(window,text='连接十四',variable=var,value=fourteen)
r13.place(x=420,y=250,width=150,height=20)
r14 = Radiobutton(window,text='连接十五',variable=var,value=fifteen)
r14.place(x=420,y=300,width=150,height=20)
r15 = Radiobutton(window,text='连接十六',variable=var,value=sixteen)
r15.place(x=420,y=350,width=150,height=20)
r16 = Radiobutton(window,text='连接十七',variable=var,value=seventeen)
r16.place(x=420,y=400,width=150,height=20)
r17 = Radiobutton(window,text='连接十八',variable=var,value=eighteen)
r17.place(x=420,y=450,width=150,height=20)
r18 = Radiobutton(window,text='连接十九',variable=var,value=nineteen)
r18.place(x=420,y=500,width=150,height=20)
r19 = Radiobutton(window,text='连接二十',variable=var,value=twenty)
r19.place(x=420,y=550,width=150,height=20)
r20 = Radiobutton(window,text='连接21',variable=var,value=TwentyOne)
r20.place(x=620,y=100,width=150,height=20)
r21 = Radiobutton(window,text='连接22',variable=var,value=TwentyTwo)
r21.place(x=620,y=150,width=150,height=20)
r22 = Radiobutton(window,text='连接23',variable=var,value=TwentyThree)
r22.place(x=620,y=200,width=150,height=20)
r23 = Radiobutton(window,text='连接24',variable=var,value=TwentyFour)
r23.place(x=620,y=250,width=150,height=20)
r24 = Radiobutton(window,text='连接25',variable=var,value=TwentyFive)
r24.place(x=620,y=300,width=150,height=20)
r25 = Radiobutton(window,text='连接26',variable=var,value=TwentySix)
r25.place(x=620,y=350,width=150,height=20)
r26 = Radiobutton(window,text='连接27',variable=var,value=TwentySeven)
r26.place(x=620,y=400,width=150,height=20)
# r27 = Radiobutton(window,text='连接28',variable=var,value=TwentyEight)
# r27.place(x=620,y=450,width=150,height=20)
def play():
    webbrowser.open(var.get()+inp.get())
#播放按钮
btn = Button(window,text="尽情欣赏",command=play)
btn.place(x=820,y=600,width=120,height=25)
#清楚按钮
def del_text():
    inp.delete(0,'end')
btn2=Button(window,text='重新来过',width=8,command=del_text)
btn2.place(x=820,y=650,width=120,height=25)
window.mainloop()
# input()

