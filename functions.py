import json
import webbrowser
import subprocess
import urllib.parse
import urllib.request
import sys
import os

# Paleta de Cores ANSI
class Color:
    GREEN = '\033[32m'
    RED = '\033[31m'
    BLUE = '\033[34m'
    YELLOW = '\033[33m'
    RESET = '\033[0m'

dorks_filename = "dorks.json"

def load_dorks(file_path):
    """
    Abre o arquivo json e converte em dicionário.
    """
    try:

        with open(file_path, "r") as dorks_list:
            dorks = json.load(dorks_list)

        return dorks
    
    except FileNotFoundError:

        dorks_newfile = input(f"{Color.YELLOW}Arquivo dorks.json não encontrado! Deseja baixá-lo novamente do repositório remoto? (S/n): {Color.RESET}").lower()

        if dorks_newfile == "s" or dorks_newfile == "":
            dorks_url_raw = "https://raw.githubusercontent.com/aureliosccpovoa/dork-web/refs/heads/main/dorks.json"
            urllib.request.urlretrieve(dorks_url_raw, dorks_filename)

            return load_dorks(file_path)
        else:
            print(f"{Color.RED}Execução interrompida (FileNotFoundError).{Color.RESET}")
            sys.exit(1)

    except json.JSONDecodeError:

        print(f"{Color.RED}Erro ao carregar o arquivo dorks.json. Verificar sintaxe.{Color.RESET}")
        sys.exit(1)


def select_dorks(dorks):
    """
    Lista os dorks disponíveis e mapeia aqueles selecionados pelo usuário.
    """

    # Variáveis e listas prévias
    list_number = 1
    dorks_mapped = []
    dorks_selected = []

    for dork_category, dork_details in dorks.items():
    # Itera sobre o dicionário criado pelo arquivo json para fornecer as categorias de pesquisa
        for dork in dork_details:
            dork_alias = dork["alias"]
            dork_name = dork["nome"]
            # dork_content = dork["dork"]
            # dork_description = dork["descricao"]

            print(f"[{Color.BLUE}{list_number}{Color.RESET}] {dork_alias}: {dork_name}")

            list_number +=1

            dorks_mapped.append(dork)
    
    while True:
        # Solicita ao usuário que selecione opções e separa em itens de lista
        usr_input = input(f"\n{Color.BLUE}Escolha uma ou mais opções acima (somente números separados por espaço): {Color.RESET}")
        usr_input = usr_input.split()

        input_valid = True

        for item in usr_input:
            if item.isdigit():
                item = int(item)

                if item == 0 or item > len(dorks_mapped):
                    input_valid = False
                    print(f"{Color.RED}Opção inválida!{Color.RESET}")
                else:
                    pass
            else:
                input_valid = False
                print(f"{Color.RED}Favor digitar somente números!{Color.RESET}")

        if input_valid:
            break

    # Itera sobre as opções selecionadas pelo usuário e adiciona o dork correspondente à lista de pesquisa
    for item in usr_input:
        item = int(item)
        index = item - 1
        dork_chosen = dorks_mapped[index]
        dorks_selected.append(dork_chosen["dork"])

    return dorks_selected


def build_query(dorks_selected):
    """
    Estrutura a pesquisa com mais preferências do usuário.
    """

    full_query  = []

    # Solicita a inserção de um domínio a vasculhar
    target_domain = input(f"{Color.BLUE}Insira o domínio alvo (ex.: exemplo.com.br): {Color.RESET}")

    # Se o campo for vazio, passa adiante
    if not target_domain:
        pass
    else:
    # Caso contrário, adiciona o domínio à pesquisa`
        target_domain = f"site:{target_domain}"
        full_query.append(target_domain)

    # Verifica se o usuário deseja adicionar algo à pesquisa
    add_keywords = input(f"{Color.BLUE}Insira palavras-chave adicionais (ex.: senha, config etc): {Color.RESET}")

    if add_keywords == "":
        pass
    else:
        full_query.append(add_keywords)

    # Verifica se o usuário deseja adicionar texto à query
    modify_query = input(f"{Color.BLUE}Deseja adicionar ou modificar algo manualmente nesta pesquisa? (s/N): {Color.RESET}").lower()

    if modify_query == "n" or modify_query == "":
        pass
    else:
        extra_query = input(f"{Color.BLUE}Insira os parâmetros adicionais que deseja: {Color.RESET}")
        if not extra_query:
            pass
        else:
            full_query.append(extra_query)
            query_string = ' '.join(full_query)

    # Concatena a pesquisa até aqui
    full_query.extend(dorks_selected)
    query_string = ' '.join(full_query)
 
    return query_string


def execute_query(query_string):
    """
    Abre uma nova aba no navegador padrão do sistema com a URL da pesquisa ou copia para a área de transferência.
    FUTURAMENTE: retornará a pesquisa Google diretamente no terminal.
    """
    
    # Verifica se o usuário deseja exibir resultados de IA
    ai_selection = input(f"{Color.YELLOW}Deseja exibir resultados de IA? (s/N): {Color.RESET}").lower()
    no_ai_code = "&udm=14"

    if ai_selection == "n" or ai_selection == "":
        query_string_parsed = urllib.parse.quote_plus(query_string) + no_ai_code
    else:
        query_string_parsed = urllib.parse.quote_plus(query_string)

    url_start = "https://www.google.com/search?q="
    final_url = url_start + query_string_parsed

    open_browser = input(f"{Color.YELLOW}Deseja abrir o navegador já com a pesquisa selecionada? (S/n): {Color.RESET}").lower()

    # Abre o navegador padrão do sistema ou copia a pesquisa para a área de transferência
    if open_browser == "s" or open_browser == "":
        webbrowser.open_new_tab(final_url)
    else:
        match sys.platform:
            case "win32":
                # Define clipboard_call para Windows
                clipboard_call = ["clip"]
            case "darwin":
                # Define clipboard_call para macOS
                clipboard_call = ["pbcopy"]
            case "linux":
                # Verifica o ambiente Linux
                os_env = os.environ.get("XDG_SESSION_TYPE")
                if os_env == "wayland":
                    clipboard_call = ["wl-copy"]
                else:
                    clipboard_call = ["xclip", "-selection", "clipboard"]
            case _:
                # Caso o sistema seja desconhecido (ex: FreeBSD)
                print(f"{Color.RED}Sistema não suportado para área de transferência automática.{Color.RESET}")
                return

        subprocess.run(clipboard_call, input=query_string, text=True, check=True)

        # Mostra a query gerada
        print(f"\n{Color.GREEN}[!] PESQUISA COPIADA: {query_string}\n{Color.RESET}")