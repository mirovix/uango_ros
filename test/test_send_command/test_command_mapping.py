import unittest

from src.send_command.command_mapping import CommandMapping


class TestMappingCommand(unittest.TestCase):
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

    def test_wrongCommand_whenCallCommand_thenRaiseException(self):
        wrong_command = "wrong_command"
        with self.assertRaises(Exception):
            self.mapping_command(wrong_command)

    def test_givenCommand_whenStrCommand_thenReturnString(self):
        self.mapping_command(self.yaml_data)
        self.assertEqual(f"attributes={self.mapping_command.__dict__})", str(self.mapping_command))


if __name__ == '__main__':
    unittest.main()
