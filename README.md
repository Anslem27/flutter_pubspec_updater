# Readme

## Description

> Open files for further documentation

This project consists of three Python scripts that facilitate the version updating, testing, and building process for a Flutter project.

### 1. `tester.py`

`tester.py` is a Python script that performs tests on the Flutter project's version updating functionality using the `app_version_updater.py` script. It uses Python's unittest module to run tests and checks if the version in the 'pubspec.yaml' file is updated correctly.

### 2. `app_version_updater.py`

`app_version_updater.py` is a Python script responsible for updating the version in the 'pubspec.yaml' file of the Flutter project. The script automatically increments the MAJOR version while resetting the MINOR version to zero. The updated version is based on the current year, in the format 'YYYY.MAJOR.MINOR'.

### 3. `create_build.py`

`create_build.py` is a Python script that automates the process of running the version updater and building both a Flutter APK and an app bundle. It ensures that the version is updated before building the APK and app bundle.
