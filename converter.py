import pandas as pd

def clean_data(df):
    df = df[['Name', 'Grade']]
    df['Name'] = df['Name'].str.strip().fillna("Unknown")
    df['Grade'] = df['Grade'].astype(str).str.strip().fillna("Not Assigned")
    return df

try:
    input_file = "data.csv"
    output_file = "output.xlsx"

    df = pd.read_csv(input_file)
    df = clean_data(df)
    df.to_excel(output_file, index=False)

    print("✅ Conversion Successful!")
    print("File saved as:", output_file)

except FileNotFoundError:
    print("❌ Error: data.csv file not found.")
except Exception as e:
    print("❌ Error:", e)