import unittest
from unittest.mock import patch

from send_command.command_main import CommandMain


class TestCommandMain(unittest.TestCase):
    def setUp(self):
        self.mocked_mapping = {'command': {'function': 'function', 'id': 1}}
        self.wrong_command_main = CommandMain(["sys1", "wrong_command"])
        self.command_main = CommandMain(["sys1", "command"])

    def test_GivenCommandMain_WhenInitCommandMain_ThenReturnCommandMain(self):
        self.assertEqual("command", self.command_main.command)
        self.assertTrue(self.command_main.yaml_path.endswith("mapping.yaml"))

    def test_givenCommandMain_WhenCommandIsEmpty_ThenRaiseException(self):
        with self.assertRaises(SystemExit):
            self.empty_command_main = CommandMain(["sys1"])

    def test_givenCommandMain_WhenMappingFileIsNotFound_ThenRaiseException(self):
        self.command_main.yaml_path = "not_found.yaml"
        with self.assertRaises(FileNotFoundError):
            self.command_main._load_mapping_yaml()

    def test_givenCommandMain_WhenLoadMappingYaml_ThenReturnMapping(self):
        mapping = self.command_main._load_mapping_yaml()
        self.assertGreater(len(mapping), 4)
        self.assertIsInstance(mapping, dict)

    @patch('send_command.command_main.CommandMain._load_mapping_yaml')
    def test_givenCommandMain_WhenCallCommandMain_ThenReturnCommandMapping(self, mock_load_mapping_yaml):
        mock_load_mapping_yaml.return_value = self.mocked_mapping
        command_mapping = self.command_main()
        self.assertEqual("command", command_mapping.command)
        self.assertEqual("function", command_mapping.function)
        self.assertEqual(1, command_mapping.id)

    @patch('send_command.command_main.CommandMain._load_mapping_yaml')
    def test_givenCommandMain_WhenCommandNotFound_ThenRaiseException(self, mock_load_mapping_yaml):
        mock_load_mapping_yaml.return_value = self.mocked_mapping
        with self.assertRaises(SystemExit):
            self.wrong_command_main()
