Este projeto envolve a raspagem de avaliações de produtos de uma URL fornecida, seguido de um processamento detalhado dessas avaliações. O objetivo é extrair insights valiosos a partir de textos de avaliações, realizando etapas como limpeza, tokenização e correção ortográfica.

## Principais Funcionalidades:

- **Raspagem de Dados**: Utiliza a biblioteca BeautifulSoup para coletar avaliações de produtos de uma página da web.
- **Limpeza de Texto**: Remove ruídos como números, símbolos e espaços desnecessários, e aplica normalização ao texto.
- **Tokenização**: Segmenta o texto em palavras ou tokens utilizando a biblioteca NLTK.
- **Correção Ortográfica**: Corrige erros de digitação e ortografia nas avaliações coletadas.

## Tecnologias Utilizadas:

- Python
- Flask (framework web)
- BeautifulSoup (raspagem de dados)
- NLTK (tokenização e processamento de linguagem natural)
- SpellChecker (correção ortográfica)

## Como Usar:

1. Clone o repositório.
2. Instale as dependências listadas no `requirements.txt`.
3. Execute o aplicativo Flask e acesse a interface web.
4. Insira a URL do produto para começar a raspagem e processamento das avaliações (diretamente do mercado livre).

## Objetivo do Projeto:

O projeto visa facilitar a análise de avaliações de produtos, permitindo a identificação de padrões e sentimentos nas opiniões dos consumidores, assim como possibilitar melhorias contínuas no processo de processamento de linguagem natural.
"""


