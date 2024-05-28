import Paciente as pc
import TreeBheap as tr


def mostrar_menu():
    print("\nMenú de Gestión de Pacientes de Urgencias")
    print("1. Registrar nuevo paciente")
    print("2. Consultar próximo paciente a atención")
    print("3. Atender al siguiente paciente")
    print("4. Ver todos los pacientes en espera")
    print("5. Ver pacientes en espera por nivel de triaje")
    print("6. Eliminar un paciente")
    print("7. Salir")


def main():
    cola = tr.ColaHospital()
    
    while True:
        mostrar_menu()
        opcion = input("\n\n\nSeleccione una opción: ")
        
        if opcion == '1':

            while True:
                num = input("Número de paciente: ")
                if num.isdigit():
                    nuevonumero = int(num)
                    break
                else:
                    print("Ingrese un número por favor")

            genero = input("Género del paciente: ")
            nombre = input("Nombre del paciente: ")

            while True:
                edad = input("Edad del paciente: ")
                if edad.isdigit():
                    nuevaedad = int(edad)
                    break
                else:
                    print("Ingrese un número por favor")

            while True:
                triaje = input("Nivel de triaje (1-5): ")
                if triaje.isdigit() and 0 < int(triaje) <= 5:
                    nuevotriaje = int(triaje)
                    break
                else:
                    print("Ingrese un número entre 1 y 5 por favor")
            paciente = pc.Paciente(nuevonumero, genero, nombre, nuevaedad, nuevotriaje)
            cola.registrar_paciente(paciente)
            print("Paciente registrado exitosamente.\n\n\n")
            
        
        elif opcion == '2':
            paciente = cola.consultar_proximo_paciente()
            if paciente:
                print("Próximo paciente a ser atendido:", paciente)
            else:
                print("No hay pacientes en espera.")
        
        elif opcion == '3':
            paciente = cola.atender_siguiente()
            if paciente:
                print("Atendiendo a:", paciente)
            else:
                print("No hay pacientes en espera.")
        
        elif opcion == '4':
            pacientes = cola.consultar_pacientes_en_espera()
            if pacientes:
                for p in pacientes:
                    print(p)
                cola.printT(cola.root)
            else:
                print("No hay pacientes en espera.")
        
        elif opcion == '5':
            nivel = int(input("Ingrese el nivel de triaje a consultar (1-5): "))
            pacientes = cola.consultar_pacientes_por_triaje(nivel)
            if pacientes:
                for p in pacientes:
                    print(p)
            else:
                print(f"No hay pacientes en espera con triaje {nivel}.")
        
        elif opcion == '6':
            identificador = input("Ingrese el número de paciente: ")
            if identificador:
                identificador = int(identificador)
                cola.eliminar_paciente(identificador)
                print(f"Paciente con ID {identificador} eliminado.")
            else:
                print("Número de paciente no proporcionado.")
        
        elif opcion == '7':
            
            print("Saliendo del programa.")
            break
        
        else:
            print("Opción no válida, intente de nuevo.")


if __name__ == "__main__":
    main()
