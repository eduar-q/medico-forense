# El Médico Forense 🩺

Una herramienta de diagnóstico rápido (triage) en Python para servidores Linux. 
Diseñada para realizar un análisis inicial del estado del sistema sin dependencias externas y sin modificar ningún archivo.

## 🚀 Características
- **Cero dependencias externas**: Utiliza únicamente la librería estándar de Python (`shutil`, `json`, etc.).
- **Inspección directa del Kernel**: Lee la información del sistema directamente desde la interfaz `/proc`.
- **Sin modificaciones**: Herramienta de solo lectura que genera un reporte sin alterar el sistema hospedador.
- **Salida estandarizada**: Formato visual legible en consola y exportación estructurada en JSON.

## 📊 Módulos de Triage

| Módulo | Fuente de datos | Qué evalúa |
| :--- | :--- | :--- |
| **DISK** | `shutil.disk_usage` | Uso de espacio en el directorio raíz (`/`) |
| **RAM** | `/proc/meminfo` | Porcentaje de presión y disponibilidad de memoria |
| **NETWORK** | `/proc/net/tcp` | Detección de puertos TCP en estado de escucha (`LISTEN`) |
| **SSH** | `/etc/ssh/sshd_config` | Verificación de políticas de seguridad (ej. `PermitRootLogin`) |

## 🖥️ Ejemplo de Salida

```text
SYSTEM TRIAGE
────────────────────
DISK        ✓ Normal
RAM         ✓ Normal
NETWORK     ⚠ Puertos abiertos: [53, 53]
SSH         ✓ PermitRootLogin deshabilitado

INITIAL ASSESSMENT
Priority: HIGH

Reasons:
• Puertos abiertos: [53, 53]

Recommended investigation:
1. Inspeccionar procesos en puertos abiertos

No changes made to system.
```

## 🚀 Uso
Ejecuta el script de diagnóstico en cualquier entorno Linux con Python 3:
```
python3 medico_forense.py
```
El reporte detallado se guardará automáticamente en examples/ejemplo_reporte.json

## 🧪 Pruebas Automatizadas
Para validar los módulos de diagnóstico mediante la suite de pruebas unitarias:

```
python3 -m unittest discover tests

```
## ⚠️ Alcance
El Médico Forense es una herramienta de triage inicial.
Sus resultados deben interpretarse como señales que pueden requerir una investigación posterior, no como evidencia definitiva de un incidente de seguridad.
El proyecto comienza con cuatro chequeos:
DISK
RAM
NETWORK
SSH
La idea es mantener cada componente sencillo, comprensible y fácil de ampliar.



