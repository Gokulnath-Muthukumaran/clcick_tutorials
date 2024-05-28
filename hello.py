# hello.py

import click

@click.command("Hello")
@click.version_option("0.1.0", prog_name="Hello")
def hello():
    click.echo("Hello, World!")

if __name__ == "__main__":
    hello()