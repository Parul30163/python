import pandas as pd
import numpy as np
from faker import Faker

# Initialize Faker
fake = Faker()

# Number of records
num_records = 100

# Generate random data
data = {
    "Property ID": range(1, num_records + 1),
    "Location": [fake.city() + ", " + fake.state_abbr() for _ in range(num_records)],
    "Property Type": np.random.choice(["Apartment", "House", "Condo"], num_records),
    "Bedrooms": np.random.randint(1, 6, num_records),
    "Bathrooms": np.random.randint(1, 5, num_records),
    "Square Feet": np.random.randint(600, 3500, num_records),
    "Price Range": ["${:,} - ${:,}".format(price, price + np.random.randint(50000, 150000)) for price in np.random.randint(100000, 2000000, num_records)],
    "Sale Date": [fake.date_between(start_date='-2y', end_date='today') for _ in range(num_records)],
    "Historical Market Data (YoY Change)": np.round(np.random.uniform(-5, 10, num_records), 1),
    "Economic Indicator (Local GDP Growth)": np.round(np.random.uniform(1, 5, num_records), 1),
    "Search Patterns (Monthly Inquiries)": np.random.randint(50, 500, num_records),
    "Past Purchases (Last 12 Months)": np.random.randint(1, 20, num_records),
    "Customer Profile": np.random.choice(["Young Professional", "Family", "Retiree", "Young Couple", "Tech Professional", "Investor", "Large Family", "Single Professional", "Academic", "Mid-career Professional"], num_records),
    "Customer Preferences": np.random.choice(["Proximity to work", "Good schools", "Quiet neighborhood", "Proximity to nightlife", "Modern amenities", "Rental income potential", "Space", "Downtown location", "Proximity to universities", "Suburban"], num_records)
}

# Create DataFrame
df = pd.DataFrame(data)

# Display the first 10 rows of the DataFrame
print(df.head(10))

# Save to CSV
df.to_csv("real_estate_data.csv", index=False)
