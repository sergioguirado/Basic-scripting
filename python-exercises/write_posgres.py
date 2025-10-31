from sqlalchemy import create_engine, text

# URL de conexión a PostgreSQL
# 🔹 Cambia testuser / testpass / your_db si usas otros valores
DB_URL = "postgresql+psycopg2://testuser:testpass@localhost:5432/your_db"


def create_table():
    """
    Crea la tabla 'sales' si no existe.
    """
    engine = create_engine(DB_URL)

    create_query = text("""
    CREATE TABLE IF NOT EXISTS sales (
        id SERIAL PRIMARY KEY,
        product VARCHAR(50),
        price NUMERIC,
        quantity INT
    );
    """)

    with engine.begin() as conn:
        conn.execute(create_query)

    print("✅ Tabla 'sales' verificada o creada correctamente.")


def write_to_postgres(data):
    """
    Inserta una lista de diccionarios en la tabla 'sales'.
    """
    engine = create_engine(DB_URL)

    insert_query = text("""
        INSERT INTO sales (product, price, quantity)
        VALUES (:product, :price, :quantity)
    """)

    with engine.begin() as conn:
        conn.execute(insert_query, data)

    print(f"✅ {len(data)} filas insertadas correctamente.")


def read_sales():
    from sqlalchemy import create_engine, text
    engine = create_engine(DB_URL)

    with engine.connect() as conn:
        result = conn.execute(text("SELECT * FROM sales"))
        rows = result.mappings().all()   # ← devuelve dict-like

    print("\n📊 Contenido de la tabla 'sales':")
    for row in rows:
        print(dict(row))                 # ← ahora sí



def main():
    # 1️⃣ Crear la tabla si no existe
    create_table()

    # 2️⃣ Datos de ejemplo
    sales_data = [
        {"product": "shoes", "price": 50, "quantity": 3},
        {"product": "shirt", "price": 30, "quantity": 2},
        {"product": "pants", "price": 60, "quantity": 1},
    ]

    # 3️⃣ Insertar datos
    write_to_postgres(sales_data)

    # 4️⃣ Mostrar contenido
    read_sales()


if __name__ == "__main__":
    main()
