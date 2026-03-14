# 🪓 Vinland Rush

> Meu primeiro projeto em Python — desenvolvido como trabalho acadêmico para a faculdade.

**Vinland Rush** é um jogo de endless runner desenvolvido em Python com Pygame, inspirado na era viking. Desvie dos obstáculos, sobreviva o máximo que puder e bata seu próprio recorde!

---

## 🛠️ Tecnologias utilizadas

- **Python 3.14**
- **Pygame** — biblioteca para criação de jogos 2D
- **cx_Freeze** — para geração do executável

---

## ▶️ Como instalar e rodar

### Pré-requisitos

- Python 3.14 instalado → [python.org](https://www.python.org/downloads/)
- pip (geralmente já vem com o Python)

### Instalação

1. Clone ou baixe este repositório:
   ```bash
   git clone https://github.com/m1st3rV/vinland-rush.git
   cd vinland-rush
   ```

2. Crie e ative um ambiente virtual (recomendado):
   ```bash
   python -m venv .venv
   .venv\Scripts\activate   # Windows
   source .venv/bin/activate  # Linux/Mac
   ```

3. Instale as dependências:
   ```bash
   pip install pygame
   ```

4. Rode o jogo:
   ```bash
   python main.py
   ```

### Ou execute diretamente pelo `.exe`

Caso prefira não instalar Python, baixe o executável na seção [Releases](https://github.com/seu-usuario/vinland-rush/releases) e execute o arquivo `VinlandRush.exe`.

---

## 🎮 Como jogar

| Tecla | Ação |
|-------|------|
| `Espaço` ou `↑` | Pular |
| `CTRL` | Atirar |
| `ESC` | Pausar / Sair |

- Desvie dos obstáculos para continuar vivo
- Quanto mais inimigos matar, maior a pontuação. Boa sorte!

---

## 📁 Estrutura do projeto

```
vinland-rush/
├── main.py          # Arquivo principal
├── setup.py         # Configuração do executável
├── icon.ico         # Ícone do jogo
├── code/
│   └── Game.py      # Lógica do jogo
└── assets/          # Imagens e sons
```

---

## 👨‍💻 Autor

Desenvolvido por **Danilo** como projeto da faculdade.  
Primeiro projeto em Python — feito com dedicação e muito café. ☕

---

## 📄 Licença

Este projeto é de uso acadêmico e está disponível livremente para fins educacionais.
