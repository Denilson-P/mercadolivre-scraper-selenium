import pandas as pd    

df = pd.read_excel("reports/notebooks_report.xlsx")

filtered_df = df[df["price"] > 800]


brand_analysis = df.groupby("brand").agg({
    "price": ["mean", "min", "max", "count"]
})


print(brand_analysis)
