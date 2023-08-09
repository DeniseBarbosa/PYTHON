class Funcionario:
    def __init__(self, nome, cargo, salario):
        self.nome = nome
        self.cargo = cargo
        self.salario = salario

def exibir_informacoes_funcionario(funcionario, atributos=None):
    if atributos is None:
        atributos = vars(funcionario)
    else:
        atributos = {attr: valor for attr, valor in vars(funcionario).items() if attr in atributos}
    
    print("Informações do Funcionário:")
    for attr, valor in atributos.items():
        print(f"{attr.capitalize()}: {valor}")

# Criando um funcionário
funcionario = Funcionario("Alice", "Gerente", 50000)
funcionario2 = Funcionario("Denise", "Desenvolvedora de Software", 10000)

# Mostrando todas as informações do funcionário
# exibir_informacoes_funcionario(funcionario2)

# Mostrando apenas o nome e o cargo do funcionário
exibir_informacoes_funcionario(funcionario2, atributos=["nome", "cargo"])
