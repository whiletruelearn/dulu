# Dulu

Dulu is a small python library for doing OCR on image. Under the hood it uses florence model from microsoft, which is a state of the art vision model for many downstream tasks including OCR.


## Installation

```
pip install dulu

```


### Example Code

Here is a snippet of the code used in the notebook:

```python
from dulu import OCR
from PIL import Image

# Load the image
image = Image.open("./sample_image.png")
image

# Initialize the OCR object
ocr = OCR()

# Recognize text without bounding boxes
text = ocr.recognize_text("./sample_image.png", bbox=False)
print(text)

# Recognize text with bounding boxes
text_with_bbox = ocr.recognize_text("./sample_image.png")
print(text_with_bbox)
```



## Acknowledgments

- [Florence2 model](https://arxiv.org/abs/2311.06242)