# 🧾 Invoice Text Extraction System (OpenCV + Tesseract OCR)

This project is an **Invoice OCR (Optical Character Recognition)** system that extracts text from scanned invoice images using **OpenCV preprocessing** and **Tesseract OCR**.

It converts invoice documents into machine-readable text for further analytics, automation, and data extraction.

---

## 🚀 Features

✅ Load invoice images using OpenCV  
✅ Preprocess images (grayscale, blur, thresholding)  
✅ Improve OCR accuracy with morphological operations  
✅ Extract invoice text using Tesseract OCR  
✅ Works on scanned documents and real invoices  

---

## 🛠 Tech Stack

- Python  
- OpenCV  
- Tesseract OCR  
- NumPy  

---

## 📂 Project Structure

invoice-ocr/
│
├── invoice_ocr.py # Main OCR script
├── invoice.png # Sample invoice image
├── requirements.txt # Dependencies
├── README.md # Documentation


---

## ▶️ How to Run the Project

### 1️⃣ Clone Repository

`bash
git clone https://github.com/your-username/invoice-ocr.git
cd invoice-ocr

2️⃣ Install Dependencies
pip install -r requirements.txt
3️⃣ Install Tesseract OCR (Windows)
Download and install from:

👉 https://github.com/UB-Mannheim/tesseract/wiki

Then update the path inside code:

pytesseract.pytesseract.tesseract_cmd =
r"C:\Program Files\Tesseract-OCR\tesseract.exe"
4️⃣ Run the Script
python invoice_ocr.py


🧠 OCR Pipeline Steps
1.Read invoice image
2.Convert to grayscale
3.Apply Gaussian Blur
4.Thresholding (Binarization)
5.Morphological operations
6.Extract text using OCR
