#!/bin/bash

# Cores para o terminal (estética do instalador)
GREEN='\033[0;32m'
BLUE='\033[0;34m'
NC='\033[0m' # Sem cor

echo -e "${BLUE}[*] Iniciando a instalação do Dork Web...${NC}"

# Define o diretório padrão de binários do usuário
BIN_DIR="$HOME/.local/bin"
TARGET_BIN="$BIN_DIR/dorkweb"

# 1. Cria o diretório de binários caso ele ainda não exista
mkdir -p "$BIN_DIR"

# 2. Garante que o arquivo principal tenha permissão de execução
chmod +x main.py

# 3. Captura o caminho absoluto de onde o repositório foi clonado/salvo
PROJECT_DIR="$(pwd)"

# 4. Cria o script wrapper dentro do diretório de binários do sistema
cat <<EOF > "$TARGET_BIN"
#!/bin/bash
# Navega para o diretório base do projeto para localizar o dorks.json
cd "$PROJECT_DIR" || exit
# Executa o orquestrador nativamente
./main.py "\$@"
EOF

# 5. Dá permissão de execução ao novo comando
chmod +x "$TARGET_BIN"

echo -e "${GREEN}[+] Instalação concluída com sucesso!${NC}"
echo -e "O executável foi criado em: ${TARGET_BIN}"
echo -e "\nAgora você pode chamar a ferramenta de qualquer lugar do seu sistema digitando simplesmente:"
echo -e "  ${BLUE}dorkweb${NC}\n"