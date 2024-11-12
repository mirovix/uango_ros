import unittest

from text_parser.general_message import GeneralMessage


class TestGeneralMessage(unittest.TestCase):
    def test_givenValues_whenGeneralMessageIsCreated_thenValuesAreSet(self):
        msg = GeneralMessage("TestName", "TestFunction", 123)
        self.assertEqual(msg.name, "TestName")
        self.assertEqual(msg.function, "TestFunction")
        self.assertEqual(msg.value, 123)

    def test_givenEqualMessages_whenCompared_thenTheyAreEqual(self):
        msg1 = GeneralMessage("TestName", "TestFunction", 123)
        msg2 = GeneralMessage("TestName", "TestFunction", 123)
        msg3 = GeneralMessage("DifferentName", "TestFunction", 123)
        self.assertEqual(msg1, msg2)
        self.assertNotEqual(msg1, msg3)

    def test_givenMessage_whenConvertedToString_thenStringIsReturned(self):
        msg = GeneralMessage("TestName", "TestFunction", 123)
        self.assertEqual(str(msg), "name = TestName, value = 123")
