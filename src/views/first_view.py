def introduction_page():
    message = """
        Sistema Cadastral

        * Cadastrar Pessoa - 1
        * Cadastrar Pessoa Por Nome - 2
        * Sair - 3
    """

    print(message)
    command = input("Comando: ")
    
    return command