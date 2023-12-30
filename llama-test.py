import transformers
from transformers import AutoTokenizer
import torch

mps = torch.device("cpu")
tokenizer = AutoTokenizer.from_pretrained('EleutherAI/gpt-neox-20b')
# model = transformers.AutoModelForCausalLM.from_pretrained(
#   'mosaicml/mpt-7b',
#   trust_remote_code=True
# ).to(mps)

text = "John Lennon is a famous singer."
tokenized_sentence = tokenizer(text, return_tensors='pt')
print(tokenized_sentence)
# output = model(**tokenized_sentence, output_attentions=True)

#print(output.attentions)