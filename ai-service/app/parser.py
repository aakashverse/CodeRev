
def chunk_file(content, max_lines=50):
    lines = content.split("\n")
    chunks = []

    for i in range(0, len(lines), max_lines):
        chunk = "\n".join(lines[i:i+max_lines])
        chunks.append(chunk)

    return chunks