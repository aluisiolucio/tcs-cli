git_data: dict = {
   "part1":[
      {
         "description":"Initialize a new Git repository.",
         "command":"git init"
      },
      {
         "description":"Clone an existing repository into a new directory.",
         "command":"git clone <repository>"
      },
      {
         "description":"Stage changes to a file for the next commit.",
         "command":"git add <file>"
      },
      {
         "description":"Commit staged changes with a descriptive message.",
         "command":"git commit -m '<message>'"
      },
      {
         "description":"Show the working tree status.",
         "command":"git status"
      },
      {
         "description":"Show the commit history for the current branch.",
         "command":"git log"
      },
      {
         "description":"List all local branches in the repository.",
         "command":"git branch"
      },
      {
         "description":"Switch to a specified branch.",
         "command":"git checkout <branch>"
      },
      {
         "description":"Merge changes from the specified branch into the current branch.",
         "command":"git merge <branch>"
      },
      {
         "description":"Fetch changes from the remote repository and merge them into the current branch.",
         "command":"git pull"
      }
   ],
   "part2":[
      {
         "description":"Push local changes to the remote repository.",
         "command":"git push"
      },
      {
         "description":"Show the remote repositories associated with the local repository.",
         "command":"git remote -v"
      },
      {
         "description":"Fetch changes from the remote repository without merging.",
         "command":"git fetch"
      },
      {
         "description":"Unstage a file while retaining its changes in the working directory.",
         "command":"git reset <file>"
      },
      {
         "description":"Remove a file from the working directory and staging area.",
         "command":"git rm <file>"
      },
      {
         "description":"Save changes in a dirty working directory and revert to a clean state.",
         "command":"git stash"
      },
      {
         "description":"Reapply changes saved in a stash.",
         "command":"git stash apply"
      },
      {
         "description":"Create a tag to mark a specific point in history.",
         "command":"git tag <tag_name>"
      },
      {
         "description":"Apply the changes from a specific commit onto the current branch.",
         "command":"git cherry-pick <commit>"
      }
   ]
}
