import click

# Define the group and indicate that we're going to be using context
@click.group()
@click.pass_context
def hello(cli_ctx):
    # `ctx.obj` is a special object that's used for sharing data between commands
    # You can store whatever you like in here
    cli_ctx.ensure_object(dict)
    cli_ctx.obj['abc'] = 'Hello World!'
    click.echo(cli_ctx.obj)

# Define a command that belongs to the group, and indicate that it accepts context
@hello.group()
# @click.argument("ct", type=click.INT)
@click.pass_context
def greet(a):
    # When this command gets called, print the data stored in context
    click.echo(a.obj)
    pass

@greet.command("list")
@click.pass_context
def _list_jobs(cli_ctx):
    click.echo(cli_ctx.obj)

@greet.command("list1")
@click.pass_context
def _list_jobs1(cli_ctx):
    click.echo('a')\
    
def main():
    # load the processing jobs defined in the current folder
    # load_job_processors(op.dirname(op.abspath(__file__)))
    print('ggege')
    hello()

if __name__ == '__main__':
    main()