from unittest import TestCase
from app import app

# Make Flask errors be real errors, rather than HTML pages with error info
app.config['TESTING'] = True


class LuckyNumsTests(TestCase):
    """Tests for LuckyNums app."""

    def test_valid(self):
        """Test response with valid payload."""
        with app.test_client() as client:
            resp = client.post(
                "/api/get-lucky-num", json={
                    "name": "test1",
                    "email": "test@gmail.com",
                    "year": "1990",
                    "color": "blue"
                })
            self.assertEqual(resp.status_code, 200)


            self.assertIsInstance(resp.json["num"]["fact"], str)
            self.assertIsInstance(resp.json["year"]["fact"], str)
            self.assertIsInstance(resp.json["num"]["num"], int)
            data = resp.json.copy()
            # Delete randomness of responses, and set number for testing
            # since the number is randomly generated.
            del data["num"]["fact"], data["year"]["fact"]
            data["num"]["num"] = 50
            self.assertEqual(
                data,
                {"num": {
                    "num": 50
                },
                "year": {
                    "year": "1990"
                }})

    def test_invalid(self):
        """Test response with an invalid payload."""
        with app.test_client() as client:
            resp = client.post(
                "/api/get-lucky-num", json={
                    "name": "",
                    "email": "test",
                    "year": "1000",
                    "color": "black"
                })
            self.assertEqual(resp.status_code, 200)

            self.assertEqual(resp.json,
                             {"error": {
                                 "color": [
                                    "Invalid value, must be one of: blue, green, red, orange."
                                 ],
                                 "email": [
                                     "Invalid email address."
                                 ],
                                 "name": [
                                     "Input required."
                                 ],
                                 "year": [
                                     "Year range must be between 1900 and 2000"
                                 ]}})
