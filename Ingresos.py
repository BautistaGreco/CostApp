#ACCESO DE DATOS
#   Toma los datos sobre el ingreso y egreso de divisas ahr. Uy se podria agregar distintas monedas.
#   Los asigna a una variable (i_valorX / i_nombreX) para almacenarlos en una BD. [[[Esto se hace con otra funcion, hay que usar clases y 
#lo otro que manipula las clases, para que en "i_valorX", X se asigne automaticamente y se guarde en la BD.]]]
#   Calcular el valor total de los ingresos. [[[Despues aca hay que linkearlo con el valor de Egresos para sacar la diferencia, 
#deberia ser otro archivo. Aca manejar las clases]]]




print("CoastApp")
print(" ")


#Class ingresos:
nombre_ingreso = input ("Inserte el nombre del ingreso: ")
valor_ingreso = input ("Inserte el valor del ingreso: ")
categoria_ingreso = input ("Seleccione la categoria del ingreso: ")

i_valor1= valor_ingreso 
i_valor2 = valor_ingreso
i_valor3 = valor_ingreso
#En esto hay que hacer la iteracion.
i_nombre1 = nombre_ingreso
i_nombre3 = nombre_ingreso
i_nombre2 = nombre_ingreso
#Categoria


total_ingresos = (i_valor1 + i_valor2 + i_valor3)


#Class egresos:
nombre_egreso = input("Ingrese el nombre del egreso: ")
valor_egreso = input("Ingrese el valor del egreso: ")
categoria_egreso = input("Seleccione la categoria del egreso: ")

e_valor1 = valor_egreso
e_valor2 = valor_egreso
e_valor3 = valor_egreso
#Nombre
#Categoria


total_egresos = (e_valor1 + e_valor2 + e_valor3)



#Balance seria la diferencia entre ingresos y egresos. Cuanto vamos gastando 
#El balance diario se muestra en la tabla siempre al final

balance_diario = (total_ingresos - total_egresos)



#   El presupuesto tiene que haber sido creado antes con los gastos ponderados para la situacion: viaje, mes, semana
#por ejemplo, si tenes un alquiler, pasajes, entradas. Y porque no, estimaods como comida, taxis...


presupuesto = "total_ingresos_presupuesto - total_egresos_presupuesto"

#   Luego hay que dar la relacion entre el presupuesto y el balance, siendo "deficit" para
#balances negativos y "superavit" para balances positivos. Y el valor.

if balance_diario > presupuesto:
    deficit = balance_diario - presupuesto
    print(f"deficit: ", deficit)
else:
    if presupuesto > balance_diario:
        superavit = presupuesto - balance_diario
        print(f"superavit", superavit)


#   Despues esto deberia desarrollarse para que se pueda comparar balance y presupuesto por categorias y por el nombre
#todas variables asignadas cuando se hace el presupuesto y luego seleccionarlas para hacer el balance diario



#   Tambien se podria hacer balance diario sin necesidad de un presupuesto