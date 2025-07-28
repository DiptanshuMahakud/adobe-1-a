import os
import json
from extractor import extract_text_structure_from_pdf
from classify_heading import classify_text
from build_document import build_document_structure


BASE_DIR = os.path.abspath(os.path.dirname(__file__))
INPUT_DIR = os.path.join(BASE_DIR, "input")
OUTPUT_DIR = os.path.join(BASE_DIR, "output")

# Ensure output directory exists
os.makedirs(OUTPUT_DIR, exist_ok=True)

# Final combined result
combined_output = {}

# Process each PDF
for filename in os.listdir(INPUT_DIR):
    if filename.lower().endswith(".pdf"):
        input_path = os.path.join(INPUT_DIR, filename)
        extracted_content = extract_text_structure_from_pdf(input_path)
        classified_contents = classify_text(extracted_content)
        structured_output = build_document_structure(classified_contents)

        name_without_ext = os.path.splitext(filename)[0]
        output_filename = f"{name_without_ext}.json"  # 🔁 changed here
        output_path = os.path.join(OUTPUT_DIR, output_filename)

        # Write individual file output
        with open(output_path, "w", encoding="utf-8") as f:
            json.dump(structured_output, f, indent=2, ensure_ascii=False)

        # Add to combined output
        combined_output[filename] = extracted_content

# Write combined output
combined_output_path = os.path.join(OUTPUT_DIR, "output.json")
with open(combined_output_path, "w", encoding="utf-8") as f:
    json.dump(combined_output, f, indent=2, ensure_ascii=False)

print("✅ All PDFs processed. Individual and combined outputs are saved.")
