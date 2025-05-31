from flask import Flask, request, jsonify
import google.generativeai as genai
from dotenv import load_dotenv
import os
import json

load_dotenv()

app = Flask(__name__)

genai.configure(api_key=os.getenv("GEMINI_API_KEY"), transport='rest')


model = genai.GenerativeModel('gemini-2.0-flash')  

with open('../data/cars.json', 'r') as f:
    cars_data = json.load(f)

@app.route('/chat', methods=['POST'])
def chat():
    try:
        user_message = request.json.get('message', '').lower()

        filtered_cars = [
            car for car in cars_data
            if any(str(keyword).lower() in user_message for keyword in [car['Name'], car['Model'], car['Price'], car['Location']])
            ] or cars_data[:3]

        prompt = f"""
                        Você é o assistente virtual especializado da Klubi Consórcios, focado em ajudar clientes a encontrar o veículo ideal para ele conforme suas especificações.

                        Dados os carros disponíveis em nosso sistema: {filtered_cars}

                        Instruções específicas:
                        1. Identifique o perfil do cliente pela mensagem: "{user_message}"
                        2. Priorize veículos sustentáveis (elétricos/híbridos) quando relevante
                        3. Siga rigorosamente estas regras de resposta:

                        - Para carros DISPONÍVEIS na cidade solicitada:
                        "Temos ótimas opções para você! [detalhe 2-3 características do veículo]. Na Klubi, você pode adquirir este modelo com [benefício específico de consórcio]. Esse modelo de carro está disponível na sua cidade."

                        - Para carros INDISPONÍVEIS na cidade mas no sistema:
                        "Este modelo não está disponível em sua localidade no momento, mas como valorizamos seu interesse, já estou acionando nosso time para verificar a viabilidade de: (1) agendar visita em nossa concessionária parceira mais próxima, ou (2) trazer o veículo até você. Um especialista entrará em contato em até 24h."

                        - Para solicitações SEM correspondência:
                        "Estamos verificando disponibilidade em nossa rede de parceiros. Para agilizar, nosso especialista em consórcios entrará em contato com opções personalizadas dentro do seu perfil."

                        - Para dúvidas TÉCNICAS:
                        "[Resposta técnica objetiva]. Lembrando que na Klubi você adquire este veículo com [vantagem do consórcio relacionada à característica técnica]."

                        - Para comparações:
                        "Analisando seu perfil, recomendo [Modelo X] para [razão 1] e [razão 2]. Comparando com outros do segmento: [diferencial competitivo]. No consórcio Klubi, você terá [benefício específico]."

                        Regras de comunicação:
                        • Use tom empático mas profissional
                        • Inclua sempre 1 benefício exclusivo do consórcio
                        • Encerre com chamada para ação clara
                        • Formate valores como "R$ 99.990,00"
                        • Para elétricos/híbridos, destaque "Economia de até X% no custo total pelo programa Klubi Sustentável"
                        
                    """


        response = model.generate_content(prompt)

        return jsonify({
            "success": True,
            "response": response.text,
            "cars": filtered_cars[:5],
            "suggestions": [f"{car['Name']} {car['Model']}" for car in filtered_cars[:3]]
        })

    except Exception as e:
        return jsonify({
            "success": False,
            "error": str(e),
            "message": "Erro ao processar sua requisição"
        }), 500

if __name__ == '__main__':
    app.run(port=5000, debug=True)
