# Dork Web (Orquestrador OSINT)

Uma ferramenta de linha de comando (CLI) desenvolvida em Python para agilizar operações de inteligência de código aberto (OSINT). O aplicativo gera, formata e executa *Google Dorks* de maneira estruturada, evitando erros de digitação e poupando tempo em investigações.

## 🚀 Funcionalidades Atuais

* **Leitura Dinâmica:** Importa categorias e dorks diretamente de um arquivo `.json` externo, permitindo atualizações na base de dados sem necessidade de alterar o código-fonte.
* **Seleção em Lote:** Capacidade de escolher múltiplos operadores lógicos de uma só vez.
* **Motor de Montagem:** Concatenação inteligente de domínios-alvo, palavras-chave e dorks selecionados.
* **Busca Limpa (No-AI):** Injeção automatizada do parâmetro `&udm=14` na URL para contornar resumos de Inteligência Artificial do Google e retornar resultados puros de web tradicional.
* **Integração de Sistema:** Abertura automática da pesquisa orquestrada diretamente no navegador padrão do sistema operacional.

## 🛠️ Tecnologias Utilizadas
* Python 3.x
* Bibliotecas nativas: `json`, `urllib.parse`, `webbrowser`, `subprocess` 

## ⚙️ Como executar

1. Clone este repositório.
2. Certifique-se de ter o Python instalado em sua máquina.
3. Execute o script principal no terminal:
   ```bash
   python3 main.py
   ```

## 🚧 Próximos Passos (Roadmap)
[*] FEITO: ~~Implementar cópia automática da string gerada para a área de transferência do SO.~~

[ ] Refatorar código em blocos funcionais (Funções).

[ ] Adicionar suporte a interface gráfica no terminal (TUI) para checkboxes interativos.