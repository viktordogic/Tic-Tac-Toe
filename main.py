import tkinter as tk

btn = [[object for y in range(0, 3)] for z in range(0, 3)]

root_window = tk.Tk()

x = tk.PhotoImage(file=r'C:\\Users\\vikto\\Projects\\x.gif')
#o = tk.PhotoImage(file=r'C:\\Users\\vikto\\Projects\\o.png')

def btn_pressed(buton):
    buton['image'] = x


def intro():
    mess = tk.Toplevel()
    root_window.eval(f'tk::PlaceWindow {mess} center')
    mess.title('Tip igre')
    tk.Label(mess, text='Zelite li igrati PvP ili protiv bot-a?').grid(row=0, padx=20, pady=20)
    tk.Button(mess, text='PvP', command=lambda: [root_window.deiconify(), mess.destroy()]).grid(row=1, column=0, )
    tk.Button(mess, text='AI', command=lambda: [root_window.deiconify(), mess.destroy()]).grid(row=1, column=1)






root_window.eval('tk::PlaceWindow %s center' % root_window.winfo_toplevel())
root_window.title('Krizic kruzic!')
label = tk.Label(root_window, text='Krizic kruzic!')
label.grid(row=0, column=0)

frame00 = tk.Frame(master=root_window, width=50, height=50)
frame00.grid(row=1, column=0)
btn[0][0] = tk.Button(master=frame00, relief=tk.RAISED, text=' ', width=15, height=5, command=lambda: btn_pressed(btn[0][0]))
btn[0][0].pack(padx=5, pady=5)

frame01 = tk.Frame(master=root_window, width=50, height=50)
frame01.grid(row=1, column=1)
btn[0][1] = tk.Button(master=frame01, relief=tk.RAISED, text=' ', width=15, height=5, command=lambda: btn_pressed(btn[0][1]))
btn[0][1].pack(padx=5, pady=5)

frame02 = tk.Frame(master=root_window, width=50, height=50)
frame02.grid(row=1, column=2)
btn[0][2] = tk.Button(master=frame02, relief=tk.RAISED, text=' ', width=15, height=5, command=lambda: btn_pressed(btn[0][2]))
btn[0][2].pack(padx=5, pady=5)

frame10 = tk.Frame(master=root_window, width=50, height=50)
frame10.grid(row=2, column=0)
btn[1][0] = tk.Button(master=frame10, relief=tk.RAISED, text=' ', width=15, height=5, command=lambda: btn_pressed(btn[1][0]))
btn[1][0].pack(padx=5, pady=5)

frame11 = tk.Frame(master=root_window, width=50, height=50)
frame11.grid(row=2, column=1)
btn[1][1] = tk.Button(master=frame11, relief=tk.RAISED, text=' ', width=15, height=5, command=lambda: btn_pressed(btn[1][1]))
btn[1][1].pack(padx=5, pady=5)

frame12 = tk.Frame(master=root_window, width=50, height=50)
frame12.grid(row=2, column=2)
btn[1][2] = tk.Button(master=frame12, relief=tk.RAISED, text=' ', width=15, height=5, command=lambda: btn_pressed(btn[1][2]))
btn[1][2].pack(padx=5, pady=5)

frame20 = tk.Frame(master=root_window, width=50, height=50)
frame20.grid(row=3, column=0)
btn[2][0] = tk.Button(master=frame20, relief=tk.RAISED, text=' ', width=15, height=5, command=lambda: btn_pressed(btn[2][0]))
btn[2][0].pack(padx=5, pady=5)

frame21 = tk.Frame(master=root_window, width=50, height=50)
frame21.grid(row=3, column=1)
btn[2][1] = tk.Button(master=frame21, relief=tk.RAISED, text=' ', width=15, height=5, command=lambda: btn_pressed(btn[2][1]))
btn[2][1].pack(padx=5, pady=5)

frame22 = tk.Frame(master=root_window, width=50, height=50)
frame22.grid(row=3, column=2)
btn[2][2] = tk.Button(master=frame22, relief=tk.RAISED, text=' ', width=15, height=5, command=lambda: btn_pressed(btn[2][2]))
btn[2][2].pack(padx=5, pady=5)



root_window.withdraw()

intro()

root_window.mainloop()
