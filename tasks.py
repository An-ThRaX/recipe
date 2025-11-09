from invoke import task


@task
def run(c):
    """
    Run the app in web mode - hot reload enabled
    """
    c.run("flet run recipe_app/main.py -w -r", pty=True)


@task
def build(c):
    """
    Build Windows executable.
    """
    c.run("pyinstaller recipe_app.spec", pty=True)


@task
def lint(c):
    c.run("isort .", pty=True)
    c.run("flake8 .", pty=True)
    c.run("mypy .", pty=True)
