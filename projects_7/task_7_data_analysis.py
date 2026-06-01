import psycopg2
import pandas as pd
import matplotlib.pyplot as plt
import matplotlib.gridspec as gridspec
from matplotlib.patches import Patch

# БЛОК 1: ПОДКЛЮЧЕНИЕ И ИЗВЛЕЧЕНИЕ ДАННЫХ
try:
    connection = psycopg2.connect(
        host="localhost",
        port="5432",
        user="postgres",
        password="example",
        database="testdb"
    )
    print("✓ Подключение установлено")

    # --- Запрос 1: средняя цена и количество товаров по каждой категории ---
    df_categories = pd.read_sql("""
        SELECT
            p.category,
            ROUND(AVG(pr.price)::numeric, 2) AS avg_price,
            COUNT(DISTINCT p.id) AS total_products
        FROM products p
        JOIN prices pr ON p.id = pr.product_id
        WHERE p.category IS NOT NULL
        GROUP BY p.category
        ORDER BY avg_price DESC
    """, connection)

    # --- Запрос 2: самая актуальная цена для каждого товара ---
    df_current_prices = pd.read_sql("""
        SELECT
            p.name,
            p.category,
            pr.price
        FROM products p
        JOIN prices pr ON p.id = pr.product_id
        WHERE (pr.product_id, pr.created_at) IN (
            SELECT product_id, MAX(created_at)
            FROM prices
            GROUP BY product_id
        )
        ORDER BY p.category, p.name
    """, connection)

    # --- Запрос 3: все цены — для гистограммы распределения ---
    df_all_prices = pd.read_sql("SELECT price FROM prices", connection)

    # --- Запрос 4: аномалии — товары, у которых нет поставщиков ---
    df_missing_suppliers = pd.read_sql("""
        SELECT
            p.name AS product,
            p.category
        FROM products p
        LEFT JOIN suppliers s ON p.id = s.product_id
        WHERE s.id IS NULL
        ORDER BY p.category, p.name
    """, connection)

    print(f"Категорий в выборке: {len(df_categories)}")
    print(f"Всего цен в истории: {len(df_all_prices)}")
    print(f"Товаров без поставщиков (аномалии): {len(df_missing_suppliers)}")

    # --- Запрос 5: количество поставщиков по категориям (для графика 3) ---
    df_suppliers_per_category = pd.read_sql("""
        SELECT
            p.category,
            COUNT(DISTINCT s.id) AS total_suppliers
        FROM products p
        JOIN suppliers s ON p.id = s.product_id
        WHERE p.category IS NOT NULL
        GROUP BY p.category
        ORDER BY total_suppliers DESC
    """, connection)

except Exception as error:
    print(f"Ошибка подключения: {error}")
    raise SystemExit
finally:
    connection.close()
    print("✓ Соединение закрыто\n")

# БЛОК 2: ПОДГОТОВКА ДАННЫХ ДЛЯ ГРАФИКОВ
# Порог «нормы» — товары дешевле этого выделим цветом
PRICE_THRESHOLD = df_categories["avg_price"].median()

# Цвет столбца: синий — выше медианы, оранжевый — ниже
bar_colors = [
    "#d9534f" if price < PRICE_THRESHOLD else "#4a90d9"
    for price in df_categories["avg_price"]
]

# Подписи для круговой диаграммы (используем количество товаров)
pie_labels = [
    f"{row.category} ({row.total_products} шт.)"
    for row in df_categories.itertuples()
]


# БЛОК 3: ПОСТРОЕНИЕ ГРАФИКОВ
plt.rcParams.update({
    "font.family": "DejaVu Sans",
    "font.size": 10,
    "axes.spines.top": False,
    "axes.spines.right": False,
    "axes.grid": True,
    "grid.alpha": 0.3,
    "grid.linestyle": "--",
    "figure.dpi": 130,
})

fig = plt.figure(figsize=(16, 10))
fig.suptitle("Анализ товаров, цен и поставщиков", fontsize=15, fontweight="bold", y=1.01)

gs = gridspec.GridSpec(2, 3, figure=fig,
                       height_ratios=[5, 4],
                       width_ratios=[2, 1, 2],
                       hspace=0.45, wspace=0.35)

# ax1 — средняя цена по категориям (горизонтальный)
ax1 = fig.add_subplot(gs[0, 0:2])
# ax2 — количество товаров в категориях (круговая диаграмма)
ax2 = fig.add_subplot(gs[0, 2])
# ax3 — распределение актуальных цен по категориям ( bar)
ax3 = fig.add_subplot(gs[1, 0])
# ax4 — гистограмма распределения всех цен 
ax4 = fig.add_subplot(gs[1, 1:3])

# ── ГРАФИК 1: Горизонтальная столбчатая — средняя цена по категориям ──
bars1 = ax1.barh(
    df_categories["category"],
    df_categories["avg_price"],
    color=bar_colors,
    edgecolor="white",
    height=0.6,
)

# Подпись значения на конце каждого столбца
for bar, val in zip(bars1, df_categories["avg_price"]):
    ax1.text(
        bar.get_width() + 1.0,
        bar.get_y() + bar.get_height() / 2,
        f"{val:.2f}",
        va="center", fontsize=9,
    )

# Пунктирная вертикальная линия — общая медиана цен
median_price = df_categories["avg_price"].median()
ax1.axvline(median_price, color="darkorange", linestyle="--",
            linewidth=1.3, label=f"Медиана: {median_price:.2f}")

ax1.set_xlabel("Средняя цена (руб.)")
ax1.set_title("Средняя цена по категориям товаров", fontweight="bold", pad=8)

