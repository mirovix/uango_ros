import unittest

from text_parser.general_message import GeneralMessage
from text_parser.stream_message.stream import Stream


class TestStreamMessage(unittest.TestCase):
    def setUp(self):
        self.input_text = "2322730,115,2296,43690,0,0,7,0,4,0,70,0"

    def test_givenInputText_whenStreamIsCreated_thenInputTextIsSet(self):
        expected_list = ['2322730', '115', '2296', '43690', '0', '0', '7', '0', '4', '0', '70', '0']
        stream = Stream(self.input_text)
        self.assertEqual(stream.input_command, expected_list)
        self.assertEqual(len(stream.input_command), 12)

    def test_givenWrongInputText_whenStreamIsCreated_thenGetError(self):
        input_text = "2322730,115,2296,43690,0,0"
        with self.assertRaises(ValueError):
            Stream(input_text)

    def test_givenInputText_whenCall_thenGetVariables(self):
        variables_dict = {"var1": "function1"}
        input_text = '100'
        upper_length = 1

        stream = Stream(input_text, upper_length)
        stream(variables_dict)

        expected_message = GeneralMessage("var1", "function1", 100)
        actual_message = self._find_general_message(stream)

        self.assertEqual(actual_message, expected_message)

    @staticmethod
    def _find_general_message(stream):
        for value in stream.__dict__.values():
            if isinstance(value, GeneralMessage):
                return value
        return None
