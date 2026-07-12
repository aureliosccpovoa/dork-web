import json
import webbrowser
import subprocess
import urllib.parse
import urllib.request
import sys

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

        dorks_newfile = input("Arquivo dorks.json não encontrado! Deseja baixá-lo novamente do repositório remoto? (S/n): ").lower()

        if dorks_newfile == "s" or dorks_newfile == "":
            dorks_url_raw = "https://raw.githubusercontent.com/aureliosccpovoa/dork-web/refs/heads/main/dorks.json"
            urllib.request.urlretrieve(dorks_url_raw, dorks_filename)

            return load_dorks(file_path)
        else:
            print("Execução interrompida (FileNotFoundError).")
            sys.exit(1)

    except json.JSONDecodeError:

        print("Erro ao carregar o arquivo dorks.json. Verificar sintaxe.")
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

            print(f"[{list_number}] {dork_alias}: {dork_name}")

            list_number +=1

            dorks_mapped.append(dork)
    
    while True:
        # Solicita ao usuário que selecione opções e separa em itens de lista
        usr_input = input("\nEscolha uma ou mais opções acima (somente números separados por espaço): ")
        usr_input = usr_input.split()

        input_valid = True

        for item in usr_input:
            if item.isdigit():
                item = int(item)

                if item == 0 or item > len(dorks_mapped):
                    input_valid = False
                    print("Opção inválida!")
                else:
                    pass
            else:
                input_valid = False
                print("Favor digitar somente números!")

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
    target_domain = input("Insira o domínio alvo (ex.: exemplo.com.br): ")

    # Se o campo for vazio, passa adiante
    if not target_domain:
        pass
    else:
    # Caso contrário, adiciona o domínio à pesquisa`
        target_domain = f"site:{target_domain}"
        full_query.append(target_domain)

    # Verifica se o usuário deseja adicionar algo à pesquisa
    add_keywords = input("Insira palavras-chave adicionais (ex.: senha, config etc): ")

    if add_keywords == "":
        pass
    else:
        full_query.append(add_keywords)

    # Verifica se o usuário deseja adicionar texto à query
    modify_query = input("Deseja adicionar ou modificar algo manualmente nesta pesquisa? (S/n): ").lower()

    if modify_query == "s" or modify_query == "":
        extra_query = input("Insira os parâmetros adicionais que deseja: ")
        if not extra_query:
            pass
        else:
            full_query.append(extra_query)
            query_string = ' '.join(full_query)
    else:
        pass

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
    ai_selection = input("Deseja exibir resultados de IA? (s/N): ").lower()
    no_ai_code = "&udm=14"

    if ai_selection == "n" or ai_selection == "":
        query_string_parsed = urllib.parse.quote_plus(query_string) + no_ai_code
    else:
        query_string_parsed = urllib.parse.quote_plus(query_string)

    url_start = "https://www.google.com/search?q="
    final_url = url_start + query_string_parsed

    open_browser = input("Deseja abrir o navegador já com a pesquisa selecionada? (S/n): ").lower()

    # Abre o navegador padrão do sistema ou copia a pesquisa para a área de transferência
    if open_browser == "s" or open_browser == "":
        webbrowser.open_new_tab(final_url)
    else:
        clipboard_call = ["wl-copy"]
        subprocess.run(clipboard_call, input=query_string, text=True, check=True)

        # Mostra a query gerada
        print(f"\n[!] PESQUISA COPIADA: {query_string}\n")