# Meteorological data processing exercise

Example of processing meteorological data for an HPC I/O exercise

## Running the pipeline:

### 1. Clone the repository

```bash
git clone git@github.com:coderefinery/meteorological-data-processing-exercise.git
cd meteorological-data-processing-exercise
```

### 2. Install dependencies

```bash
pip install -r requirements.txt
```

### 3. Generate example data

```bash
python generate_data.py
```

This generates random temperature measurements from 20 measurement once per
second for each day of a year. This might take a few minutes. Take time to
understand what each script does while it's happening.

### 4. Process the data

```bash
python pipeline.py
```

This step reads in the data for each 