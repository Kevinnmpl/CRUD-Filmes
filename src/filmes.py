class FilmeDuplicadoException(Exception):
    pass

class FilmeInvalidoException(Exception):
    pass


class Filme:
    def __init__(self, titulo: str, nota: float, genero: str):
        if not titulo or titulo.strip() == "":
            raise FilmeInvalidoException("Título não pode ser vazio.")
        if nota < 0 or nota > 10:
            raise FilmeInvalidoException("Nota deve estar entre 0 e 10.")
        if not genero or genero.strip() == "":
            raise FilmeInvalidoException("Gênero não pode ser vazio.")

        self.titulo = titulo
        self.nota = nota
        self.genero = genero


class CatalogoFilmes:
    def __init__(self):
        self.filmes = []

    def adicionar_filme(self, filme: Filme):
        for f in self.filmes:
            if f.titulo.lower() == filme.titulo.lower():
                raise FilmeDuplicadoException("Filme já cadastrado.")
        self.filmes.append(filme)
        return filme

    def listar_filmes(self):
        return self.filmes

    def buscar_por_titulo(self, titulo: str):
        for f in self.filmes:
            if f.titulo.lower() == titulo.lower():
                return f
        return None

    def remover_filme(self, titulo: str):
        filme = self.buscar_por_titulo(titulo)
        if filme:
            self.filmes.remove(filme)
            return True
        return False
