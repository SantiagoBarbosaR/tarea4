def imprimir_valores_por_tipo(diccionario):
    
    tipos = {type(valor) for valor in diccionario.values()}
    
    
    for tipo in tipos:
        valores_del_tipo = [valor for valor in diccionario.values() if isinstance(valor, tipo)]
        
        if valores_del_tipo:
            
            valores_ordenados = sorted(valores_del_tipo)
            print(f"Valores de tipo {tipo.__name__}:")
            for valor in valores_ordenados:
                print(valor)


diccionario = {'a': 3,'b': 1.5,'c': 2,'d': 4.2,'e': 'texto'}

imprimir_valores_por_tipo(diccionario)

def verificar_claves_valores(diccionario1, diccionario2):
   
    for clave, valor in diccionario1.items():
        if clave not in diccionario2 or diccionario2[clave] != valor:
            return False
    return True


diccionario1 = {'a': 1, 'b': 2,'c': 3}

diccionario2 = {'a': 1,'b': 2,'c': 3,'d': 4}

diccionario3 = {'a': 1,'b': 3, 'c': 3}

print(verificar_claves_valores(diccionario1, diccionario2)) 
print(verificar_claves_valores(diccionario1, diccionario3))  

def mezclar_diccionarios(a, b):
    mezclar = b.copy()
    mezclar.update(a)
    print(mezclar)


diccionario1 = {'a': "  DICCIONARIOS", 'b': "BIENVENIDO", 'c': "AL"}
diccionario2 = {'b': 3, 'c':20,'d': "MEZCALDOR", 'e':"DE"}
resultado = mezclar_diccionarios(diccionario1, diccionario2)





def filtrar_por_rango_edad(personas):
    filtro = {}
    min = 15
    max = 30

    for persona in personas:
        nombre, apellido, edad = persona
        
        if min <= edad <= max:
            filtro[f"{nombre} {apellido}"] = edad

    for nombre_completo, edad in filtro.items():
        print(f"{nombre_completo}: {edad} años")
#grupo3 es mi grupo de proyecto :v
grupo3 = [("MAYCOL", "FIGUEROA", 20),("HECTOR", "PATIÑO", 30),("MGUEL", "PANA", 22),("SANTIAGO", "BARBOSA", 35)]

filtrar_por_rango_edad(grupo3)