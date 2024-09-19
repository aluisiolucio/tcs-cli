from typer import Argument, Context, Exit, Typer, Option
from rich.panel import Panel
from rich.console import Console

from tcs_cli.factory import Factory

console = Console()
app = Typer()

__version__ = '0.0.1.0'


def version_func(arg):
    if arg:
        console.print(
            Panel(
                f'[b]tcs-cli[/] version: [red]{__version__}[/]',
                expand=False
            )
        )
        raise Exit(code=0)


@app.callback(invoke_without_command=True)
def callcaback(
    ctx: Context,
    version: bool = Option(
        False,
        '--version', '-v',
        callback=version_func,
        is_flag=True,
        help='Show the version and exit'
    )
):

    message = """Usage: [b]tcs-cli [SUBCOMMAND] [ARGUMENTS][/]

There are 2 subcommands available for this application:

[b]docker[/]: Provides a set of commands to manage Docker containers, images, networks, and volumes
[b]git[/]: Provides a set of commands to manage Git

[b]Usage examples:[/]

tcs-cli docker --images
tcs-cli git --status

[b]For more information: [red]tcs-cli --help[/]
    """

    if ctx.invoked_subcommand:
        return
    
    console.print(
        Panel(
            message,
            expand=False
        )
    )
    
@app.command(help='Docker commands')
def docker(arg: str = Argument('all', help='Argument to execute', metavar='[all | images | containers | networks | volumes]')):
    factory = Factory()
    context = factory.create_strategy('docker')
        
    console.print(
        Panel(
            context.commands(arg),
            expand=False,
            style='green',
        )
    )


if __name__ == "__main__":
    app()
