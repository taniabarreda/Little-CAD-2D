from copy import deepcopy
#Crear lista de 83 x 42 caracteres
w,h=42, 83;

grabado=False
def recta(x1,y1,x2,y2):
    if x2 == x1:  # pendiente infinito dividion entre cero
        for f in range(y1,y2):
            matriz[x1][f]="*"
    else:

        for m in range(x1,x2+1):
            # Ecuación de la recta
            j =(((y2-y1)/(x2-x1))*m)+(y1-(((y2-y1)/(x2-x1))*x1))
            j=int(round(j/1))
            matriz[m][j] = "*"
    return
def circulo_elipse(cx,cy,r1,r2):
    for k in range(cx-r1,cx+r1+1):
        # Ecuación de la elipse, si los radios son = sale un círculo
        l=r2*(1-(((k-cx)**2)/(r1**2)))**(1/2)+cy
        l=int(round(l/1))
        matriz[k][l]="*"
        l = -1* (r2*(1-(((k-cx)**2)/(r1**2)))**(1/2))+cy
        l = int(round(l / 1))
        matriz[k][l] = "*"
    return
def cuadrado_rectangulo(ix,iy,ba,h):
    recta(ix, iy+h, ix+ba, iy+h)
    recta(ix, iy, ix + ba, iy)
    recta(ix, iy, ix , iy + h)
    recta(ix+ba, iy, ix + ba, iy + h)
    return
def triangulo_isoceles(iex,iey,base,alt):
    recta(iex, iey, iex+base, iey)
    recta(iex, iey, iex + round(base/2), iey+alt)
    recta(iex + round(base/2), iey+alt,iex + base , iey)
    return
def graficar():
    for y in reversed(range(0, w)):
        for x in range(0, h):
            print(matriz[x][y], end="")
        print("")

matriz=[[0 for x in range(w)] for y in range(h)]
for x in range(0, h):
    for y in range(0, w):
        if x == 0:  # primera linea
            matriz[x][y]= "."
        else:
            if x == h-1:
                matriz[x][y]="."
            else:
                if y == 0:
                    matriz[x][y]="."
                else:
                    if y == w-1:
                        matriz[x][y]="."
                    else:
                        matriz[x][y]=" "




Menu=1
while Menu!="0":
    print("MENÚ")
    Menu = input('1. Agregar una línea\n2.Agregar una elipse o circulo\n3.Agregar un rectángulo o cuadrado\n4.Agregar un triangulo\n5.Mostrar un dibujo\n6.Leer un dibujo\n7.Grabar un dibujo\n0.Salir del programa')

    if Menu=='1':
        p1x = int(input("Ingrese el valor de las coordenadas del eje x en el punto 1:", ))
        p1 = int(input("Ingrese el valor de las coordenadas del eje y en el punto 1:", ))
        p2x = int(input("Ingrese el valor de las coordenadas del eje x en el punto 2:", ))
        p2 = int(input("Ingrese el valor de las coordenadas del eje y en ek punto 2:", ))
        if (0<= p1 < h) and ( 0<=  p1x < w) and (0<= p2 <= h) and (0<= p1x <= w):
            if p1x>p2x:
             recta(p1,p1x,p2,p2x)
            else:
             recta(p1x, p1, p2x, p2)
        else:
            print("Ingrese valores dentro del rango")
    if Menu=='2':
        p1x = int(input("Ingrese el valor de las coordenadas del eje x en el centro:", ))
        p1 = int(input("Ingrese el valor de las coordenadas del eje y en el centro:", ))
        r = int(input("Ingrese el valor de las coordenadas del radio en x:", ))
        rd= int(input("Ingrese el valor de las coordenadas del radio en y:", ))
        if (0<=p1 <= 42) and ( 0 <= p1x <= 82) and (0<= r <= 21) and(0<=rd<=40) and (p1>rd) and (p1x>r):
            circulo_elipse(p1x,p1,r,rd)
        else:
            print("Ingrese valores dentro del rango")
    if Menu=='3':
     pix = int(input("Ingrese el valor de las coordenadas del eje x en el punto inferior izquierdo:", ))
     pi = int(input("Ingrese el valor de las coordenadas del eje y en el punto inferior izquierdo:", ))
     b = int(input("Ingrese el valor de la base:", ))
     a = int(input("Ingrese el valor de la altura:", ))
     if (0 <= pi <= 42) and (0 <= pix <= 82) and (0 <= b <= 82) and (0 <= a <= 42):
         cuadrado_rectangulo(pix, pi, b, a)
     else:
         print("Ingrese valores dentro del rango")
    if Menu=='4':
        pix = int(input("Ingrese el valor de las coordenadas del eje x en el punto inferior izquierdo:", ))
        pi = int(input("Ingrese el valor de las coordenadas del eje y en el punto inferior izquierdo:", ))
        b = int(input("Ingrese el valor de la base:", ))
        a = int(input("Ingrese el valor de la altura:", ))
        if (0 <= pi <= 42) and (0 <= pix <= 82) and (0 <= b <= 82) and (0 <= b <= 42):
            triangulo_isoceles(pix, pi, b, a)

        else:
            print("Ingrese valores dentro del rango")
    if Menu=='5':
        # imprimir grafica
        graficar()
    if Menu=='6':
        if grabado==True:
            matriz=deepcopy(guardar)
            print("Dibujo leido")
        else:
            print("No se ha guardado ninguna matriz")
    if Menu=='7':
        guardar=deepcopy(matriz)
        grabado=True
        print("Dibujo Guardado")
#for y in reversed(range(0, w)):
        #for x in range(0, h):
            #print(matriz[x][y], end="")
        #print("")








