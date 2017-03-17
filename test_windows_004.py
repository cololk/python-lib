#本程式主要展示選單式列表的使用方式
import tkinter as tk

window = tk.Tk()
window.title('My window')
window.geometry('200x200')
#指定var1為字串變數
var1 = tk.StringVar()
#建立標籤物件
l =tk.Label(window, bg='yellow', width=4, textvariable=var1) #var1 這個字串變數作為標籤顯示的值
l.pack()

def print_selection():
	value=lb.get(lb.curselection())  #curselection意指光標, 此段指從listbox物件的光標讀取
	var1.set(value) #讀取到的光標指到的數值設定為var1

#建立按鈕物件
b1 = tk.Button(window, text='print selection', width=15, 
	height=2, command=print_selection)
b1.pack() #進行擺放

var2 = tk.StringVar()
var2.set((11,22,33,44))
#建立Listbox物件
lb = tk.Listbox(window,listvariable=var2)
list_items=[1,2,3,4]
for item in list_items:
	lb.insert('end',item)
lb.insert(1,'first')
lb.insert(2,'second')
lb.delete(2)
lb.pack()



window.mainloop()


