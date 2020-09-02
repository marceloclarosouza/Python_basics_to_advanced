
def seja_educado(funcao):
    def boas_maneiras():
        print("olá seja bem vindo")
        funcao()
        print("Volte sempre")
    return boas_maneiras

@seja_educado#decorator
def apresentacao():
    print("Muito obrigado pela hospitalidade")
    

apresentacao ()

