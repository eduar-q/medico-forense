# 🩻 El Médico Forense — Linux Triage Tool

Herramienta de triage ligero y diagnóstico rápido para sistemas Linux. Diseñada para respuesta a incidentes y auditorías iniciales sin alterar el estado del sistema.

## ✨ Características
* ⚡ **Cero Dependencias Externas**: Desarrollado exclusivamente con la librería estándar de Python (`shutil`, `json`, `os`).
* 🐧 **Lectura Directa del Kernel**: Consulta `/proc/meminfo` y `/proc/net/tcp` para obtener datos en tiempo real sin ejecutar subprocesos innecesarios.
* 🛡️ **Seguro e Inofensivo**: Modo de solo lectura; no realiza modificaciones en el sistema auditado.
* 📊 **Doble Formato de Salida**: Genera un reporte legible en terminal y exporta los datos en `examples/ejemplo_reporte.json`.

## 📁 Estructura del Proyecto

```text
medico-forense/
├── medico_forense.py       # Script principal de diagnóstico
├── README.md               # Documentación del proyecto
├── .gitignore              # Archivos ignorados por Git
├── examples/
│   └── ejemplo_reporte.json # Ejemplo de salida estructurada
└── tests/
    └── test_medico_forense.py # Pruebas unitarias automatizadas
```

🚀 Uso
Ejecuta el script de diagnóstico en cualquier entorno Linux con Python 3:
```
python3 medico_forense.py

```

🧪 Pruebas Automatizadas
Para validar los módulos de diagnóstico mediante la suite de pruebas unitarias:
```
python3 -m unittest discover -s tests
```


