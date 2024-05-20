import torch
from transformers import BertTokenizer, BertForQuestionAnswering, AdamW
from torch.utils.data import DataLoader, Dataset

# Load your text data
with open('haranhui_had.txt', 'r') as f:
    texts = f.readlines()

# Tokenize your text data
tokenizer = BertTokenizer.from_pretrained('bert-base-uncased')
tokenized_texts = [tokenizer.tokenize(text) for text in texts]

# Convert tokenized texts to input IDs
input_ids = [tokenizer.convert_tokens_to_ids(tokens) for tokens in tokenized_texts]

# Define a custom dataset class
class MyDataset(Dataset):
    def __init__(self, input_ids):
        self.input_ids = input_ids

    def __len__(self):
        return len(self.input_ids)

    def __getitem__(self, idx):
        return self.input_ids[idx]

dataset = MyDataset(input_ids)

# Load the pre-trained BERT model
model = BertForQuestionAnswering.from_pretrained('bert-base-uncased')

# Define your optimizer
optimizer = AdamW(model.parameters(), lr=5e-5)

# Define your training loop
device = torch.device('cuda' if torch.cuda.is_available() else 'cpu')
model.to(device)

for epoch in range(num_epochs):
    for input_ids_batch in DataLoader(dataset, batch_size=batch_size, shuffle=True):
        input_ids_batch = input_ids_batch.to(device)

        outputs = model(input_ids=input_ids_batch)
        loss = outputs.loss

        optimizer.zero_grad()
        loss.backward()
        optimizer.step()

    print(f'Epoch {epoch+1}/{num_epochs}, Loss: {loss.item()}')

# Save the pretrained model
model.save_pretrained('pretrained_bert_model')
