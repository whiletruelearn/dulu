from PIL import Image
from transformers.dynamic_module_utils import get_imports

def load_image(image_path):
    image = Image.open(image_path).convert('RGB')
    return image


def fixed_get_imports(filename="modeling_florence2.py") -> list[str]:
    if not str(filename).endswith("modeling_florence2.py"):
        return get_imports(filename)
    imports = get_imports(filename)
    imports.remove("flash_attn")
    return imports