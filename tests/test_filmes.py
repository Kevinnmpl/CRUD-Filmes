import sys
import os
import pytest

sys.path.append(os.path.join(os.path.dirname(__file__), '..', 'src'))

from filmes import (
    Filme,
    CatalogoFilmes,
    FilmeDuplicadoException,
    FilmeInvalidoException
)


def test_criar_filme_valido():
    filme = Filme("KPop Demon Hunters", 9.0, "Animação")
    assert filme.titulo == "KPop Demon Hunters"
    assert filme.nota == 9.0
    assert filme.genero == "Animação"

def test_nao_deve_permitir_titulo_vazio():
    with pytest.raises(FilmeInvalidoException):
        Filme("", 8.0, "Drama")

def test_nao_deve_permitir_nota_invalida():
    with pytest.raises(FilmeInvalidoException):
        Filme("Flow", 11, "Musical")

def test_nao_deve_permitir_nota_negativa():
    with pytest.raises(FilmeInvalidoException):
        Filme("V de Vingança", -1, "Ação")

def test_nao_deve_permitir_genero_vazio():
    with pytest.raises(FilmeInvalidoException):
        Filme("Flow", 8, "")


def test_deve_adicionar_filme_no_catalogo():
    catalogo = CatalogoFilmes()
    filme = Filme("KPop Demon Hunters", 10, "Animação")
    catalogo.adicionar_filme(filme)
    assert len(catalogo.listar_filmes()) == 1

def test_nao_deve_permitir_filme_duplicado():
    catalogo = CatalogoFilmes()
    f1 = Filme("Flow", 8.5, "Musical")
    f2 = Filme("flow", 9.0, "Drama")
    catalogo.adicionar_filme(f1)
    with pytest.raises(FilmeDuplicadoException):
        catalogo.adicionar_filme(f2)

def test_deve_buscar_filme_por_titulo():
    catalogo = CatalogoFilmes()
    filme = Filme("V de Vingança", 9, "Ação")
    catalogo.adicionar_filme(filme)
    resultado = catalogo.buscar_por_titulo("V de Vingança")
    assert resultado.nota == 9

def test_buscar_filme_inexistente_retorna_none():
    catalogo = CatalogoFilmes()
    resultado = catalogo.buscar_por_titulo("FilmeQueNaoExiste")
    assert resultado is None

def test_deve_remover_filme():
    catalogo = CatalogoFilmes()
    filme = Filme("KPop Demon Hunters", 8, "Animação")
    catalogo.adicionar_filme(filme)
    assert catalogo.remover_filme("KPop Demon Hunters") is True
    assert len(catalogo.listar_filmes()) == 0

def test_remover_filme_inexistente_retorna_false():
    catalogo = CatalogoFilmes()
    assert catalogo.remover_filme("FilmeQueNaoExiste") is False
