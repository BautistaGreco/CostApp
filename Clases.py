nombre_ingreso = input ("Inserte el nombre del ingreso: ")
valor_ingreso = input ("Inserte el valor del ingreso: ")
categoria_ingreso = input ("Seleccione la categoria del ingreso: ")


class Ingresos:
    def __init__(self):
        self.ingresos = []  # Lista para almacenar los valores de ingreso

    def agregar_ingreso(self, nombre, valor, categoria): # Definimos los parametros que va a tener la clase
        self.nombre = nombre_ingreso                    # Asignamos a cada parametro la variable externa 
        self.valor = valor_ingreso
        self.categoria = categoria_ingreso
        
#Chat GTP sugiere hacerlo asi:

    def agregar_ingreso(self, nombre, valor, categoria):
        self.ingresos.append((nombre, float(valor), categoria))  # Agregar el ingreso a la lista

    def total_ingresos(self):
        return sum(ingreso[1] for ingreso in self.ingresos)  # Sumar todos los valores de ingreso


# Crear una instancia de la clase Ingresos
ingresos = Ingresos()

# Luego, puedes agregar los ingresos ingresados por el usuario
nombre_ingreso = input("Inserte el nombre del ingreso: ")
valor_ingreso = input("Inserte el valor del ingreso: ")
categoria_ingreso = input("Seleccione la categoria del ingreso: ")

ingresos.agregar_ingreso(nombre_ingreso, valor_ingreso, categoria_ingreso)

# Para obtener el total de ingresos
total = ingresos.total_ingresos()
print("El total de ingresos es:", total)




#   Ahora hay que hacer metodos dentro de la clase. La iteracion de los valores ¿esto lo hace solo la funcion clase? donde los voy a  
#ir guardando y la suma de todos los valores para dar el total

#    def total_ingresos (valor):  #
#        pass
        






