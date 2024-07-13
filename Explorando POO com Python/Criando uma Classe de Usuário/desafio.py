# Classe UsuarioTelefone
class UsuarioTelefone:
    # Método especial __init__, que é o construtor da classe
    def __init__(self, nome, numero, plano):
        # Atributos da classe, encapsulados dentro da classe
        self.__nome = nome
        self.__numero = numero
        self.__plano = plano

    # Método especial __str__, que retorna uma representação em string do objeto
    def __str__(self):
        return f"Usuário {self.__nome} criado com sucesso."


# Entrada
nome = input()  
numero = input()  
plano = input()  

# Crie um novo objeto UsuarioTelefone com os dados fornecidos
usuario = UsuarioTelefone(nome, numero, plano)

print(usuario)