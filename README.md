# AI-Powered Discharge Summary Generator

## Overview

This project implements a LangGraph-based agentic workflow for generating clinical discharge summaries from scanned patient records.

## Features

* PDF ingestion
* OCR using Gemini Vision
* Structured information extraction
* Medication reconciliation
* Missing data detection
* Conflict detection
* Discharge summary generation
* Reasoning trace generation

## Architecture

PDF → Image Conversion → Gemini OCR → LangGraph Workflow → Validation → Summary Generation

## Technologies Used

* Python
* LangGraph
* Gemini API
* PyMuPDF
* Pillow

## How to Run

```bash
pip install -r requirements.txt
python app.py
```

## Output

Generated files:

* outputs/discharge_summary.txt
* outputs/discharge_summary.json
* outputs/reasoning_trace.json
