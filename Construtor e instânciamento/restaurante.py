class Restaurante:
    def __init__(self, nome, categoria, capacidade, nota_avaliacao, ativo=False):
        self.nome = nome
        self.categoria = categoria
        self.capacidade = capacidade
        self.nota_avaliacao = nota_avaliacao
        self.ativo = ativo

restaurante_exemplo = Restaurante(
    nome='Comida Boa',
    categoria='Gourmet',
    capacidade=50,
    nota_avaliacao=4.5,
    ativo=True
)
