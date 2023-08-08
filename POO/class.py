class Pessoa:
    def __init__(esse, nome, sobrenome):
        esse.nome = nome
        esse.sobrenome = sobrenome

p1 = Pessoa('Denise', 'Pereira')

# print(p1.nome, p1.sobrenome)

class Pet:
  def __init__(self, nome ='Dog'):
     self.nome = nome

  def comportamentos(self):
        comportamento = f'{self.nome} gosta de latir'
        return comportamento
        

# pets = Pet()
# print(pets.nome)
print(Pet().comportamentos())