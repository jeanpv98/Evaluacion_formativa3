# Evaluacion Formativa 3

import os
trabajadores =  []
cargos = ["CEO", "Desarrollador", "Analista de datos"]
def limpiar_consola():
 
 os.system('cls' if os.name == 'nt' else 'clear')


def calcular_descuento_salud(sueldo_bruto):
 return sueldo_bruto *0.07


def calcular_descuento_afp(sueldo_bruto):
 return sueldo_bruto *0.12


def calcular_liquido_pagar(sueldo_bruto, descuento_salud, descuento_afp):
 return sueldo_bruto - descuento_salud - descuento_afp


def registrar_trabajador():
    limpiar_consola()
    nombre = input("Ingrese el nombre del trabajador: ")
    apellido = input("Ingrese el apellido del trabajador: ")
    cargo = input("Ingrese el cargo del trabajador (CEO, Desarrollador, Analista de datos): ")
    while cargo not in cargos:
        print("Cargo no válido. Los cargos válidos son CEO, Desarrollador y Analista de datos.")
        cargo = input("Ingrese el cargo del trabajador: ")
    sueldo_bruto = float(input("Ingrese el sueldo bruto del trabajador: "))

    descuento_salud = calcular_descuento_salud(sueldo_bruto)
    descuento_afp = calcular_descuento_afp(sueldo_bruto)
    liquido_pagar = calcular_liquido_pagar(sueldo_bruto, descuento_salud, descuento_afp)
   
    trabajador = {
        "nombre": nombre,
        "apellido": apellido,
        "cargo": cargo,
        "sueldo_bruto": sueldo_bruto,
        "descuento_salud": descuento_salud,
        "descuento_afp": descuento_afp,
        "liquido_pagar": liquido_pagar
    }
    trabajadores.append(trabajador)
    print("Trabajador registrado exitosamente.")
    input("Presione Enter para continuar...")


def listar_trabajadores():
    limpiar_consola()
    if not trabajadores:
        print("No hay trabajadores registrados.")
    else:
        print("Lista de trabajadores:")
        for trabajador in trabajadores:
            print(f"Nombre: {trabajador['nombre']} {trabajador['apellido']}, Cargo: {trabajador['cargo']}, Sueldo bruto: {trabajador['sueldo_bruto']}, Descuento salud: {trabajador['descuento_salud']}, Descuento AFP: {trabajador['descuento_afp']}, Líquido a pagar: {trabajador['liquido_pagar']}")
    input("Presione Enter para continuar...")


def imprimir_planilla_sueldos():
    limpiar_consola()
    opcion = input("Seleccione una opción:\n1. Imprimir planilla de todos los cargos\n2. Imprimir planilla por cargo\n")


    if opcion == "1":
        with open("planilla_sueldos.txt", "w") as archivo:
            archivo.write("Planilla de sueldos:\n")
            for trabajador in trabajadores:
                archivo.write(f"Nombre: {trabajador['nombre']} {trabajador['apellido']}, Cargo: {trabajador['cargo']}, Sueldo bruto: {trabajador['sueldo_bruto']}, Descuento salud: {trabajador['descuento_salud']}, Descuento AFP: {trabajador['descuento_afp']}, Líquido a pagar: {trabajador['liquido_pagar']}\n")
        print("Planilla de sueldos generada exitosamente.")


    elif opcion == "2":
        cargo_seleccionado = input(f"Ingrese el cargo ({', '.join(cargos)}): ")
        if cargo_seleccionado in cargos:
            with open(f"planilla_sueldos_{cargo_seleccionado}.txt", "w") as archivo:
                archivo.write(f"Planilla de sueldos para el cargo {cargo_seleccionado}:\n")
                for trabajador in trabajadores:
                    if trabajador['cargo'] == cargo_seleccionado:
                        archivo.write(f"Nombre: {trabajador['nombre']} {trabajador['apellido']}, Cargo: {trabajador['cargo']}, Sueldo bruto: {trabajador['sueldo_bruto']}, Descuento salud: {trabajador['descuento_salud']}, Descuento AFP: {trabajador['descuento_afp']}, Líquido a pagar: {trabajador['liquido_pagar']}\n")
            print(f"Planilla de sueldos para el cargo {cargo_seleccionado} generada exitosamente.")
        else:
           print("Cargo no válido.")


    else:
        print("Opción no válida.")


    input("Presione Enter para continuar...")
def menu():
    while True:
        limpiar_consola()
        print("\nMenú principal:")
        print("1. Registrar trabajador")
        print("2. Listar trabajadores")
        print("3. Imprimir planilla de sueldos")
        print("4. Salir del programa")
        opcion = input("Ingrese una opción: ")


        if opcion == "1":
            registrar_trabajador()
        elif opcion == "2":
            listar_trabajadores()
        elif opcion == "3":
            imprimir_planilla_sueldos()
        elif opcion == "4":
            print("Saliendo del programa...")
            break
        else:
            print("Opción no válida. Intente nuevamente.")
menu()