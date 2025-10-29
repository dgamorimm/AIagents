import gradio as gr
from transformers import pipeline

# Inicializando o pipeline de imagem para texto
image_to_text = pipeline("image-to-text", model="nlpconnect/vit-gpt2-image-captioning")

def generate_caption(image):
    # Gera a legenda para a imagem
    captions = image_to_text(image)
    return captions[0]['generated_text']  # Retorna o texto gerado

# Cria a interface do Gradio
interface = gr.Interface(
    fn=generate_caption,
    inputs=gr.components.Image(type="filepath"),
    outputs="text",
    title="Gerador de Legendas para Imagens",
    description="Envie uma imagem para gerar uma legenda automaticamente."
)

# Executa a aplicação
if __name__ == "__main__":
    interface.launch()
