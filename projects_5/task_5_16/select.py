import psycopg2



try:

    # Устанавливаем соединение

    connection = psycopg2.connect(

        host="localhost",          # База в контейнере, но доступна через localhost

        port="5432",               # Порт из секции ports

        user="postgres",           # POSTGRES_USER

        password="example",        # POSTGRES_PASSWORD

        database="testdb"          # POSTGRES_DB

    )

    cursor = connection.cursor()



    # 1. Выполняем запрос

    cursor.execute("SELECT name, category FROM products;")



    # 2. Извлекаем все строки

    products = cursor.fetchall()



    for product in products:

        print(f"Продукт: {product[0]} {product[1]}")



    # Не забываем закрыть курсор

    cursor.close()



except Exception as error:

    print(f"Ошибка при подключении: {error}")