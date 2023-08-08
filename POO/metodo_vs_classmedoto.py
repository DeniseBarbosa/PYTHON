class Conexao:
    def __init__(self, host='localhost'):
        self.host = host
        #(None) é um valor especial que representa a ausência de valor ou a falta de um valor significativo
        self.usuario = None
        self.senha = None
    def set_usuario(self, usuario):
        self.usuario = usuario
    def set_senha(self, senha):
        self.senha = senha
    @classmethod
    def criar_usuario_senha(classe, usuario, senha):
        conexao = classe()
        conexao.usuario = usuario
        conexao.senha = senha
        return conexao
   


# cliente = Conexao()
cliente = Conexao.criar_usuario_senha('Denise', '1234')
# cliente.set_usuario('Denise')
# cliente.set_senha('123')
print(cliente.usuario)
print(cliente.senha)