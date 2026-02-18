import os
from dotenv import load_dotenv
from google import genai
from google.genai import types

# Cargar configuración de variables de entorno
load_dotenv()
API_KEY = os.getenv("GEMINI_API_KEY")

# Inicializar el cliente
client = genai.Client(api_key=API_KEY)

# Configuración del modelo y rol
system_instruction = """Eres un vendedor amable y entusiasta. 
Tu objetivo es ayudar al cliente a encontrar el producto ideal y cerrar 
la venta de manera cordial. Si te hacen preguntas que no están relacionadas 
con el área de tecnología, responde 'lo siento, solo te puedo ayudar con 
preguntas relacionadas con tecnología'"""

# Historial de ejemplos (Few-shot learning)
historial_ejemplos = [
    types.Content(
        role="user",
        parts=[types.Part(text="¿Qué me recomiendas para empezar a programar?")]
    ),
    types.Content(
        role="model",
        parts=[types.Part(text="¡Excelente iniciativa! Para empezar, te recomiendo una laptop con buen procesador (i5 o Ryzen 5 en adelante) y al menos 16GB de RAM. Tenemos modelos como la Dell Inspiron o la MacBook Air que son perfectas para estudiantes. ¿Prefieres Windows o Mac?")]
    ),
    types.Content(
        role="user",
        parts=[types.Part(text="Busco unos audífonos con buena cancelación de ruido.")]
    ),
    types.Content(
        role="model",
        parts=[types.Part(text="¡Tengo justo lo que necesitas! Los Sony WH-1000XM5 son líderes en el mercado con una cancelación de ruido increíble y una batería de larga duración. ¿Te gustaría conocer el precio y las opciones de financiación?")]
    )
]

# Configuración de generación
configuration = types.GenerateContentConfig(
    system_instruction=system_instruction,
    temperature=0.7,
    max_output_tokens=2000
)

# Inicialización del chat con historial
chat = client.chats.create(
    model="gemini-3-flash-preview",
    config=configuration,
    history=historial_ejemplos,
)


print("--- Chat de Ventas (Escribe 'finalizar' para terminar) ---")
print("Vendedor: ¡Hola! ¿En qué puedo ayudarte hoy?\n")

while True:
    user_input = input("Cliente: ")

    if user_input.lower() == "finalizar":
        print("Vendedor: ¡Gracias por tu visita! Esperamos verte pronto.")
        break

    try:
        # Envío del mensaje
        response = chat.send_message(user_input)
        print(f"Vendedor: {response.text}\n")
    except Exception as e:
        print(f"Error al procesar la solicitud: {e}")