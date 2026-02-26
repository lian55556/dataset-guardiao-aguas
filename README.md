# Guardião das Águas - Monitoramento Hídrico com IA e IoT 💧

Este repositório contém o conjunto de dados (dataset), os algoritmos de geração **e a implementação da Inteligência Artificial (Redes Neurais LSTM)** utilizados no artigo científico:
*"Guardião das Águas: Monitoramento Autônomo da Qualidade Hídrica em Territórios Indígenas via Inteligência Artificial e IoT"*

## Estrutura do Repositório
* `gerador_dataset.py`: Script responsável por simular o comportamento hidrológico e injetar anomalias.
* `dataset_guardiao_aguas.csv`: Série temporal de 4.320 registros gerada pelo script.
* `modelo_lstm.py`: Implementação da arquitetura da rede neural profunda (LSTM) utilizando TensorFlow/Keras para a detecção das anomalias. *(Certifique-se de que o nome do arquivo bate com o que você subiu)*

---

## Sobre os Dados
O arquivo `dataset_guardiao_aguas.csv` consiste em uma série temporal de 4.320 registros (simulando 6 meses de coleta horária) contendo parâmetros físico-químicos da água e status de telemetria. Estes dados são sintéticos. Abaixo explicamos a justificativa técnica e a metodologia de calibração utilizada.

### Por que utilizamos Dados Sintéticos?
A opção pela geração de dados simulados se deve a três fatores críticos identificados durante a pesquisa:
1. **Escassez de Rótulos de Desastre:** Embora existam dados hidrológicos históricos (ANA), é extremamente raro encontrar datasets públicos que contenham momentos exatos e rotulados de contaminação aguda por rejeitos de garimpo ou falhas críticas de sensores em quantidade suficiente para o treinamento supervisionado de Redes Neurais.
2. **Validação de Cenários Extremos:** Para garantir a segurança do sistema antes da implantação física em território indígena, precisávamos testar a IA contra cenários de "pior caso" (contaminação severa e perda total de energia), situações que não ocorrem todo dia na natureza.
3. **Prova de Conceito (PoC):** O objetivo do estudo é validar a arquitetura de detecção da IA. Dados sintéticos bem calibrados permitem isolar variáveis e provar que o algoritmo é capaz de identificar padrões anômalos.

### Metodologia de Calibração
Para garantir que a simulação fosse fiel à realidade da Bacia Amazônica, o algoritmo gerador (`gerador_dataset.py`) foi calibrado utilizando parâmetros reais:
* **Fonte de Calibração:** As médias e desvios padrão dos parâmetros "normais" foram definidos com base em séries históricas do Portal HidroWeb (Agência Nacional de Águas - ANA) para rios da região Norte (Classe 2 - CONAMA).
* **Comportamento Estocástico:** Aplicamos ruído gaussiano (μ=0, σ=variável) para reproduzir a imprecisão natural e a oscilação de leitura de sensores eletrônicos reais.
* **Ciclo de Energia:** A coluna de tensão da bateria simula o ciclo de carga e descarga de um sistema fotovoltaico real (painel solar + bateria LiFePO4), variando conforme a incidência solar diurna/noturna.

**Parâmetros Base (Baseline):**
* **pH:** 6.8 (±0.15) - Faixa natural de rios amazônicos (Levemente ácidos/Neutros).
* **Turbidez:** 15 NTU (Base) - Água clara com picos estocásticos de sedimentos.
* **Temperatura:** 28°C - Clima tropical úmido.

### Cenários Injetados (Anomalias)
O dataset contém três classes de comportamento para classificação pela IA:
* **Classe 0 (Normal):** Oscilação padrão dentro dos limites do CONAMA.
* **Classe 1 (Contaminação):** Simulação de rejeitos de mineração. *Característica:* Aumento abrupto da Turbidez (>100 NTU) e queda do pH (acidificação).
* **Classe 2 (Falha de Hardware):** Simulação de problemas na estação. *Característica:* Queda crítica de tensão da bateria (<10.5V) resultando em leituras nulas ou erráticas dos sensores.

---

## O Modelo de Inteligência Artificial (LSTM)
O script `modelo_lstm.py` contém a arquitetura da rede neural encarregada de processar essas séries temporais. Construído em TensorFlow/Keras, o modelo é capaz de aprender o padrão "Normal" do rio e emitir alertas preditivos ao identificar a correlação inversa entre pH e Turbidez (Contaminação) ou ao detectar a quebra do limiar de segurança da bateria (acionando o modo *Deep Sleep*).

---

## Como Reproduzir
1. Execute o script `gerador_dataset.py` para criar o dataset sintético e reproduzir exatamente a mesma distribuição estatística do experimento original.
2. Execute o script `modelo_lstm.py` para treinar a rede neural com os dados gerados e visualizar as métricas de precisão e a perda (*loss*).

**Tecnologias Utilizadas:** Python, Pandas, NumPy, TensorFlow/Keras.

---
**Autores:** Thalisson Lian Gomes Oliveira & Prof. Hugo  
**Instituição:** UEPA Campus XV - Universidade do Estado do Pará
