import os
import fitz  # PyMuPDF

def extract_text_structure_from_pdf(pdf_path):
    doc = fitz.open(pdf_path)
    content = []

    for page_num, page in enumerate(doc, start=1):
        blocks = page.get_text("dict")["blocks"]
        spans_info = []

        for block in blocks:
            for line in block.get("lines", []):
                for span in line["spans"]:
                    text = span["text"].strip()
                    if text:
                        spans_info.append({
                            "text": text,
                            "size": span["size"],
                            "bold": span["flags"] & 2 != 0,
                            "font": span["font"],
                            "y": span["bbox"][1],
                            "page": page_num
                        })

        sizes = [s["size"] for s in spans_info]
        if not sizes:
            continue
        body_font_size = sorted(sizes)[len(sizes) // 2]

        buffer = []
        last_type = None
        buffer_size = 0
        buffer_page = 0

        def flush_buffer():
            if buffer:
                content.append({
                    "text": " ".join(buffer).strip(),
                    "size": buffer_size,
                    "page": buffer_page
                })

        for span in spans_info:
            is_heading = span["size"] > body_font_size or span["bold"]
            current_type = "heading" if is_heading else "paragraph"

            if current_type != last_type:
                flush_buffer()
                buffer = []
                buffer_size = span["size"]
                buffer_page = span["page"]

            buffer.append(span["text"])
            last_type = current_type

        flush_buffer()

    return content





# import os
# import fitz  # PyMuPDF

# def extract_text_structure_from_pdf(pdf_path):
#     doc = fitz.open(pdf_path)
#     content = []

#     for page in doc:
#         blocks = page.get_text("dict")["blocks"]
#         spans_info = []

#         for block in blocks:
#             for line in block.get("lines", []):
#                 for span in line["spans"]:
#                     text = span["text"].strip()
#                     if text:
#                         spans_info.append({
#                             "text": text,
#                             "size": span["size"],
#                             "bold": span["flags"] & 2 != 0,
#                             "font": span["font"],
#                             "y": span["bbox"][1]
#                         })

#         # Heuristic: base font size is the body text
#         sizes = [s["size"] for s in spans_info]
#         if not sizes:
#             continue
#         body_font_size = sorted(sizes)[len(sizes) // 2]

#         buffer = []
#         last_type = None  # 'heading' or 'paragraph'

#         for span in spans_info:
#             is_heading = span["size"] > body_font_size or span["bold"]
#             current_type = "heading" if is_heading else "paragraph"

#             if current_type != last_type:
#                 if buffer:
#                     content.append(" ".join(buffer).strip())
#                     buffer = []
#             buffer.append(span["text"])
#             last_type = current_type

#         if buffer:
#             content.append(" ".join(buffer).strip())

#     return content


# def extract_from_directory(directory_path):
#     result = {}
#     for filename in os.listdir(directory_path):
#         if filename.lower().endswith(".pdf"):
#             file_path = os.path.join(directory_path, filename)
#             result[filename] = extract_text_structure_from_pdf(file_path)
#     return result
