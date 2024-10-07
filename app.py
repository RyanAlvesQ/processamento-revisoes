from flask import Flask, render_template, request
import requests
from bs4 import BeautifulSoup
import re
import time
import nltk

# Inicializar NLTK
nltk.download('punkt')

app = Flask(__name__)

# Função de raspagem de dados
def scrape_reviews(url):
    start_time = time.time()
    response = requests.get(url)
    soup = BeautifulSoup(response.text, 'html.parser')
    
    # Raspagem das avaliações do site
    review_elements = soup.find_all('article', class_='ui-review-capability-comments__comment')  # Ajustar a classe conforme o site
    reviews = []
    for review in review_elements:
        text = review.get_text(" ", strip=True)
        formatted_text = ' '.join(text.split())  # Remove espaços extras
        reviews.append(formatted_text)
    
    end_time = time.time()
    scrape_time = end_time - start_time
    return reviews, scrape_time  # Retorna o tempo da raspagem

# Função para limpar ruídos (remover números, símbolos, etc.)
def clean_text(text):
    start_time = time.time()
    pattern = r'\b[a-zA-Z]+\b'  # Mantém apenas palavras
    cleaned_tokens = re.findall(pattern, text)
    end_time = time.time()
    clean_time = end_time - start_time
    return cleaned_tokens, clean_time

# Função de tokenização usando NLTK
def tokenize_nltk(text):
    start_time = time.time()
    tokens = nltk.word_tokenize(text)
    end_time = time.time()
    return tokens, end_time - start_time

@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        url = request.form.get('url')
        
        # Raspagem de dados
        reviews, scrape_time = scrape_reviews(url)
        
        # Inicializando variáveis para medir os tempos totais
        clean_time_total = 0
        nltk_time_total = 0
        
        processed_reviews = []
        
        for review in reviews:
            # Limpeza de ruído
            cleaned_review, clean_time = clean_text(review)
            clean_time_total += clean_time
            
            # Tokenização com NLTK
            nltk_tokens, nltk_time = tokenize_nltk(" ".join(cleaned_review))
            nltk_time_total += nltk_time
            
            # Adicionando os resultados processados
            processed_reviews.append({
                'original': review,
                'cleaned': cleaned_review,
                'nltk_tokens': nltk_tokens
            })
        
        # Retornar os resultados e os tempos de cada etapa
        return render_template('index.html', 
                               reviews=processed_reviews, 
                               scrape_time=scrape_time, 
                               clean_time=clean_time_total, 
                               nltk_time=nltk_time_total)
    return render_template('index.html')

if __name__ == '__main__':
    app.run(debug=True)
