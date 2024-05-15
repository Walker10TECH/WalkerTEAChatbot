
import google.generativeai as genai

GOOGLE_API_KEY="AIzaSyDtzOBprQ3AvPrtieLJJjVf69X_PkotWT4"
genai.configure(api_key=GOOGLE_API_KEY)

# List available models
for m in genai.list_models():
    if 'generateContent' in m.supported_generation_methods:
        print(m.name)

# Define generation configuration and safety settings
generation_config = {
    "candidate_count": 1,
    "temperature": 1
}

safety_settings = {
    'HATE': 'BLOCK_NONE',
    'HARASSMENT': 'BLOCK_NONE',
    'SEXUAL' : 'BLOCK_NONE',
    'DANGEROUS' : 'BLOCK_NONE'
}

# Inicializar o modelo generativo
model = genai.GenerativeModel(model_name='gemini-1.0-pro-latest',
    generation_config=generation_config,
    safety_settings=safety_settings
)

# Função para processar o comando com base nas palavras-chave
def process_command(command):
    if "rotina" in command:
        rotina_response = model.generate_content("Dicas para organizar a rotina diária e facilitar as atividades do dia a dia.")['candidates'][0]['text']
        print(f"Aqui estão algumas dicas para ajudar nas rotinas:\n{rotina_response}")
    elif "alimentação" in command:
        alimentacao_response = model.generate_content("Dicas para uma alimentação saudável e equilibrada.")['candidates'][0]['text']
        print(f"Aqui estão algumas dicas de alimentação saudável:\n{alimentacao_response}")
    elif "controle emocional" in command:
        emocional_response = model.generate_content("Dicas para manter o controle emocional em situações desafiadoras.")['candidates'][0]['text']
        print(f"Aqui estão algumas dicas para manter o controle emocional:\n{emocional_response}")
    elif "brincadeiras" in command:
        brincadeiras_response = model.generate_content("Explore brincadeiras nas quais as crianças precisam esperar sua vez. Jogos com bola, amarelinha e jogo da memória são excelentes opções.")['candidates'][0]['text']
        print(f"Aqui estão algumas dicas de brincadeiras para promover o desenvolvimento social:\n{brincadeiras_response}")
    elif "adapte o ambiente" in command:
        adaptar_response = model.generate_content("Adapte o ambiente para atender às necessidades específicas do autista, como reduzir o ruído e a luminosidade.")['candidates'][0]['text']
        print(f"Aqui estão algumas dicas para adaptar o ambiente para pessoas com TEA:\n{adaptar_response}")
    elif "estratégias de relaxamento" in command:
        relaxamento_response = model.generate_content("Use estratégias de relaxamento, como técnicas de respiração e meditação, para ajudar a reduzir o estresse e a ansiedade.")['candidates'][0]['text']
        print(f"Aqui estão algumas estratégias de relaxamento para pessoas com TEA:\n{relaxamento_response}")
    elif "educação alimentar" in command:
        educacao_response = model.generate_content("Pratique comportamentos alimentares agradáveis e saudáveis durante as refeições em família.")['candidates'][0]['text']
        print(f"Aqui estão algumas dicas para promover uma educação alimentar positiva:\n{educacao_response}")
    elif "direitos do autista" in command:
        direitos_response = model.generate_content("Promova a conscientização sobre os direitos das pessoas com TEA e defenda a inclusão e a igualdade de oportunidades.")['candidates'][0]['text']
        print(f"Aqui estão algumas informações sobre os direitos do autista:\n{direitos_response}")
    else:
        print(f"Desculpe, não entendi o que você quis dizer com '{command}'.")

# Iniciar a conversa
print("Bem-vindo(a) ao ChatBot para Pessoas com TEA da WalkerTECH®️!")
user_name = input("Por favor, digite seu nome: ")
user_age = int(input("Digite sua idade: "))  # Solicitar a idade do usuário

print(f"Prazer em conhecê-lo, {user_name}! Em que posso te ajudar? Aqui estão algumas palavras-chave que você pode usar: rotina, alimentação, controle emocional, brincadeiras, adapte o ambiente, estratégias de relaxamento, educação alimentar, direitos do autista.")

chat = model.start_chat(history=[])
chat.send_message(user_name)

while True:
    user_input = input("Você: ")

    if user_input.lower() == "fim":
        print("Até mais!")
        break

    response = chat.send_message(user_input)
    response_text = response.text

    if "comando" in response_text:
        command = response_text.split(": ")[1].strip()
        process_command(command)
    else:
        print("Resposta:", response_text)