
import pandas as pd

def clean_dataset(filepath):
    df = pd.read_csv(filepath)

    # Convert Date to datetime
    df['Date'] = pd.to_datetime(df['Date'], errors='coerce')

    # Fill missing values in Bleaching Severity with 'Unknown'
    df['Bleaching Severity'] = df['Bleaching Severity'].fillna('Unknown')

    # Remove duplicate rows
    df = df.drop_duplicates()

    # Save cleaned data
    cleaned_path = filepath.replace('.csv', '_cleaned.csv')
    df.to_csv(cleaned_path, index=False)
    print(f"Cleaned data saved to: {cleaned_path}")

if __name__ == '__main__':
    clean_dataset('../data/realistic_ocean_climate_dataset.csv')
