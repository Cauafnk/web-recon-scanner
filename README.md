
Ferramenta em Python para análise de conteúdo web durante a fase de reconhecimento (recon) em testes de segurança (pentest).

 Descrição

O Web Recon Scanner permite buscar palavras-chave sensíveis dentro de páginas web e exibir o contexto onde elas aparecem.

É útil para identificar possíveis informações expostas como:
- admin
- password
- login
- token

 Funcionalidades

- Busca por múltiplas palavras-chave
- Exibição de contexto ao redor das ocorrências
- Destaque visual das palavras encontradas
- Interface via linha de comando (CLI)

 Uso

```bash
python scanner.py -u https://example.com -k admin,password
