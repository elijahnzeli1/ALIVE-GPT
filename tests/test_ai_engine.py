import unittest
from ai_engine.model import GenAIModel

class TestAIEngine(unittest.TestCase):
    def setUp(self):
        self.model = GenAIModel()

    def test_generate(self):
        prompt = "Once upon a time"
        generated_text = self.model.generate(prompt)
        self.assertIsInstance(generated_text, str)
        self.assertGreater(len(generated_text), len(prompt))

if __name__ == '__main__':
    unittest.main()