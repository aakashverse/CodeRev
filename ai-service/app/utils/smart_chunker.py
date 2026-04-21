from utils.ast_chunker import chunk_by_functions
from utils.line_chunker import chunk_file

def smart_chunk(file_path:str, content:str):
    ast_chunk_res = chunk_by_functions(file_path, content)

    if len(ast_chunk_res) > 0:
        return ast_chunk_res
    else:
        return chunk_file(file_path, content)