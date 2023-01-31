# uma estrutura paracida com o "switch" de outras linguagem de programação

lang = input("Mês do ano: ")

match lang:
    case "1":
        print("Janeiro")
    case "2":
        print("Fevereiro")
    case "3":
        print("Março")
    case _:  # default se não entrar em nenhum dos anteriores
        print("Abril ou posterior")