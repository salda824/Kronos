# Kronos

## Descripción uso carpeta Postulantes
Este script requiere una cuenta de servicio de Google para acceder a la API de Google Sheets. Sigue estos pasos para configurar las credenciales:

1. **Crear un proyecto en Google Cloud Console**:
   - Ve a [Google Cloud Console](https://console.cloud.google.com/).
   - Crea un nuevo proyecto o selecciona uno existente.

2. **Activar la API de Google Sheets**:
   - En el menú de navegación, ve a **API y servicios > Biblioteca**.
   - Busca "Google Sheets API" y actívala.
   - Haz lo mismo para la **Google Drive API**.

3. **Crear una cuenta de servicio**:
   - En el menú de navegación, ve a **API y servicios > Credenciales**.
   - Haz clic en **Crear credenciales** y selecciona **Cuenta de servicio**.
   - Asigna un nombre a la cuenta de servicio y completa la configuración.
   - Cuando la cuenta esté creada, selecciona **Crear clave** y elige el formato **JSON**. Esto descargará un archivo `.json` que contiene tus credenciales.

4. **Asignar permisos a la cuenta de servicio**:
   - En Google Sheets, abre la hoja de cálculo a la que quieres acceder.
   - Comparte la hoja con la dirección de correo electrónico de la cuenta de servicio (encontrarás la dirección en el archivo `.json` descargado, en el campo `"client_email"`).

5. **Guardar el archivo de credenciales**:
   - Mueve el archivo `.json` descargado a la misma carpeta que tu script de Python.

Con esto deberias poder ejecutar el codigo de python sin ningun problema

##Instrucciones codigo para enviar correos
Debes entrar a google Apps Scripts y agregar el codigo en la parte del editor de codigo, no debe ir nada mas aparte del codigo. De igual manera se debe configurar en el icono del reloj un activador que ejecute la función verificar y enviar correo y que el tipo de evento sea al editarse, lo demas permanece en predeterminado. Le das a guardar y listo, el codigo debería servir sin problemas.
