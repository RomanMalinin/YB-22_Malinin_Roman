import requests
from tkinter import *


def click():
    username = us.get()
    repositoriy = re.get()
    r = requests.get(f'https://api.github.com/repos/{username}/{repositoriy}').json()
    with open('C:\\Users\\malin\\PycharmProjects\\PY\\venv\\pr11', 'a+') as f:
        if 'company' in r:
            f.write(f"'company': '{r['company']}\n")
        else:
            f.write("'company: None'\n")
        if 'created_at' in r:
            f.write(f"'created_at': '{r['created_at']}\n")
        else:
            f.write("'None'\n")
        if 'email' in r:
            f.write(f"'email': '{r['email']}\n")
        else:
            f.write("'email: None'\n")
        if 'id' in r:
            f.write(f"'id': '{r['id']}\n")
        else:
            f.write("'None'\n")
        if 'name' in r:
            f.write(f"'name': '{r['name']}\n")
        else:
            f.write("'None'\n")
        if 'url' in r:
            f.write(f"'url': '{r['url']}\n")
        else:
            f.write("'None'\n")

window = Tk()
window.title('Malinin Roman')
window.geometry('640x360')
lbl = Label(window, text='Type username', font=('Times New Roman', 25))
lbl.grid(column=0, row=0)
lbl = Label(window, text='Type repositoriy', font=('Times New Roman', 25))
lbl.grid(column=0, row=4)
btn = Button(window, text='Enter', command=click, width=15)
btn.grid(column=4, row=3)
us = Entry(window, width=25)
us.grid(column=1, row=0)
re = Entry(window, width=25)
re.grid(column=1, row=4)
window.mainloop()
print (r)
