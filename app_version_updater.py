import re
from datetime import datetime
import fileinput
from termcolor import colored

def update_version():
    """
    Updates the version in the pubspec.yaml file based on the current year.

    The function reads the 'pubspec.yaml' file and searches for the version pattern
    in the format 'YYYY.MAJOR.MINOR'. It increments the MAJOR version and sets the MINOR version to 0,
    updating the version to 'YYYY.(MAJOR+1).0'. The updated version is written back to the file.

    The updated version will be colored green, and if no version update is performed,
    a message will be printed in yellow.

    Note:
    The script assumes the presence of a 'pubspec.yaml' file in the current working directory.
    The version pattern in the 'pubspec.yaml' file should be of the format 'YYYY.MAJOR.MINOR'.

    Example:
    - If the original version is '2023.1.0', it will be updated to '2023.2.0'.
    - If the original version is '2023.3.5', it will be updated to '2023.4.0'.

    Raises:
        FileNotFoundError: If 'pubspec.yaml' file is not found in the current working directory.
    """
    current_year = datetime.now().year
    version_pattern = r'^version: (\d{4}\.\d+\.\d+)'

    next_version = None  # Initialize next_version with a default value

    with fileinput.FileInput('pubspec.yaml', inplace=True, backup='.bak') as file:
        for line in file:
            match = re.match(version_pattern, line)
            if match:
                current_version = match.group(1)
                parts = current_version.split('.')
                next_version = f'{current_year}.{int(parts[1]) + 1}.0'
                line = line.replace(current_version, next_version)
            print(line, end='')

    if next_version is not None:
        print(colored(f'Version updated to {next_version}', 'green'))
    else:
        print(colored('No version update.', 'yellow'))


if __name__ == "__main__":
    update_version()
