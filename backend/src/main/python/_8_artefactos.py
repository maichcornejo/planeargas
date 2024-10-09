import os

def submenu_opciones_avanzadas(artefacto):
    while True:
        print("1. Artefacto de cocción")
        print("2. Artefacto de calefacción")
        print("3. Calentador de agua")
        
        opcion = input("Selecciona una opción: ")
        
        if opcion == "1":
            artefacto.append(opcion)
            submenu_coccion(artefacto)
            break
        elif opcion == "2":
            artefacto.append(opcion)
            submenu_calefaccion(artefacto)
            break
        elif opcion == "3":
            artefacto.append(opcion)
            submenu_calentador_agua(artefacto)
            break
        else:
            print("Opción no válida. Inténtalo de nuevo.")

def submenu_coccion(artefacto):
    print("1. Cocina")
    print("2. Horno")
    print("3. Anafe")
    opcion = input("Selecciona una opción: ")
    if opcion in ["1", "2", "3"]:
        artefacto.append(opcion)
        submenu_opciones_direcciones(artefacto)
    else:
        print("Opción no válida. Inténtalo de nuevo.")

def submenu_calefaccion(artefacto):
    print("1. Calefactor TB")
    print("2. Calefactor TBL")
    print("3. Calefactor TBU")
    opcion = input("Selecciona una opción: ")
    if opcion in ["1", "2", "3"]:
        artefacto.append(opcion)
        submenu_opciones_direcciones(artefacto)
    else:
        print("Opción no válida. Inténtalo de nuevo.")

def submenu_calentador_agua(artefacto):
    print("1. Termotanque TN")
    print("2. Calefón TN")
    print("3. Caldera TBF")
    opcion = input("Selecciona una opción: ")
    if opcion in ["1", "2", "3"]:
        artefacto.append(opcion)
        submenu_opciones_direcciones(artefacto)
    else:
        print("Opción no válida. Inténtalo de nuevo.")

def submenu_opciones_direcciones(artefacto):
    while True:
        print("1. Norte")
        print("2. Sur")
        print("3. Este")
        print("4. Oeste")
        opcion = input("Selecciona una opción: ")
        if opcion in ["1", "2", "3", "4"]:
            artefacto.append(opcion)
            submenu_opciones_llaves(artefacto)
            break
        else:
            print("Opción no válida. Inténtalo de nuevo.")

def submenu_opciones_llaves(artefacto):
    while True:
        print("Llave en mano (mirando de frente):")
        print("1. Izquierda")
        print("2. Derecha")
        opcion = input("Selecciona una opción: ")
        if opcion in ["1", "2"]:
            artefacto.append(opcion)
            break
        else:
            print("Opción no válida. Inténtalo de nuevo.")

def menu_principal():

        print("1. Subida o bajada de cañería")
        print("2. ¿Qué artefacto es?")
        
        opcion = input("Selecciona una opción: ")
        
        if opcion == "1":
            numero = float(input("Ingresa cuánto sube o baja la cañería: "))  # Cambiado a input para capturar la entrada del usuario
            return None, numero
        elif opcion == "2":
            artefacto = []
            submenu_opciones_avanzadas(artefacto)  # Llamar al submenú
            return artefacto, None
        else:
            print("Opción no válida. Inténtalo de nuevo.")

# Ejecutar el menú principal
menu_principal()


