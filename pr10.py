# weather data processing

import csv
from multiprocessing import Pool

def process_year_data(chunk):
    year_temps = {}  # Dictionary to store temperatures for each year
    
    for row in chunk:
        year = row['Year']
        min_temp = float(row['MinTemp'])
        max_temp = float(row['MaxTemp'])
        
        if year not in year_temps:
            year_temps[year] = []
        
        year_temps[year].append(min_temp)
        year_temps[year].append(max_temp)
    
    return year_temps

def find_coolest_hottest_year(data_file):
    chunks = []
    with open(data_file, 'r') as file:
        reader = csv.DictReader(file)
        chunk_size = 50  # Number of rows to process in each chunk
        
        chunk = []
        for row in reader:
            chunk.append(row)
            if len(chunk) == chunk_size:
                chunks.append(chunk)
                chunk = []
        if chunk:  # Process remaining rows
            chunks.append(chunk)
    
    with Pool() as pool:
        mapped_data = pool.map(process_year_data, chunks)
    
    # Reduce phase
    year_temps_combined = {}
    for data in mapped_data:
        for year, temps in data.items():
            if year not in year_temps_combined:
                year_temps_combined[year] = temps
            else:
                year_temps_combined[year].extend(temps)
    
    # Calculate average temperatures for each year
    year_avg_temps = {year: sum(temps) / len(temps) for year, temps in year_temps_combined.items()}
    
    # Find coolest and hottest years
    coolest_year = min(year_avg_temps, key=year_avg_temps.get)
    hottest_year = max(year_avg_temps, key=year_avg_temps.get)
    
    return coolest_year, hottest_year

if __name__ == "__main__":
    data_file = "weather_data.csv"  # Update with your data file path
    coolest, hottest = find_coolest_hottest_year(data_file)
    
    print(f"Coolest year based on average temperature: {coolest}")
    print(f"Hottest year based on average temperature: {hottest}")
