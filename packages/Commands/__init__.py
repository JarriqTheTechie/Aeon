import os
import shutil
import click
from inflection import camelize, pluralize


class Commands:
    def __init__(self, app=None):
        if app is not None:
            self.init_app(app)

    def init_app(self, app):
        @app.cli.command("mv-component:config")
        def create_config_command():
            from importlib import resources
            import mv_components as mv
            package_dir = resources.path(package=mv, resource="").__enter__()
            stub = str(package_dir.absolute()) + r"\stubs\mv_component.stub"
            shutil.copyfile(stub, os.getcwd() + "\\config\\mv_component.py")
            click.echo(f"Configuration file created - config\mv_component.py")

        @app.cli.command("mv-component:make")
        @click.option('--name', prompt='Component name', help='Name of component.')
        @click.option('--sidecar', prompt="Should this be placed in subdir? Yes or No",
                      help='Generate component in subdirectory structure.', type=click.BOOL)
        def create_component_command(name, sidecar):
            from mv_components import config_loader
            from inflection import camelize
            from importlib import resources
            import mv_components as mv
            package_dir = resources.path(package=mv, resource="").__enter__()

            name = name
            sidecar = sidecar

            COMPONENTS_DIR = config_loader()
            if not sidecar:
                """templates folder must be root directory of components path."""
                file_name_py = f"{camelize(name)}.py"
                file_name_html = f"{camelize(name)}.html"
                full_directory_path = os.path.join(os.getcwd() + '\\templates', COMPONENTS_DIR)

                if os.path.exists(os.path.join(full_directory_path, file_name_py)) or os.path.exists(
                        os.path.join(full_directory_path, file_name_html)):
                    click.echo(
                        f'<error>Component "{name}" Already Exists ({full_directory_path}\\{file_name_py} or {file_name_html})</error>'
                    )
                    return

                stub = str(package_dir.absolute()) + r"\stubs\component.stub"
                f = open(stub).read()
                component = f.replace("__CLASS__", camelize(name))
                f = open(os.path.join(full_directory_path, file_name_py), 'w').write(component)
                f = open(os.path.join(full_directory_path, file_name_html), 'w').write("")
                click.echo(f"Component created: {name}")
            else:
                """templates folder must be root directory of components path."""
                file_name_py = f"{camelize(name)}.py"
                file_name_html = f"{camelize(name)}.html"
                full_directory_path = os.path.join(os.getcwd() + '\\templates', COMPONENTS_DIR + f'\\{camelize(name)}')
                print(full_directory_path)
                if os.path.exists(os.path.join(full_directory_path, file_name_py)) or os.path.exists(
                        os.path.join(full_directory_path, file_name_html)):
                    click.echo(
                        f'<error>Component "{name}" Already Exists ({full_directory_path}\\{file_name_py} or {file_name_html})</error>'
                    )
                    return

                stub = str(package_dir.absolute()) + r"\stubs\component.stub"
                f = open(stub).read()
                component = f.replace("__CLASS__", camelize(name))
                # print(os.path.join(full_directory_path, file_name_py))
                os.makedirs(full_directory_path)
                f = open(os.path.join(full_directory_path, file_name_py), 'w').write(component)
                f = open(os.path.join(full_directory_path, file_name_html), 'w').write("")
                click.echo(f"Component created: {name}")

        @app.cli.command("make:action")
        @click.argument('action_name')
        @click.argument('resource')
        def make_action(action_name, resource):
            stub = os.path.join(os.getcwd(), 'stubs/action.stub')
            with open(stub, 'r') as f:
                tmpl = f.read()
                tmpl = tmpl.replace('ACTION_NAME', camelize(action_name)).replace('RESOURCES', pluralize(resource))
                print(tmpl)
            with open(f"application/actions/{camelize(action_name)}Action.py", 'w') as f:
                f.write(tmpl)
            click.echo(f"{camelize(action_name)}Action created.")

        @app.cli.command("make:service")
        @click.argument('service_name')
        def make_service(service_name):
            stub = os.path.join(os.getcwd(), 'stubs/service.stub')
            with open(stub, 'r') as f:
                tmpl = f.read()
                tmpl = tmpl.replace('Service_NAMEService', camelize(service_name)+'Service')
                print(tmpl)
            with open(f"application/services/{camelize(service_name)}Service.py", 'w') as f:
                f.write(tmpl)
            click.echo(f"{camelize(service_name)}Service created.")

        @app.cli.command("make:repository")
        @click.argument('repository_name')
        def make_repository(repository_name):
            stub = os.path.join(os.getcwd(), 'stubs/repository.stub')
            with open(stub, 'r') as f:
                tmpl = f.read()
                tmpl = tmpl.replace('Repository_NAMERepository', camelize(repository_name)+'Repository')
                print(tmpl)
            with open(f"application/repositories/{camelize(repository_name)}Repository.py", 'w') as f:
                f.write(tmpl)
            click.echo(f"{camelize(repository_name)}Repository created.")