import unittest

from web_socket.text_parser.message import Message
from web_socket.text_parser.parser import Parser


class TestParser(unittest.TestCase):
    def setUp(self):
        self.input_text = "2322730,115,2296,43690,0,0,7,0,4,0,70,0"
        self.length = 12

    def test_givenInputText_whenStreamIsCreated_thenInputTextIsSet(self):
        expected_list = ['2322730', '115', '2296', '43690', '0', '0', '7', '0', '4', '0', '70', '0']
        stream = Parser(self.input_text, self.length)
        self.assertEqual(stream.input_command, expected_list)
        self.assertEqual(len(stream.input_command), self.length)

    def test_givenWrongInputText_whenStreamIsCreated_thenGetError(self):
        input_text = "2322730,115,2296,43690,0,0"
        with self.assertRaises(ValueError):
            Parser(input_text, self.length)

    def test_givenInputText_whenCall_thenGetVariables(self):
        variables_dict = {"var1": "function1"}
        input_text = '100'
        upper_length = 1

        stream = Parser(input_text, upper_length)
        stream(variables_dict)

        expected_message = Message("var1", "function1", 100)
        actual_message = self._find_general_message(stream)

        self.assertEqual(actual_message, expected_message)

    def test_givenInputText_whenConvertedToString_thenStringIsReturned(self):
        stream = Parser(self.input_text, self.length)
        variables_dict = {"var1": "function1"}
        stream(variables_dict)
        expected = "var1 = 2322730"
        self.assertEqual(str(stream), expected)

    @staticmethod
    def _find_general_message(stream):
        for value in stream.__dict__.values():
            if isinstance(value, Message):
                return value
        return None
