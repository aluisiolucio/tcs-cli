npm_data: dict ={
   "part1":[
      {
         "description":"Initialize a new package.json file.",
         "command":"npm init"
      },
      {
         "description":"Install a package and add it to dependencies.",
         "command":"npm install <package>"
      },
      {
         "description":"Install a package and add it to devDependencies.",
         "command":"npm install <package> --save-dev"
      },
      {
         "description":"Uninstall a package and remove it from dependencies.",
         "command":"npm uninstall <package>"
      },
      {
         "description":"List installed packages.",
         "command":"npm list"
      },
      {
         "description":"Run a script defined in package.json.",
         "command":"npm run <script>"
      },
      {
         "description":"Update a package to the latest version.",
         "command":"npm update <package>"
      },
      {
         "description":"Show information about a package.",
         "command":"npm info <package>"
      },
   ],
   "part2":[
      {
         "description":"Check for outdated packages.",
         "command":"npm outdated"
      },
      {
         "description":"Install all dependencies listed in package.json.",
         "command":"npm install"
      },
      {
         "description":"Publish a package to the npm registry.",
         "command":"npm publish"
      },
      {
         "description":"Run a command in the context of your package.",
         "command":"npm exec <command>"
      },
      {
         "description":"Create a new npm package with the default configuration.",
         "command":"npm init -y"
      },
      {
         "description":"Show global packages.",
         "command":"npm list -g --depth=0"
      },
      {
         "description":"Remove a package globally.",
         "command":"npm uninstall -g <package>"
      },
      {
         "description":"Clear the npm cache.",
         "command":"npm cache clean --force"
      }
   ]
}