# Clean Images API!

Um conjunto de microserviços utilizado para remover manchas e pequenas imperfeições de imagens de documentos\
Utilizando tecnicas de autoencoder


## Dependencias

1 - [docker](https://www.docker.com/get-started): Para criar e gerenciar containers \
2 - [docker-compose](https://docs.docker.com/compose/install/): Para gerenciar lotes de containers.


## Funcionamento:

1 - Clone o repositório para uma basta local \
2 - Verifique se o docker esta rodando \
3 - Execute o comando " docker-compose up -d " sem aspas \
4 - Acesse o swagger da api pelo endereço http://localhost:5000/ \
5 - Realize o upload das imagens em base64 utilizando o método POST\
    * Para gerar o encoding base64 da imagem [click aqui](https://base64.guru/converter/encode/image) \
6 - Realize o download das imagens limpa em Base64 utilizando o método GET \
7 - Exclua imagens utilizando o método DELETE


As imagens enviadas serão salvas na pasta resources/1.dirty \
Apos o processamento, a imagem limpa sera salva na pasta resources/2.cleaned


## Referencias:

[Denoising Noisy Documents](https://towardsdatascience.com/denoising-noisy-documents-6807c34730c4) por Chinmay Wyawahare, 2020