# Chungthang GLOF Analysis

A Python-based image analysis project exploring historical imagery of the Chungthang region in North Sikkim, with a focus on the 2023 glacial lake outburst flood (GLOF) and its surrounding landscape.

## Project Overview

This project organizes historical Google Earth imagery and generates side-by-side visual comparisons of selected locations around Chungthang. It provides a reproducible starting point for examining landscape differences across observation periods.

The current implementation focuses on image metadata extraction, dataset organization, and automated visual comparison.

## Objectives

- Build an organized inventory of source images.
- Extract image metadata using Python.
- Automate pre-event and later-image comparisons.
- Generate reproducible visual outputs.
- Establish a foundation for further data analysis.

## Technologies Used

- Python
- Pillow
- Pandas
- Matplotlib
- pathlib

## Project Structure

```text
chungthang-glof-analysis/
├── data/
│   ├── raw/
│   └── image_metadata.csv
├── src/
│   ├── inventory.py
│   └── compare_imgs.py
├── outputs/
│   └── image_comparisons/
├── .gitignore
├── requirements.txt
└── README.md
```

## Workflow

### 1. Image Inventory

The `src/inventory.py` script scans the raw-image directory and extracts:

- Filename
- Image width and height
- Image format
- Color mode

The metadata is exported to `data/image_metadata.csv`.

### 2. Visual Comparison

The `src/compare_imgs.py` script uses the metadata to identify image pairs, opens the images with Pillow, and generates side-by-side comparison figures using Matplotlib.

The figures are saved in `outputs/image_comparisons/`.

## Setup and Usage

Create and activate a Python virtual environment, then install the project dependencies.

Run these commands from the project root:

```bash
python -m venv .venv
```

Windows PowerShell:

```powershell
.\.venv\Scripts\Activate.ps1
pip install -r requirements.txt
```

Generate the image inventory:

```bash
python src/inventory.py
```

Generate the comparison figures:

```bash
python src/compare_imgs.py
```

## Data and Methodology

The project uses saved Google Earth imagery representing selected locations in the Chungthang region. Image filenames and metadata are used to organize and process the images.

The imagery acquisition dates, source details, and geographic comparability should be verified before drawing conclusions about changes between observation periods.

## Limitations

- Visual differences alone do not establish that the GLOF caused the observed changes.
- Differences in image acquisition date, viewing angle, scale, and alignment may affect comparisons.
- The current implementation performs image inventory and visual comparison; it does not yet perform validated geospatial measurements or automated change detection.

## Future Work

- Improve input validation and error handling.
- Record and verify imagery acquisition dates and source information.
- Investigate defensible quantitative measurements where the imagery supports them.
- Generate analytical charts and document evidence-based findings.

## Disclaimer

This is an independent educational project. It is not an official ISRO or NRSC project, and the analysis should not be interpreted as an official disaster assessment.
