# Proyecto "Gestor de Tareas"

## Configuración e Instalación
Pasos para ejecutar el proyecto:

### 1. Clonar el repositorio y preparar el entorno
Primero se tiene que clonar el proyecto, crear el entorno virtual y activarlo

### 2. Instalar las dependencias
Instala todos los paquetes de Python necesarios para el proyecto:

```bash
pip install -r requirements.txt
```

### 3. Importar la base de datos
1. Abre SQL Server Management Studio (SSMS) y conéctate a tu instancia de `SQLEXPRESS`.
2. En el menú superior de SSMS, ve a File (Archivo) luego a Open (Abrir) despues a File... (Archivo...) y selecciona el archivo `schema.sql` que se encuentra dentro de la carpeta database de este proyecto (database/schema.sql).
3. Ejecuta la base de datos.

### 4. Configurar el Archivo de Entorno (`.env`)
1. Localiza el archivo `.env.example` en la raíz del proyecto.
2. Duplica el archivo y cámbiale el nombre a `.env` (asegúrate de que empiece con un punto).
3. Abre el archivo `.env` y rellena las variables:
   * En `DB_SERVER` puedes dejarlo como `"."` o modificarlo a tu instacia por defecto.
   * En `SECRET_KEY` pega una clave aleatoria segura. Puedes generar una ejecutando este comando en tu terminal:
     ```bash
     python -c "import secrets; print(secrets.token_hex(32))"
     ```

### 5. Ejecución del Servidor

Para encender la API en modo de desarrollo, ejecuta el comando:
```bash
fastapi dev src/main.py
```

## Pruebas en `/docs`

Para probar los endpoints protegidos en la interfaz se tiene que seguir estos pasos:

1. Registro: Crea un usuario en el endpoint `POST /users/Create User`.
2. Login: Inicia sesión en el endpoint de login para obtener tu token. Copia la cadena larga de texto del campo `access_token`.
3. Autorización: Sube al botón "Authorize" (icono de candado) arriba a la derecha. Pega el token directamente en el cuadro de texto Value y haz clic en Authorize.
4. Protección: A partir de este momento, todos los candados se cerrarán. Al crear o listar tareas, el sistema sabrá de forma automática y encriptada quién eres, impidiendo que un usuario vea o modifique las tareas de otros.

