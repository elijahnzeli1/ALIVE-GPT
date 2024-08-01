import unittest
from api import app, db
from api.models import GeneratedContent

class TestAPI(unittest.TestCase):
    def setUp(self):
        app.config['TESTING'] = True
        app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///:memory:'
        self.client = app.test_client()
        db.create_all()

    def tearDown(self):
        db.session.remove()
        db.drop_all()

    def test_generate_endpoint(self):
        response = self.client.post('/api/generate', json={'prompt': 'Test prompt'})
        self.assertEqual(response.status_code, 200)
        self.assertIn('generated_text', response.json)

    def test_history_endpoint(self):
        response = self.client.get('/api/history')
        self.assertEqual(response.status_code, 200)
        self.assertIsInstance(response.json, list)

if __name__ == '__main__':
    unittest.main()