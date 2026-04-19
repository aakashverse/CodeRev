import {cloneRepo, scanRepo, cleanRepo } from "../services/repoService";

export async function handleGitGommand(repoUrl){
    let repoPath;

    try{
        // clone
        repoPath = await cloneRepo(repoUrl);

        //scan
        const files = await scanRepo(repoPath);

        console.log(`FOUND ${files.length} FILES`);

        // send to python AI service
        // ...

    } catch(err){
        console.error("ERROR: ", err.message);
    } finally {
        await cleanRepo(repoPath);
    }
}