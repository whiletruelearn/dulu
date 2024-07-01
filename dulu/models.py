from transformers import AutoProcessor, AutoModelForCausalLM  
from unittest.mock import patch
from .preprocessing import fixed_get_imports
from PIL import Image

def load_model(model_name='microsoft/Florence-2-base-ft'):
    processor = AutoProcessor.from_pretrained(model_name, trust_remote_code=True)
    with patch("transformers.dynamic_module_utils.get_imports", fixed_get_imports): #workaround for unnecessary flash_attn requirement
        model = AutoModelForCausalLM.from_pretrained(model_name, trust_remote_code=True).eval()
    return processor, model

