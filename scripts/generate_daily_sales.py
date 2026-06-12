import csv
import random
from datetime import datetime
from pathlib import Path

BASE_DIR = Path(__file__).resolve().parents[1]
OUTPUT_DIR = BASE_DIR / "data" / "generated"

OUTPUT_DIR.mkdir(parents=True, exist_ok=True)

today_date = datetime.today().strftime("%Y-%m-%d")
today_file = datetime.today().strftime("%Y%m%d")

output_file = OUTPUT_DIR / f"sales_{today_file}.csv"

store_distribution = {
    "STR-001": (250, 500),  # Madrid
    "STR-002": (200, 400),  # Barcelona
    "STR-003": (150, 300),  # Valencia
}

popular_products = [
    "PRD-001", "PRD-002", "PRD-005",
    "PRD-006", "PRD-009", "PRD-013"
]

regular_products = [
    "PRD-004", "PRD-007", "PRD-010", "PRD-011",
    "PRD-012", "PRD-014", "PRD-015", "PRD-016",
    "PRD-017", "PRD-018", "PRD-019"
]

low_rotation_products = [
    "PRD-003", "PRD-008", "PRD-020"
]

product_pool = (
    popular_products * 6
    + regular_products * 3
    + low_rotation_products * 1
)

quantity_pool = (
      [1] * 70
    + [2] * 20
    + [3] * 8
    + [4] * 1
    + [5] * 1
)

sales_rows = []
sale_counter = 1

for store_id, (min_sales, max_sales) in store_distribution.items():
    num_sales = random.randint(min_sales, max_sales)

    for _ in range(num_sales):
        sale_id = f"SAL-{today_file}-{sale_counter:04d}"

        sales_rows.append([
            sale_id,
            today_date,
            random.choice(product_pool),
            store_id,
            random.choice(quantity_pool),
        ])

        sale_counter += 1

with open(output_file, mode="w", newline="", encoding="utf-8") as file:
    writer = csv.writer(file)
    writer.writerow(["sale_id", "sale_date", "product_id", "store_id", "quantity"])
    writer.writerows(sales_rows)

print(f"Archivo generado: {output_file}")
print(f"Total ventas generadas: {len(sales_rows)}")
