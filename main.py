import json
import urllib.parse
import webbrowser
import subprocess

# Abre o arquivo json e converte em dicionário
with open("dorks.json", "r") as dorks_list:
    dorks = json.load(dorks_list)

print("--- DORK WEB: MENU DE SELEÇÃO ---\n")

# Variáveis e listas prévias
list_number = 1
dorks_mapped = []
full_query = []

# Solicita a inserção de um domínio a vasculhar
target_domain = input("Insira o domínio alvo (ex.: exemplo.com.br): ")

# Se o campo for vazio, passa adiante
if not target_domain:
    pass
else:
# Caso contrário, adiciona o domínio à pesquisa`
    target_domain = f"site:{target_domain}"
    full_query.append(target_domain)

# Itera sobre o dicionário criado pelo arquivo json para fornecer as categorias de pesquisa
for dork_category, dork_details in dorks.items():
    for dork in dork_details:
        dork_alias = dork["alias"]
        dork_name = dork["nome"]
        dork_content = dork["dork"]
        dork_description = dork["descricao"]

        print(f"[{list_number}] {dork_alias}: {dork_name}")

        list_number +=1

        dorks_mapped.append(dork)

# Solicita ao usuário que selecione opções e separa em itens de lista
usr_input = input("\nEscolha uma ou mais opções acima (somente números separados por espaço): ")
usr_input = usr_input.split()

# Itera sobre as opções selecionadas pelo usuário e adiciona o dork correspondente à lista de pesquisa
for item in usr_input:
    item = int(item)
    index = item - 1
    dork_chosen = dorks_mapped[index]
    full_query.append(dork_chosen["dork"])

# Verifica se o usuário deseja adicionar algo à pesquisa
add_keywords = input("Insira palavras-chave adicionais (ex.: senha, config etc): ")

if add_keywords == "":
    pass
else:
    full_query.append(add_keywords)

# Bloco de personalização da query
print("\n--- PERSONALIZAÇÃO ---\n")

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
query_string = ' '.join(full_query)

# Verifica se o usuário deseja exibir resultados de IA
ai_selection = input("Deseja exibir resultados de IA? (s/N): ").lower()
no_ai_code = "&udm=14"

if ai_selection == "n" or ai_selection == "":
    query_string_parsed = urllib.parse.quote_plus(query_string) + no_ai_code
else:
    query_string_parsed = urllib.parse.quote_plus(query_string)

url_start = "https://www.google.com/search?q="
final_url = url_start + query_string_parsed

# Mostra a query gerada
print(f"\n[!] PESQUISA GERADA: {query_string}\n")

open_browser = input("Deseja abrir o navegador já com a pesquisa selecionada? (S/n): ").lower()

# Abre o navegador padrão do sistema ou copia a pesquisa para a área de transferência
if open_browser == "s" or open_browser == "":
    webbrowser.open_new_tab(final_url)
else:
    clipboard_call = ["wl-copy"]
    subprocess.run(clipboard_call, input=query_string, text=True, check=True)
    print("Pesquisa copiada para a área de transferência")