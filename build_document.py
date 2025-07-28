from model.classifier import classify

def build_document_structure(classified_entries):
    """
    classified_entries: List of dicts like {'text': ..., 'size': ..., 'page': ..., 'level': ...}
    """
    title = None
    outline = []

    for entry in classified_entries:
        prediction = classify(entry["text"])  # Your ML model returns 0, 1, or 2

        if prediction == 0:
            if not title:
                title = entry["text"]  # Set the first title
            else:
                # Subsequent titles can also be part of the outline
                outline.append({
                    "level": entry["level"],
                    "text": entry["text"],
                    "page": entry["page"]
                })

        elif prediction == 1:
            outline.append({
                "level": entry["level"],
                "text": entry["text"],
                "page": entry["page"]
            })

        # If prediction == 2, ignore

    return {
        "title": title or "Untitled Document",
        "outline": outline
    }
