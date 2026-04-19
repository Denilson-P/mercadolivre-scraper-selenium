import pandas as pd
from pathlib import Path


def clean_price_column(df):
    df["price"] = (
        df["price"]
        .astype(str)
        .str.replace(".", "", regex=False)
        .str.replace(",", ".", regex=False)
    )

    df["price"] = pd.to_numeric(df["price"], errors="coerce")
    return df


def get_brand(title):
    brands = ["Dell", "Acer", "Lenovo", "Samsung", "Asus", "HP"]
    for brand in brands:
        if brand.lower() in str(title).lower():
            return brand
    return "Other"


def analyze_data(df):
    df = df.copy()

    df = clean_price_column(df)
    df = df.dropna(subset=["price"])

    df["brand"] = df["title"].apply(get_brand)

    df_sorted = df.sort_values(by="price")

    cheapest = df_sorted.iloc[0]
    most_expensive = df_sorted.iloc[-1]
    average_price = df["price"].mean()

    price_by_brand = (
    df.groupby("brand")["price"]
    .agg(["mean", "min", "max", "count"])
    .sort_values(by="mean")
    .reset_index()

)

    return df, df_sorted, cheapest, most_expensive, average_price, price_by_brand


def analyze_price_range(df, min_price=800):
    price_range = df[df["price"] > min_price]

    if price_range.empty:
        return price_range, None, None

    price_range_sorted = price_range.sort_values(by="price")

    cheapest = price_range_sorted.iloc[0]
    most_expensive = price_range_sorted.iloc[-1]

    return price_range_sorted, cheapest, most_expensive


def generate_report(
    df,
    df_sorted,
    price_range,
    average_price,
    cheapest,
    most_expensive,
    price_by_brand,
):
    reports_dir = Path("reports")
    reports_dir.mkdir(exist_ok=True)

    output_file = reports_dir / "notebooks_report.xlsx"

    reduced_df = df[["brand", "price"]]

    with pd.ExcelWriter(output_file) as writer:
        reduced_df.to_excel(writer, sheet_name="processed_data", index=False)

        df_sorted[["brand", "price"]].to_excel(
            writer, sheet_name="price_ranking", index=False
        )

        price_range[["brand", "price"]].to_excel(
            writer, sheet_name="price_range", index=False
        )

        price_by_brand.to_excel(
            writer, sheet_name="price_by_brand", index=False
        )

        summary = pd.DataFrame(
            {
                "metric": ["average_price", "cheapest", "most_expensive"],
                "value": [
                    average_price,
                    cheapest["price"] if cheapest is not None else None,
                    most_expensive["price"] if most_expensive is not None else None,
                ],
            }
        )

        summary.to_excel(writer, sheet_name="summary", index=False)


