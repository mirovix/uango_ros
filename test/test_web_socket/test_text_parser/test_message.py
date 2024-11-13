import unittest

from text_parser.message import Message


class TestMessage(unittest.TestCase):
    def test_givenValues_whenGeneralMessageIsCreated_thenValuesAreSet(self):
        msg = Message("TestName", "TestFunction", 123)
        self.assertEqual(msg.name, "TestName")
        self.assertEqual(msg.function, "TestFunction")
        self.assertEqual(msg.value, 123)

    def test_givenEqualMessages_whenCompared_thenTheyAreEqual(self):
        msg1 = Message("TestName", "TestFunction", 123)
        msg2 = Message("TestName", "TestFunction", 123)
        msg3 = Message("DifferentName", "TestFunction", 123)
        self.assertEqual(msg1, msg2)
        self.assertNotEqual(msg1, msg3)

    def test_givenMessage_whenConvertedToString_thenStringIsReturned(self):
        msg = Message("TestName", "TestFunction", 123)
        self.assertEqual(str(msg), "TestName = 123")
