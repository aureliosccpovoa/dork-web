#!/usr/bin/env python3

import functions

dorks = functions.load_dorks("dorks.json")

print("--- DORK WEB: MENU DE SELEÇÃO ---\n")

dorks_selected = functions.select_dorks(dorks)

# Bloco de personalização da query
print("\n--- PERSONALIZAÇÃO ---\n")

query_final = functions.build_query(dorks_selected)

functions.execute_query(query_final)