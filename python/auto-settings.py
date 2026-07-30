def add_setting(settings, setting):
    key, value = setting
    key = key.lower()
    value = value.lower()
    print(key, value)
    if key in settings.keys():
        return f"Setting '[{key}]' already exists! Cannot add a new setting with this name."

    # settings.update(dict(setting))
    settings[key] = value
    return f"Setting '[{key}]' added with value '[{value}]' successfully!"


def update_setting(settings, setting):
    key, value = setting
    key = key.lower()
    value = value.lower()
    if key in settings.keys():
        settings[key] = value
        return f"Setting '[{key}]' updated to '[{value}]' successfully!"

    return f"Setting '[{key}]' does not exist! Cannot update a non-existing setting."


def delete_setting(settings, key):
    key = key.lower()
    if key in settings.keys():
        del settings[key]
        return f"Setting '[{key}]' deleted successfully!"

    return f"Setting {key} not found!"


def view_settings(settings):
    if not settings:
        return "No settings available."

    res = "Current User Settings:\n"
    for key, value in settings.items():
        res += key.capitalize() + ": " + str(value) + "\n"

    return res


test_settings = {"name": 'product', "port": 8080}

res = view_settings(test_settings)
print(res)

res = add_setting({'theme': 'light'}, ('volume', 'high'))
print(res)
print(add_setting({'theme': 'light'}, ('THEME', 'dark')))


