import torch
from transformers import GPT2LMHeadModel, GPT2Tokenizer, TextDataset, DataCollatorForLanguageModeling
from transformers import Trainer, TrainingArguments
from ai_engine.model import GenAIModel
import os

class ModelTrainer:
    def __init__(self, model_name='gpt2', output_dir='./fine_tuned_model'):
        self.model_name = model_name
        self.output_dir = output_dir
        self.tokenizer = GPT2Tokenizer.from_pretrained(model_name)
        self.model = GPT2LMHeadModel.from_pretrained(model_name)

    def prepare_data(self, train_file, valid_file):
        train_dataset = TextDataset(
            tokenizer=self.tokenizer,
            file_path=train_file,
            block_size=128)

        valid_dataset = TextDataset(
            tokenizer=self.tokenizer,
            file_path=valid_file,
            block_size=128)

        data_collator = DataCollatorForLanguageModeling(
            tokenizer=self.tokenizer, mlm=False)

        return train_dataset, valid_dataset, data_collator

    def train(self, train_file, valid_file, num_train_epochs=3, per_device_train_batch_size=4):
        train_dataset, valid_dataset, data_collator = self.prepare_data(train_file, valid_file)

        training_args = TrainingArguments(
            output_dir=self.output_dir,
            overwrite_output_dir=True,
            num_train_epochs=num_train_epochs,
            per_device_train_batch_size=per_device_train_batch_size,
            save_steps=10_000,
            save_total_limit=2,
        )

        trainer = Trainer(
            model=self.model,
            args=training_args,
            data_collator=data_collator,
            train_dataset=train_dataset,
            eval_dataset=valid_dataset
        )

        trainer.train()
        self.model.save_pretrained(self.output_dir)
        self.tokenizer.save_pretrained(self.output_dir)

def fine_tune_model(train_file, valid_file):
    trainer = ModelTrainer()
    trainer.train(train_file, valid_file)
    return GenAIModel(model_path=trainer.output_dir)

if __name__ == "__main__":
    train_file = "data/processed/advanced_train.txt"
    valid_file = "data/processed/advanced_valid.txt"
    fine_tuned_model = fine_tune_model(train_file, valid_file)
    print("Fine-tuning completed. Model saved in ./fine_tuned_model")