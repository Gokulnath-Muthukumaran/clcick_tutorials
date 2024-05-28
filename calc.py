# calc.py v1

import click

@click.group()
@click.pass_context
def cli(cli_ctx):
    print(cli_ctx)
    cli_ctx.ensure_object(dict)
    print(cli_ctx)
    # pass

# @cli.group()
# @click.argument("a", type=click.FLOAT)
# @click.argument("b", type=click.FLOAT)
# @click.pass_context
# def add(a, b):
#     click.echo(a + b)

# @cli.group()
# @click.argument("a", type=click.FLOAT)
# @click.argument("b", type=click.FLOAT)
# def sub(a, b):
#     click.echo(a - b)

# @cli.group()
# @click.argument("a", type=click.FLOAT)
# @click.argument("b", type=click.FLOAT)
# def mul(a, b):
#     click.echo(a * b)

# @cli.group()
# @click.argument("a", type=click.FLOAT)
# @click.argument("b", type=click.FLOAT)
# def div(a, b):
#     click.echo(a / b)

if __name__ == "__main__":
    cli()