# tarea seleccionar por combo o por radio button la operacion
# matematica que desea realizar (sumar, restar , multiplicar y potencia)
import tkinter as tk
from tkinter import ttk

class Calculator():
    def __init__(self):        
        #Creating interface
        self.win = tk.Tk()
        self.win.title('Calculator') #tittle
        self.win.geometry('360x100') #size
        self.win.configure(background='#cdcdcd') #setting bg color

        ########Declaring functions
        self.sum_val = lambda first_num, second_num: first_num+second_num
        self.subs_val = lambda first_num, second_num: first_num-second_num
        self.prod_val = lambda first_num, second_num: first_num*second_num
        self.pow_val = lambda first_num, second_num: first_num**second_num
        
        ########
        self.lb1 = tk.Label(self.win,text='Choose one: ')
        self.lb1.grid(row=1,column=0)
        self.lb1.configure(background='#cdcdcd')
        ########
        self.cbo = ttk.Combobox(self.win)
        self.cbo['values'] = ['Select..','Sum','Substraction','Product','Pow']
        self.cbo.current(0) #Current selection
        self.cbo.grid(row=1,column=1,sticky="W") #Moving to the left(West)
        ########
        self.lbFirst = tk.Label(self.win,text='First: ')
        self.lbFirst.grid(row=2,column=0,sticky="W") 
        self.lbFirst.configure(background='#cdcdcd')
        ########
        #first_number = tk.IntVar() #Declaring integer variable
        self.txtBox_first = tk.Entry(self.win,width=5)
        self.txtBox_first.delete(first=0) #CLearing up first character which appears by default
        self.txtBox_first.grid(row=2,column=1,sticky="W") 
        ########
        self.lbSecond = tk.Label(self.win,text='Second: ')
        self.lbSecond.grid(row=3,column=0,sticky="W") 
        self.lbSecond.configure(background='#cdcdcd')
        ########        
        self.txtBox_second = tk.Entry(self.win,width=5)
        self.txtBox_second.delete(first=0)
        self.txtBox_second.grid(row=3,column=1,sticky="W")
        
        ########
        self.total = tk.IntVar() #Declaring Integer variable 
        ########
        self.lb_result = tk.Label(self.win,textvariable=self.total,font='bold')
        self.lb_result.grid(row=4,column=1,sticky="W")
        self.lb_result.configure(background='#cdcdcd')        
        ########
        self.txt_result = tk.Label(self.win,text='Result: ')               
        self.txt_result.grid(row=4,column=0,sticky="W")
        self.txt_result.configure(background='#cdcdcd')        
        ########        
        self.cal_button = ttk.Button(self.win,text="Calculate",command=self.calculate)
        self.cal_button.grid(row=1,column=4,rowspan=4,ipady=30) #With rowspan, you get the 3 first rows, then with ipady you can enlarge vertically        

        self.win.mainloop() #Running interface  

    def calculate(self):
        total = 0
        try:
            if self.cbo.get() == 'Sum':
                total = self.sum_val(int(self.txtBox_first.get()),int(self.txtBox_second.get()))
            elif self.cbo.get() == 'Substraction':
                total = self.subs_val(int(self.txtBox_first.get()),int(self.txtBox_second.get()))
            elif self.cbo.get() == 'Product':
                total = self.prod_val(int(self.txtBox_first.get()),int(self.txtBox_second.get()))
            elif self.cbo.get() == 'Pow':
                total = self.pow_val(int(self.txtBox_first.get()),int(self.txtBox_second.get()))
            else:
                total = 'Select an option..'
            self.total.set(total) #Setting value to total, which is going to be textvariable of lb_result       
        except ValueError:
            total = 'Error'
            self.total.set(total) #Setting value to total, which is going to be textvariable of lb_result       
        
def main():
    my_app = Calculator()
    return 0    
if __name__=='__main__':
    main()