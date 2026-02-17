import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from pathlib import Path
import sys
import openpyxl


def calculate_absorbance(frequencies, intensities, linewidth=20):
    """
    Simulate an IR absorbance spectrum using Lorentzian line shapes.
    
    Parameters:
    - frequencies: array of vibrational frequencies (cm⁻¹)
    - intensities: corresponding IR intensities (km/mol)
    - linewidth: full width at half maximum (FWHM) of each Lorentzian peak (default = 20 cm⁻¹)

    Returns:
    - x: wavenumber grid from 400 to 4000 cm⁻¹ (2000 points)
    - y: simulated absorbance values on the x-grid
    """
    x = np.linspace(400, 4000, 2000)  # Wavenumber axis (cm⁻¹)
    y = np.zeros_like(x)              # Initialize spectrum intensity array

    # Add a Lorentzian peak for each frequency-intensity pair
    for freq, inten in zip(frequencies, intensities):
        y += inten * 0.5 * linewidth / ((x - freq)**2 + (0.5 * linewidth)**2)
    return x, y


def process_file(file_path, df):
    """
    Process a single CSV file containing computed vibrational data and update the main DataFrame.
    
    Input file name format expected: <FRACTION>_<ID>.csv (e.g., 'As_5.csv')
    
    Parameters:
    - file_path: Path object pointing to a .csv file with columns 'Frequency (cm-1)' and 'Intensity (km/mol)'
    - df: main DataFrame with columns 'FRACTION' and 'ID'; will be updated in-place with spectral data
    """
    # Extract fraction name and molecule ID from filename (e.g., 'As_5' → fraction='As', number=5)
    name = file_path.stem
    fraction, number_str = name.split('_')
    number = int(number_str)

    try:
        # Load computed vibrational data
        data = pd.read_csv(file_path)
        freqs = data['Frequency (cm-1)'].to_numpy()
        intensities = data['Intensity (km/mol)'].to_numpy()

        # Simulate continuous IR spectrum
        x, y = calculate_absorbance(freqs, intensities)

        # Create column names for each wavenumber point (rounded to 2 decimals as strings)
        y_columns = [f"{val:.2f}" for val in x]

        # Ensure all required columns exist in the main DataFrame
        for col in y_columns:
            if col not in df.columns:
                df[col] = np.nan

        # Find the matching row in df by FRACTION and ID, then insert the spectrum
        row_mask = (df['FRACTION'] == fraction) & (df['ID'] == number)
        df.loc[row_mask, y_columns] = y
        print(f"Processed {file_path.name}")

    except Exception as e:
        print(f"Error processing {file_path.name}: {e}")


def main():
    """
    Main function: reads input folder path from command line,
    loads metadata from Excel, processes all CSV files, and saves result.
    """
    if len(sys.argv) < 2:
        print("Usage: python script.py <input_folder>")
        print("  <input_folder>: directory containing .csv files named as FRACTION_ID.csv")
        return

    input_folder = Path(sys.argv[1])  # Folder with computed spectra (CSV files)

    # Load metadata table (must contain columns 'FRACTION' and 'ID')
    metadata_path = "metadata.xlsx"  # CHANGE THIS TO YOUR ACTUAL FILE NAME 
    df = pd.read_excel(metadata_path)

    # Process every CSV file in the input folder
    for file in input_folder.glob("*.csv"):
        process_file(file, df)

    # Save final dataset with spectra embedded as columns
    output_file = "summary_with_spectra.csv"
    df.to_csv(output_file, index=False)
    print(f"\nDone. Output saved to {output_file}")


if __name__ == "__main__":
    main()
