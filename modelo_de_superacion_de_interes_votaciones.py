votos_de_candidatos = {
    "Doctor Strange": {"votos": 0, "cedulas": []},
    "The Flash": {"votos": 0, "cedulas": []},
    "Iron Man": {"votos": 0, "cedulas": []},
}

while True:

    print("\nSistema de Votación para la Alcaldía")
    print("==========================================")
    print("1. Votar")
    print("2. Ver los votos por cada candidato")
    print("3. Salir del progrma")
    opcion = input("Seleccione un numero: ")

    if opcion == "1":
        while True:
            cedula = input("Ingrese su DNI (número de cédula de identidad): ")
            if not cedula.isdigit() or len(cedula) < 8 or len(cedula) > 12:
                print("El número de DNI debe tener entre 8 y 12 dígitos. Intente nuevamente.")
            else:
                break       
        for candidato, info in votos_de_candidatos.items():
            if cedula in info["cedulas"]:
                print("Intentar emitir varios votos es una violación grave de la integridad electoral y puede tener repercusiones legales")
                break
        else:
            print("Candidatos a la Alcaldía:")
            i = 1
            for candidato in votos_de_candidatos:
                print(f"{i}. {candidato}")
                i += 1
            opcion = int(input("Ingrese el número del candidato a la Alcaldía por el cual desea votar: "))

            # Verificar si el número del candidato es válido
            if opcion >= 1 and opcion <= len(votos_de_candidatos):
                candidato_elegido = list(votos_de_candidatos.keys())[opcion - 1]
                votos_de_candidatos[candidato_elegido]["votos"] += 1
                votos_de_candidatos[candidato_elegido]["cedulas"].append(cedula)
                print("Gracias por su participación 👍🏾🎉")
            else:
                print("Número de candidato no reconocido. Por favor, vuelva a intentar.")
    elif opcion == "2":
        print("Voto total de cada candidato a la Alcaldía:")
        for candidato, info in votos_de_candidatos.items():
            print("========================================")
            print(f"{candidato}: {info['votos']} votos")
            print("Cédulas de los votantes:")
            for cedula in info["cedulas"]:
                print(cedula)
    elif opcion == "3":
        print("Le agradecemos por utilizar nuestro sistema de votación 👍🏾🫡.")
        break
    else:
        print("La opción ingresada no es válida. Por favor, intente de nuevo.")