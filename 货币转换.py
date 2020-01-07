import requests
import re
import tkinter
from tkinter import ttk

def send(url,f,t,j,input2):
    input2.delete(0.0,'end')
    headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:70.0) Gecko/20100101 Firefox/70.0','Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8',
                'Accept-Language': 'zh-CN,zh;q=0.8,zh-TW;q=0.7,zh-HK;q=0.5,en-US;q=0.3,en;q=0.2',
                'Accept-Encoding': 'gzip, deflate',
                'Connection': 'close',
                'Referer': 'https://huobiduihuan.51240.com/?f=USD&t=CNY&j=46',
                'Cookie': 'Hm_lvt_fbe0e02a7ffde424814bef2f6c9d36eb=1578363307; Hm_lpvt_fbe0e02a7ffde424814bef2f6c9d36eb=1578363335',
                'Upgrade-Insecure-Requests': '1'}
    url = url + 'f={}&t={}&j={}'.format(f,t,j)
    try:
        rex = requests.get(url=url,headers=headers)
        result = ''.join(re.findall(r'可以兑换 (\d+\.\d{0,2})',rex.text))
        input2.insert(1.0,result)
    except Exception as e:
        print("错误是:{}".format(e))


def get_parameter(choice1,choice2,text):
    global j,f,t
    j = text.get()
    f = (choice1.get())[0:3]
    t = (choice2.get())[0:3]

if __name__ == "__main__":
    url = 'http://huobiduihuan.51240.com/?'
    win = tkinter.Tk()
    win.title("汇率实时查询")
    win.geometry('400x300')     #x是小写字母x，而不是乘号
    
    text1 = tkinter.Text(win)
    text1.insert(1.0,'原始货币')
    text1.place(x=66,y=70,width=80,height=20)
    choice1 = ttk.Combobox(win)
    choice1.place(x=66,y=100,width=100)
    choice1['value'] = ('AUD澳元','CNY人名币','EUR欧元','GBP英镑','HKD港元','JPY日元','KRW韩元','TWD台币','USD美元')
    choice1.current(8)
    input1 = tkinter.Entry(win)
    input1.place(x=66,y=120,width=120,height=20)
    print(input1)

    text2 = tkinter.Text(win)
    text2.insert(1.0,'目标货币')
    text2.place(x=66+100+66,y=70,width=100,height=20)
    choice2 = ttk.Combobox(win)
    choice2.place(x=66+100+66,y=100,width=100)
    choice2['value'] = ('AUD澳元','CNY人名币','EUR欧元','GBP英镑','HKD港元','JPY日元','KRW韩元','TWD台币','USD美元')
    choice2.current(1)
    input2 = tkinter.Text(win)
    input2.insert(1.0,'')
    input2.place(x=66+100+66,y=120,width=120,height=20)

    but = tkinter.Button(win,text='确定')
    but.bind("<Enter>",lambda event:get_parameter(choice1,choice2,input1))
    but.bind("<Button-1>",lambda event:send(url,f,t,j,input2))
    but.pack(side=tkinter.BOTTOM,ipadx = 20,pady=20)

    win.attributes("-alpha",0.95)
    win.mainloop()