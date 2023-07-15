```python
import os
import json
import subprocess
import sys

def get_os_type():
    if os.name == 'nt':
        return 'Windows'
    elif sys.platform == 'darwin':
        return 'macOS'
    else:
        return 'Linux'

def install_packages(packages):
    for package in packages:
        try:
            subprocess.check_call([sys.executable, '-m', 'pip', 'install', package])
        except subprocess.CalledProcessError as e:
            handle_errors(e)

def configure_environment(config_settings, env_vars):
    os.environ.update(env_vars)
    with open('config.json', 'w') as f:
        json.dump(config_settings, f)

def handle_errors(e):
    print(f"An error occurred: {e}")
    sys.exit(1)

def customize_setup(customizations):
    for key, value in customizations.items():
        os.environ[key] = value

def main():
    os_type = get_os_type()
    with open('requirements.txt') as f:
        packages = f.read().splitlines()
    with open('config.json') as f:
        config = json.load(f)
    config_settings = config['settings']
    env_vars = config['env_vars']
    customizations = config['customizations']

    print(f"Setting up development environment on {os_type}...")
    install_packages(packages)
    configure_environment(config_settings, env_vars)
    customize_setup(customizations)
    print("Setup completed successfully!")

if __name__ == "__main__":
    main()
```