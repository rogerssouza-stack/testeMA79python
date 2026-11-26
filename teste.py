#Aqui vou desenvolver meu código de teste para revisão.
# ==========================================
# SISTEMA DE CADASTRO DE MOTORES (EM MEMÓRIA)
# ==========================================

# Array (lista) principal que armazenará os motores como dicionários
motores = []
proximo_id = 1


def exibir_menu():
    print("\n" + "=" * 40)
    print("       SISTEMA DE CADASTRO DE MOTORES")
    print("=" * 40)
    print("1. Cadastrar novo motor")
    print("2. Listar todos os motores")
    print("3. Buscar motor por ID ou Modelo")
    print("4. Atualizar dados de um motor")
    print("5. Excluir motor")
    print("0. Sair")
    print("=" * 40)


def cadastrar_motor():
    global proximo_id
    print("\n--- NOVO CADASTRO ---")

    modelo = input("Modelo/Referência (ex: W22 IR3): ").strip()
    fabricante = input("Fabricante (ex: WEG, Siemens): ").strip()

    # Validação simples para garantir números
    try:
        potencia_cv = float(input("Potência (CV): "))
        tensao_v = int(input("Tensão Nominal (V) (ex: 220, 380, 440): "))
        rpm = int(input("Rotação (RPM) (ex: 1750, 3500): "))
    except ValueError:
        print(
            "\n[ERRO] Potência, Tensão e RPM devem ser valores numéricos. Cadastro cancelado."
        )
        return

    tipo = (
        input("Tipo (ex: Trifásico, Monofásico, Servo) [Padrão: Trifásico]: ").strip()
        or "Trifásico"
    )

    motor = {
        "id": proximo_id,
        "modelo": modelo,
        "fabricante": fabricante,
        "potencia_cv": potencia_cv,
        "tensao_v": tensao_v,
        "rpm": rpm,
        "tipo": tipo,
    }

    motores.append(motor)
    print(f"\n[SUCESSO] Motor '{modelo}' cadastrado com o ID {proximo_id}!")
    proximo_id += 1


def listar_motores():
    print("\n--- LISTA DE MOTORES CADASTRADOS ---")
    if not motores:
        print("Nenhum motor cadastrado no momento.")
        return

    print(
        f"{'ID':<4} | {'MODELO':<15} | {'FABRICANTE':<12} | {'POT (CV)':<8} | {'TENSÃO':<8} | {'RPM':<6} | {'TIPO'}"
    )
    print("-" * 75)
    for m in motores:
        print(
            f"{m['id']:<4} | {m['modelo']:<15} | {m['fabricante']:<12} | {m['potencia_cv']:<8} | {m['tensao_v']}V{'':<4} | {m['rpm']:<6} | {m['tipo']}"
        )


def buscar_motor():
    print("\n--- BUSCAR MOTOR ---")
    if not motores:
        print("Nenhum motor cadastrado.")
        return

    termo = input("Digite o ID ou parte do nome do Modelo: ").strip().lower()
    encontrados = []

    for m in motores:
        if str(m["id"]) == termo or termo in m["modelo"].lower():
            encontrados.append(m)

    if not encontrados:
        print("Nenhum motor encontrado com esse critério.")
    else:
        print(f"\nForam encontrados {len(encontrados)} registro(s):")
        for m in encontrados:
            print(
                f" -> ID: {m['id']} | Modelo: {m['modelo']} ({m['fabricante']}) - {m['potencia_cv']} CV, {m['tensao_v']}V, {m['rpm']} RPM [{m['tipo']}]"
            )


