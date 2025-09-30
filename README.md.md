# 🧺 Lavandería RÍOS - Sistema de Gestión

Sistema web para gestión de boletas y servicios de lavandería desarrollado con Flask y SQLite.

## 🚀 Características

- ✅ Gestión completa de boletas
- ✅ Cálculo automático de precios
- ✅ Base de datos SQLite integrada
- ✅ Interfaz responsive y amigable
- ✅ Progressive Web App (PWA)
- ✅ Sistema de impresión de boletas

## 📁 Estructura del Proyecto

```
lavanderia-rios/
├── app.py                    # Aplicación principal Flask
├── database.py               # Gestión de base de datos SQLite
├── pricing.py                # Lógica de cálculo de precios
├── config_precios.py         # Configuración de precios
├── templates/                # Plantillas HTML
│   ├── base.html
│   ├── index.html
│   ├── boletas.html
│   ├── boleta_nueva.html
│   ├── boleta_detalle.html
│   └── error.html
├── static/
│   ├── style.css            # Estilos CSS
│   ├── manifest.json        # PWA manifest
│   └── sw.js               # Service Worker
├── requirements.txt         # Dependencias Python
└── README.md
```

## 🛠️ Instalación Local

1. **Clonar el repositorio:**
   ```bash
   git clone https://github.com/tu-usuario/lavanderia-rios.git
   cd lavanderia-rios
   ```

2. **Crear entorno virtual:**
   ```bash
   python -m venv venv
   source venv/bin/activate  # En Windows: venv\Scripts\activate
   ```

3. **Instalar dependencias:**
   ```bash
   pip install -r requirements.txt
   ```

4. **Ejecutar la aplicación:**
   ```bash
   python app.py
   ```

5. **Abrir en el navegador:** `http://localhost:5000`

## 🌐 Deploy en Render.com

### Método Automático:
1. Fork este repositorio
2. Ir a [render.com](https://render.com)
3. Crear nuevo "Web Service"
4. Conectar con tu repositorio
5. Configuración automática con `render.yaml`

### Configuración Manual:
- **Build Command:** `pip install -r requirements.txt`
- **Start Command:** `gunicorn app:app`
- **Environment:** Python 3.9+

## 🔧 Variables de Entorno

| Variable | Descripción | Valor por Defecto |
|----------|-------------|-------------------|
| `SECRET_KEY` | Clave secreta de Flask | `dev-only-change-in-production` |
| `FLASK_ENV` | Entorno de ejecución | `development` |
| `PORT` | Puerto del servidor | `5000` |

## 📱 PWA (Progressive Web App)

La aplicación funciona como PWA y puede instalarse en dispositivos móviles:
- Icono en pantalla de inicio
- Funciona offline (caché básico)
- Experiencia nativa en móviles

## 🎨 Personalización

### Precios:
Editar `config_precios.py` para ajustar precios base.

### Estilos:
Modificar `static/style.css` - Usa paleta de colores amigable predefinida.

### Base de Datos:
SQLite integrada, se crea automáticamente al iniciar.

## 🐛 Solución de Problemas

### Error de Base de Datos:
```bash
python recreate_db.py  # Recrear BD desde cero
python fix_db.py       # Reparar BD existente
```

### Error de Dependencias:
```bash
pip install --upgrade -r requirements.txt
```

## 📄 Licencia

Este proyecto es de uso libre para lavanderías y pequeños negocios.

---

**Desarrollado para Lavandería RÍOS** 🧺✨