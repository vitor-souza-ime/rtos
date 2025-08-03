# RTOS - Controle de LEDs com FreeRTOS

Este projeto demonstra o uso de tarefas em um sistema operacional de tempo real (RTOS), utilizando o FreeRTOS para controle independente de três LEDs com diferentes prioridades e tempos de piscar.

## 📁 Estrutura do Projeto

```

rtos/
├── main.py
└── README.md

````

> **Nota:** Embora o nome do arquivo seja `main.py`, o código está em C++ para plataformas como ESP32/ESP-IDF ou Arduino com suporte ao FreeRTOS. Renomeie para `main.cpp` ou `main.c` conforme o seu ambiente de desenvolvimento.

## 🚦 Descrição

Cada LED (vermelho, amarelo e verde) é controlado por uma *task* com prioridade e intervalo de piscar distintos. As tarefas são executadas concorrentemente utilizando o agendador do FreeRTOS.

| Cor do LED | GPIO       | Tempo de Piscar | Prioridade da Task |
|------------|------------|------------------|---------------------|
| Verde      | GPIO_NUM_7 | 300 ms           | 3 (mais alta)       |
| Amarelo    | GPIO_NUM_6 | 1000 ms          | 2                   |
| Vermelho   | GPIO_NUM_5 | 2000 ms          | 1 (mais baixa)      |

## ⚙️ Instalação

1. Clone este repositório:

   ```bash
   git clone https://github.com/vitor-souza-ime/rtos.git
   cd rtos
````

2. Renomeie `main.py` para `main.cpp` (ou `main.c`, conforme seu ambiente).

3. Compile e envie para sua placa ESP32 utilizando Arduino IDE, PlatformIO ou ESP-IDF.

## 🧠 Conceitos Utilizados

* FreeRTOS: tarefas, prioridades e delays (`vTaskDelay`)
* Controle de GPIOs com `digitalWrite()` e `digitalRead()`
* Programação concorrente para sistemas embarcados

## 📸 Demonstração

![Demonstração LEDs](https://user-images.githubusercontent.com/placeholder/demo.gif)

> *Adicione aqui um vídeo ou imagem de demonstração se possível.*

## 🛠️ Requisitos

* ESP32 ou placa compatível com FreeRTOS
* IDE com suporte a FreeRTOS (Arduino, ESP-IDF ou PlatformIO)
* Biblioteca FreeRTOS configurada



Se desejar, posso também gerar o GIF ou imagem de demonstração futuramente. Quer que eu adicione um `LICENSE` padrão MIT ao projeto também?
```
