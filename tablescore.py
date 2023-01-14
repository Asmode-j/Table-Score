import tkinter as tk
from tkinter import scrolledtext
import random


all_authors={}


class Lenta:
    def __init__(self, name, score):
        self.name = name
        self.score = score

def tick():
    copy=all_authors.copy()
    mesto=1
    x1=[]
    x2=[]
    for i in (txt_area0, txt_area1, txt_area2, txt_area3, txt_area4):
        for n in copy.items():
            x1.append(n[0])
            x2.append(int(n[1]))
        try:
            max_index=x2.index(max(x2))
            name=x1[max_index]
            score=x2[max_index]
            i.configure(text=f'{mesto} | {name}:{score}')
            copy.pop(name)
            x1=[]
            x2=[]
            mesto+=1
        except:
            continue
    window.after(1000, tick)
    
def napolnenie():
    zapic_name=entry_author.get()
    zapic_score=entry_score.get()
    if zapic_name not in all_authors:
        all_authors[zapic_name] = zapic_score
        globals() [f"{zapic_name}"] = Lenta(f'{zapic_name}',f'{zapic_score}')
        
    if zapic_score < all_authors.get(zapic_name):
        pass
    else:     
        all_authors[zapic_name] = zapic_score
        globals() [f"{zapic_name}"] = Lenta(f'{zapic_name}',f'{zapic_score}')


window = tk.Tk()
window.title("Лента новостей")  
window.geometry('750x550')

for i in range(5):
    exec (f"txt_area{i} = tk.Label(window, text=f'Место {i+1}',width = 10, heigh=1)")
    exec (f'txt_area{i}.grid(sticky="we", row={i},column=0, columnspan=2, padx=3)')
    
entry_author = tk.Entry(width=20)
entry_author.grid(sticky='w', row=5,column=0, pady=5, padx=3)

entry_score = tk.Entry(width=20)
entry_score.grid(sticky='w', row=5,column=1, pady=5, padx=3)

btn = tk.Button(text = 'Добавить сообщение', command=napolnenie)
btn.grid(sticky='nw', column=1, row=6)

tick()
window.mainloop()
