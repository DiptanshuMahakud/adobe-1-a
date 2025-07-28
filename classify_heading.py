from collections import Counter

def classify_text(spans, top_n_levels=3):
    """
    Dynamically classify headings based on font size frequencies.
    Picks the top `top_n_levels` sizes as H1, H2, H3, etc.
    """
    size_counter = Counter(round(span["size"], 1) for span in spans if span.get("text", "").strip())
    most_common_sizes = [size for size, _ in size_counter.most_common()]
    heading_sizes = sorted(most_common_sizes[:top_n_levels], reverse=True)

    level_map = {size: f"H{idx+1}" for idx, size in enumerate(heading_sizes)}

    headings = []
    for span in spans:
        size = round(span.get("size", 0), 1)
        text = span.get("text", "").strip()
        page = span.get("page", 1)

        if size in level_map:
            headings.append({
                "level": level_map[size],
                "text": text,
                "page": page
            })

    return headings
