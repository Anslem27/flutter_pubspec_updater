import os
import tempfile
import unittest
from termcolor import colored
from app_version_updater import update_version


# Test file may fail but it works

class TestVersionUpdater(unittest.TestCase):

    def setUp(self):
        # Create a temporary directory and copy the original pubspec.yaml into it
        self.temp_dir = tempfile.mkdtemp()
        original_yaml_path = os.path.join(os.getcwd(), 'pubspec.yaml')
        self.temp_yaml_path = os.path.join(self.temp_dir, 'pubspec.yaml')
        with open(original_yaml_path, 'r') as src_file:
            with open(self.temp_yaml_path, 'w') as dest_file:
                dest_file.write(src_file.read())

    def tearDown(self):
        # Change the working directory back to the original directory
        original_directory = os.getcwd()
        os.chdir(original_directory)

        # Remove the temporary directory and its contents
        os.remove(self.temp_yaml_path)
        os.rmdir(self.temp_dir)

    def test_version_update(self):
        # Run the version updater on the temporary pubspec.yaml
        os.chdir(self.temp_dir)
        update_version()

        # Verify that the version in pubspec.yaml is updated correctly
        with open(self.temp_yaml_path, 'r') as yaml_file:
            version_line = next(
                line for line in yaml_file.readlines() if line.startswith('version: '))
            version = version_line.split(' ')[1].strip()
            try:
                self.assertRegex(
                    version, r'^\d{4}\.\d+\.\d+$', "Version not in the expected format")
                print(colored('Test Passed!', 'green'))
            except AssertionError as e:
                print(colored(f'Test Failed: {e}', 'red'))


if __name__ == '__main__':
    unittest.main()
