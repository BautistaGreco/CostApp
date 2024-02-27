#Balance seria la diferencia entre ingresos y egresos. Cuanto vamos gastando 
#El balance diario se muestra en la tabla siempre al final

balance_diario = 50



#   El presupuesto tiene que haber sido creado antes con los gastos ponderados para la situacion: viaje, mes, semana
#por ejemplo, si tenes un alquiler, pasajes, entradas. Y porque no, estimaods como comida, taxis...


presupuesto = 200

#   Luego hay que dar la relacion entre el presupuesto y el balance

if balance_diario > presupuesto:
    deficit = balance_diario - presupuesto
    print (f"deficit:", deficit)
else:
    if presupuesto > balance_diario:
        superavit = presupuesto - balance_diario
        print(f"superavit", superavit)