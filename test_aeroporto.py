from aeroporto import Aeroporto
from aviao import Aviao


def test_add_aviao_fila():
    aeroporto = Aeroporto()

    # Verifique se a fila está vazia inicialmente
    assert aeroporto.total_avioes_na_fila() == 0

    # Adicione um avião à fila diretamente nos testes
    aeroporto.add_aviao_fila("Boeing 747", "Gool", "Recife", "Curitiba", 300)

    # Verifique se a fila agora tem um avião
    assert aeroporto.total_avioes_na_fila() == 1

    # Verifique se o avião foi adicionado corretamente com o número de voo correto
    assert aeroporto.fila_decolagem[0].num_voo == 1

def test_decolar_proximo_aviao():
    aeroporto = Aeroporto()

    aviao1 = Aviao("Boeing 747", "Gool", "Recife", "Curitiba", 300, 123)
    aviao2 = Aviao("Airbus A320", "FlyNow", "São Paulo", "Rio de Janeiro", 250, 456)

    aeroporto.add_aviao_fila(aviao1)
    aeroporto.add_aviao_fila(aviao2)

    aviao_decolado = aeroporto.decolar_proximo_aviao()

    # Verifique se o avião decolado não está mais na fila de decolagem
    assert aviao_decolado not in aeroporto.fila_decolagem

def test_listar_fila_de_decolagem():
    aeroporto = Aeroporto()
    aviao1 = Aviao("Boeing 747", "Gool", "Recife", "Curitiba", 300, 123)
    aviao2 = Aviao("Airbus A320", "FlyNow", "São Paulo",
                   "Rio de Janeiro", 250, 456)

    # Adicione dois aviões à fila
    aeroporto.add_aviao_fila(aviao1)
    aeroporto.add_aviao_fila(aviao2)

    # Liste a fila de decolagem
    aeroporto.listar_fila_de_decolagem()

    # Verifique se os aviões estão listados corretamente
    # O primeiro avião deve ser o aviao1
    assert aeroporto.fila_decolagem[0] == aviao1
    # O segundo avião deve ser o aviao2
    assert aeroporto.fila_decolagem[1] == aviao2


def test_gerar_numero_voo():
    aeroporto = Aeroporto()

    # Adicione dois aviões à fila com informações completas
    aeroporto.add_aviao_fila("Boeing 747", "Gool", "Recife", "Curitiba", 300)
    aeroporto.add_aviao_fila("Airbus A320", "FlyNow", "São Paulo", "Rio de Janeiro", 250)

    # Verifique se o número de voo gerado para o terceiro avião é 3 (após aviao1 e aviao2)
    num_voo = aeroporto.gerar_numero_voo()
    assert num_voo == 3

    # Adicione o terceiro avião à fila com informações completas
    aeroporto.add_aviao_fila("Embraer E190", "SkyJet", "Belo Horizonte", "Brasília", 180)

    # Verifique se o número de voo gerado para o quarto avião é 4
    num_voo = aeroporto.gerar_numero_voo()
    assert num_voo == 4

def test_total_avioes_na_fila():
    aeroporto = Aeroporto()
    aviao1 = Aviao("Boeing 747", "Gool", "Recife", "Curitiba", 300, 123)
    aviao2 = Aviao("Airbus A320", "FlyNow", "São Paulo", "Rio de Janeiro", 250, 456)

    aeroporto.add_aviao_fila(aviao1)
    aeroporto.add_aviao_fila(aviao2)

    assert aeroporto.total_avioes_na_fila() == 2

def test_listar_fila_de_decolagem(capsys):
    aeroporto = Aeroporto()

    # Adicione dois aviões à fila com informações completas
    aeroporto.add_aviao_fila("Boeing 747", "Gool", "Recife", "Curitiba", 300)
    aeroporto.add_aviao_fila("Airbus A320", "FlyNow", "São Paulo", "Rio de Janeiro", 250)

    # Liste a fila de decolagem
    aeroporto.listar_fila_de_decolagem()

    # Capture a saída padrão para verificar as mensagens
    captured = capsys.readouterr()
    assert "Os próximos voos são:" in captured.out
    assert "Posição 1:" in captured.out
    assert "Posição 2:" in captured.out
    assert "Não há aviões na fila de decolagem" not in captured.out  # Verifique se não há mensagem de fila vazia


def test_mostrar_aviao(capsys):
        aeroporto = Aeroporto()
        aviao1 = Aviao("Boeing 747", "Gool", "Recife", "Curitiba", 300, 123)

        # Mostre as características de um avião
        aeroporto.mostrar_aviao(aviao1)

        # Capture a saída padrão para verificar as características
        captured = capsys.readouterr()
        assert "Voo 123" in captured.out
        assert "Modelo: Boeing 747" in captured.out
        assert "Empresa Aérea: Gool" in captured.out

def test_interacao_operador(capsys, mocker):
        aeroporto = Aeroporto()

        # Use o módulo `mocker` para simular a entrada do usuário
        mocker.patch("builtins.input", side_effect=["1", "4"])

        # Execute a interação do operador (opção 1 e depois opção 4 para sair)
        aeroporto.interacao_operador()

        # Capture a saída padrão para verificar as mensagens
        captured = capsys.readouterr()
        assert "Opções:" in captured.out
        assert "1. Listar fila de decolagem" in captured.out
        assert "4. Sair" in captured.out
