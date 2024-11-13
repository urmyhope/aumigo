class Cadastropet:
    def __init__(self):
        Listapet = {}
    
    def cadastro(self):
        print("------------------ CADASTRO PET ---------------------")
        print("Faça seu cadastro do seu animalzinho aqui:")
        nome=input("Qual o nome do animalzinho?")
        especie=input("Canino ou Felino?:")
        idade=input("Coloque a idade:")
        procedimento=input("Qual procedimento sera realizado?") 
        tutor=input("Qual o nome do tutor?")
        cpf=int(input("Qual cpf do tutor?"))
        self.registra(nome, especie, idade, procedimento, tutor, cpf)
    
    def registra(self, nome, especie, idade, procedimento, tutor, cpf):
        self.Listapet.apend({nome: {"Nome":nome,
                                    "Especie":especie,
                                    "idade":idade,
                                    "procedimento":procedimento,
                                    "tutor":tutor,
                                    "cpf":cpf}})