def atualizar_motor():
    print("\n--- ATUALIZAR MOTOR ---")
    listar_motores()
    if not motores:
        return

    try:
        id_busca = int(input("\nDigite o ID do motor que deseja atualizar: "))
    except ValueError:
        print("[ERRO] ID inválido.")
        return

    for m in motores:
        if m["id"] == id_busca:
            print(
                f"\nEditando ID {m['id']} ({m['modelo']}). Pressione ENTER para manter o valor atual."
            )

            novo_modelo = input(f"Modelo [{m['modelo']}]: ").strip()
            if novo_modelo:
                m["modelo"] = novo_modelo

            novo_fab = input(f"Fabricante [{m['fabricante']}]: ").strip()
            if novo_fab:
                m["fabricante"] = novo_fab

            nova_pot = input(f"Potência CV [{m['potencia_cv']}]: ").strip()
            if nova_pot:
                try:
                    m["potencia_cv"] = float(nova_pot)
                except ValueError:
                    print("Valor inválido para potência, mantendo o anterior.")

            nova_tensao = input(f"Tensão V [{m['tensao_v']}]: ").strip()
            if nova_tensao:
                try:
                    m["tensao_v"] = int(nova_tensao)
                except ValueError:
                    print("Valor inválido para tensão, mantendo o anterior.")

            novo_rpm = input(f"RPM [{m['rpm']}]: ").strip()
            if novo_rpm:
                try:
                    m["rpm"] = int(novo_rpm)
                except ValueError:
                    print("Valor inválido para RPM, mantendo o anterior.")

            novo_tipo = input(f"Tipo [{m['tipo']}]: ").strip()
            if novo_tipo:
                m["tipo"] = novo_tipo

            print("\n[SUCESSO] Dados do motor atualizados!")
            return

    print(f"[ERRO] Motor com ID {id_busca} não encontrado.")


def excluir_motor():
    print("\n--- EXCLUIR MOTOR ---")
    listar_motores()
    if not motores:
        return

    try:
        id_busca = int(input("\nDigite o ID do motor que deseja excluir: "))
    except ValueError:
        print("[ERRO] ID inválido.")
        return

    for i, m in enumerate(motores):
        if m["id"] == id_busca:
            confirmacao = (
                input(f"Tem certeza que deseja excluir o motor '{m['modelo']}'? (s/n): ")
                .strip()
                .lower()
            )
            if confirmacao == "s":
                motores.pop(i)
                print("[SUCESSO] Motor removido do sistema.")
            else:
                print("Operação cancelada.")
            return

    print(f"[ERRO] Motor com ID {id_busca} não encontrado.")


def popular_dados_teste():
    """Adiciona alguns motores iniciais para facilitar os testes"""
    global proximo_id
    dados_iniciais = [
        {
            "modelo": "W22 IR3 Premium",
            "fabricante": "WEG",
            "potencia_cv": 5.0,
            "tensao_v": 380,
            "rpm": 1750,
            "tipo": "Trifásico",
        },
        {
            "modelo": "1LE0",
            "fabricante": "Siemens",
            "potencia_cv": 10.0,
            "tensao_v": 440,
            "rpm": 3500,
            "tipo": "Trifásico",
        },
        {
            "modelo": "W21",
            "fabricante": "WEG",
            "potencia_cv": 1.5,
            "tensao_v": 220,
            "rpm": 1720,
            "tipo": "Monofásico",
        },
    ]
    for d in dados_iniciais:
        d["id"] = proximo_id
        motores.append(d)
        proximo_id += 1


# ==========================================
# LOOP PRINCIPAL DE EXECUÇÃO
# ==========================================
if __name__ == "__main__":
    # Carrega 3 motores de exemplo automaticamente para agilizar seus testes
    popular_dados_teste()

    while True:
        exibir_menu()
        opcao = input("Escolha uma opção: ").strip()

        if opcao == "1":
            cadastrar_motor()
        elif opcao == "2":
            listar_motores()
        elif opcao == "3":
            buscar_motor()
        elif opcao == "4":
            atualizar_motor()
        elif opcao == "5":
            excluir_motor()
        elif opcao == "0":
            print("\nEncerrando o sistema. Até logo!")
            break
        else:
            print("\n[ERRO] Opção inválida. Tente novamente.")