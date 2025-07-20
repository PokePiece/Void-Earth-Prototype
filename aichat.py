from transformers import AutoTokenizer, AutoModelForCausalLM
import sys
import io
from torch.cuda.amp import autocast

    
  

# Ensure the correct encoding for the console output
sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding='utf-8')

# Initialize the model and tokenizer
model_name = "openai-community/gpt2"
tokenizer = AutoTokenizer.from_pretrained(model_name)
model = AutoModelForCausalLM.from_pretrained(model_name, device_map="cpu")


# Function to generate responses based on prompt and profile
def generate(prompt, profile):
    system_prompt = f"You're a {profile['tone']} assistant. Be {profile['style']}."
    full_prompt = system_prompt + "\nUser: " + prompt + "\nAI:"
    inputs = tokenizer(full_prompt, return_tensors="pt").to(model.device)
    outputs = model.generate(
        **inputs,
        max_new_tokens=500,
        do_sample=True,
        top_p=0.9,
        temperature=0.2, #lower output more predicatable
        repetition_penalty=1.2,
    )
    generated_tokens = outputs[0][inputs['input_ids'].size(1):]
    return tokenizer.decode(generated_tokens, skip_special_tokens=True)

# Main interactive loop
if __name__ == "__main__":
    print("Welcome to the interactive AI assistant. Type 'quit' to exit.")
    while True:
        prompt = input("You: ")
        if prompt.lower() in ("quit", "exit"):
            print("Exiting... Goodbye!")
            break
        # Adjust the profile based on your tone and style preferences
        profile = {"tone": "realistic", "style": "technical"}
        response = generate(prompt, profile)
        print("AI:", response)
