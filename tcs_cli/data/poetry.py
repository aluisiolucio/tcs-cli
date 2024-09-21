poetry_data: dict ={
  "part1": [
    {
      "description": "Creates a new Python package.",
      "command": "poetry new <package-name>",
    },
    {
      "description": "Adds a package to your project dependencies.",
      "command": "poetry add <package-name>",
    },
    {
      "description": "Removes a package from your project dependencies.",
      "command": "poetry remove <package-name>",
    },
    {
      "description": "Installs the dependencies defined in the `pyproject.toml` file.",
      "command": "poetry install",
    },
    {
      "description": "Updates the dependencies to the latest versions according to the constraints.",
      "command": "poetry update",
    },
    {
      "description": "Locks the current dependencies and creates or updates the `poetry.lock` file.",
      "command": "poetry lock",
    },
    {
      "description": "Runs a command within the virtual environment.",
      "command": "poetry run <command>",
    },
  ],
  "part2": [
    {
      "description": "Spawns a new shell within the virtual environment.",
      "command": "poetry shell",
    },
    {
      "description": "Sets configuration options for Poetry.",
      "command": "poetry config",
    },
    {
      "description": "Publishes the package to a repository.",
      "command": "poetry publish",
    },
    {
      "description": "Builds the package into a distributable format.",
      "command": "poetry build",
    },
    {
      "description": "Searches for packages in the repository.",
      "command": "poetry search <query>",
    },
    {
      "description": "Displays the information about installed packages.",
      "command": "poetry show",
    },
    {
      "description": "Checks the `pyproject.toml` file for consistency.",
      "command": "poetry check",
    },
    {
      "description": "Updates the version of the package.",
      "command": "poetry version <new-version>",
    }
  ]
}
