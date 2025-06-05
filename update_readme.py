#!/usr/bin/env python3

import re
from datetime import datetime

# Read the existing README.md content
with open("README.md", "r", encoding="utf-8") as f:
    content = f.read()

# Construct the new month-year string, e.g. "February 2025"
current_date_str = datetime.now().strftime("%d %B %Y")

# Regex pattern to match something like:
# "# IDM Trial Reset Tool (v6.42 Build 23) - January 2025"
pattern = r"(# IDM Trial Reset Tool \(v\d+\.\d+ Build \d+\) - )(\d*\s*[A-Za-z]+\s+\d{4})"
replacement = r"\g<1>" + current_date_str

new_content = re.sub(pattern, replacement, content)

# Overwrite README.md with the updated content
with open("README.md", "w", encoding="utf-8") as f:
    f.write(new_content)
