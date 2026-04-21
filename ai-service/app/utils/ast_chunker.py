import ast
from utils.line_chunker import chunk_file

def chunk_by_functions(file_path: str, content: str):
    chunks = []

    try:
        tree = ast.parse(content)
    except:
        return chunk_file(file_path, content)  # fallback of ast not workked
    
    lines = content.split("\n")
    
    for node in ast.walk(tree):
        if isinstance(node, (ast.FunctionDef, ast.ClassDef)):
            start = node.lineno # start linee
            end = getattr(node, "end_lineno", start+ 20) # end line

            chunk = "\n".join(lines[start-1:end])
            chunks.append(
                {
                    "file":file_path,
                    "start_line":start,
                    "end_line": end,
                    "name": getattr(node).__name__,
                    "content": chunk

                }
            )
            
    return chunks


