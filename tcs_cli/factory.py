from tcs_cli.strategy_pattern import Strategy, Context

from tcs_cli.data.docker import docker_data
from tcs_cli.data.poetry import poetry_data
from tcs_cli.data.git import git_data
from tcs_cli.data.npm import npm_data
from tcs_cli.data.pip import pip_data
from tcs_cli.data.pyenv import pyenv_data


def build_values(data):
    values = ''
    for command in data:
        values += f'[b]{command["description"]}[/]\n\n[b][white]{command["command"]}[/][/]'

        if command != data[-1]:
            values += '\n\n\n'

    return values

class ConcreteStrategyDocker(Strategy):
    def do_commands(self, arg: str):
        if arg == 'all':
            obj = {}

            categories = ['images', 'containers', 'networks', 'volumes', 'logs', 'exec', 'stats', 'inspect', 'prune']
            for category in categories:
                obj[category] = build_values(docker_data[category])

            return obj
        
        return build_values(docker_data[arg])


class ConcreteStrategyPoetry(Strategy):
    def do_commands(self, arg: str = None):
        obj = {}

        parts = ['part1', 'part2']
        for part in parts:
            obj[part] = build_values(poetry_data[part])

        return obj


class ConcreteStrataegyGit(Strategy):
    def do_commands(self, arg: str = None):
        obj = {}

        parts = ['part1', 'part2']
        for part in parts:
            obj[part] = build_values(git_data[part])

        return obj

class ConcreteStrategyNpm(Strategy):
    def do_commands(self, arg: str = None):
        obj = {}

        parts = ['part1', 'part2']
        for part in parts:
            obj[part] = build_values(npm_data[part])

        return obj

class ConcreteStrategyPipe(Strategy):
    def do_commands(self, arg: str = None):
        obj = {}

        parts = ['part1', 'part2']
        for part in parts:
            obj[part] = build_values(pip_data[part])

        return obj

class ConcreteStrategyPyenv(Strategy):
    def do_commands(self, arg: str = None):
        obj = {}

        parts = ['part1', 'part2']
        for part in parts:
            obj[part] = build_values(pyenv_data[part])

        return obj

class Factory():
    def create_strategy(self, subcommand: str) -> Context:
        context = Context()
        
        if subcommand == 'docker':
            context.strategy = ConcreteStrategyDocker()
        elif subcommand == 'poetry':
            context.strategy = ConcreteStrategyPoetry()
        elif subcommand == 'git':
            context.strategy = ConcreteStrataegyGit()
        elif subcommand == 'npm':
            context.strategy = ConcreteStrategyNpm()
        elif subcommand == 'pip':
            context.strategy = ConcreteStrategyPipe()
        elif subcommand == 'pyenv':
            context.strategy = ConcreteStrategyPyenv()
        else:
            raise ValueError(f'Invalid subcommand: {subcommand}')

        return context
