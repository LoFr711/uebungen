from turtle import *

def sierpinski(size: int, n: int):
    # Zeichnet das Sierpinski Dreieck in gegebener Rekursionstiefe

    # Berechnen des Pfades mithilfe des Lindenmayer-Systems
    route = "F-G-G"
    while n > 0:
        new_route = ""
        for character in route:
            if character == "F":
                new_route += "F-G+F+G-F"
            elif character == "G":
                new_route += "GG"
            elif character == "+":
                new_route += "+"
            elif character == "-":
                new_route += "-"
        route = new_route
        n = n-1
    
    color('black', 'white')
    print(route)
    begin_fill()
    penup()
    goto(-200,-100)
    pendown()
    
    # Zeichnen des Dreiecks mithilfe des Pfades und des Turtle Moduls
    while True:
        if route[:1] == "F":
            forward(size)
            route = route[1:]
        elif route[:1] == "G":
            forward(size)
            route = route[1:]
        elif route[:1] == "-":
            left(120)
            forward(size)
            
            route = route[2:]
        elif route[:1] == "+":
            
            left(-120)
            forward(size)
            route = route[2:]
        elif route == "":
            break
        
    end_fill()
    done()

if __name__ == '__main__':
    n = 2
    size = 400 / (2 ** n)
    sierpinski(size, n)
