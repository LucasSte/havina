
import transformers
from transformers import AutoTokenizer
import torch

mps = torch.device("mps")
tokenizer = AutoTokenizer.from_pretrained('EleutherAI/gpt-neox-20b')
model = transformers.AutoModelForCausalLM.from_pretrained(
  'mosaicml/mpt-7b',
  trust_remote_code=True
).to(mps)

text = "John Lennon is a famous singer."
tokenized_sentence = tokenizer(text, return_tensors='pt')
tokenized_sentence['input_ids'] = tokenized_sentence['input_ids'].to(mps)
tokenized_sentence['attention_mask'] = tokenized_sentence['attention_mask'].to(mps)

output = model(**tokenized_sentence)
