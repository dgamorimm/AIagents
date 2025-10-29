import gradio as gd
from transformers import pipeline
from PIL import Image
from pysentimiento import create_analyzer

# Inicializando os pipelines
background_removal_model = pipeline("image-segmentation", model="briaai/RMBG-1.4", trust_remote_code=True)
image_captioning_model = pipeline("image-to-text", model="nlpconnect/vit-gpt2-image-captioning")

# Inicializando o analisador de sentimentos
model_analyser_sent = create_analyzer(task="sentiment", lang="pt")

def remove_background(img):
    # Executa o modelo de remoção de fundo
    output = background_removal_model(img, return_mask=True)
    image_pillow = background_removal_model(img)  # Aplica o modelo novamente para obter a imagem sem fundo
    return image_pillow

def generate_caption(img):
    captions = image_captioning_model(img)
    return captions[0]['generated_text']  # Retorna o texto gerado

def analyze_sentiment(text):
    result = model_analyser_sent.predict(text)
    return result.output

def process_input(input_type, img=None, text=None):
    if input_type == "Remover Fundo":
        processed_img = remove_background(img)
        return processed_img, None  # Retorna a imagem processada e None para o texto
    elif input_type == "Gerar Legenda":
        caption = generate_caption(img)
        return img, caption  # Retorna a imagem original e a legenda gerada
    elif input_type == "Análise de Sentimento":
        sentiment_result = analyze_sentiment(text)
        return None, sentiment_result  # Retorna None para a imagem e o resultado do sentimento

    return None, None  # Garante que sempre retornamos duas saídas

# Interface do Gradio
app = gd.Interface(
    title="Ferramentas de Imagem e Texto",
    description="Escolha uma opção: Remover fundo de imagem, gerar legenda para imagem ou analisar sentimento de texto.",
    fn=process_input,
    inputs=[
        gd.components.Radio(choices=["Remover Fundo", "Gerar Legenda", "Análise de Sentimento"], label="Escolha uma opção"),
        gd.components.Image(type="pil", label="Imagem (se aplicável)"),
        gd.components.Textbox(label="Texto (se aplicável)")
    ],
    outputs=[
        gd.components.Image(type="pil", format="png", label="Resultado da Imagem"),
        gd.components.Textbox(label="Sentimento ou Legenda")
    ],
)

if __name__ == "__main__":
    app.launch(share=True)
