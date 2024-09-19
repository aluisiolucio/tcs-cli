from tcs_cli.strategy_pattern import Strategy, Context

from tcs_cli.data.docker import docker_data
from tcs_cli.data.git import git_data


class ConcreteStrategyDocker(Strategy):
    def do_commands(self, arg: str):
        values = ''
        if arg == 'all':
            for key in docker_data:
                values += f'[b]{key.capitalize()}[/]\n\n'
                for command in docker_data[key]:
                    values += f'[b]{command["description"]}[/]\n\n{command["command"]}'
                    
                    if command != docker_data[key][-1]:
                        values += '\n\n\n'
                
                if key != list(docker_data.keys())[-1]:
                    values += '\n\n\n'
            
            return values
        
        for command in docker_data[arg]:
            values += f'[b]{command["description"]}[/]\n\n{command["command"]}'
            
            if command != docker_data[arg][-1]:
                values += '\n\n\n'
        
        return values


class ConcreteStrategyGit(Strategy):
    def do_commands(self, arg: str):
        return git_data[arg]


class Factory():
    def create_strategy(self, subcommand: str) -> Context:
        context = Context()
        
        if subcommand == 'docker':
            context.strategy = ConcreteStrategyDocker()
        elif subcommand == 'git':
            context.strategy = ConcreteStrategyGit()

        return context
