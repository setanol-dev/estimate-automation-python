# Estimate Automation Tool (Python)

## Overview
This project is a Python-based business automation tool that converts CSV input
files into formatted Excel estimation documents automatically.

It is designed to reduce manual Excel work, prevent calculation errors, and
speed up repetitive estimation tasks.

## Problem
Many small teams still create estimates manually using Excel.
This process is time-consuming, error-prone, and difficult to standardize.

## Solution
This tool automates the estimation workflow by:
- Reading structured CSV input files
- Applying rule-based calculations
- Generating Excel output files automatically
- Logging execution details and errors

## Target Users
- Small manufacturing teams
- Back-office staff
- Engineers handling repetitive estimation tasks

## Workflow Design

### Input
- CSV file (estimation source data)
- Required columns:
  - `item_name`: item name
  - `quantity`: quantity (integer)
  - `unit_price`: unit price (numeric)
  - `rush_flag`: rush order flag (0 or 1)
  - `discount_rate`: discount rate (0.0–0.3)

### Process
- Load CSV file
- For each row:
  - Calculate subtotal as `quantity × unit_price`
  - Add 10% surcharge if `rush_flag = 1`
  - Apply discount if `discount_rate` is specified
- Sum all subtotals to calculate total amount
- Generate estimate ID in format `EST-YYYYMMDD-XXX`
- Record execution timestamp
- Log invalid rows or processing errors

### Output
- Excel file containing estimation results
- File name format: `estimate_YYYYMMDD.xlsx`
- Output directory: `sample_output/`
- Processing log file (text)

## How to Run

1. Place your input CSV file into the `sample_input/` directory
2. Install dependencies:
3. Run the script:
4. The generated Excel file will appear in the `sample_output/` directory

## Status
Work in progress.
This project is intended as a portfolio sample for business automation tasks.
