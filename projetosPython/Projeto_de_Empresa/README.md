# Projeto Django de Gestão de Empresas

Este projeto é uma aplicação Django para gerenciar informações sobre empresas, incluindo seu estágio de desenvolvimento, área de atuação, tempo de existência, entre outros.

## Modelos

### Empresas

O modelo `Empresas` contém os seguintes campos:

- `user`: Chave estrangeira para o modelo `User` do Django.
- `nome`: Nome da empresa (máximo de 50 caracteres).
- `cnpj`: CNPJ da empresa (máximo de 30 caracteres).
- `site`: URL do site da empresa.
- `tempo_existencia`: Tempo de existência da empresa, com as seguintes opções:
  - `-6`: Menos de 6 meses
  - `+6`: Mais de 6 meses
  - `+1`: Mais de 1 ano
  - `+5`: Mais de 5 anos
- `descricao`: Descrição da empresa.
- `data_final_captacao`: Data final de captação.
- `percentual_equity`: Percentual de equity esperado.
- `estagio`: Estágio da empresa, com as seguintes opções:
  - `I`: Tenho apenas uma ideia
  - `MVP`: Possuo um MVP
  - `MVPP`: Possuo um MVP com clientes pagantes
  - `E`: Empresa pronta para escalar
- `area`: Área de atuação da empresa, com as seguintes opções:
  - `ED`: Ed-tech
  - `FT`: Fintech
  - `AT`: Agrotech
- `publico_alvo`: Público alvo da empresa.
- `valor`: Valor total a ser vendido.
- `pitch`: Arquivo de pitch da empresa.
- `logo`: Arquivo de logo da empresa.

Crie um ambiente virtual e ative-o:
    ```bash
    python -m venv venv
    source venv/bin/activate  # No Windows use `venv\Scripts\activate`
    ```

3. Instale as dependências:
    ```bash
    pip install -r requirements.txt
    ```

4. Execute as migrações:
    ```bash
    python manage.py migrate
    ```

5. Inicie o servidor de desenvolvimento:
    ```bash
    python manage.py runserver
    ```

## Uso

Após iniciar o servidor, acesse `http://127.0.0.1:8000/` no seu navegador para usar a aplicação.

## Contribuição

Contribuições são bem-vindas! Sinta-se à vontade para abrir issues e pull requests.

## Licença

Este projeto está licenciado sob a licença MIT. Veja o arquivo LICENSE para mais detalhes.