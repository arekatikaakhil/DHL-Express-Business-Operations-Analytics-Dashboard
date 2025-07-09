import pandas as pd

# Read the file
file_path = '/Users/akhilarekatika/Work/Projects/Power Bi Project/cleaned_dataset.csv'
# Load dataset
df = pd.read_csv(file_path, encoding='latin1')

# Orders fact table
orders = df[[
    'Order Id', 'Order Customer Id', 'order date (DateOrders)', 'Order Status',
    'Order Item Id', 'Order Item Cardprod Id', 'Order Item Quantity',
    'Order Item Discount', 'Order Item Discount Rate', 'Order Item Product Price',
    'Order Item Total', 'Order Profit Per Order', 'Sales', 'Benefit per order',
    'Sales per customer', 'Delivery Status', 'Late_delivery_risk'
]]

# Customers dimension
customers = df[[
    'Customer Id', 'Customer Segment', 'Customer City', 'Customer State',
    'Customer Country', 'Latitude', 'Longitude', 'Market'
]].drop_duplicates()

# Products dimension
products = df[[
    'Product Card Id', 'Product Category Id', 'Category Id', 'Category Name',
    'Department Id', 'Department Name', 'Product Name', 'Product Price'
]].drop_duplicates()

# Shipping dimension
shipping = df[[
    'Order Id', 'shipping date (DateOrders)', 'Shipping Mode',
    'Days for shipping (real)', 'Days for shipment (scheduled)'
]]

# Save to separate CSVs
orders.to_csv("Orders.csv", index=False)
customers.to_csv("Customers.csv", index=False)
products.to_csv("Products.csv", index=False)
shipping.to_csv("Shipping.csv", index=False)

print("✅ Split into 4 tables: Orders, Customers, Products, Shipping")
