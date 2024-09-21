pyenv_data: dict = {
   "part1":[
      {
         "description":"Install a specific version of Python.",
         "command":"pyenv install <version>"
      },
      {
         "description":"Set the global Python version.",
         "command":"pyenv global <version>"
      },
      {
         "description":"Set the local Python version for the current directory.",
         "command":"pyenv local <version>"
      },
      {
         "description":"Show the current Python version being used.",
         "command":"pyenv version"
      },
      {
         "description":"List all installed Python versions.",
         "command":"pyenv versions"
      },
      {
         "description":"List all available Python versions for installation.",
         "command":"pyenv install --list"
      }
   ],
   "part2":[
      {
         "description":"Uninstall a specific Python version.",
         "command":"pyenv uninstall <version>"
      },
      {
         "description":"Rehash shims for newly installed versions.",
         "command":"pyenv rehash"
      },
      {
         "description":"Set the shell-specific Python version.",
         "command":"pyenv shell <version>"
      },
      {
         "description":"Display the path to the current Python version.",
         "command":"pyenv which <command>"
      },
      {
         "description":"Check for the current Python version set by Pyenv.",
         "command":"pyenv current"
      },
      {
         "description":"Show help for Pyenv commands.",
         "command":"pyenv help"
      }
   ]
}