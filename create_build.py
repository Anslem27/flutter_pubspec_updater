import os
import subprocess
from termcolor import colored

def run_updater():
    """
    Runs the app_version_updater.py script to update the version in pubspec.yaml.

    The function executes the app_version_updater.py script in the current working directory.
    It prints colored messages to indicate the status of the updater's execution.

    Raises:
        subprocess.CalledProcessError: If there's an error during the execution of the updater script.
    """
    updater_script = os.path.join(os.getcwd(), 'app_version_updater.py')
    print(colored('Running updater...', 'cyan'))
    subprocess.run(['python', updater_script], check=True)
    print(colored('Updater completed successfully.', 'green'))

def build_apk():
    """
    Builds the Flutter APK.

    The function executes the 'flutter build apk' command using the 'subprocess.run()' method.
    It prints colored messages to indicate the status of the APK build process.

    Raises:
        subprocess.CalledProcessError: If there's an error during the APK build process.
    """
    print(colored('Building Flutter APK...', 'cyan'))
    try:
        subprocess.run('flutter build apk', check=True, shell=True)
        print(colored('APK build completed successfully.', 'green'))
    except subprocess.CalledProcessError as e:
        print(colored(f'APK build error: {e}', 'red'))
        exit(1)

def build_app_bundle():
    """
    Builds the Flutter App Bundle.

    The function executes the 'flutter build appbundle' command using the 'subprocess.run()' method.
    It prints colored messages to indicate the status of the app bundle build process.

    Raises:
        subprocess.CalledProcessError: If there's an error during the app bundle build process.
    """
    print(colored('Building Flutter App Bundle...', 'cyan'))
    try:
        subprocess.run('flutter build appbundle', check=True, shell=True)
        print(colored('App Bundle build completed successfully.', 'green'))
    except subprocess.CalledProcessError as e:
        print(colored(f'App Bundle build error: {e}', 'red'))
        exit(1)

if __name__ == "__main__":
    try:
        run_updater()
        build_apk()
        build_app_bundle()
    except Exception as e:
        print(colored(f'An error occurred: {e}', 'red'))
        exit(1)

    print(colored('Build process completed successfully!', 'green'))
