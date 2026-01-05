import pandas as pd
from datetime import datetime
from pathlib import Path
import logging

# ===== 設定 =====
INPUT_CSV = Path("sample_input/input.csv")
OUTPUT_DIR = Path("sample_output")
OUTPUT_DIR.mkdir(exist_ok=True)

TODAY = datetime.now().strftime("%Y%m%d")
ESTIMATE_ID = f"EST-{TODAY}-001"
OUTPUT_FILE = OUTPUT_DIR / f"estimate_{TODAY}.xlsx"
LOG_FILE = OUTPUT_DIR / "process.log"

# ===== ログ設定 =====
logging.basicConfig(
    filename=LOG_FILE,
    level=logging.INFO,
    format="%(asctime)s [%(levelname)s] %(message)s"
)

def main():
    try:
        logging.info("Process started")

        # CSV読み込み
        df = pd.read_csv(INPUT_CSV)

        # 必須カラム確認
        required_columns = [
            "item_name",
            "quantity",
            "unit_price",
            "rush_flag",
            "discount_rate"
        ]
        for col in required_columns:
            if col not in df.columns:
                raise ValueError(f"Missing required column: {col}")

        # 計算処理
        def calculate_row(row):
            subtotal = row["quantity"] * row["unit_price"]

            if row["rush_flag"] == 1:
                subtotal *= 1.10  # 10% surcharge

            if pd.notna(row["discount_rate"]):
                subtotal *= (1 - row["discount_rate"])

            return round(subtotal, 2)

        df["subtotal"] = df.apply(calculate_row, axis=1)
        total_amount = df["subtotal"].sum()

        # 出力用データ整形
        summary_df = pd.DataFrame({
            "estimate_id": [ESTIMATE_ID],
            "date": [TODAY],
            "total_amount": [round(total_amount, 2)]
        })

        # Excel出力
        with pd.ExcelWriter(OUTPUT_FILE, engine="openpyxl") as writer:
            df.to_excel(writer, sheet_name="Details", index=False)
            summary_df.to_excel(writer, sheet_name="Summary", index=False)

        logging.info("Process completed successfully")

    except Exception as e:
        logging.error(f"Process failed: {e}")
        raise

if __name__ == "__main__":
    main()
