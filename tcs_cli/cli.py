from typer import Argument, Context, Exit, Typer, Option
from rich.panel import Panel
from rich.console import Console
from rich.layout import Layout
from rich.text import Text

from tcs_cli.factory import Factory

app = Typer()
console = Console()

__version__ = '1.0.0'


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

There are the following subcommands available for this application:

[b]docker[/]: Provides a set of commands to manage Docker containers, images, networks, and volumes
[b]git[/]: Provides a set of commands to manage Git
[b]npm[/]: Provides a set of commands to manage Npm
[b]pip[/]: Provides a set of commands to manage Pip
[b]poetry[/]: Provides a set of commands to manage Poetry
[b]pyenv[/]: Provides a set of commands to manage Pyenv

[b]Usage examples:[/]

tcs-cli docker images
tcs-cli git

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


def create_layout(data, *sections, title, isExpanded=True):
    layout = Layout()
    panels = []
    
    for section in sections:
        text_title = Text(f'{title} {section.capitalize()}')
        text_title.stylize("bold")

        if isinstance(data, dict):
            content = f'\n{data[section]}'
        else:
            content = f'\n{data}'       

        panel = Panel(content, title=text_title, style='blue', expand=isExpanded)
        panels.append(panel)
    
    layout.split_column(*panels)

    return layout


@app.command(help='Docker commands')
def docker(arg: str = Argument('all', help='Argument to execute', metavar='[images | containers | networks | volumes]')):
    factory = Factory()
    context = factory.create_strategy('docker')
    
    data = context.commands(arg)

    layout = Layout()

    if arg == 'all':
        l1 = create_layout(data, 'containers', title='Docker')
        l2 = create_layout(data, 'images', 'networks', title='Docker')
        l3 = create_layout(data, 'volumes', 'logs', 'exec', title='Docker')
        l4 = create_layout(data, 'stats', 'inspect', 'prune', title='Docker')

        layout.split_row(l1, l2, l3, l4)
    else:
        l1 = create_layout(data, arg, isExpanded=False, title='Docker')
        layout.split_row(l1)

    console.print(layout)


@app.command(help='Poetry commands')
def poetry():
    factory = Factory()
    context = factory.create_strategy('poetry')
    
    data = context.commands()

    text_title = Text('Poetry commands')
    text_title.stylize("bold")

    layout = Layout()
    
    l1 = create_layout(data, 'part1', title='Poetry')
    l2 = create_layout(data, 'part2', title='Poetry')

    layout.split_row(l1, l2)

    console.print(layout)

@app.command(help='Git commands')
def git():
    factory = Factory()
    context = factory.create_strategy('git')
    
    data = context.commands()

    layout = Layout()

    l1 = create_layout(data, 'part1', title='Git')
    l2 = create_layout(data, 'part2', title='Git')

    layout.split_row(l1, l2)

    console.print(layout)


@app.command(help='Npm commands')
def npm():
    factory = Factory()
    context = factory.create_strategy('npm')
    
    data = context.commands()

    layout = Layout()

    l1 = create_layout(data, 'part1', title='Npm')
    l2 = create_layout(data, 'part2', title='Npm')

    layout.split_row(l1, l2)

    console.print(layout)


@app.command(help='Pip commands')
def pip():
    factory = Factory()
    context = factory.create_strategy('pip')
    
    data = context.commands()

    layout = Layout()

    l1 = create_layout(data, 'part1', title='Pip')
    l2 = create_layout(data, 'part2', title='Pip')

    layout.split_row(l1, l2)

    console.print(layout)


@app.command(help='Pyenv commands')
def pyenv():
    factory = Factory()
    context = factory.create_strategy('pyenv')
    
    data = context.commands()

    layout = Layout()

    l1 = create_layout(data, 'part1', title='Pyenv')
    l2 = create_layout(data, 'part2', title='Pyenv')

    layout.split_row(l1, l2)

    console.print(layout)


if __name__ == "__main__":
    app()
