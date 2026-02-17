import pandas as pd
import subprocess
import concurrent.futures
import re
from tqdm import tqdm
import time
from collections import defaultdict
import csv

SCRIPT = 'compute_ir.py'
EXCEL = '400_molecules.xlsx'

timing = defaultdict(float)
df = pd.read_excel(EXCEL, header=0)
records = df[['FRACTION', 'ID', 'SMILES']].astype(str).to_dict(orient='records')

def safe_filename(s):
    return re.sub(r'[^A-Za-z0-9\(\)\.\-\+\_]+', '_', s)

def run_one(record):
    smiles = record['SMILES']
    fraction = record['FRACTION']
    out_file = f"{safe_filename(record['FRACTION'])}_{safe_filename(record['ID'])}.csv"
    start = time.time()
    cmd = [
        'python', SCRIPT, smiles, '--nproc', '2'
    ]
    with open(out_file, 'w') as out:
        result = subprocess.run(cmd, stdout=out, stderr=subprocess.STDOUT)
    duration = time.time() - start

    return out_file, result.returncode, fraction, duration

def main():
    with concurrent.futures.ThreadPoolExecutor(max_workers=10) as executor:
        futures = {executor.submit(run_one, rec): rec for rec in records}
        with tqdm(total=len(futures)) as pbar:
            for f in concurrent.futures.as_completed(futures):
                filename, retcode, fraction, duration = f.result()
                timing[fraction] += duration
                status = "OK" if retcode == 0 else "ERROR"
                tqdm.write(f"{filename}: {status} ({duration:.2f} s)")
                pbar.update(1)

    with open('timing.csv', 'w', newline='', encoding='utf-8') as f:
        writer = csv.writer(f)
        writer.writerow(['fraction', 'time_seconds'])
        for frac, t in timing.items():
            writer.writerow([frac, round(t, 2)])

if __name__ == '__main__':
    main()
