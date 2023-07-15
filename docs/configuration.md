# Configuration Guide

This guide will help you understand how to configure the Smol Developer Setup Script.

## Configuring the Setup Script

The configuration of the setup script is managed through the `config.json` file. This file contains various settings and environment variables that are used by the `setup_script.py`.

### Structure of `config.json`

The `config.json` file is structured as follows:

```json
{
    "os_type": "<operating_system_type>",
    "packages": ["<package1>", "<package2>", "..."],
    "config_settings": {
        "<setting1>": "<value1>",
        "<setting2>": "<value2>",
        "..."
    },
    "env_vars": {
        "<var1>": "<value1>",
        "<var2>": "<value2>",
        "..."
    }
}
```

### Explanation of Fields

- `os_type`: This field specifies the type of operating system. It can be "Windows", "macOS", or "Linux".

- `packages`: This is an array of software packages to be installed. Each package should be specified by its name.

- `config_settings`: This is an object that contains various configuration settings. Each setting is specified by its name and value.

- `env_vars`: This is an object that contains environment variables. Each variable is specified by its name and value.

## Modifying `config.json`

To modify the `config.json` file, open it in a text editor and change the values as needed. Save the file when you are done.

## Applying Configuration Changes

To apply the changes made in the `config.json` file, run the `setup_script.py` again. The script will read the `config.json` file and apply the configuration settings and environment variables.

## Conclusion

This guide has shown you how to configure the Smol Developer Setup Script. By modifying the `config.json` file, you can customize the setup process to suit your needs.