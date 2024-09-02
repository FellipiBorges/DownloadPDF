# PDFDownloader
Este projeto automatiza o download de arquivos a partir de uma lista de URLs, salva informações sobre o sucesso ou falha de cada download em uma planilha Excel, e realiza análises dos dados coletados, apresentando os resultados em gráficos interativos usando Plotly.

## Features

- Através de um link, você baixa o documento que está nesse link
- Em caso de erro, você visualiza os arquivos na planilha Excel gerada ou no resultado do Plotly


## Instalação

Para essa instalação, vamos utilizar o PyCharm para setar nosso ambiente de teste.

Instale o PyCharm - https://www.jetbrains.com/pt-br/pycharm/download/?section=windows

Após configurar sua IDE, faça o clone do repositorio.
```sh
git clone https://github.com/FellipiBorges/DownloadPDF
cd nome-do-repositorio
```

Dentro da IDE, baixe os packages necessarios para o programa ser executado.

```sh
requests
pandas
openpyxl
plotly
dash
```

## Saidas do App
Código que contém os links onde utilizaremos para baixar os arquivos.
![Saida do Código](https://github.com/user-attachments/assets/e1ebc0e7-d07f-4686-a580-94ce442b8a79)

Resultado do Excel após execução do código
![Saida do Excel](https://github.com/user-attachments/assets/68599f62-a2fb-4b4c-821e-7d9ed2e321d8)

Resultado do Plotly
![Saida do Plotly](https://github.com/user-attachments/assets/10caa366-48f5-4670-90e3-0ed170ba08b7)

Resultado da pasta com os arquivos baixados
[image](https://github.com/user-attachments/assets/f1a83609-5097-4555-9f9e-8dacd62986b5)



## License

MIT

**Software livre!**
