import re
import language_tool_python
from transformers import T5ForConditionalGeneration, T5Tokenizer
import google.generativeai as genai
from gramformer import Gramformer

def clean_text(text):
    """
    İstenmeyen sembolleri kaldırarak, aralıkları iyileştirerek ve karakterleri standartlaştırarak metni temizleyin.
    """

    # İngilizce veya Türkçe olmayan tüm karakterleri veya rakamları kaldırın (boşluklar hariç)
    text = re.sub(r'[^a-zA-Z0-9ğüşöçİıĞÖŞÇ ]', '', text)

    # # Fazla boşlukları kaldırın
    # text = re.sub(r'\s+', ' ', text).strip()

    text = text.lower()

    gf = Gramformer(models=1, use_gpu=False)
    text = gf.correct(text).pop()

    genai.configure(api_key="AIzaSyB95u3O1AUlshKAKPP7pOG69jeQC-i3ACQ")
    model = genai.GenerativeModel("gemini-1.5-flash")
    response = model.generate_content(f"Correct the sentence without changing the structure. (return only the corrected text) \"{text}\"")

    return response.text
