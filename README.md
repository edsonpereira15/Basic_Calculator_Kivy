# 🧮 Basic_Calculator_Kivy

Este projeto é uma calculadora básica desenvolvida em **Python**, utilizando a biblioteca **Kivy** para a criação de uma interface gráfica de usuário (GUI) multiplataforma.

## ✨ Funcionalidades

* Realiza operações aritméticas básicas: soma, subtração, multiplicação e divisão.
* Interface gráfica intuitiva e responsiva.
* Botão 'C' para limpar o visor.

## 🚀 Requisitos de Desenvolvimento

Para configurar o ambiente e desenvolver esta aplicação, os seguintes requisitos são necessários:

### Ambiente de Desenvolvimento

* **Python:** Versão 3.12.x ou superior (recomendado Python 3.13.x, como 3.13.5).
* **Editor de Código:**
    * Visual Studio Code (Microsoft)
    * PyCharm (JetBrains)
* **Ambiente Virtual:** É altamente recomendado criar um ambiente virtual para a aplicação (ex: `python -m venv venv` ou `py -m venv venv`) para isolar as dependências do projeto.
* **Arquivo Principal:** Um arquivo Python principal que conterá a lógica da aplicação (ex: `main.py`).
* **Biblioteca Kivy:** Instale a biblioteca Kivy no seu ambiente virtual.

### Pré-requisitos de Conhecimento

Para entender e modificar o código, é útil ter conhecimentos em:

* **Python Básico:**
    * Lógica de programação com Python.
    * Programação Orientada a Objetos (POO) com Python.
* **Fundamentos do Kivy:**
    * Compreender o paradigma de desenvolvimento do Kivy, que possui sua própria lógica de construção de UI (baseada em widgets, árvore de widgets e sistema de eventos), que se integra à linguagem Python.

## 💡 Por Que Kivy?

A biblioteca Kivy foi escolhida para este projeto pelas seguintes razões:

* **Independência de Conexão:** Não exige conexão com a internet para execução e testes do aplicativo, tornando-o ideal para aplicações offline.
* **Multiplataforma:** Permite exportar a aplicação para diversos sistemas operacionais, utilizando uma única base de código.

### Formatos de Exportação Suportados

* **Windows:** `.exe`
* **macOS:** `.app` ou `.dmg`
* **iOS:** `.ipa`
* **Android:** `.apk`
* **Linux/Unix:**
    * **Executável Autônomo:** Um arquivo executável (sem extensão `.exe`) gerado por ferramentas como `PyInstaller`.
    * **AppImage:** Um formato distribuível que empacota toda a aplicação e suas dependências em um único arquivo, permitindo a execução sem instalação prévia na maioria das distribuições Linux.

## ⚙️ Como Executar

1.  **Clone o repositório:**
    ```bash
    git clone [https://github.com/SeuUsuario/Basic_Calculator_Kivy.git](https://github.com/SeuUsuario/Basic_Calculator_Kivy.git) # Substitua pelo link do seu repositório
    cd Basic_Calculator_Kivy
    ```
2.  **Crie e ative o ambiente virtual:**
    ```bash
    python -m venv venv
    # No Windows:
    .\venv\Scripts\activate
    # No Linux/macOS:
    source venv/bin/activate
    ```
3.  **Instale as dependências:**
    ```bash
    pip install kivy
    ```
4.  **Execute a aplicação:**
    ```bash
    python main.py # Ou o nome do seu arquivo principal, se for diferente
    ```

## 📸 Capturas de Tela (Opcional, mas Altamente Recomendado)

![Captura de tela da calculadora Kivy](caminho/para/sua/imagem.png)
*Substitua `caminho/para/sua/imagem.png` pela localização da sua imagem.*

Este projeto está licenciado sob a Licença MIT. Veja o arquivo [LICENSE](LICENSE) para mais detalhes.
