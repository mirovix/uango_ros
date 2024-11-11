import re
import unittest

from send_command.command_mapping import CommandMapping


class TestCommandMapping(unittest.TestCase):
    def setUp(self):
        self.yaml_data = {
            'id': 1,
            'femur_angle_in_sitting_position': 0,
            'knee_angle_in_sitting_position': 0,
            'min_femur_angle': -90,
            'max_femur_angle': 90,
            'min_knee_angle': -90,
            'max_knee_angle': 90,
            'function': 'sets the values of the angles'
        }
        self.cmd = "set_homing_down_cmd"
        self.mapping_command = CommandMapping(self.cmd)

    def test_givenCommand_whenInitCommand_thenReturnCommand(self):
        self.assertEqual(self.cmd, self.mapping_command.command)

    def test_givenCommand_whenCallCommand_thenReturnCommand(self):
        self.mapping_command(self.yaml_data)
        mapping_dict = self.mapping_command.__dict__
        mapping_dict.pop('command')
        for key, value in mapping_dict.items():
            self.assertEqual(self.yaml_data[key], value)

    def test_givenEmptyCommand_whenCallCommand_thenReturnEmptyCommand(self):
        self.mapping_command({})
        mapping_dict = self.mapping_command.__dict__
        mapping_dict.pop('command')
        for key, value in mapping_dict.items():
            self.assertEqual(None, value)

    def test_givenCommand_whenStrCommand_thenReturnString(self):
        self.mapping_command(self.yaml_data)

        expected = """
        command: set_homing_down_cmd
        id: 1
        femur_angle_in_sitting_position: 0
        knee_angle_in_sitting_position: 0
        min_femur_angle: -90
        max_femur_angle: 90
        min_knee_angle: -90
        max_knee_angle: 90
        function: sets the values of the angles"""

        expected = re.sub(r'\s+', '', expected)
        result = re.sub(r'\s+', '', str(self.mapping_command))
        self.assertEqual(expected, result)

    def test_givenCommand_whenGetCommandSequence_thenReturnSequenceString(self):
        self.mapping_command(self.yaml_data)
        expected = "1,0,0,-90,90,-90,90;"
        self.assertEqual(expected, self.mapping_command.get_command_sequence())
