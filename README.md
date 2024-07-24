# placa

Este repositório contém uma aplicação Flask que fornece uma API e interface web para buscar informações sobre placas veiculares.

## Instalação

1. Clone este repositório:

   ```bash
   git clone https://github.com/fumireko/placa.git
   cd placa
   ```

2. Instale as dependências e inicie o servidor:

   ```bash
   pip install -r requirements.txt
   python main.py
   ```
   
## Uso

### Endpoint

- **Endpoint**: `/api/<placa>`
- **Método**: GET
- **Descrição**: Retorna informações detalhadas sobre a placa do veículo especificada.

### Exemplo 

```bash
curl http://localhost:5000/api/ABC1234
```

```json
{
  "UF": "PR",
  "ano": 1986,
  "chassi": "*****P246344",
  "cilindrada": 0,
  "combustivel": "Gasolina",
  "cor": "Vermelha",
  "especie": null,
  "fipe": [
    {
      "codigo_fipe": "005102-0",
      "modelo": "Santana CS/CD/CG",
      "valor": 8740.0
    }
  ],
  "importado": false,
  "marca": "VOLKSWAGEN",
  "modelo": "SANTANA CG",
  "motor": null,
  "municipio": "LOBATO",
  "placa": "abc1234",
  "potencia": 94,
  "segmento": "Auto"
}
```
