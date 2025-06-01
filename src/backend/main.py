from flask import Flask, request, jsonify
import google.generativeai as genai
from dotenv import load_dotenv
import os
import json
from flask_cors import CORS  
import re

load_dotenv()

app = Flask(__name__)

CORS(app, resources={
    r"/*": {
        "origins": ["http://localhost:3000", "http://127.0.0.1:3000"]  
    }
})


genai.configure(api_key=os.getenv("GEMINI_API_KEY"), transport='rest')


model = genai.GenerativeModel('gemini-2.0-flash')  

with open('../data/cars.json', 'r') as f:
    cars_data = json.load(f)



def extract_price(text):
    price_match = re.findall(r'\d{1,3}(?:[\.\,]?\d{3})*(?:[\.\,]?\d{2})?', text.replace('.', '').replace(',', '.'))
    try:
        price_numbers = [float(p) for p in price_match if float(p) > 1000]  # Filtra valores plausíveis
        return max(price_numbers) if price_numbers else None
    except:
        return None



@app.route('/chat', methods=['POST'])
def chat():
    try:
        user_message = request.json.get('message', '').lower()
        budget = extract_price(user_message)

        if budget:
            affordable_cars = [car for car in cars_data if float(car['Price']) <= budget]
        else:
            affordable_cars = []

        filtered_cars = [
            car for car in cars_data
            if any(str(keyword).lower() in user_message for keyword in [car['Name'], car['Model'], car['Price'], car['Location']])
        ] or cars_data[:3]

        prompt = f"""
                    Você é o assistente virtual do Klubi Consórcios, especializado em ajudar clientes a encontrar o veículo ideal.

                    ### Dados:
                    Mensagem do cliente: "{user_message}"

                    Orçamento detectado: {'R$ {:.2f}'.format(budget) if budget else 'Não informado'}

                    ### Veículos no sistema:
                    {filtered_cars if not budget else affordable_cars[:5]}

                    ### Objetivo:
                    • Identifique se o cliente deseja um veículo específico, mas possui um valor abaixo do necessário.  
                    • Se sim, ofereça **alternativas compatíveis com o orçamento**.  
                    • Sempre destaque **1 benefício do consórcio Klubi**, e conclua com pedido de contato (e-mail/telefone) + agradecimento.

                    ### Exemplo de resposta para orçamento insuficiente:
                    "Entendo que você busca um [modelo mencionado], mas ele está acima do seu orçamento atual.  
                    Contudo, encontrei estas opções que se encaixam no seu perfil e valor disponível:  
                    • [Carro 1 – destaque curto]  
                    • [Carro 2 – destaque curto]  
                    Com o consórcio Klubi, você ainda garante [benefício relevante, como parcelas reduzidas ou crédito flexível].  
                    Se quiser mais informações ou uma simulação, envie seu e-mail ou telefone e um especialista entrará em contato em até 2 horas.  
                    Posso te ajudar com mais alguma coisa? Se não, agradeço pela preferência e desejo um excelente dia!"

                    ### Regras de comunicação:
                    [mesmas regras anteriores...]
                """

        response = model.generate_content(prompt)

        return jsonify({
            "success": True,
            "response": response.text,
            "cars": (affordable_cars[:5] if budget else filtered_cars[:5]),
            "suggestions": [f"{car['Name']} {car['Model']}" for car in (affordable_cars if budget else filtered_cars[:3])]
        })

    except Exception as e:
        return jsonify({
            "success": False,
            "error": str(e),
            "message": "Erro ao processar sua requisição"
        }), 500

if __name__ == '__main__':
    app.run(port=5000, debug=True)