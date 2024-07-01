from .preprocessing import load_image
from .models import load_model


class OCR:
    def __init__(self, model_name='microsoft/Florence-2-base-ft'):
        self.processor , self.model = load_model(model_name)

    def recognize_text(self, image_input, bbox=True):
        from PIL import Image

        prompt = '<OCR_WITH_REGION>' 

        if isinstance(image_input, str):
            image = load_image(image_input)
        elif isinstance(image_input, Image.Image):
            image = image_input
        else:
            raise ValueError("image_input must be a file path or a PIL image")

        inputs = self.processor(text=prompt, images=image, return_tensors="pt")
        generated_ids = self.model.generate(
        input_ids=inputs["input_ids"],
        pixel_values=inputs["pixel_values"],
        max_new_tokens=1024,
        early_stopping=False,
        do_sample=False,
        num_beams=3,
        )

        generated_text = self.processor.batch_decode(generated_ids, skip_special_tokens=False)[0]
        parsed_answer = self.processor.post_process_generation(
            generated_text, 
            task=prompt, 
            image_size=(image.width, image.height)
        )
     
        if not bbox:
            parsed_answer = " ".join(parsed_answer[prompt]["labels"])
        return parsed_answer


