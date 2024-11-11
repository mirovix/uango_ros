import importlib.util
import logging
import os
import sys
import unittest
from pathlib import Path

if __name__ == "__main__":
    original_stdout = sys.stdout
    sys.stdout = open(os.devnull, 'w')
    script_directory = Path(__file__).resolve().parent

    loader = unittest.TestLoader()
    suite = unittest.TestSuite()

    for file in script_directory.glob("test/**/*.py"):
        module_name = file.stem
        spec = importlib.util.spec_from_file_location(module_name, file)
        test_module = importlib.util.module_from_spec(spec)
        spec.loader.exec_module(test_module)
        suite.addTests(loader.loadTestsFromModule(test_module))

    runner = unittest.TextTestRunner(verbosity=2)
    test_result = runner.run(suite)

    logging.shutdown()
    sys.stdout = original_stdout

    sys.exit(0 if test_result.wasSuccessful() else 1)
