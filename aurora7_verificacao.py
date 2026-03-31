"""
============================================================
MISSÃO AURORA-7 — SISTEMA DE VERIFICAÇÃO PRÉ-LANÇAMENTO
Atividade Integradora — Análise de Telemetria Espacial
============================================================
"""

# ─────────────────────────────────────────────
# 1 ,. ORGANIZAÇÃO E DESCRIÇÃO DA TELEMETRIA
# ─────────────────────────────────────────────

def obter_dados_telemetria() -> dict:
    """
    Simula a leitura dos dados de telemetria da espaçonave.
    Em um sistema real, estes dados viriam de sensores físicos.

    Retorna:
        dict: dicionário com todos os dados de telemetria
    """
    dados = {
        # Temperatura interna do compartimento (°C)
        "temperatura_interna": 22.0,

        # Temperatura externa (ambiente / órbita) (°C)
        "temperatura_externa": -18.0,

        # Integridade estrutural: 1 = OK, 0 = FALHA
        "integridade_estrutural": 1,

        # Nível de energia das baterias (%)
        "nivel_energia": 87.0,

        # Pressão dos tanques de combustível (bar)
        "pressao_tanques": 220.0,

        # Status dos módulos críticos: True = ativo, False = falha
        "modulos": {
            "propulsao":     True,
            "navegacao":     True,
            "comunicacao":   True,
            "suporte_vida":  True,
            "controle":      True,
        }
    }
    return dados


# ─────────────────────────────────────────────
# 2. FAIXAS SEGURAS (parâmetros de referência)
# ─────────────────────────────────────────────

LIMITES = {
    "temperatura_interna": {"min": -10.0,  "max": 80.0},
    "temperatura_externa": {"min": -55.0,  "max": 40.0},
    "nivel_energia":       {"min": 70.0,   "max": 100.0},
    "pressao_tanques":     {"min": 150.0,  "max": 300.0},
}

MODULOS_CRITICOS = ["propulsao", "navegacao", "comunicacao"]

# ─────────────────────────────────────────────
# 3. ALGORITMO DE VERIFICAÇÃO
# ─────────────────────────────────────────────

def verificar_parametro(nome: str, valor: float) -> tuple[bool, str]:
    """
    Verifica se um parâmetro está dentro da faixa segura.

    Args:
        nome:  chave do parâmetro (deve existir em LIMITES)
        valor: valor medido pelo sensor

    Returns:
        (bool, str): (aprovado, mensagem de status)
    """
    limites = LIMITES[nome]
    aprovado = limites["min"] <= valor <= limites["max"]
    status = "OK" if aprovado else "FALHA"
    msg = (
        f"[{status}] {nome.replace('_', ' ').capitalize()}: "
        f"{valor} "
        f"(faixa segura: {limites['min']} – {limites['max']})"
    )
    return aprovado, msg


def verificar_integridade_estrutural(valor: int) -> tuple[bool, str]:
    """Verifica se a integridade estrutural está OK (valor deve ser 1)."""
    aprovado = valor == 1
    status = "OK" if aprovado else "FALHA"
    return aprovado, f"[{status}] Integridade estrutural: {'APROVADA' if aprovado else 'COMPROMETIDA'}"


def verificar_modulos(modulos: dict) -> tuple[bool, str]:
    """
    Verifica se todos os módulos críticos estão ativos.

    Args:
        modulos: dict com nome do módulo → True/False

    Returns:
        (bool, str): (todos ativos, mensagem)
    """
    falhas = [m for m in MODULOS_CRITICOS if not modulos.get(m, False)]
    aprovado = len(falhas) == 0
    if aprovado:
        return True, "[OK] Módulos críticos: todos ATIVOS"
    else:
        return False, f"[FALHA] Módulos críticos com falha: {', '.join(falhas)}"


