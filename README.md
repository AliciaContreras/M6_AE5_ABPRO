# 🔒 Plataforma de Gestión de Eventos (Seguridad y Roles)

Este proyecto es una aplicación web desarrollada en Django centrada en la implementación de un sistema robusto de **autenticación y autorización**. Permite la gestión de eventos con control de acceso basado en roles, asegurando que cada usuario solo pueda realizar las acciones permitidas por su perfil.

## 🚀 Funcionalidades Clave

*   **Autenticación Completa:** Login, Logout y protección de rutas.
*   **Control de Acceso (RBAC):** Sistema de roles diferenciados (Administrador, Organizador, Asistente).
*   **Seguridad en Vistas:** Implementación de `LoginRequiredMixin` y `PermissionRequiredMixin`.
*   **Manejo de Errores:** Redirección amigable y mensajes de alerta (`messages`) en lugar de errores 403 genéricos.
*   **Seguridad:** Configuración de protección de cookies y headers en `settings.py`.

## 👥 Roles y Permisos Definidos

El sistema está diseñado para funcionar con los siguientes grupos de usuarios (configurables desde el Admin):

1.  **Administrador:** Acceso total (Crear, Editar, Eliminar eventos).
2.  **Organizador:** Puede **Crear** y **Editar** eventos, pero **NO** puede eliminarlos.
3.  **Asistente:** Acceso de solo lectura (Ver listado de eventos).

## 🛠️ Instalación y Puesta en Marcha

1.  **Crear y activar entorno virtual:**
    ```bash
    python -m venv venv
    # Windows: venv\Scripts\activate
    # Mac/Linux: source venv/bin/activate
    ```

2.  **Instalar Django:**
    ```bash
    pip install django
    ```

3.  **Aplicar migraciones:**
    ```bash
    python manage.py migrate
    ```

4.  **Crear Superusuario (para gestionar roles):**
    ```bash
    python manage.py createsuperuser
    ```

5.  **Iniciar Servidor:**
    ```bash
    python manage.py runserver
    ```

## ⚙️ Configuración Inicial (Importante)

Para probar los roles correctamente:

1.  Accede a `http://127.0.0.1:8000/admin/` con tu superusuario.
2.  Crea dos Grupos: **"Organizadores"** y **"Asistentes"**.
3.  Asigna al grupo **Organizadores** los permisos: `eventos | evento | Can add evento` y `Can change evento`.
4.  Crea usuarios de prueba y asígnalos a estos grupos para verificar las restricciones.

## 📂 Estructura del Proyecto

*   `gestion_eventos/`: Configuración global, `settings.py` (con variables de seguridad) y `urls.py` (rutas de login/logout).
*   `eventos/`:
    *   `models.py`: Modelo `Evento` vinculado al `User`.
    *   `views.py`: Vistas basadas en clases (CBV) protegidas con Mixins personalizados.
    *   `templates/`: Plantillas para login, listados y formularios.

## ✒️ Autor
*   Alicia Contreras