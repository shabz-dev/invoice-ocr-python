import cv2
import pytesseract

pytesseract.pytesseract.tesseract_cmd = r"C:\Program Files\Tesseract-OCR\tesseract.exe"

img = cv2.imread(r"C:\Users\shaba\OneDrive\Desktop\projects\invoice ocr\invoice.png")

gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

blur = cv2.GaussianBlur(gray, (3, 3), 0)

thresh = cv2.threshold(blur, 0, 255,
                       cv2.THRESH_BINARY + cv2.THRESH_OTSU)[1]

kernel = cv2.getStructuringElement(cv2.MORPH_RECT, (2, 2))
processed = cv2.morphologyEx(thresh, cv2.MORPH_CLOSE, kernel)

# ✅ OCR Extraction
text = pytesseract.image_to_string(processed, config="--oem 3 --psm 6")

print("----- Extracted Text -----")
print(text)

cv2.imshow("Processed Invoice", processed)
cv2.waitKey(0)
cv2.destroyAllWindows()
