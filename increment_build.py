import re

version_string = "v6.42 Build 23"
match = re.match(r"^(.* Build )(\d+)$", version_string)

if match:
    prefix = match.group(1)
    build_number = int(match.group(2))
    new_build_number = build_number + 1
    new_version_string = f"{prefix}{new_build_number}"
    print(new_version_string)
else:
    print(f"Error: Could not parse version string: {version_string}")
