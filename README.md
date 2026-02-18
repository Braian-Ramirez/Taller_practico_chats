# 🤖 Taller Práctico de Chats con IA (Google Gemini)

Este repositorio contiene ejercicios prácticos para aprender a utilizar la API de Google Gemini en Python, desde una llamada básica hasta un chatbot interactivo con roles y memoria.

## 📋 Requisitos Previos

1.  **Python 3.9 o superior** instalado.
2.  Una **API Key de Google Gemini** (puedes obtenerla en [Google AI Studio](https://aistudio.google.com/)).

## ⚙️ Configuración e Instalación

1.  **Clonar o descargar** este código.
2.  **Crear un entorno virtual** (recomendado):
    ```bash
    python -m venv env
    source env/bin/activate  # En Linux/Mac
    env\Scripts\activate     # En Windows
    ```
3.  **Instalar dependencias**:
    ```bash
    pip install -r requirements.txt
    ```
4.  **Configurar la API Key**:
    *   Crea un archivo llamado `.env` en la raíz del proyecto.
    *   Añade tu clave de API en el archivo `.env`:
    ```env
    GEMINI_API_KEY=tu_clave_api_aqui
    ```

## 🚀 Ejecución de los Ejercicios

### 1️⃣ Ejercicio 1: Llamada Básica
Realiza una consulta simple al modelo para explicar un concepto.
```bash
python Ejercicio_1.py
```

### 2️⃣ Ejercicio 2: Procesamiento de Texto (Roles y Tareas)
Una función que actúa como un **Editor Editorial**, capaz de resumir o profesionalizar textos.
```bash
python Ejercicio_2.py
```

### 3️⃣ Ejercicio 3: Chat Interactivo (Vendedor de Tecnología)
Un chatbot que simula ser un **vendedor amable**, con memoria de conversación (few-shot learning) para recomendar productos.
*   Escribe tu pregunta y presiona Enter.
*   Escribe `finalizar` para terminar la sesión.

```bash
python Ejercicio_3.py
```

## 🛠️ Solución de Problemas Comunes

*   **Error de API Key**: Asegúrate de que el archivo `.env` esté bien escrito y la variable se llame `GEMINI_API_KEY`.
*   **ModuleNotFoundError**: Verifica que activaste el entorno virtual y ejecutaste `pip install -r requirements.txt`.
