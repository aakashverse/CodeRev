import simpleGit from "simple-git";
import fs from "fs-extra";
import path from "path";
import os from "os";

const git = simpleGit();

// clone repo into temp dir
export async function cloneRepo(repoUrl){
    try{
        const tempDir = path.join(os.tempdir(), `codereview-${Date.now()}`);
        console.log(`cloning repo into: ${tempDir}`);

        await git.clone(repoUrl, tempDir);  // actual cloninog
        return tempDir;
    } catch(err){
        console.error("error in cloning :( ", err.message);
        throw err;
    }
}

// scan repo & return code files
export async function scanRepo(repoPath){
    const allFiles = []; 

    async function traverse(dir){
        const files = await fs.readdir(dir);

        for(const file of files){
            const fullPath = path.join(dir, file);
            const stat = fs.stat(fullPath);

            if((await stat).isDirectory()){
                if(!IgnoreDir(file)){
                    await traverse(fullPath);
                }
            }
            else{
                if(filterFiles(fullPath)){
                    const content = await fs.read(fullPath, "utf-8");  // read with utf-8 encoding

                    allFiles.push({
                        path: fullPath,
                        content,
                    })
                }
            }

        }
    }

    await traverse(repoPath);
    return allFiles;
}

// cleanup temp repo
export async function cleanRepo(repoPath){
    try{
        await fs.remove(repoPath);
        console.log("temp repo cleaned up..")
    } catch(err){
        console.error("cleanup failed: ", err.message);
    }
}

// skip unnecessary dirs
function IgnoreDir(dir){
    const dirsIgnored = ["node_modules", ".git", "dist", "build", "__pycache__", ".next"];
    return dirsIgnored.includes(dir);
}