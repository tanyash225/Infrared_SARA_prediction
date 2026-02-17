# A computational approach for pre-assessing infrared spectroscopy effectiveness for analysis crude oil composition 
This repository implements a computational framework for evaluating the theoretical informativeness of infrared (IR) spectroscopy in crude oil analysis. Using quantum-chemically simulated spectra of molecular-level “digital oils,” it constructs a synthetic dataset linking SARA (Saturates, Aromatics, Resins, Asphaltenes) composition to measurable signals. Machine learning models are trained on these data to quantify the maximum achievable accuracy of IR-based SARA prediction. The project demonstrates how in silico analytics can support method selection and rational experimental design in complex chemical systems.
<img width="1391" height="508" alt="pipeline_draw (5)" src="https://github.com/user-attachments/assets/dafe4a99-9ac1-4676-86c0-ceff7d73ea26" />
- `datasets/`
  - `molecules_spectra_absorbanse.csv` — SMILES → IR spectrum
  - `df_0_1200.csv` — Oil sample set 0
  - `df_1_1200.csv` — Oil sample set 1
  - ...
- `dataset_creation/`
  - `Selfies_based_generation_of_molecules.ipynb`
  - `generate_weights_of_molecules.ipynb`
  - `generating_IR_spectra/`
    - `compute_IR.py`
    - `batch_compute_ir.py`
    - `Lorentzian_broadening.py`
- `ML_based_on_spectra_with_noise.ipynb`
- `ML_based_on_spectra_without_noise_and_alr_regime.ipynb`
- `requirements.txt`
- `README.md`
