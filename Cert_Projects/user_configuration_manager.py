def add_setting(settings: dict[str, str], setting: tuple[str, str]) -> str:
    """Add setting key-value pair to settings dict."""
    k: str = setting[0].lower()
    v: str = setting[1].lower()

    if k in settings:
        return f"Setting '{k}' already exists! Cannot add a new setting with this name."
    else:
        settings[k] = v
        return f"Setting '{k}' added with value '{v}' successfully!"


def update_setting(settings: dict[str, str], setting: tuple[str, str]) -> str:
    """Update settings dict with setting."""
    k: str = setting[0].lower()
    v: str = setting[1].lower()

    if k in settings:
        settings[k] = v
        return f"Setting '{k}' updated to '{v}' successfully!"
    else:
        return f"Setting '{k}' does not exist! Cannot update a non-existing setting."


def delete_setting(settings: dict[str, str], key: str) -> str:
    """Delete entry from settings dict"""
    k: str = key.lower()

    if k in settings:
        del settings[k]
        return f"Setting '{k}' deleted successfully!"
    else:
        return "Setting not found!"


def view_settings(settings: dict[str, str]) -> str:
    """Build and return formatted string output for settings dict."""
    settings_output: str = "Current User Settings:\n"

    if not settings:
        return "No settings available."
    else:
        for k, v in settings.items():
            settings_output += f"{k.capitalize()}: {v}\n"

    return settings_output


TEST_SETTINGS = {
    "theme": "dark",
    "language": "english",
    "notifications": "enabled",
    "volume": "high"
}
