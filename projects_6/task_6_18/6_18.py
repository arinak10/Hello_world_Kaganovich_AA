import psycopg2
import pandas as pd
try:
    # Устанавливаем соединение
    connection = psycopg2.connect(
        host="localhost",          # База в контейнере, но доступна через localhost
        port="5432",               # Порт из секции ports
        user="postgres",           # POSTGRES_USER
        password="example",        # POSTGRES_PASSWORD
        database="testdb"          # POSTGRES_DB
    )
    print("✓ Подключение установлено")
except Exception as error:
    print(f"Ошибка при подключении: {error}")

query = """
SELECT
    p.id AS product_id,
    p.name AS product_name,
    p.category,
    pr.price,
    pr.created_at
FROM prices pr
JOIN products p ON pr.product_id = p.id
ORDER BY p.category, p.name, pr.created_at
"""
df = pd.read_sql(query, connection)
df['price_rub'] = df['price'].apply(lambda x: f"{x:,.2f} руб.")
print(df[['product_id', 'product_name', 'category', 'price_rub', 'created_at']].head(10))
print(df.info())
print(f"\nВсего записей: {len(df)}")
print(f"Уникальных продуктов: {df['product_id'].nunique()}")
print(f"Уникальных категорий: {df['category'].nunique()}")
print("\n=== describe() (в руб.) ===")
print(df['price'].describe().round(2))
print("\n=== Метрики вручную ===")
metrics = {
    'Среднее (mean)' : df['price'].mean(),
    'Медиана (median)' : df['price'].median(),
    'Ст. отклонение (std)' : df['price'].std(),
    'Минимум (min)' : df['price'].min(),
    'Максимум (max)' : df['price'].max(),
}
for name, val in metrics.items():
    print(f" {name:30s}: {val:,.2f} руб.")

q1  = df['price'].quantile(0.25)
q2  = df['price'].quantile(0.50)
q3  = df['price'].quantile(0.75)
iqr = q3 - q1
print(f"Q1  (25%): {q1}")
print(f"Q2  (50%): {q2}")
print(f"Q3  (75%): {q3}")
print(f"IQR (Q3-Q1): {iqr}")
pct_q3 = (df['price'] > q3 ).mean()
print(f"\nцена превышает Q3: {pct_q3:.2f} ")

by_category = df.groupby('category')['price'].agg(
    count='count',
    mean='mean',
    median='median',
    std='std',
    min='min',
    max='max'
).round(2)
print("\n=== Цены ===")
print(by_category)

by_name = df.groupby('product_name').agg(
    min_price=('price', 'min'),
    max_price=('price', 'max')
).reset_index()
by_name['price_diff'] = by_name['max_price'] - by_name['min_price']
top5 = by_name.nlargest(5, 'price_diff')
print("\n=== ТОП-5 товаров с наибольшим разбросом цен ===\n")
for _, row in top5.iterrows():
    print(f"Товар: {row['product_name']})")
    print(f"  Мин. цена: {row['min_price']:,.2f} руб.")
    print(f"  Макс. цена: {row['max_price']:,.2f} руб.")
    print(f"  Разница: {row['price_diff']:,.2f} руб.\n")