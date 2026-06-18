# API de Carros (Flask)

API REST desenvolvida em **Flask** para gerenciar um cadastro de carros, com todas as operações **CRUD** (Create, Read, Update, Delete). Os dados ficam em uma estrutura em memória (`bd.py`), simulando um banco de dados.

## Tecnologias
- Python 3
- Flask

## Estrutura
| Arquivo | Descrição |
|---------|-----------|
| `main.py` | Definição da API e das rotas |
| `bd.py` | "Banco de dados" em memória (lista de carros) |

## Endpoints
| Método | Rota | Descrição |
|--------|------|-----------|
| `GET` | `/carros` | Lista todos os carros |
| `GET` | `/carros/<id>` | Retorna um carro por ID |
| `POST` | `/carros` | Cadastra um novo carro |
| `PUT` | `/carros/<id>` | Atualiza um carro existente |
| `DELETE` | `/carros/<id>` | Remove um carro |

## Como executar
```bash
pip install -r requirements.txt
python main.py
```
A API ficará disponível em `http://localhost:5000`.

### Exemplo de requisição (POST)
```json
{
  "id": 6,
  "marca": "Toyota",
  "modelo": "Corolla",
  "ano": 2022
}
```