def executar_verificacao(dados: dict) -> tuple[bool, list[str]]:
    """
    Executa todas as verificações de segurança pré-lançamento.

    Args:
        dados: dicionário de telemetria

    Returns:
        (bool, list[str]): (pronto_para_decolar, lista_de_logs)
    """
    logs = []
    aprovado_geral = True

    print("=" * 55)
    print("  PROTOCOLO DE VERIFICAÇÃO PRÉ-LANÇAMENTO — AURORA-7")
    print("=" * 55)

    # Verificação 1 — Temperatura interna
    ok, msg = verificar_parametro("temperatura_interna", dados["temperatura_interna"])
    aprovado_geral = aprovado_geral and ok
    logs.append(msg)
    print(msg)

    # Verificação 2 — Temperatura externa
    ok, msg = verificar_parametro("temperatura_externa", dados["temperatura_externa"])
    aprovado_geral = aprovado_geral and ok
    logs.append(msg)
    print(msg)

    # Verificação 3 — Nível de energia
    ok, msg = verificar_parametro("nivel_energia", dados["nivel_energia"])
    aprovado_geral = aprovado_geral and ok
    logs.append(msg)
    print(msg)

    # Verificação 4 — Pressão dos tanques
    ok, msg = verificar_parametro("pressao_tanques", dados["pressao_tanques"])
    aprovado_geral = aprovado_geral and ok
    logs.append(msg)
    print(msg)

    # Verificação 5 — Integridade estrutural
    ok, msg = verificar_integridade_estrutural(dados["integridade_estrutural"])
    aprovado_geral = aprovado_geral and ok
    logs.append(msg)
    print(msg)

    # Verificação 6 — Módulos críticos
    ok, msg = verificar_modulos(dados["modulos"])
    aprovado_geral = aprovado_geral and ok
    logs.append(msg)
    print(msg)

    return aprovado_geral, logs


# ─────────────────────────────────────────────
# 4. ANÁLISE ENERGÉTICA
# ─────────────────────────────────────────────

def analisar_energia(nivel_pct: float) -> dict:
    """
    Calcula a autonomia energética para o lançamento.

    Fórmula:
        carga_atual   = capacidade_total × (nivel_pct / 100)
        perdas        = carga_atual × taxa_perda
        reserva       = carga_atual - consumo_decolagem - perdas

    Args:
        nivel_pct: nível de carga atual em porcentagem (0–100)

    Returns:
        dict com todos os valores calculados
    """
    CAPACIDADE_TOTAL_KWH   = 450.0   # capacidade máxima das baterias
    CONSUMO_DECOLAGEM_KWH  = 120.0   # energia consumida no lançamento
    TAXA_PERDA             = 0.05    # 5% de perdas energéticas

    carga_atual    = CAPACIDADE_TOTAL_KWH * (nivel_pct / 100)
    perdas         = carga_atual * TAXA_PERDA
    reserva        = carga_atual - CONSUMO_DECOLAGEM_KWH - perdas
    autonomia_pct  = (reserva / CAPACIDADE_TOTAL_KWH) * 100

    resultado = {
        "capacidade_total_kwh":  CAPACIDADE_TOTAL_KWH,
        "nivel_bateria_pct":     nivel_pct,
        "carga_atual_kwh":       round(carga_atual, 2),
        "consumo_decolagem_kwh": CONSUMO_DECOLAGEM_KWH,
        "perdas_kwh":            round(perdas, 2),
        "reserva_kwh":           round(reserva, 2),
        "autonomia_reserva_pct": round(autonomia_pct, 1),
        "energia_suficiente":    reserva > 0,
    }
    return resultado


def imprimir_analise_energetica(analise: dict) -> None:
    """Imprime o relatório de análise energética formatado."""
    print("\n" + "=" * 55)
    print("  ANÁLISE ENERGÉTICA")
    print("=" * 55)
    print(f"  Capacidade total:          {analise['capacidade_total_kwh']} kWh")
    print(f"  Nível de carga:            {analise['nivel_bateria_pct']}%")
    print(f"  Carga atual:               {analise['carga_atual_kwh']} kWh")
    print(f"  Consumo estimado (decolagem): {analise['consumo_decolagem_kwh']} kWh")
    print(f"  Perdas energéticas (5%):   {analise['perdas_kwh']} kWh")
    print(f"  Reserva pós-decolagem:     {analise['reserva_kwh']} kWh ({analise['autonomia_reserva_pct']}%)")

    if analise["energia_suficiente"]:
        print("  [OK] Energia SUFICIENTE para lançamento seguro.")
    else:
        print("  [FALHA] ENERGIA INSUFICIENTE — lançamento comprometido!")