# Легенда цветов
legend_patches = [
    Patch(facecolor="#4a90d9", label=f"Выше медианы (≥ {median_price:.2f})"),
    Patch(facecolor="#d9534f", label="Ниже медианы"),
]
ax1.legend(handles=legend_patches, fontsize=8, loc="lower right")

# ── ГРАФИК 2: Круговая диаграмма — количество товаров по категориям ──
pie_colors = ["#7b68ee", "#4a90d9", "#2ecc71", "#f0ad4e", "#d9534f"]

wedges, texts, autotexts = ax2.pie(
    df_categories["total_products"],
    labels=None,
    autopct="%1.0f%%",
    colors=pie_colors[:len(df_categories)],  # чтобы не было ошибки, если категорий < 5
    startangle=90,
    wedgeprops={"edgecolor": "white", "linewidth": 1.5},
    pctdistance=0.7,
)

for autotext in autotexts:
    autotext.set_fontsize(10)
    autotext.set_fontweight("bold")

ax2.set_title("Количество товаров\nпо категориям", fontweight="bold", pad=8)

ax2.legend(
    wedges, pie_labels,
    loc="lower center",
    bbox_to_anchor=(0.5, -0.22),
    fontsize=8,
    frameon=False,
)

# ── ГРАФИК 3: Средняя актуальная цена на товар внутри категорий ──
# Считаем, сколько уникальных поставщиков приходится на каждую категорию
bars3 = ax3.bar(
    df_suppliers_per_category["category"],
    df_suppliers_per_category["total_suppliers"],
    color="#5cb85c",
    edgecolor="white",
    width=0.6,
)

# Подпись значения над каждым столбцом
for bar, val in zip(bars3, df_suppliers_per_category["total_suppliers"]):
    ax3.text(
        bar.get_x() + bar.get_width() / 2,
        bar.get_height() + 0.15,
        str(val),
        ha="center", fontsize=9,
    )

ax3.set_ylabel("Количество поставщиков")
ax3.set_title("Поставщики\nпо категориям", fontweight="bold", pad=8)
ax3.set_xticks(range(len(df_suppliers_per_category)))
ax3.set_xticklabels(df_suppliers_per_category["category"], rotation=40, ha="right", fontsize=8)

# Горизонтальная линия — среднее количество поставщиков
mean_suppliers = df_suppliers_per_category["total_suppliers"].mean()
ax3.axhline(mean_suppliers, color="crimson", linestyle="--", linewidth=1.2,
            label=f"Среднее: {mean_suppliers:.1f}")
ax3.legend(fontsize=8)

# ── ГРАФИК 4: Гистограмма распределения всех цен ──
# Используем hist() вместо bar() для автоматического подбора корзин
n, bins, patches = ax4.hist(
    df_all_prices["price"],
    bins=15,  # 15 корзин — хороший баланс между детализацией и читаемостью
    color="#f0ad4e",
    edgecolor="white",
    alpha=0.8
)

# Подпись количества над каждым столбцом
for count, patch in zip(n, patches):
    if count > 0:  # подписываем только непустые столбцы
        ax4.text(
            patch.get_x() + patch.get_width() / 2,
            count + max(n) * 0.02,  # чуть выше столбца
            str(int(count)),
            ha="center", fontsize=8,
        )

# Вертикальная линия — медиана
median_all = df_all_prices["price"].median()
ax4.axvline(median_all, color="crimson", linestyle="--", linewidth=1.5,
            label=f"Медиана: {median_all:.2f} руб.")

# Вертикальная линия — среднее
mean_all = df_all_prices["price"].mean()
ax4.axvline(mean_all, color="blue", linestyle=":", linewidth=1.5,
            label=f"Среднее: {mean_all:.2f} руб.")

ax4.set_xlabel("Цена (руб.)")
ax4.set_ylabel("Количество записей")
ax4.set_title("Распределение всех цен в истории", fontweight="bold", pad=8)
ax4.legend(fontsize=8)

# Вспомогательный текст с ключевыми метриками
stats_text = (
    f"Всего записей: {len(df_all_prices)}\n"
    f"Среднее: {mean_all:.2f} руб.\n"
    f"Медиана: {median_all:.2f} руб.\n"
    f"Ст. откл.: {df_all_prices['price'].std():.2f}"
)
ax4.text(0.97, 0.95, stats_text,
         transform=ax4.transAxes,
         va="top", ha="right", fontsize=8,
         bbox={"boxstyle": "round,pad=0.4", "facecolor": "lightyellow",
               "edgecolor": "lightgray", "alpha": 0.8})

# Аномалия на отдельном текстовом блоке под всей фигурой
# Предварительно получим общее количество продуктов
try:
    temp_conn = psycopg2.connect(
        host="localhost",
        port="5432",
        user="postgres",
        password="example",
        database="testdb"
    )
    total_products = pd.read_sql("SELECT COUNT(*) as cnt FROM products", temp_conn)["cnt"].iloc[0]
    temp_conn.close()
except:
    total_products = "?"

fig.text(
    0.5, -0.03,
    f"⚠ Аномалия: {len(df_missing_suppliers)} из {total_products} товаров "
    "не имеют ни одного поставщика (отсутствуют в таблице suppliers)",
    ha="center", fontsize=9, color="#8b0000",
    bbox={"boxstyle": "round,pad=0.4", "facecolor": "#fff3f3", "edgecolor": "#d9534f"}
)

# БЛОК 4: СОХРАНЕНИЕ
OUTPUT_FILE = "products_charts.png"
plt.savefig(OUTPUT_FILE, bbox_inches="tight", dpi=150)
print(f"✓ График сохранён: {OUTPUT_FILE}")
plt.show()