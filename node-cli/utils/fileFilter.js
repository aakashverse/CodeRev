import path from "path";

// filter relevant files
export function filterFiles(filePath){
    const allowedExtensions = [
        ".js", ".ts", ".html", ".css", ".php", ".jsx",
        ".c", ".cpp", ".rs", ".go", ".asm",
        ".swift", ".kt", ".java", ".dart", ".m",
        ".py", ".r", ".jl", ".ipynb", ".scala",
        ".sh", ".ps1", ".rb", ".pl", ".lua"
    ];
    
    const ext = path.extname(filePath);
    return allowedExtensions.includes(ext);
}