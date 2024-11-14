import tkinter as tk
import unittest
from unittest.mock import patch, MagicMock

from uango_connector.gui.control_app import ControlApp


class TestControlApp(unittest.TestCase):
    def setUp(self):
        self.root = tk.Tk()
        self.app = ControlApp(self.root)

    def tearDown(self):
        self.root.destroy()

    @patch('uango_connector.gui.control_app.WebSocketApp')
    @patch('uango_connector.gui.control_app.ControlApp.get_buttons_name')
    def test_givenControlApp_whenCall_thenButtonsAreCreated(self, mock_get_buttons_name, mock_run):
        self.assertEqual(self.app.root.title(), "Uango Control")
        self.assertEqual(self.app.root.geometry(), '1x1+0+0')

        mock_run.return_value = MagicMock()
        mock_get_buttons_name.return_value = ['button_1']
        self.app()
        self.assertEqual(1, len(self.root.winfo_children()))
        self.assertEqual('BUTTON 1', self.root.winfo_children()[0].cget('text'))
        self.assertEqual(6, self.root.winfo_children()[0].cget('height'))
        self.assertEqual(30, self.root.winfo_children()[0].cget('width'))

    def test_givenControlApp_whenGetButtonName_thenReturnList(self):
        self.assertEqual(15, len(self.app.get_buttons_name()))
