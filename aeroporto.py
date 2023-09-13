from aviao import Aviao

class Aeroporto:
    def __init__(self):
        self.fila_decolagem = []

    def decolar_proximo_aviao(self):
        if not self.fila_decolagem:
            print("Não há aviões na fila de decolagem.")
            return None

        aviao = self.fila_decolagem[0]
        self.mostrar_aviao(aviao)
        confirmacao = input("Confirmar a decolagem deste avião? (S/N) ").strip().lower()

        if confirmacao == "s":
            self.fila_decolagem.pop(0)
            print(f"O avião com destino à {aviao.destino} decolou.")
            return aviao  # Retorna o avião decolado
        else:
            print(f"Decolagem do avião do Voo {aviao.num_voo} foi cancelada.")
            return None  # Retorna None se a decolagem for cancelada

            
               
        
    def add_aviao_fila(self, modelo=None, empresa_aerea=None, origem=None, destino=None, qtd_passageiros=None):
        # Se informações completas do avião foram fornecidas, crie o avião diretamente
        if modelo and empresa_aerea and origem and destino and qtd_passageiros is not None:
            novo_numero_voo = self.gerar_numero_voo()
            aviao = Aviao(modelo, empresa_aerea, origem, destino, qtd_passageiros, novo_numero_voo)
            print(f"Avião cadastrado e adicionado à fila")
            self.fila_decolagem.append(aviao)
        else:
            # Verifique se todos os campos obrigatórios foram preenchidos
            while True:
                modelo = input("Modelo do avião: ")
                empresa_aerea = input("Empresa Aérea: ")
                origem = input("Origem: ")
                destino = input("Destino: ")
                qtd_passageiros = input("Quantidade de Passageiros: ")
                try:
                    qtd_passageiros = int(qtd_passageiros)
                except ValueError:
                    print("Erro: A quantidade de passageiros deve ser um número inteiro.")
                    continue  # Pede novamente os dados se a quantidade de passageiros não for um número

                if not modelo or not empresa_aerea or not origem or not destino or qtd_passageiros is None:
                    print("Erro: Todos os campos (modelo, empresa aérea, origem, destino, quantidade de passageiros) devem ser preenchidos.")
                    continue  # Pede novamente os dados se algum campo estiver ausente
                else:
                    novo_numero_voo = self.gerar_numero_voo()
                    aviao = Aviao(modelo, empresa_aerea, origem, destino, qtd_passageiros, novo_numero_voo)
                    print(f"Avião cadastrado e adicionado à fila")
                    self.fila_decolagem.append(aviao)
                    break  # Sai do loop se todos os campos estiverem preenchidos corretamente


    def total_avioes_na_fila(self):
        return len(self.fila_decolagem)
    
    def listar_fila_de_decolagem(self):
        quantidade = 10
        if not self.fila_decolagem:
            print(" Não há aviões na fila de decolagem ")
            return
         
        fila_organizada = sorted(self.fila_decolagem, key=lambda aviao: aviao.num_voo)

        print(f"Os próximos voos são: ")
        for i, aviao in enumerate(fila_organizada[:quantidade]):
            print (f"Posição {i+1}: Voo {aviao.num_voo} - {aviao.modelo}, {aviao.empresa_aerea}")

    def mostrar_aviao(self, aviao):
        print(f"Características do avião:\n"
              f"Voo {aviao.num_voo}\n"
              f"Modelo: {aviao.modelo}\n"
              f"Empresa Aérea: {aviao.empresa_aerea}\n"
              f"Origem: {aviao.origem}\n"
              f"Destino: {aviao.destino}\n"
              f"Quantidade de Passageiros: {aviao.qtd_passageiros}")

    def interacao_operador(self):
        while True:
            print("\nOpções:")
            print("1. Listar fila de decolagem")
            print("2. Adicionar um avião à fila de decolagem")
            print("3. Decolar o próximo avião")
            print("4. Sair")
            escolha = input("Escolha uma opção: ")

            if escolha == "1":
                self.listar_fila_de_decolagem()
            elif escolha == "2":
                self.add_aviao_fila()               
            elif escolha == "3":
                self.decolar_proximo_aviao()
            elif escolha == "4":
                break
            else:
                print("Opção inválida. Tente novamente.")

    def gerar_numero_voo(self):
        if self.fila_decolagem:
            fila_organizada = sorted(self.fila_decolagem, key=lambda aviao: aviao.num_voo)
            ultimo_aviao = fila_organizada[-1]
            novo_numero_voo = ultimo_aviao.num_voo + 1
        else:
            novo_numero_voo = 1

        return novo_numero_voo

if __name__ == "__main__":
    aeroporto = Aeroporto()
    aeroporto.interacao_operador()
        