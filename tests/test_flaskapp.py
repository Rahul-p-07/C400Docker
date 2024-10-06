import unittest
from flaskapp import app

class FlaskAppTestCase(unittest.TestCase):

    # This method will be called before each test to set up the test environment
    def setUp(self):
        # Creates a test client for the app
        self.app = app.test_client()
        # Propagate exceptions to the test client
        self.app.testing = True

    # Test case for the index route
    def test_index(self):
        # Sends a GET request to the '/' route
        response = self.app.get('/')
        
        # Ensure the response status code is 200 (OK)
        self.assertEqual(response.status_code, 200)

        # Ensure the response data matches the expected output
        #self.assertEqual(response.json, {'message': 'Hello, World!'})

    # Test case for an invalid route
    def test_404(self):
        # Sends a GET request to a non-existent route
        response = self.app.get('/invalid-route')

        # Ensure the response status code is 404 (Not Found)
        self.assertEqual(response.status_code, 404)

if __name__ == '__main__':
    unittest.main()
