from functions import *
from view import *

but1.bind('<Button-1>', get_plus)
but2.bind('<Button-1>', get_minus)
but3.bind('<Button-1>', get_mult)
but4.bind('<Button-1>', get_div)

ent1.pack()
ent2.pack()
but1.pack()
but2.pack()
but3.pack()
but4.pack()

lab.pack()

root.mainloop()