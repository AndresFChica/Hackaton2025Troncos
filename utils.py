from transformers import AutoTokenizer, AutoModelForSequenceClassification, pipeline
import pandas as pd

# ---- Clasificación de Intención ----
def clasificar_intencion(texto):
    tokenizer = AutoTokenizer.from_pretrained("dccuchile/distilbert-base-spanish-uncased")
    model = AutoModelForSequenceClassification.from_pretrained("ruta/a/mi-modelo-finetuneado")  # Fine-tuning previo
    inputs = tokenizer(texto, return_tensors="pt")
    outputs = model(**inputs)
    intenciones = ["extensión_plazo", "reducción_intereses", "ayuda_emergencia"]
    return intenciones[outputs.logits.argmax()]

# ---- Generación de Respuestas ----
def generar_respuesta(texto_cliente, intencion):
    generator = pipeline("text-generation", model="deepseek-ai/deepseek-r1")
    prompt = f"""
    Cliente dice: '{texto_cliente}'. 
    Genera una respuesta EMPÁTICA y PROFESIONAL basada en la intención '{intencion}'.
    Usa plantillas de reestructuración de deuda y ofrece opciones reales.
    """
    respuesta = generator(prompt, max_length=200)
    return respuesta[0]['generated_text']