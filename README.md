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

### List of models 

| Model Id                  | Model size | Model Description                                      |
|-------------------------|------------|--------------------------------------------------------|
| Florence-2-base     | 0.23B      | Pretrained model with FLD-5B                           |
| Florence-2-large    | 0.77B      | Pretrained model with FLD-5B                           |
| Florence-2-base-ft  | 0.23B      | Finetuned model on a collection of downstream tasks    |
| Florence-2-large-ft | 0.77B      | Finetuned model on a collection of downstream tasks    |

By default we use `Florence-2-base-ft` model, you can over ride this with any other above in the list when
instantiating `OCR(model_name="microsoft/{model_id})`


## Acknowledgments

- [Florence2 model](https://arxiv.org/abs/2311.06242)