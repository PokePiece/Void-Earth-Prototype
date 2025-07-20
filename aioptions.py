from transformers import AutoTokenizer, AutoModelForCausalLM
import sys
import io
import torch

# Ensure the correct encoding for the console output
sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding='utf-8')

# Initialize the model and tokenizer
model_name = "openai-community/gpt2"
tokenizer = AutoTokenizer.from_pretrained(model_name)
model = AutoModelForCausalLM.from_pretrained(model_name, device_map="cpu")

# Function to generate responses based on prompt and profile
def generate(prompt, options, profile):
    # Create a system prompt with tone and style
    system_prompt = f"You're a {profile['tone']} assistant. Be {profile['style']}."
    
    # Construct the options and append the instruction to choose the first option
    options_prompt = f"Option 1: {options[0]}\nOption 2: {options[1]}\nOption 3: {options[2]}"
    full_prompt = system_prompt + "\nUser: " + prompt + "\nAI: " + options_prompt + "\nAnswer: Option 1"
    
    # Tokenize the input and send it to the model
    inputs = tokenizer(full_prompt, return_tensors="pt").to(model.device)
    
    # Generate response, use deterministic sampling (lower temperature)
    outputs = model.generate(
        **inputs,
        max_new_tokens=50,
        do_sample=False,  # Disable sampling to make it deterministic
        temperature=0.0,  # Set temperature to 0 to always select the most probable token
        top_p=1.0,
        repetition_penalty=1.0
    )
    
    # Decode and return the output
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
        
        # Provide the three options
        options = ["Option 1: This is always the correct answer.", 
                   "Option 2: This is never correct.", 
                   "Option 3: This is also never correct."]
        
        # Call the generate function and print the response
        response = generate(prompt, options, profile)
        print("AI:", response)
