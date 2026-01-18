# Dataset: Guardião das Águas (Simulação Calibrada)

Este repositório contém o conjunto de dados (dataset) e os algoritmos de geração utilizados no artigo científico:
> **"Guardião das Águas: Monitoramento Autônomo da Qualidade Hídrica em Territórios Indígenas via Inteligência Artificial e IoT"**

## Sobre os Dados
O arquivo `dataset_guardiao_aguas.csv` consiste em uma série temporal de 4.320 registros (simulando 6 meses de coleta horária) contendo parâmetros físico-químicos da água e status de telemetria.

**Estes dados são sintéticos.** Abaixo explicamos a justificativa técnica e a metodologia de calibração utilizada.

---

## Por que utilizamos Dados Sintéticos?
A opção pela geração de dados simulados se deve a três fatores críticos identificados durante a pesquisa:

1.  **Escassez de Rótulos de Desastre:** Embora existam dados hidrológicos históricos (ANA), é extremamente raro encontrar datasets públicos que contenham momentos exatos e rotulados de *contaminação aguda por rejeitos de garimpo* ou *falhas críticas de sensores* em quantidade suficiente para o treinamento supervisionado de Redes Neurais (LSTM).
2.  **Validação de Cenários Extremos:** Para garantir a segurança do sistema antes da implantação física em território indígena, precisávamos testar a IA contra cenários de "pior caso" (contaminação severa e perda total de energia), situações que não ocorrem todo dia na natureza.
3.  **Prova de Conceito (PoC):** O objetivo do estudo é validar a *arquitetura de detecção* da IA. Dados sintéticos bem calibrados permitem isolar variáveis e provar que o algoritmo é capaz de identificar padrões anômalos.

---

## Metodologia de Calibração
Para garantir que a simulação fosse fiel à realidade da Bacia Amazônica, o algoritmo gerador (`gerador_dataset.py`) foi calibrado utilizando parâmetros reais:

* **Fonte de Calibração:** As médias e desvios padrão dos parâmetros "normais" foram definidos com base em séries históricas do **Portal HidroWeb (Agência Nacional de Águas - ANA)** para rios da região Norte (Classe 2 - CONAMA).
* **Comportamento Estocástico:** Aplicamos ruído gaussiano ($\mu=0, \sigma=variável$) para reproduzir a imprecisão natural e a oscilação de leitura de sensores eletrônicos reais.
* **Ciclo de Energia:** A coluna de tensão da bateria simula o ciclo de carga e descarga de um sistema fotovoltaico real (painel solar + bateria LiFePO4), variando conforme a incidência solar diurna/noturna.

### Parâmetros Base (Baseline):
| Sensor | Valor Médio | Referência |
| :--- | :--- | :--- |
| **pH** | 6.8 (±0.15) | Faixa natural de rios amazônicos (Levemente ácidos/Neutros). |
| **Turbidez** | 15 NTU (Base) | Água clara com picos estocásticos de sedimentos. |
| **Temperatura** | 28°C | Clima tropical úmido. |

---

## Cenários Injetados (Anomalias)
O dataset contém três classes de comportamento para classificação pela IA:

* **Classe 0 (Normal):** Oscilação padrão dentro dos limites do CONAMA.
* **Classe 1 (Contaminação):** Simulação de rejeitos de mineração.
    * *Característica:* Aumento abrupto da Turbidez (>100 NTU) e queda do pH (acidificação).
* **Classe 2 (Falha de Hardware):** Simulação de problemas na estação.
    * *Característica:* Queda crítica de tensão da bateria (<10.5V) resultando em leituras nulas ou erráticas dos sensores.

## Como Reproduzir
O script `gerador_dataset.py` incluído neste repositório permite reproduzir exatamente a mesma distribuição estatística dos dados, garantindo a transparência e reprodutibilidade do experimento.

---
**Autores:** [Seu Nome] & [Nome do Orientador]
**Instituição:** UEPA - Universidade do Estado do Pará
