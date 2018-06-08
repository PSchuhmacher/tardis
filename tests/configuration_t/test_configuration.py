from tardis.configuration.configuration import Configuration

from unittest import TestCase
import os


class TestConfiguration(TestCase):
    def setUp(self):
        self.test_path = os.path.dirname(os.path.realpath(__file__))
        self.configuration1 = Configuration(os.path.join(self.test_path, 'CloudStackAIO.yml'))
        self.configuration2 = Configuration()

    def test_configuration_instances(self):
        self.assertNotEqual(id(self.configuration1), id(self.configuration2))

    def test_shared_state(self):
        self.assertEqual(id(self.configuration1.CloudStackAIO), id(self.configuration2.CloudStackAIO))

    def test_load_configuration(self):
        self.configuration1.load_config(os.path.join(self.test_path, 'Sites.yml'))
        self.assertEqual(id(self.configuration1.Sites), id(self.configuration2.Sites))
        self.assertEqual(self.configuration1.Sites, ['Exoscale'])
        self.assertEqual(self.configuration2.CloudStackAIO, {'api_key': 'asdfghjkl', 'api_secret': 'qwertzuiop'})

    def test_access_missing_attribute(self):
        with self.assertRaises(AttributeError):
            _ = self.configuration2.FooBar
