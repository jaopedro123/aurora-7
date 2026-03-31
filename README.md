# 🚀 AURORA-7 — Sistema de Verificação Pré-Lançamento

> **Atividade Integradora — Análise de Telemetria Espacial**  
> Disciplina: Lógica de Programação / Fundamentos de Python

---

## 📋 Descrição do Projeto

O **Aurora-7** é um sistema simulado de verificação pré-lançamento de uma espaçonave, desenvolvido como atividade integradora acadêmica. O programa lê dados de telemetria (temperatura, energia, pressão, integridade estrutural e status de módulos), executa verificações de segurança automatizadas, analisa a autonomia energética e gera um relatório com análise assistida por IA simulada.

O sistema determina ao final se a espaçonave está **pronta para decolar** ou se o **lançamento deve ser abortado**.

---

## 🗂️ Estrutura do Projeto

```
aurora-7/
│
├── aurora7_verificacao.py   # Código principal do sistema
└── README.md                # Documentação do projeto
```

---

## ⚙️ Funcionalidades

| Módulo | Descrição |
|---|---|
| **Telemetria** | Leitura simulada de sensores (temperatura, energia, pressão, módulos) |
| **Verificação de Parâmetros** | Checagem de cada sensor contra faixas seguras pré-definidas |
| **Integridade Estrutural** | Validação do status estrutural da espaçonave |
| **Módulos Críticos** | Verificação de propulsão, navegação e comunicação |
| **Análise Energética** | Cálculo de carga, perdas e reserva pós-decolagem |
| **Análise de IA (simulada)** | Classificação de dados, detecção de anomalias e avaliação de risco |
| **Resultado Final** | Decisão de lançamento: ✅ AUTORIZADO ou ❌ ABORTADO |

---

## 🌡️ Parâmetros de Telemetria e Faixas Seguras

| Parâmetro | Mínimo | Máximo | Unidade |
|---|---|---|---|
| Temperatura Interna | −10.0 | 80.0 | °C |
| Temperatura Externa | −55.0 | 40.0 | °C |
| Nível de Energia | 70.0 | 100.0 | % |
| Pressão dos Tanques | 150.0 | 300.0 | bar |

**Módulos críticos verificados:** `propulsão`, `navegação`, `comunicação`

---

## 🔋 Fórmula de Análise Energética

```
carga_atual  = capacidade_total × (nível_pct / 100)
perdas       = carga_atual × 0.05              (5% de perdas)
reserva      = carga_atual − consumo_decolagem − perdas
autonomia    = (reserva / capacidade_total) × 100
```

**Constantes utilizadas:**
- Capacidade total das baterias: **450 kWh**
- Consumo estimado no lançamento: **120 kWh**
- Taxa de perdas energéticas: **5%**

---

## ▶️ Instruções de Execução

### Pré-requisitos

- **Python 3.10** ou superior  
  *(uso de `tuple[bool, str]` como type hint nativo requer Python 3.10+)*

Verifique sua versão com:

```bash
python --version
```

### Como rodar

```bash
# Clone ou baixe o repositório e acesse a pasta
cd aurora-7

# Execute o script principal
python aurora7_verificacao.py
```

Nenhuma biblioteca externa é necessária — o projeto utiliza apenas a biblioteca padrão do Python.

---

## 🖥️ Print da Execução

Saída real gerada pelo sistema com os dados de telemetria padrão:

```
🚀 SISTEMA DE CONTROLE DE LANÇAMENTO — AURORA-7

=======================================================
  PROTOCOLO DE VERIFICAÇÃO PRÉ-LANÇAMENTO — AURORA-7
=======================================================
[OK] Temperatura interna: 22.0 (faixa segura: -10.0 – 80.0)
[OK] Temperatura externa: -18.0 (faixa segura: -55.0 – 40.0)
[OK] Nivel energia: 87.0 (faixa segura: 70.0 – 100.0)
[OK] Pressao tanques: 220.0 (faixa segura: 150.0 – 300.0)
[OK] Integridade estrutural: APROVADA
[OK] Módulos críticos: todos ATIVOS

=======================================================
  ANÁLISE ENERGÉTICA
=======================================================
  Capacidade total:             450.0 kWh
  Nível de carga:               87.0%
  Carga atual:                  391.5 kWh
  Consumo estimado (decolagem): 120.0 kWh
  Perdas energéticas (5%):      19.58 kWh
  Reserva pós-decolagem:        251.93 kWh (56.0%)
  [OK] Energia SUFICIENTE para lançamento seguro.

=======================================================
  ANÁLISE ASSISTIDA POR IA
=======================================================

  [1] Classificação dos dados:
    Temperatura interna:  NORMAL
    Temperatura externa:  NORMAL
    Nível de energia:     ALTA (87.0%)
    Pressão dos tanques:  NORMAL (220.0 bar)

  [2] Possíveis anomalias detectadas:
    Nenhuma anomalia crítica detectada nos parâmetros atuais.

  [3] Sugestões e avaliação de risco:
    Nível de risco estimado: BAIXO
    Recomendação: realizar nova leitura dos sensores em T-10 minutos.
    Manter equipe de solo em alerta durante janela de lançamento.

=======================================================
  RESULTADO FINAL
=======================================================
  ✅  PRONTO PARA DECOLAR
  Todos os sistemas verificados. Lançamento autorizado.
=======================================================
```

---

## 🧪 Como Simular Falhas

Para testar o comportamento do sistema em cenários de falha, edite os valores dentro da função `obter_dados_telemetria()`:

```python
# Simular nível de energia crítico
"nivel_energia": 60.0,          # abaixo do mínimo de 70%

# Simular falha de módulo crítico
"modulos": {
    "propulsao": False,          # módulo com falha
    ...
}

# Simular temperatura interna fora da faixa
"temperatura_interna": 95.0,    # acima do máximo de 80°C
```

---

## 📐 Conceitos de Programação Aplicados

- **Funções com type hints** e docstrings detalhadas
- **Dicionários aninhados** para estruturação de dados de telemetria
- **Funções puras** com retorno de tuplas `(bool, str)`
- **List comprehensions** para filtragem de módulos com falha
- **Constantes** organizadas em dicionários (`LIMITES`, `MODULOS_CRITICOS`)
- **Separação de responsabilidades** (leitura, verificação, análise, saída)
- **Fluxo de controle** com acumulação de resultado booleano

---

## 👨‍💻 Autor - João Pedro

Desenvolvido como atividade acadêmica integradora.  
Curso: **[Ciência da Computação]** — **[FIAP]**  
Período: **[2026/ 1º (semestre/fase)]**

---

> *"A segurança de uma missão começa muito antes do lançamento."*
