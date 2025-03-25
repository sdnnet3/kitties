import argparse
from bs4 import BeautifulSoup
import os

# Set up argument parser
parser = argparse.ArgumentParser(description="Format all HTML files in the current folder and subfolders and save as XML.")
args = parser.parse_args()

# Get the current directory where the script is located
current_directory = os.path.dirname(os.path.abspath(__file__))

# Process each HTML file in the current directory and subdirectories
for root, dirs, files in os.walk(current_directory):
    for filename in files:
        if filename.endswith(".html"):
            input_file = os.path.join(root, filename)
            output_file = os.path.join(root, os.path.splitext(filename)[0] + ".xml")

            # Read the input file
            with open(input_file, "r", encoding="utf-8") as file:
                html = file.read()

            soup = BeautifulSoup(html, "html.parser")
            pretty_html = soup.prettify()

            # Save to the output file
            with open(output_file, "w", encoding="utf-8") as file:
                file.write(pretty_html)

            print(f"Formatted output saved to {output_file}")