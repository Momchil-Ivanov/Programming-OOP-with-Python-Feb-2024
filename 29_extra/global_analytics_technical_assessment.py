import pandas as pd
import sys

path_separator = ""

if sys.platform == "win32":
    path_separator = "\\"

else:
    path_separator = "/"

data = pd.read_excel(f"..{path_separator}29_extra{path_separator}global_analytics_technical_assessment.xlsx")

# Remove 'NA' values and convert to numeric
data['Sales'] = data['Sales'].str.replace(' USD', '').str.replace(',', '').astype(float)

# Filter out rows with 'NA' in the Drug column
df = data[data['Drug'].notna()]  # Exclude rows with NaN values in the 'Drug' column

# Group by Region and sum the sales
total_sales_by_region = data.groupby('Region')['Sales'].sum()


# Restore 'USD' and comma separators
total_sales_by_region = total_sales_by_region.map('${:,.0f}'.format)

# Convert total sales by region to a DataFrame with the index reset
total_sales_df = total_sales_by_region.reset_index()

# Print total drug sales by region with the 'Region' column
print(total_sales_df.to_string(index=False) + f'\n')

total_sales_by_region.to_excel('total_sales_by_region.xlsx', index=True)

# Group by Region and Drug, then sum the sales
total_sales_by_drug = df.groupby(['Region', 'Drug'])['Sales'].sum()

# Find the highest selling drug across regions
highest_selling_drug = total_sales_by_drug.idxmax()

# Print the highest selling drug
print(f"The highest selling drug across regions is: {highest_selling_drug}\n")

# Iterate over unique regions
unique_regions = data['Region'].unique()
for region in unique_regions:
    # Filter data for the current region
    region_data = total_sales_by_drug.loc[region]
    # Find the highest selling drug for this region
    highest_selling_drug = region_data.idxmax()
    # Print the result
    print(f"Highest selling drug in {region}: {highest_selling_drug}")

print('\n')

# Calculate the average drug sales by region
average_sales_by_region = total_sales_by_drug.groupby('Region').mean()
average_sales_by_region_formatted = average_sales_by_region.map('${:,.0f}'.format)

# Print the average drug sales by region
print(f"Average drug sales by region:\n")
for region, avg_sales in average_sales_by_region_formatted.items():
    print(f"{region}: {avg_sales}")
print('\n')

# Filter drugs starting with "E"
drugs_starting_with_e = df[df['Drug'].str.startswith('E')]['Drug'].unique()

print("Drugs whose names start with 'E':")
for drug in drugs_starting_with_e:
    print(drug)
print('\n')

# Extract numeric values from 'Drug' column
drug_numeric_values = df['Drug'].str.extract(r'(\d+)\s*mg', expand=False)

# Filter drugs with unit of measurement exceeding 120 mg and excluding NaN values
drugs_exceeding_120mg = df[drug_numeric_values.astype(float).fillna(-1) > 120]

# Group by Region and Drug, then sum the sales
total_sales_exceeding_120mg = drugs_exceeding_120mg.groupby(['Region', 'Drug'])['Sales'].sum()

# Total drug sales per region for drugs with unit of measurement exceeding 120 mg
total_sales_per_region_exceeding_120mg = total_sales_exceeding_120mg.groupby('Region').sum()

# Reset index and format 'Sales' column as USD
total_sales_per_region_exceeding_120mg_formatted = total_sales_per_region_exceeding_120mg.reset_index()
total_sales_per_region_exceeding_120mg_formatted['Sales'] = total_sales_per_region_exceeding_120mg_formatted['Sales'].map('${:,.0f}'.format)

# Print the formatted DataFrame
print("Total drug sales per region for drugs with unit of measurement exceeding 120 mg:")
print(total_sales_per_region_exceeding_120mg_formatted.to_string(index=False))