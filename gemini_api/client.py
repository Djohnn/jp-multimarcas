from django.conf import settings
from google import genai




def get_car_ai_bio(model, brand, year):
    prompt = f"""
    Me mostre uma descrição de venda para o carro {model} {brand} {year} em apenas 250 caracteres.
    Fale coisas específicas, técnicas, desse modelo de carro.
    """

    client = genai.Client(api_key=settings.GEMINI_API_KEY)
    response = client.models.generate_content(
        model="gemini-2.5-flash",
        contents=prompt,
    )

    return response.text


def get_motorcycle_ai_bio(model, brand, year, moto_type, engine_cc):
    prompt = f"""
    Me mostre uma descrição de venda para a moto {model} {brand} {year}, 
    tipo {moto_type}, {engine_cc}cc, em apenas 250 caracteres.
    Fale coisas específicas, técnicas, desse modelo de moto.
    """
    client = genai.Client(api_key=settings.GEMINI_API_KEY)
    response = client.models.generate_content(
        model="gemini-2.5-flash",
        contents=prompt,
    )
    return response.text
