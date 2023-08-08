# update_readme.py

from datetime import datetime

with open("README.md", "a") as file:
    file.write("\nLast update: " + datetime.now().strftime('%Y-%m-%d %H:%M:%S'))
