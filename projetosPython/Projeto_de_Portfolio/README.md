# Projeto Django de Blog e Portfólio

Este projeto é uma aplicação Django que inclui funcionalidades para postagens de blog, comentários, gerenciamento de projetos e solicitações de serviços.

## Modelos

### Postagem

O modelo `Postagem` contém os seguintes campos:

- `autor`: Chave estrangeira para o modelo `User` do Django.
- `titulo`: Título da postagem (máximo de 200 caracteres).
- `conteudo`: Conteúdo da postagem.
- `criado_em`: Data e hora de criação da postagem.
- `atualizado_em`: Data e hora da última atualização da postagem.

### Comentario

O modelo `Comentario` contém os seguintes campos:

- `postagem`: Chave estrangeira para o modelo `Postagem`, com relação nomeada `comentarios`.
- `usuario`: Chave estrangeira para o modelo `User` do Django.
- `conteudo`: Conteúdo do comentário.
- `criado_em`: Data e hora de criação do comentário.
- `atualizado_em`: Data e hora da última atualização do comentário.

### Project

O modelo `Project` contém os seguintes campos:

- `title`: Título do projeto (máximo de 100 caracteres).
- `description`: Descrição do projeto.
- `technology`: Tecnologia usada no projeto (máximo de 20 caracteres).
- `image`: Imagem do projeto, armazenada no S3.

### SolicitacaoServico

O modelo `SolicitacaoServico` contém os seguintes campos:

- `nome_completo`: Nome completo do solicitante (máximo de 255 caracteres).
- `email`: Email do solicitante.
- `whatsapp`: Número de WhatsApp do solicitante (máximo de 15 caracteres).
- `servico`: Tipo de serviço solicitado, com as seguintes opções:
  - `portfolio`: Portfólio
  - `blog`: Blog
  - `site`: Site

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