import unittest

from app.meta_weather import MetaWeather


class TestMetaWeather(unittest.TestCase):

    def test_weather(self):
        self.assertIn(member="Clear", container=MetaWeather("dubai").forecast(), msg="Keyword Not Found")

    def test_woeid_id(self):
        self.assertIn(member="1940345", container=MetaWeather("dubai").find_location_woeid_id(),
                      msg="Woeid Id Not Match")

    def test_wrong_city(self):
        self.assertIn(member="Woeid Id Not Valid", container=MetaWeather("wrong_city").find_location_woeid_id(),
                      msg="Woeid id should not come")


if __name__ == '__main__':
    unittest.main()
