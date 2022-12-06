import requests
from tkinter import *


def pars():
    username = us.get()
    repositoriy = re.get()
    req = requests.get(f'https://api.github.com/repos/{username}/{repositoriy}').json()
    with open('pr11.txt', 'a+') as f:
        if 'company' in req:
            f.write(f"'company': '{req['company']}\n")
        else:
            f.write("'company: None'\n")
        if 'created_at' in r:
            f.write(f"'created_at': '{req['created_at']}\n")
        else:
            f.write("'None'\n")
        if 'email' in req:
            f.write(f"'email': '{req['email']}\n")
        else:
            f.write("'email: None'\n")
        if 'id' in req:
            f.write(f"'id': '{req['id']}\n")
        else:
            f.write("'None'\n")
        if 'name' in req:
            f.write(f"'name': '{req['name']}\n")
        else:
            f.write("'None'\n")
        if 'url' in req:
            f.write(f"'url': '{req['url']}\n")
        else:
            f.write("'None'\n")

window = Tk()
window.title('Malinin Roman')
window.geometry('640x360')
lbl = Label(window, text='Type username', font=('Times New Roman', 25))
lbl.grid(column=0, row=0)
lbl = Label(window, text='Type repositoriy', font=('Times New Roman', 25))
lbl.grid(column=0, row=4)
btn = Button(window, text='Enter', command=pars, width=15)
btn.grid(column=4, row=3)
us = Entry(window, width=25)
us.grid(column=1, row=0)
re = Entry(window, width=25)
re.grid(column=1, row=4)
window.mainloop()
print (req)
