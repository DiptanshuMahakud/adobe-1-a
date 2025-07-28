
import os
import json
from extractor import extract_text_structure_from_pdf

# Base directory (adobe/)
BASE_DIR = os.path.abspath(os.path.dirname(__file__))

# Input/output paths
INPUT_DIR = os.path.join(BASE_DIR, "input")
OUTPUT_DIR = os.path.join(BASE_DIR, "output")

# Ensure output directory exists
os.makedirs(OUTPUT_DIR, exist_ok=True)

# Process each PDF file in the input directory
for filename in os.listdir(INPUT_DIR):
    if filename.lower().endswith(".pdf"):
        input_path = os.path.join(INPUT_DIR, filename)
        extracted_content = extract_text_structure_from_pdf(input_path)

        name_without_ext = os.path.splitext(filename)[0]
        output_filename = f"extracted_output_{name_without_ext}.json"
        output_path = os.path.join(OUTPUT_DIR, output_filename)

        with open(output_path, "w", encoding="utf-8") as f:
            json.dump(extracted_content, f, indent=2, ensure_ascii=False)

        print(f"✅ Extracted: {filename} → {output_filename}")



# import os
# import json
# from extractor import extract_from_directory

# # Get the base directory (adobe/)
# BASE_DIR = os.path.abspath(os.path.dirname(__file__))

# # Define input and output paths
# INPUT_DIR = os.path.join(BASE_DIR, "input")
# OUTPUT_DIR = os.path.join(BASE_DIR, "output")
# OUTPUT_FILE = os.path.join(OUTPUT_DIR, "extracted_output.json")

# # Ensure output directory exists
# os.makedirs(OUTPUT_DIR, exist_ok=True)

# # Extract text structure from all PDFs in the input directory
# extracted_data = extract_from_directory(INPUT_DIR)

# # Save results to a JSON file
# with open(OUTPUT_FILE, "w", encoding="utf-8") as f:
#     json.dump(extracted_data, f, indent=2, ensure_ascii=False)

# print(f"\n✅ Extracted content saved to: {OUTPUT_FILE}")
