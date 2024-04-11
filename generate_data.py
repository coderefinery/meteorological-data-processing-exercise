import pandas as pd
import numpy as np
from datetime import datetime, timedelta
import os


def generate_data(date, devices):
    """Generate a DataFrame with synthetic meteorological data for a specified day and devices."""
    # Generate a timestamp for every second of the specified day
    size = 24*60*60
    n_devices = len(devices)
    timestamps = [date.replace(hour=0, minute=0, second=0, microsecond=0) + timedelta(seconds=i) for i in range(size)]
    
    temperatures = np.random.uniform(low=-10.0, high=35.0, size=size*n_devices)
    timestamps = [t for t in timestamps for d in devices]
    xs = [device[0] for i in range(size) for device in devices]
    ys = [device[1] for i in range(size) for device in devices]
    df = pd.DataFrame({
        'timestamp': timestamps,
        'x': xs,
        'y': ys,
        'temperature': temperatures
    })
    
    return df


def write_data(df, file_path, date):
    """Write the DataFrame to a CSV file."""
    file_path = f"{file_path}_{date.strftime('%Y%m%d')}.csv"
    df.to_csv(file_path)


def main():
    os.makedirs('synthetic_data', exist_ok=True)
    base_file_path = 'synthetic_data/temperature'
    start_date = datetime.now()
    
    # Generate a list of 200 devices, each with a random x and y location
    devices = [(np.random.uniform(-100.0, 100.0), np.random.uniform(-100.0, 100.0)) for _ in range(20)]
    
    for i in range(365):  # Generate data for a year
        date = start_date + timedelta(days=i)
        df = generate_data(date, devices)
        write_data(df, base_file_path, date)


if __name__ == "__main__":
    main()