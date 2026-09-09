nota1 = int(input("Inserte nota 1:"))
nota2 = int(input("Inserte nota 1:"))
nota2 = int(input("Inserte nota 1:"))

promedio = (nota1 + nota2 + nota3) / 3

match promedio:
    case n if n > 7:
        print("promocionado")
    case n if n >= 4:
        print("regular")
    case n: 
            print("Reprobado")