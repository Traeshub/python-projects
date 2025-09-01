import pandas as pd
from datetime import datetime
import os

search_names = ()
search_timestamps = ()


def excel_scrubber(input_file, output_file, filers):
    
    # Read the excel file
    
    '''Args:
            input_file: path to excel file
            search_names: list of names to search for
            search_timestamps: list of timestamps
            
        Returns:
            Time frame with matching names'''
    
    df = pd.read_excel(input_file)

    # Creating a copying to avoid modifying the original
    results = df.copy()

    # Applying name filtering
    if search_names:
        name_columns = [col for col in df.columns if any(keyword in col.lower for keyword in ['name', 'first', 'last', 'full'])]

        if name_columns:
            name_mask = pd.Series([False] * len(df))
            for col in name_columns:
                for name in search_names:
                    name_mask = name_mask | (df[col].astype(str).str.contains(name, case=False, na=False))
                    results = results[name_mask]
        else:
            print("No names were found.")

    # Apply timestamp filters
    if search_timestamps:
        time_columns = [col for col in df.columns if any(keyword in col.lower() for keyword in ['time', 'date', 'timestamp'])]
    
    if time_columns:
        time_mask = pd.Series([False] * len(results))
        for col in time_columns:
            for ts in search_timestamps:
                if isinstance(ts,str):
                    ts_dt = pd.to_datetime(ts)
                else:
                    ts_dt = pd.to_datetime(ts)
                    col_dates = pd.to_datetime(df[col])
                    time_mask = time_mask | (col_dates.dt.date == ts_dt.date())
            
    return results


def main():
    input_file = input("Enter the path to your excel file: ")
    names_input = input("Enter name to search for (press Enter to skip)")
    timestamp_input = input(" Enter time/date to search for (press Enter to skip)")

    search_names = [name.strip() for name in names_input.split(',')] if names_input else None
    search_timestamps = [ts.strip() for ts in timestamp_input.split(',')] if timestamp_input else None

    if not search_names and not search_timestamps:
        print("No search criteria provided")
        return
    
    matches = (input_file, search_names, search_timestamps)
    
    if matches.empty:
        print("No matches found")
    else:
        print(f"\nFound {len(matches)} matching the name:")
