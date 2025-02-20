import pytesseract
from PIL import Image
import cv2
import os
from utils.image_preprocessing import preprocess_image
from utils.TextProcessor import clean_text


# Tesseract'ın yolunu tanımlayın
pytesseract.pytesseract.tesseract_cmd = r"C:\Program Files\Tesseract-OCR\tesseract.exe"

def extract_text_from_image(img_path, lang='eng+tur'):
    """
    Görüntüyü işleyin, ardından Tesseract'ı kullanarak metni çıkarın ve son olarak temizleyin.
    """
    #1. Başlangıç optimizasyon fonksiyonunu kullanarak görüntü işleme
    processed = preprocess_image(img_path)

    #2. İşlenen görüntüyü geçici olarak kaydedin.
    temp_path = "temp_processed.png"
    cv2.imwrite(temp_path, processed)

    #3. Tesseract Kullanarak Metin Çıkarma
    img = Image.open(temp_path)
    config = "--psm 3"
    text = pytesseract.image_to_string(img,config=config, lang=lang)

    # 4. clean_text fonksiyonunu kullanarak çıkarılan metni temizleyin
    cleaned_text = clean_text(text)

    # 5. geçici görüntüyü sil
    if os.path.exists(temp_path):
        os.remove(temp_path)

    return cleaned_text




