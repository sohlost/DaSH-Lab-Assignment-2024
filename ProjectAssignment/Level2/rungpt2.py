from transformers import GPT2LMHeadModel, GPT2Tokenizer
import torch


model_name = "gpt2"
model = GPT2LMHeadModel.from_pretrained(model_name)
tokenizer = GPT2Tokenizer.from_pretrained(model_name)


input_text = "LLM Inference is a cool topic because"

input_ids = tokenizer.encode(input_text, return_tensors="pt")
attention_mask = torch.ones(input_ids.shape, dtype=torch.long)


output = model.generate(input_ids = input_ids, attention_mask = attention_mask, do_sample=True, max_length=100, top_k=50, top_p=0.95, temperature=0.9,pad_token_id = tokenizer.eos_token_id,  )

generated_output = tokenizer.decode(output[0], skip_special_tokens=True, clean_up_tokenization_spaces=True)
print(generated_output)
