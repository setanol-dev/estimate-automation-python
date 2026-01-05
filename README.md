# Estimate Automation Tool (Python)

## Overview
This project is a Python-based business automation tool that generates estimates
from CSV input files and outputs formatted documents automatically.

## Problem
Manual estimation using Excel is time-consuming and error-prone.

## Solution
This tool automates:
- CSV-based input
- Rule-based calculation
- Automatic document generation
- Simple logging

## Target Users
- Small manufacturing teams
- Back-office staff
- Engineers handling repetitive estimation tasks

## Status
Work in progress

## Workflow Design

### Input
- CSV file (source data for estimation)
- Columns:
  - item_name: item name
  - quantity: quantity (integer)
  - unit_price: unit price (numeric)
  - rush_flag: rush order flag (0 or 1)
  - discount_rate: discount rate (0.0–0.3)

### Process
- Load the CSV file
- For each row:
  - Calculate subtotal as quantity × unit_price
  - If rush_flag = 1, add 10% surcharge
  - If discount_rate is specified, apply discount
- Calculate total amount by summing all rows
- Automatically generate an estimate ID (EST-YYYYMMDD-serial)
- Record execution timestamp
- Log any errors encountered during processing

### Output
- Excel file containing the estimation result
- File name: estimate_YYYYMMDD.xlsx
- Output directory: sample_output
- Processing log file (text)

