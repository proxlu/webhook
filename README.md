# Webhook em Python com Flask

Este projeto implementa um webhook simples em Python usando o framework Flask. O webhook recebe dados via POST e armazena a última requisição, que pode ser recuperada via GET.

## Requisitos

- Python 3.7 ou superior
- Flask

## Instalação

1. Clone este repositório:

   ```bash
   git clone https://github.com/seu-usuario/meu-webhook-python.git
   cd meu-webhook-python
   ```

2. Crie um ambiente virtual e ative-o:

   ```bash
   python3 -m venv venv
   source venv/bin/activate  # No Windows, use `venv\Scripts\activate`
   ```

3. Instale as dependências:

   ```bash
   pip install Flask
   ```

## Executando o Webhook

Execute o servidor Flask com o seguinte comando:

```bash
python webhook.py
```

O servidor estará disponível em `http://localhost:5000`.

## Como usar

### Enviar dados via POST

Você pode enviar dados para o webhook usando uma requisição POST. Exemplo com `curl`:

```bash
curl -X POST http://localhost:5000/webhook \
-H "Content-Type: application/json" \
-d '{"message": "Olá, mundo!"}'
```

O webhook aceita dados em formato JSON. O corpo da requisição será armazenado e poderá ser recuperado posteriormente.

### Recuperar a última requisição via GET

Para recuperar a última requisição POST, faça uma requisição GET:

```bash
curl http://localhost:5000/webhook
```

A resposta será o último dado enviado via POST, em formato JSON. Se nenhum dado foi enviado ainda, a resposta será:

```json
"Nenhum dado POST recebido ainda."
```

## Exemplo de uso

1. Envie uma requisição POST:

   ```bash
   curl -X POST http://localhost:5000/webhook \
   -H "Content-Type: application/json" \
   -d '{"message": "Testando o webhook!"}'
   ```

2. Recupere a última requisição:

   ```bash
   curl http://localhost:5000/webhook
   ```

   Saída esperada:

   ```json
   {
     "message": "Testando o webhook!"
   }
   ```

## Estrutura do Projeto

```
webhook/
├── webhook.py      # Código principal do webhook
├── README.md       # Este arquivo
└── venv/           # Ambiente virtual (gerado automaticamente)
```

## Licença

Este projeto está licenciado sob a licença MIT. Veja o arquivo [LICENSE](LICENSE) para mais detalhes.
