# A computational approach for pre-assessing infrared spectroscopy effectiveness for analysis crude oil composition 
This repository implements a computational framework for evaluating the theoretical informativeness of infrared (IR) spectroscopy in crude oil analysis. Using quantum-chemically simulated spectra of molecular-level “digital oils,” it constructs a synthetic dataset linking SARA (Saturates, Aromatics, Resins, Asphaltenes) composition to measurable signals. Machine learning models are trained on these data to quantify the maximum achievable accuracy of IR-based SARA prediction. The project demonstrates how in silico analytics can support method selection and rational experimental design in complex chemical systems.
<img width="1391" height="508" alt="pipeline_draw (5)" src="https://github.com/user-attachments/assets/dafe4a99-9ac1-4676-86c0-ceff7d73ea26" />
### Project Structure
- `datasets`
  - `molecules_spectra_absorbanse.csv` — SMILES → IR spectrum
  - `df_0_1200.csv` — Oil sample set of molecules 0
  - `df_1_1200.csv` — Oil sample set of molecules 1
  - `df_2_1200.csv`— Oil sample set of molecules 2
  - `df_3_1200.csv`— Oil sample set of molecules 3
  - `df_4_1200.csv`— Oil sample set of molecules 4
- `dataset_creation`
  - `Selfies_based_generation_of_molecules.ipynb` Generate molecules via SELFIES
  - `generate_weights_of_molecules.ipynb`  Create oil samples with molar fractions
  - `generating_IR_spectra`
    - `compute_IR.py`  IR modes for single molecule
    - `batch_compute_ir.py` Batch IR calculation
    - `Lorentzian_broadening.py` Continuous spectra generation
- `ML_based_on_spectra_with_noise.ipynb`
- `ML_based_on_spectra_without_noise_and_alr_regime.ipynb`
- `requirements.txt`
- `README.md`
  ##  Data Generation Pipeline

### Step 1: Generate Molecules
**File:** `dataset_creation/Selfies_based_generation_of_molecules.ipynb`

Generates synthetic molecules using SELFIES (Self-Referencing Embedded Strings) representation.

```python
# Run the notebook locally to generate molecule structures
dataset_creation/Selfies_based_generation_of_molecules.ipynb
```
Output: set of representative molecules of crude oil
### Step 2: Compute IR Spectra
**File:** `dataset_creation/generating_IR_spectra/`

#### Calculate IR modes for a single molecule
`python dataset_creation/generating_IR_spectra/compute_IR.py <smiles> <nproc> `

or

#### Batch calculating IR modes for multiple molecules
`python dataset_creation/generating_IR_spectra/batch_compute_ir.py`

#### Generate continuous spectrum with Lorentzian broadening (specify folder with CSV files of IR spectra of individual molecule)
`python dataset_creation/generating_IR_spectra/Lorentzian_broadening.py <input_folder>`

Output: molecules_spectra_absorbanse.csv 

### Step 3: Create Oil Samples
**File:** `dataset_creation/generate_weights_of_molecules.ipynb` 

Generates oil samples by computing molar fractions of molecules.
```python
# Run the notebook locally to generate spectra of oil
dataset_creation/generate_weights_of_molecules.ipynb 
```
Output: 5 CSV files (df_0_1200.csv to df_4_1200.csv) containing oil samples with SARA composition

## Machine Learning Models
Type 1: With Noise
**File:** `ML_based_on_spectra_with_noise.ipynb`
Trains ML model on IR spectra with added noise (simulates real-world conditions).

```python
# Run the notebook locally 
ML_based_on_spectra_with_noise.ipynb
```
Type 2: Without Noise and ALR Regime
**File:** `ML_based_on_spectra_without_noise_and_alr_regime.ipynb`
Trains ML model on clean spectra and model with Additive Log-Ratio (ALR) transformation 
```python
# Run the notebook locally 
ML_based_on_spectra_without_noise_and_alr_regime.ipynb
```




