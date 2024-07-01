import unittest
from dulu import OCR
from PIL import Image
import requests

class TestOCR(unittest.TestCase):
    def setUp(self):
        self.ocr = OCR()
        self.image_url =  "https://github.com/whiletruelearn/dulu/blob/main/tests/sample_image.png?raw=true"
        self.image = Image.open(requests.get(self.image_url, stream=True).raw).convert('RGB')

    def test_recognize_text_without_bbox(self):
        text = self.ocr.recognize_text(self.image, bbox=False)
        self.assertIsInstance(text, str)
        self.assertIn("Gareth James", text)

    def test_recognize_text_with_bbox(self):
        result = self.ocr.recognize_text(self.image)
        self.assertIsInstance(result, dict)
        self.assertIn('<OCR_WITH_REGION>', result)
        self.assertIn('labels', result['<OCR_WITH_REGION>'])
        self.assertIn('Gareth James', result['<OCR_WITH_REGION>']['labels'][0])

if __name__ == '__main__':
    unittest.main()
