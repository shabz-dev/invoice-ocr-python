# Invoice OCR using Python & Tesseract

This project demonstrates an end-to-end OCR pipeline that extracts text from invoice images using Python and Tesseract OCR.

## Features
- Loads invoice images using PIL
- Extracts text using Tesseract OCR
- Configured for Windows environment
- Uses Page Segmentation Mode for document text

## Tech Stack
- Python
- Tesseract OCR
- pytesseract
- Pillow (PIL)

## How it works
1. Image is loaded from disk
2. Tesseract OCR engine processes the image
3. Extracted text is returned as a string

## Setup Instructions
1. Install Tesseract OCR (Windows)
2. Update the Tesseract executable path in code
3. Install dependencies:
   ```bash
   pip install -r requirements.txt
