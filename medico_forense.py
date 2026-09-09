import json
import os
import shutil

# --- MÓDULOS DE DIAGNÓSTICO ---

def chequear_disco():
    total, usado, _ = shutil.disk_usage("/")
    porcentaje = (usado / total) * 100
    if porcentaje > 80.0:
        return "DISK", "⚠", f"/ al {porcentaje:.1f}%", True, "Revisar uso de disco en /"
    return "DISK", "✓", "Normal", False, None

def chequear_ram():
    with open('/proc/meminfo', 'r') as f:
        datos = {l.split(':')[0].strip(): int(l.split(':')[1].split()[0]) for l in f if ':' in l}
    
    total = datos.get('MemTotal', 1)
    disponible = datos.get('MemAvailable', 0)
    porcentaje = ((total - disponible) / total) * 100
    
    if porcentaje > 85.0:
        return "RAM", "⚠", f"Alta presión de memoria ({porcentaje:.1f}%)", True, "Inspeccionar memoria de procesos"
    return "RAM", "✓", "Normal", False, None

def chequear_puertos():
    puertos = []
    with open('/proc/net/tcp', 'r') as f:
        for linea in f.readlines()[1:]:
            partes = linea.strip().split()
            if partes[3] == '0A':  # Estado LISTEN
                puertos.append(int(partes[1].split(':')[1], 16))
                
    alerta = len(puertos) > 0
    detalle = f"Puertos abiertos: {puertos}" if puertos else "Sin puertos TCP activos"
    return "NETWORK", "⚠" if alerta else "✓", detalle, alerta, "Inspeccionar procesos en puertos abiertos"

def chequear_ssh(config_path="/etc/ssh/sshd_config"):
    root_login = "no"
    try:
        with open(config_path, "r") as f:
            for line in f:
                line = line.strip()
                if line and not line.startswith("#") and line.startswith("PermitRootLogin"):
                    parts = line.split()
                    if len(parts) >= 2:
                        root_login = parts[1].lower()
    except Exception:
        return "SSH", "✓", "Configuración no encontrada o ilegible", False, None

    if root_login == "yes":
        return "SSH", "⚠", "PermitRootLogin activado", True, "Desactivar PermitRootLogin en sshd_config"
    return "SSH", "✓", "PermitRootLogin deshabilitado", False, None


# --- REPORTE Y EXPORTACIÓN ---

def guardar_json(chequeos, prioridad, razones, recomendaciones):
    os.makedirs("examples", exist_ok=True)
    reporte_datos = {
        "prioridad": prioridad,
        "evaluaciones": [
            {"modulo": mod, "simbolo": sim, "detalle": det}
            for mod, sim, det, _, _ in chequeos
        ],
        "razones": razones,
        "recomendaciones": recomendaciones
    }
    with open("examples/ejemplo_reporte.json", "w") as f:
        json.dump(reporte_datos, f, indent=4)

def generar_reporte():
    # Lista con los 4 módulos activos
    chequeos = [chequear_disco(), chequear_ram(), chequear_puertos(), chequear_ssh()]
    razones = []
    recomendaciones = []
    
    print("\nSYSTEM TRIAGE")
    print("────────────────────")
    for modulo, simbolo, detalle, es_alerta, recomendacion in chequeos:
        print(f"{modulo:<11} {simbolo} {detalle}")
        if es_alerta:
            razones.append(detalle)
            recomendaciones.append(recomendacion)
            
    prioridad = "HIGH" if razones else "LOW"
    
    print("\nINITIAL ASSESSMENT")
    print(f"Priority: {prioridad}")
    if razones:
        print("\nReasons:")
        for det in razones:
            print(f"• {det}")
        print("\nRecommended investigation:")
        for idx, rec in enumerate(recomendaciones, 1):
            print(f"{idx}. {rec}")
    else:
        print("• Todos los parámetros dentro de límites normales.")
        
    print("\nNo changes made to system.\n")
    guardar_json(chequeos, prioridad, razones, recomendaciones)

if __name__ == "__main__":
    print("[*] Ejecutando El Médico Forense...")  
    generar_reporte()
