import csv
import random
from datetime import datetime
from pathlib import Path

BASE_DIR = Path(__file__).resolve().parents[1]
OUTPUT_DIR = BASE_DIR / "data" / "generated"

OUTPUT_DIR.mkdir(parents=True, exist_ok=True)

today = datetime.today().strftime("%Y_%m_%d")
output_file = OUTPUT_DIR / f"ventas_{today}.csv"

products = list(range(1, 21))
stores = [1, 2, 3]

min_sales = 600
max_sales = 1200
num_sales = random.randint(min_sales, max_sales)

with open(output_file, mode="w", newline="", encoding="utf-8") as file:
    writer = csv.writer(file)
    writer.writerow(["venta_id", "fecha", "producto_id", "tienda_id", "cantidad"])

    for sale_id in range(1, num_sales + 1):
        writer.writerow([
            sale_id,
            datetime.today().strftime("%Y-%m-%d"),
            random.choice(products),
            random.choice(stores),
            random.randint(1, 5)
        ])

print(f"Archivo generado: {output_file}")
print(f"Total ventas generadas: {num_sales}")