# ─────────────────────────────────────────────
# 5. ANÁLISE ASSISTIDA POR IA (simulada)
# ─────────────────────────────────────────────

def analise_ia(dados: dict, analise_energia: dict) -> None:
    """
    Simula a análise de IA para classificação, anomalias e riscos.
    Em produção, este módulo enviaria os dados para um modelo de ML.
    """
    print("\n" + "=" * 55)
    print("  ANÁLISE ASSISTIDA POR IA")
    print("=" * 55)

    # Classificação dos dados
    print("\n  [1] Classificação dos dados:")
    ti = dados["temperatura_interna"]
    te = dados["temperatura_externa"]
    en = dados["nivel_energia"]
    pr = dados["pressao_tanques"]

    classe_temp = "NORMAL" if -10 <= ti <= 80 else "CRÍTICA"
    classe_ext  = "NORMAL" if -55 <= te <= 40 else "CRÍTICA"
    classe_en   = "ALTA" if en >= 80 else ("MÉDIA" if en >= 70 else "BAIXA")
    classe_pr   = "NORMAL" if 150 <= pr <= 300 else "FORA DE FAIXA"

    print(f"    Temperatura interna:  {classe_temp}")
    print(f"    Temperatura externa:  {classe_ext}")
    print(f"    Nível de energia:     {classe_en} ({en}%)")
    print(f"    Pressão dos tanques:  {classe_pr} ({pr} bar)")

    # Identificação de anomalias
    print("\n  [2] Possíveis anomalias detectadas:")
    anomalias = []

    if ti > 60:
        anomalias.append("Temperatura interna elevada — risco de superaquecimento dos sistemas eletrônicos.")
    if pr < 180:
        anomalias.append("Pressão dos tanques abaixo do ideal — verificar vedação.")
    if pr > 270:
        anomalias.append("Pressão dos tanques próxima ao limite superior — monitorar.")
    if en < 80:
        anomalias.append("Nível de energia moderado — considerar recarga antes do lançamento.")
    if analise_energia["reserva_kwh"] < 50:
        anomalias.append("Reserva energética baixa pós-decolagem — risco de falha de energia em órbita.")

    if anomalias:
        for a in anomalias:
            print(f"    ⚠ {a}")
    else:
        print("    Nenhuma anomalia crítica detectada nos parâmetros atuais.")

    # Sugestões de risco
    print("\n  [3] Sugestões e avaliação de risco:")
    risco_geral = "BAIXO"
    if len(anomalias) >= 3:
        risco_geral = "ALTO"
    elif len(anomalias) >= 1:
        risco_geral = "MÉDIO"

    print(f"    Nível de risco estimado: {risco_geral}")
    print("    Recomendação: realizar nova leitura dos sensores em T-10 minutos.")
    print("    Manter equipe de solo em alerta durante janela de lançamento.")


# ─────────────────────────────────────────────
# 6. PROGRAMA PRINCIPAL
# ─────────────────────────────────────────────

def main():
    print("\n🚀 SISTEMA DE CONTROLE DE LANÇAMENTO — AURORA-7\n")

    # Leitura dos dados
    dados = obter_dados_telemetria()

    # Execução das verificações
    pronto, logs = executar_verificacao(dados)

    # Análise energética
    analise = analisar_energia(dados["nivel_energia"])
    imprimir_analise_energetica(analise)

    # Verificação final de energia também entra no resultado
    if not analise["energia_suficiente"]:
        pronto = False

    # Análise de IA
    analise_ia(dados, analise)

    # Resultado final
    print("\n" + "=" * 55)
    print("  RESULTADO FINAL")
    print("=" * 55)
    if pronto:
        print("  ✅  PRONTO PARA DECOLAR")
        print("  Todos os sistemas verificados. Lançamento autorizado.")
    else:
        print("  ❌  DECOLAGEM ABORTADA")
        print("  Uma ou mais verificações falharam. Consulte o log acima.")
    print("=" * 55 + "\n")


if __name__ == "__main__":
    main()
