import requests
import unittest
from unittest.mock import patch, Mock

#Diese code ist aus folgenden Tutorial: Professional Python Testing with Mock          von: NeuralNine upload: 2023

def get_user_data(user_id):
    response = requests.get(f"http://example15ikja8Hkee.com/users/{user_id}")
    return response.json()

class TestUserData(unittest.TestCase):
    @patch("requests.get")
    def test_get_user_data(self, mock_get):
        mock_response = Mock()
        response_dict = {"name": "John", "email": "john@gmail.com"}
        mock_response.json.return_value = response_dict
        mock_get.return_value = mock_response
        user_data = get_user_data(1)
        mock_get.assert_called_with("http://example15ikja8Hkee.com/users/1")
        self.assertEqual(user_data, response_dict)

if __name__ == "__main__":
    unittest.main()



#Nachfolgender Code von: mCoding   video Modern Python Logging          aus 2023
