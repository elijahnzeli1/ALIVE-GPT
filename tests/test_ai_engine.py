import unittest
import os
from ai_engine.model import GenAIModel
from ai_engine.training import fine_tune_model

class TestAIEngine(unittest.TestCase):
    def setUp(self):
        self.model = GenAIModel()

    def test_generate(self):
        prompt = "Once upon a time"
        generated_text = self.model.generate(prompt)
        self.assertIsInstance(generated_text, str)
        self.assertGreater(len(generated_text), len(prompt))

    def test_fine_tuning(self):
        # Create dummy train and valid files
        os.makedirs('data/processed', exist_ok=True)
        with open('data/processed/train.txt', 'w') as f:
            f.write("This is a test sentence for fine-tuning.\n" * 100)
        with open('data/processed/valid.txt', 'w') as f:
            f.write("This is a validation sentence for fine-tuning.\n" * 10)

        # Run fine-tuning
        fine_tuned_model = fine_tune_model('data/processed/train.txt', 'data/processed/valid.txt')

        # Check if the fine-tuned model exists
        self.assertTrue(os.path.exists('./fine_tuned_model/pytorch_model.bin'))

        # Test generation with fine-tuned model
        prompt = "This is a"
        generated_text = fine_tuned_model.generate(prompt)
        self.assertIsInstance(generated_text, str)
        self.assertGreater(len(generated_text), len(prompt))

if __name__ == '__main__':
    unittest.main()