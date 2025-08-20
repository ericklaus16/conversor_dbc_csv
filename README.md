# Conversor DBC para CSV do SUS

Este projeto foi criado para facilitar o acesso e análise dos dados públicos disponibilizados pelo SUS (Sistema Único de Saúde) do Brasil. O SUS fornece grandes bases de dados em formato `.dbc`, que não é facilmente manipulado por ferramentas comuns. Este conversor automatiza a leitura de todos os arquivos `.dbc` de uma pasta e os converte para o formato `.csv`, que pode ser aberto em Excel, LibreOffice, Python, R, etc.

## Por que este projeto é útil?

O SUS publica dados abertos em formato `.dbc`, que é um formato binário específico e pouco acessível para a maioria dos usuários. Com este projeto, você pode transformar rapidamente todos os arquivos `.dbc` em `.csv`, facilitando a análise, visualização e integração dos dados em outros sistemas.

## Como usar

1. Coloque todos os arquivos `.dbc` que deseja converter na pasta `dbc/`.
2. Ative o ambiente virtual (se necessário) e instale as dependências:
   ```bash
   pip install -r requirements.txt
   ```
3. Execute o script de conversão:
   ```bash
   python convert.py
   ```
4. Os arquivos `.csv` convertidos aparecerão na pasta `csv/`.

## Dependências e versões

> **Atenção:** É fundamental que as bibliotecas estejam exatamente nas versões especificadas no arquivo `requirements.txt`. Isso garante a compatibilidade entre as bibliotecas, especialmente entre `pyreaddbc`, `pandas` e `numpy`, evitando erros de execução. Além disso, o sistema só consegue rodar em sistemas **Linux** por conta da dependência do pacote `setuptools`.

Se precisar reinstalar as dependências, use:
```bash
pip install --force-reinstall -r requirements.txt
```

## Licença

Este projeto é livre para uso e modificação.
