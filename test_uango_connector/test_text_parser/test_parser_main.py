import unittest
from unittest.mock import patch

from uango_connector.text_parser.parser_main import ParserMain


class TestCommandMain(unittest.TestCase):
    def setUp(self):
        self.input_text = ("2322730,115,2296,43690,0,0,7,0,4,0,70,0,-12,6000,7500,15,"
                           "6000,6,3065,55,0,567,3,7,5,0,0,0,0,0,173,1000,0,0,0,-12,"
                           "6000,7500,15,6000,0,3152,54,0,567,3,7,5,0,0,0,0,0,173,1000,"
                           "0,0,0,0,6000,7500,15,6000,30,3103,54,0,567,3,7,5,0,0,0,0,0,"
                           "173,1000,0,0,0,0,6000,7500,15,6000,6,3125,52,0,567,3,7,5,0,"
                           "0,0,0,0,173,1000,0,0,0,25588;")
        self.mocked_exo_data = {'system_state': {2322730: 'varname1'},
                                'stream': {'system_state': 'function1'},
                                'joint': {'varname1': 'function1'}}
        self.wrong_command_main = ParserMain("wrong_command;")
        self.command_main = ParserMain(self.input_text)

    def test_GivenCommandMain_WhenInitCommandMain_ThenReturnCommandMain(self):
        self.assertEqual(self.input_text[:-1], self.command_main.concatenated_text)
        self.assertTrue(self.command_main.yaml_path.endswith("exo_data.yaml"))

    def test_GivenCommandMain_WhenMappingFileIsNotFound_ThenRaiseException(self):
        self.command_main.yaml_path = "not_found.yaml"
        with self.assertRaises(FileNotFoundError):
            self.command_main._load_mapping_yaml()

    @patch("uango_connector.text_parser.parser_main.yaml.load")
    def test_GivenCommandMain_WhenMappingFileIsFound_ThenReturnExoData(self, yaml_load):
        yaml_load.return_value = self.mocked_exo_data
        exo_data = self.command_main._load_mapping_yaml()
        self.assertEqual(self.mocked_exo_data, exo_data)

    @patch("uango_connector.text_parser.parser_main.ParserMain._load_mapping_yaml")
    def test_GivenCommandMain_WhenCallCommandMain_ThenReturnSetAttributes(self, load_mapping_yaml):
        load_mapping_yaml.return_value = self.mocked_exo_data
        self.command_main()
        self.assertTrue(hasattr(self.command_main, "stream"))
        self.assertTrue(hasattr(self.command_main, "fem_left"))
        self.assertTrue(hasattr(self.command_main, "tib_left"))
        self.assertTrue(hasattr(self.command_main, "fem_right"))
