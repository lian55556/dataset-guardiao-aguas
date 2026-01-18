# Guardião das Águas: Dataset de Monitoramento Hídrico

Este repositório contém os dados e scripts complementares ao artigo científico:
> **"Guardião das Águas: Monitoramento Autônomo da Qualidade Hídrica em Territórios Indígenas via Inteligência Artificial e IoT"**

## Conteúdo do Repositório
* **`dataset_guardiao_aguas.csv`**: Base de dados com 4.320 registros horários (simulação de 6 meses). Contém leituras de pH, Turbidez, OD, Temperatura e Bateria.
* **`gerador_dataset.py`**: Script em Python utilizado para gerar os dados estocásticos e injetar anomalias controladas.

## Metodologia
Os dados foram gerados computacionalmente para validar o modelo LSTM, seguindo estas premissas:
1.  **Calibração:** Baseada em parâmetros históricos da Bacia Amazônica (Fonte: ANA/HidroWeb).
2.  **Cenários de Teste:**
    * *Normalidade:* Oscilação natural dos sensores.
    * *Anomalia Tipo 1:* Contaminação por rejeitos (Picos de Turbidez + Queda de pH).
    * *Anomalia Tipo 2:* Falha de energia/sensor (Queda de tensão da bateria).

## Como Se Apresenta
Este conjunto de dados é parte integrante da pesquisa submetida à Revista Brasileira de Recursos Hídricos (RBRH, 2026).
