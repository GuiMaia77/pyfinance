# 📈 Estratégia de Médias Móveis com Ações da Apple (AAPL)

Este projeto implementa uma estratégia de **cruzamento de médias móveis (SMA)** aplicada ao histórico das ações da Apple (AAPL) utilizando Python.

---

## 🧠 Estratégia

A estratégia se baseia no cruzamento de duas médias móveis:
- **SMA50**: Média móvel simples de 50 dias (curto prazo)
- **SMA200**: Média móvel simples de 200 dias (longo prazo)

### Sinais Gerados:
- **Compra (1)**: Quando a SMA50 cruza acima da SMA200
- **Venda (-1)**: Quando a SMA50 cruza abaixo da SMA200

Esses sinais são utilizados para simular uma posição no ativo, e comparar os retornos da estratégia com o mercado.

---

## 📦 Bibliotecas Utilizadas

- `yfinance` – Para obter dados históricos de ações
- `pandas` – Manipulação de dados
- `numpy` – Cálculos numéricos
- `matplotlib` – Visualização gráfica

---

## ▶️ Como Executar

1. Instale os pacotes necessários (se ainda não tiver):

```bash
pip install yfinance pandas numpy matplotlib
```

2. Salve o script como `sma_strategy.py`.
3. Execute no terminal ou ambiente Jupyter:

```bash
python sma_strategy.py
```

---

## 📊 Resultados Apresentados

- **Gráfico de preço da ação com as médias móveis**
- **Gráfico de retorno acumulado do mercado vs estratégia**
- **Retorno total da estratégia vs mercado**

---

## 📈 Exemplo de Saída

```
Total Strategy Return: 150.23%
Total Market Return: 120.87%
```

---

## 🔍 Possíveis Melhorias

- Adicionar taxas de transação
- Incluir backtest com múltiplos ativos
- Testar outros tipos de médias (ex: exponencial)
- Criar interface com Streamlit para visualização interativa

---



Feito por Guilherme Maia
