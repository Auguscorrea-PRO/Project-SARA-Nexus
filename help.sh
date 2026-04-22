#!/data/data/com.termux/files/usr/bin/bash

# Colores
RED='\033[0;31m'
NC='\033[0m'

clear
echo -e "${RED}!!! AVISO IMPORTANTE !!!${NC}"
echo "Este software es para fines educativos y de investigacion."
echo "El uso indebido es responsabilidad del usuario."
echo "Dando permisos a phantom_sdk.py..."

# Dar permisos de ejecución
chmod +x phantom_sdk.py

echo -n "Procesando"
for i in {1..5}; do
    echo -n "."
    sleep 1
done

echo -e "\nListo. Abriendo Menu..."
python phantom_sdk.py
