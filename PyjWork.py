def ran():
    n = 0 | 1 | 2 | 3 | 4 | 5
    a = 6 | 7 | 8 | 9 | 10 | 11
    b = 11 | 12 | 13 | 14| 15 | 16
    BI = n + a + b
    
def pr(p):
    print(p)
    
def hel():
    print("Hello World")
    
def Pro():
    print("Hello Programmer")
    
def ser():
    spi = input()
    
def peV(v):
    pr("|" * v)
    
def peni(n):
    pr(n)
    
def pek(k):
    if k == "s":
        pr("()")
    if k == "k2":
        pr("  ..  ")
        pr(" .  . ")
        pr(".    .")
        pr(".    .")
        pr(" .  . ")
        pr("  ..  ")
    if k == "s2":
        pr("{}")
        
def button(Name, but, Command):
    pr("/" + Name)
    pr("{" + but)
    CMN = Command
    Code = input(str("Code button:"))
    if Code == but:
        CMN
        
def anime(Object, DI):
    if Object  == "Coob":
        if DI == "UP":
            for x in range(1, 10):
                pr("")
            pr(" ===== ")
            pr("|     |")
            pr("|     |")
            pr("|     |")
            pr(" ===== ")
            for x in range(1, 10):
                pr("")
            pr(" ===== ")
            pr("|     |")
            pr("|     |")
            pr("|     |")
            pr(" ===== ")
            for x in range(1, 4):
                pr("")
