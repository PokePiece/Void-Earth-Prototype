from transformers import Trainer, TrainingArguments
from transformers import AutoModelForCausalLM, AutoTokenizer

# Load model and tokenizer
model_name = "openai-community/gpt2"
tokenizer = AutoTokenizer.from_pretrained(model_name)
model = AutoModelForCausalLM.from_pretrained(model_name)

# Tokenize the dataset
def tokenize_function(examples):
    return tokenizer(examples["input"], padding="max_length", truncation=True)

tokenized_datasets = dataset.map(tokenize_function, batched=True)

# Prepare training arguments
training_args = TrainingArguments(
    output_dir="./results",
    evaluation_strategy="steps",
    logging_dir="./logs",
    num_train_epochs=3,  # Choose the number of epochs
    per_device_train_batch_size=4,
    per_device_eval_batch_size=4,
)

# Define the Trainer
trainer = Trainer(
    model=model,
    args=training_args,
    train_dataset=tokenized_datasets,
)

# Start fine-tuning
trainer.train()




#Save the fine-tuned model and tokenizer

#model.save_pretrained("./fine_tuned_model")
#tokenizer.save_pretrained("./fine_tuned_model")


#Load it
#fine_tuned_model = AutoModelForCausalLM.from_pretrained("./fine_tuned_model")
#fine_tuned_tokenizer = AutoTokenizer.from_pretrained("./fine_tuned_model")
