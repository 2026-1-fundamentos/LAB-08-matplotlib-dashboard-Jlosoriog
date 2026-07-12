# pylint: disable=line-too-long

import os
import pandas as pd
import matplotlib.pyplot as plt


def pregunta_01():

    os.makedirs("docs", exist_ok=True)

    # Cambia la ruta si en tu laboratorio es data/shipping-data.csv
    df = pd.read_csv("files/input/shipping-data.csv")

    plt.figure(figsize=(5,4))
    df["Warehouse_block"].value_counts().sort_index().plot(kind="bar")
    plt.title("Shipping per Warehouse")
    plt.xlabel("Warehouse")
    plt.ylabel("Count")
    plt.tight_layout()
    plt.savefig("docs/shipping_per_warehouse.png")
    plt.close()

    plt.figure(figsize=(5,4))
    df["Mode_of_Shipment"].value_counts().plot(kind="pie", autopct="%1.1f%%")
    plt.ylabel("")
    plt.title("Mode of Shipment")
    plt.tight_layout()
    plt.savefig("docs/mode_of_shipment.png")
    plt.close()

    plt.figure(figsize=(5,4))
    (
        df.groupby("Customer_rating")
        .size()
        .plot(kind="bar")
    )
    plt.title("Average Customer Rating")
    plt.xlabel("Rating")
    plt.ylabel("Count")
    plt.tight_layout()
    plt.savefig("docs/average_customer_rating.png")
    plt.close()

    plt.figure(figsize=(5,4))
    plt.hist(df["Weight_in_gms"], bins=20)
    plt.title("Weight Distribution")
    plt.xlabel("Weight (g)")
    plt.ylabel("Frequency")
    plt.tight_layout()
    plt.savefig("docs/weight_distribution.png")
    plt.close()

    html = """
<!DOCTYPE html>
<html>
<head>
<meta charset="UTF-8">
<title>Shipping Dashboard</title>
</head>
<body>

<h1>Shipping Dashboard</h1>

<h2>Shipping per Warehouse</h2>
<img src="shipping_per_warehouse.png" width="500">

<h2>Mode of Shipment</h2>
<img src="mode_of_shipment.png" width="500">

<h2>Average Customer Rating</h2>
<img src="average_customer_rating.png" width="500">

<h2>Weight Distribution</h2>
<img src="weight_distribution.png" width="500">

</body>
</html>
"""

    with open("docs/index.html", "w", encoding="utf-8") as file:
        file.write(html)