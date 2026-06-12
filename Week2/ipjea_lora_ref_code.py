from transformers import AutoModel, AutoProcessor, BitsAndBytesConfig
from peft import LoraConfig, get_peft_model
import torch 
import torch.nn as nn
import torch.nn.functional as F
from torchvision.datasets import CIFAR10
from torchvision import transforms
from torch.utils.data import DataLoader, random_split

quantization_config = BitsAndBytesConfig(
    load_in_4bit=True,
    bnb_4bit_quant_type="nf4",
    bnb_4bit_use_double_quant=True,
)

processor = AutoProcessor.from_pretrained("facebook/ijepa_vitg16_22k")
model = AutoModel.from_pretrained("facebook/ijepa_vitg16_22k", quantization_config=quantization_config, attn_implementation="sdpa", device_map="auto")
print(model)

lora_config = LoraConfig(
    r=16,
    lora_alpha=32,
    lora_dropout=0.05,
    bias="none",
    target_modules=["query","key","value"] # or q_proj,k_proj,v_proj
)   

model = get_peft_model(model, lora_config)

model.print_trainable_parameters()

class IJEPAClassifier(nn.Module):
    def __init__(self,backbone,num_classes=10):
        super().__init__()
        self.backbone = backbone
        self.classifier = nn.Linear(1408,num_classes)
        
    def forward(self,pixel_values):
        outputs = self.backbone(pixel_values=pixel_values)
        x = outputs.last_hidden_state.mean(dim=1)
        logits = self.classifier(x)
        return logits

model = IJEPAClassifier(model).cuda()
print(type(model.backbone))
print(model.backbone)
