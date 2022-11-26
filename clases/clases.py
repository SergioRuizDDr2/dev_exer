import os
import pprint

pi=3.14

def run():
    while (True):               
        print("""Seleccionar opcion:
        1) Calcular valores
        2) Salir""")
        opcion = int(input())
        if opcion == 1:
            valor=False
            while (True):
                if not valor:
                    valor = int(input("Ingresa valor de radio: "))
                else:
                    print("""Desea cambiar el radio:
                    1) Si
                    2) Multiplicar el radio
                    3) Salir""")
                    opcion1 = int(input())
                    if opcion1 == 1:
                        valor = int(input("Ingresa nuevo radio: "))
                    elif opcion1 == 2:
                        valor1 = int(input("Ingresa valor de n (radio * n): "))
                        if validation(valor1):      
                            valor*=valor1
                        else:
                            os.system("clear")  
                            break
                    else:
                        break
                if validation(valor):
                    print_data(circulo(valor),valor)   
                input("\nPresione tecla para continuar \n")
                os.system("clear")
        elif opcion == 2:
            break
        else:
            print("No existe la opcion \n")
            input("\nPresione tecla para continuar \n")
            os.system("clear")
            
def validation(n):
    if n <= 0:
        print("El valor ingresado esta incorrecto, debe ser mayor a 0")
        input()
        os.system("clear")
    else:
        return True
    
def print_data(data,valor):
    area,perimetro = data
    print("Radio: "+str(valor)+"\n")
    print("Area: "+str(area))
    print("Perimetro: "+str(perimetro))        

def circulo(radio):
    return area(radio),perimetro(radio)

def area(radio):
    return radio*radio*pi

def perimetro(radio):
    return 2*pi*radio

if __name__ == '__main__':
    run()