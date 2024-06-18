# Evaluacion Formativa 3

import os

trabajadores = []
cargos = ["CEO", "Desarrollador", "Analista de datos"]


def registrar_trabajador():
    nombre = input("Ingrese el nombre del trabajador: ")
    apellido = input("Ingrese el apellido del trabajador: ")
    cargo = input("Ingrese el cargo del trabajador: ")
    sueldo_bruto = float(input("Ingrese el sueldo bruto del trabajador: "))


    trabajador = ["Trabajador"] (nombre, apellido, cargo, sueldo_bruto)
    trabajadores.append(trabajador)
    print("Trabajador registrado exitosamente.")


def listar_trabajadores():
    if not trabajadores:
        print("No hay trabajadores registrados.")
    else:
        print("Lista de trabajadores:")
        for trabajador in trabajadores:
            print(f"Nombre: {trabajador.nombre} {trabajador.apellido}, Cargo: {trabajador.cargo}, Sueldo bruto: {trabajador.sueldo_bruto},
                   Descuento salud: {trabajador.descuento_salud}, Descuento AFP: {trabajador.descuento_afp}, 
                   Líquido a pagar: {trabajador.liquido_pagar}")


def imprimir_planilla_sueldos():
    opcion = input("Seleccione una opción:\n1. Imprimir planilla de todos los cargos\n2. Imprimir planilla por cargo\n")


    if opcion == "1":
        with open("planilla_sueldos.txt", "w") as archivo:
            archivo.write("Planilla de sueldos:\n")
            for trabajador in trabajadores:
                archivo.write(f"Nombre: {trabajador.nombre} {trabajador.apellido}, Cargo: {trabajador.cargo},
                               Sueldo bruto: {trabajador.sueldo_bruto}, Descuento salud: {trabajador.descuento_salud}, 
                               Descuento AFP: {trabajador.descuento_afp}, Líquido a pagar: {trabajador.liquido_pagar}\n")
        print("Planilla de sueldos generada exitosamente.")


    elif opcion == "2":
        cargo_seleccionado = input(f"Ingrese el cargo ({', '.join(cargos)}): ")
        if cargo_seleccionado in cargos:
            with open(f"planilla_sueldos_{cargo_seleccionado}.txt", "w") as archivo:
                archivo.write(f"Planilla de sueldos para el cargo {cargo_seleccionado}:\n")
                for trabajador in trabajadores:
                    if trabajador.cargo == cargo_seleccionado:
                        archivo.write(f"Nombre: {trabajador.nombre} {trabajador.apellido}, Cargo: {trabajador.cargo}, 
                                      Sueldo bruto: {trabajador.sueldo_bruto}, Descuento salud: {trabajador.descuento_salud}, 
                                      Descuento AFP: {trabajador.descuento_afp}, Líquido a pagar: {trabajador.liquido_pagar}\n")
            print(f"Planilla de sueldos para el cargo {cargo_seleccionado} generada exitosamente.")
        else:
            print("Cargo no válido.")


    else:
        print("Opción no válida.")


def menu():
    while True:
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
