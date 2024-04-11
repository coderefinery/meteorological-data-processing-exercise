import pandas as pd
import glob


def read_data(file_path):
    """Read the CSV file and return a DataFrame."""
    df = pd.read_csv(file_path)
    return df


def resample(df):
    """ Resample the data to hourly frequency for coarse processing.
    Reduces the size of the data in memory and speeds up the processing time.
    """
    df['timestamp'] = pd.to_datetime(df['timestamp'])
    df = df.set_index('timestamp')
    df = df.resample('h').mean()
    return df


def write_data(df, file_path):
    """Write the DataFrame to a new CSV file."""
    df.to_csv(file_path)


def device_monthly_average(device, files):
    """Calculate the monthly average for a specific device."""
    df = pd.DataFrame()
    for file in files:
        daily_df = read_data(file)
        daily_df = daily_df[(daily_df['x'] == device[0]) & (daily_df['y'] == device[1])]
        daily_df = resample(daily_df)
        df = pd.concat([df, daily_df])
    df = df.resample('ME').mean()
    return df


def main():
    # Read data files in the input folder and calculate the monthly
    # average for each measurement device.
    input_file_path = 'synthetic_data'
    output_file_path = 'processed_data.csv'

    files = glob.glob(f"{input_file_path}/*.csv")

    # Devices should be constant, so find them from the first list
    df = read_data(files[0])
    devices = df[['x', 'y']].drop_duplicates().values.tolist()

    print(f"Found {len(devices)} devices.")

    for device in devices:
        monthly = device_monthly_average(device, files)
        write_data(monthly, output_file_path)

if __name__ == "__main__":
    main()
