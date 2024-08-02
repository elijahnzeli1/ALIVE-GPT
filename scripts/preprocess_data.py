import os
import json
from sklearn.model_selection import train_test_split

def preprocess_data():
    raw_data_dir = 'data/raw'
    processed_data_dir = 'data/processed'
    
    if not os.path.exists(processed_data_dir):
        os.makedirs(processed_data_dir)
    
    all_data = []
    
    for filename in os.listdir(raw_data_dir):
        if filename.endswith('.txt'):
            with open(os.path.join(raw_data_dir, filename), 'r', encoding='ISO-8859-1') as f:
                data = f.read()
            
            # Perform any necessary preprocessing steps here
            processed_data = data.lower()
            all_data.append(processed_data)
    
    # Split data into train and validation sets
    train_data, valid_data = train_test_split(all_data, test_size=0.1, random_state=42)
    
    # Save train and validation data
    with open(os.path.join(processed_data_dir, 'advanced_train.txt'), 'w', encoding='utf-8') as f:
        f.write('\n'.join(train_data))
    
    with open(os.path.join(processed_data_dir, 'advanced_valid.txt'), 'w', encoding='utf-8') as f:
        f.write('\n'.join(valid_data))

    # Define rl_data before using it in the loop
    rl_data = [("seq1", 1), ("seq2", 2), ("seq3", 3)]
    
    with open(os.path.join(processed_data_dir, 'rl_data.txt'), 'w', encoding='utf-8') as f:
        for seq, rating in rl_data:
            f.write(f"{seq}\t{rating}\n")

if __name__ == "__main__":
    preprocess_data()