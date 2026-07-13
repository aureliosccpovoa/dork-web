# 🌐 Dork Web (Orquestrador OSINT)
```text
 ██████╗  ██████╗ ██████╗ ██╗  ██╗    ██╗    ██╗███████╗██████╗ 
 ██╔══██╗██╔═══██╗██╔══██╗██║ ██╔╝    ██║    ██║██╔════╝██╔══██╗
 ██║  ██║██║   ██║██████╔╝█████╔╝     ██║ █╗ ██║█████╗  ██████╔╝
 ██║  ██║██║   ██║██╔══██╗██╔═██╗     ██║███╗██║██╔══╝  ██╔══██╗
 ██████╔╝╚██████╔╝██║  ██║██║  ██╗    ╚███╔███╔╝███████╗██████╔╝
 ╚═════╝  ╚═════╝ ╚═╝  ╚═╝╚═╝  ╚═╝     ╚══╝╚══╝ ╚══════╝╚═════╝ 
```
Ferramenta de linha de comando (CLI) desenvolvida em Python para agilizar operações de inteligência de código aberto (OSINT). O aplicativo gera, formata e executa *Google Dorks* de maneira estruturada, evitando erros de digitação e poupando tempo em investigações.

![Python](https://img.shields.io/badge/Python-3.x-blue?style=for-the-badge&logo=python&logoColor=white)
![License](https://img.shields.io/badge/License-MIT-green?style=for-the-badge)
![Platform](https://img.shields.io/badge/Platform-Linux%20%7C%20Windows%20%7C%20macOS-lightgrey?style=for-the-badge)
![Terminal](https://img.shields.io/badge/CLI-Terminal-black?style=for-the-badge&logo=gnome-terminal)
![Dependencies](https://img.shields.io/badge/Dependencies-Zero_External-brightgreen?style=for-the-badge)

## 🚀 Funcionalidades Atuais

* **Leitura Dinâmica:** importa categorias e dorks diretamente de um arquivo `.json` externo, permitindo atualizações na base de dados sem necessidade de alterar o código-fonte;
* **Seleção em Lote:** capacidade de escolher múltiplos operadores lógicos de uma só vez;
* **Motor de Montagem:** Concatenação inteligente de domínios-alvo, palavras-chave e dorks selecionados.
* **Busca Limpa (No-AI):** injeção automatizada do parâmetro `&udm=14` na URL para contornar resumos de Inteligência Artificial do Google e retornar resultados puros de web tradicional;
* **Integração de Sistema:** abertura automática da pesquisa orquestrada diretamente no navegador padrão do sistema operacional.

## 🛠️ Tecnologias Utilizadas
* Projetado para garantir execução instantânea e máxima portabilidade. Para manter o consumo de recursos próximo a zero, a ferramenta utiliza estritamente a Standard Library do Python, sem necessidade de instalações adicionais:
   * `os` e `sys`: para detecção de ambiente multiplataforma em tempo de execução e integração fluida com padrões UNIX;
   * `subprocess`: executa chamadas de sistema cirúrgicas diretamente para o gerenciador de área de transferência nativo do usuário (Wayland/X11/Windows/macOS), evitando gargalos de bibliotecas gráficas;
   * `urllib.request`: garante a resiliência e a capacidade de auto-reparo de arquivos via rede sem depender de pacotes pesados de terceiros;
   * `json`: Processamento estruturado e ultrarrápido da base de dados de inteligência local.

## ⚙️ Como executar

1. Clone este repositório;
2. Certifique-se de ter o Python instalado em sua máquina;
3. Conceda permissão de execução ao script de instalação:
   ```bash
   chmod +x install.sh
   ```
4. Execute-o:
   ```bash
   ./install.sh
   ```

## 🚧 Próximos Passos (Roadmap)
### CONCLUÍDO:
- [✅] Implementar cópia automática da string gerada para a área de transferência do SO.
- [✅] Refatorar código em blocos funcionais (Funções).
- [✅] Implementar tratamento de exceções (`try/except`) para blindar entradas inválidas e falhas de leitura.
- [✅] Adicionar portabilidade multiplataforma para a área de transferência (Linux, Windows, macOS).
- [✅] Padronizar a execução como utilitário de linha de comando (CLI) nativo.
### EM BREVE: 
- [...] Adicionar suporte a interface gráfica no terminal (TUI) para seleção interativa.
- [...] Implementar sistema de "Favoritos" para salvar as combinações de dorks mais usadas.
- [...] Adicionar opções genéricas de dorks para maior personalização da pesquisa.
- [...] Criar extensão de navegador com interface gráfica (GUI).