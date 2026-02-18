import os
from google import genai
from google.genai import types
from dotenv import load_dotenv

# 1. Cargar configuración de variables de entorno
load_dotenv()
clave_api = os.getenv("GEMINI_API_KEY")

# 2. Inicializar el Cliente
client = genai.Client(api_key=clave_api)

def procesar_articulo(texto, tarea):
    """
    Procesa un texto según la tarea: 'resumir' o 'profesionalizar'.
    Utiliza una system_instruction para actuar como un Editor Editorial de prestigio.
    """
    
    # Restricción: system_instruction definida
    instruccion_sistema = "Eres un Editor editorial de prestigio."
    
    if tarea.lower() == "resumir":
        prompt_usuario = f"Por favor, genera un resumen ejecutivo del siguiente texto:\n\n{texto}"
    elif tarea.lower() == "profesionalizar":
        prompt_usuario = f"Edita y reescribe el siguiente texto para que suene formal, técnico y profesional:\n\n{texto}"
    else:
        return "Error: Tarea no válida. Use 'resumir' o 'profesionalizar'."

    try:
        # Llamada al modelo con system_instruction en la configuración
        response = client.models.generate_content(
            model="gemini-3-flash-preview",
            config=types.GenerateContentConfig(
                system_instruction=instruccion_sistema,
                temperature=1
            ),
            contents=prompt_usuario
        )
        return response.text
    except Exception as e:
        return f"Ocurrió un error al procesar el artículo: {str(e)}"

# Bloque principal para pruebas
if __name__ == "__main__":
    articulo_ejemplo = """
    La inteligencia artificial es super buena para hacer cosas rapido pero a veces se equivoca.
    Hay que tener cuidao con lo que le pides pq si no le das buen contexto te saca cualquier cosa.
    En el futuro seguro que mejora un monton y nos ayuda mas.
    """
    
    print("--- Texto Original ---")
    print(articulo_ejemplo)
    
    print("\n--- Resultado: Profesionalizar ---")
    resultado_prof = procesar_articulo(articulo_ejemplo, "profesionalizar")
    print(resultado_prof)
    
    print("\n--- Resultado: Resumir ---")
    resultado_resumen = procesar_articulo(articulo_ejemplo, "resumir")
    print(resultado_resumen)
