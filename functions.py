from view import *

def get_plus(event):
    dig1 = int(ent1.get())
    dig2 = int(ent2.get())
    res = dig1 + dig2    
    lab['text'] = res
    
def get_minus(event):
    dig1 = int(ent1.get())
    dig2 = int(ent2.get())
    res = dig1 - dig2    
    lab['text'] = res
    
def get_mult(event):
    dig1 = int(ent1.get())
    dig2 = int(ent2.get())
    res = dig1 * dig2    
    lab['text'] = res

def get_div(event):
    dig1 = int(ent1.get())
    dig2 = int(ent2.get())
    res = dig1 / dig2    
    lab['text'] = res