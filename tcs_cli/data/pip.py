pip_data: dict ={
   "part1":[
      {
         "description":"Install a package.",
         "command":"pip install <package>"
      },
      {
         "description":"Install a package from a requirements file.",
         "command":"pip install -r requirements.txt"
      },
      {
         "description":"Uninstall a package.",
         "command":"pip uninstall <package>"
      },
      {
         "description":"List installed packages.",
         "command":"pip list"
      },
      {
         "description":"Show information about a package.",
         "command":"pip show <package>"
      },
      {
         "description":"Upgrade a package to the latest version.",
         "command":"pip install --upgrade <package>"
      },
      {
         "description":"Freeze installed packages into a requirements file.",
         "command":"pip freeze > requirements.txt"
      }
   ],
   "part2":[
      {
         "description":"Search for a package in the Python Package Index (PyPI).",
         "command":"pip search <query>"
      },
      {
         "description":"Check for outdated packages.",
         "command":"pip list --outdated"
      },
      {
         "description":"Install a specific version of a package.",
         "command":"pip install <package>==<version>"
      },
      {
         "description":"Install a package directly from a Git repository.",
         "command":"pip install git+<repository-url>"
      },
      {
         "description":"Show the current version of pip.",
         "command":"pip --version"
      },
      {
         "description":"Clear the pip cache.",
         "command":"pip cache purge"
      },
      {
         "description":"Upgrade pip to the latest version.",
         "command":"pip install --upgrade pip"
      }
   ]
}