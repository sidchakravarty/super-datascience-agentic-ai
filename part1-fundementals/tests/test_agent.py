import unittest
from unittest.mock import patch, MagicMock
from src.agent import google_client
from src.config import Config

class TestGoogleAgent(unittest.TestCase):

    @patch.object(google_client.models, 'generate_content')
    def test_gemini_generation(self, mock_generate):
        # Setup: Mock the response object
        mock_response = MagicMock()
        mock_response.text = "Mocked Response"
        mock_generate.return_value = mock_response

        # Act: Call the model
        response = google_client.models.generate_content(
            model=Config.DEFAULT_GEMINI_MODEL,
            contents="Hello, World!",
            temperature=0.7,
            max_tokens=100
        )

        # Assert: Verify the logic
        self.assertEqual(response.text, "Mocked Response")
        mock_generate.assert_called_once_with(
            model=Config.DEFAULT_GEMINI_MODEL,
            contents="Hello, World!",
            temperature=0.7,
            max_tokens=100
        )


if __name__ == "__main__":
    unittest.main()