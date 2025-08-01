from datasets import Dataset
train_data = [
    {"input": "Which option should you choose?", "output": "Option 1"},
    {"input": "What is the best option?", "output": "Option 1"},
]

dataset = Dataset.from_dict(train_data)
