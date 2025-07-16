Video: https://youtu.be/0gwKRezvYx8

Passos para extrair e rodar o servidor de um projeto Django:
1. Certifique-se de ter o Django instalado
Primeiro, você precisa garantir que o Django está instalado no seu ambiente. Se você ainda não tiver o Django instalado, pode instalá-lo com o pip:

bash
Copy
Edit
pip install django
2. Verifique o diretório do seu projeto Django
Normalmente, seu projeto Django terá a seguinte estrutura de diretórios:

markdown
Copy
Edit
meu_projeto/
    manage.py
    meu_projeto/
        __init__.py
        settings.py
        urls.py
        wsgi.py
    app1/
    app2/
    ...
O arquivo mais importante para rodar o servidor é o manage.py, que fica na raiz do seu projeto. Ele é usado para interagir com seu projeto Django.

3. Inicie o servidor de desenvolvimento
Com o Django instalado e o projeto configurado, você pode rodar o servidor de desenvolvimento usando o comando runserver:

No terminal, navegue até a pasta onde está o arquivo manage.py (normalmente na raiz do seu projeto Django) e execute o comando:

bash
Copy
Edit
python manage.py runserver
4. Acesse o servidor de desenvolvimento
Após rodar o comando acima, o servidor estará em funcionamento. Por padrão, o Django roda o servidor na URL http://127.0.0.1:8000/. Abra o navegador e digite essa URL para acessar a página inicial do seu projeto Django.

Se você rodar o Django localmente, ele estará disponível no seu localhost ou 127.0.0.1 na porta 8000.

Você pode especificar uma porta diferente, se necessário. Por exemplo, para rodar o servidor na porta 8080:

bash
Copy
Edit
python manage.py runserver 8080
5. Verifique o status do servidor
Depois de rodar o comando, o terminal mostrará algo assim:

pgsql
Copy
Edit
Starting development server at http://127.0.0.1:8000/
Quit the server with CONTROL-C.
Se aparecer esse tipo de mensagem, significa que o servidor está funcionando corretamente.
