from pyvaldi.account import configure
from pyvaldi.repository import list_repositories
from pyvaldi.task import list_tasks, construct_task, get_task, submit_task, submit_tasks
import argparse


if __name__ == "__main__":
    parser = argparse.ArgumentParser(prog='valdi',
                                     description='A command-line interface for utilizing '
                                                 'VALDI services and managing your account.'
                                     )
    subparsers = parser.add_subparsers(dest='command')

    # Sub-parser for account credentials
    configure_parser = subparsers.add_parser('configure', help='Configure your account credentials')
    configure_parser.set_defaults(func=configure)

    # Sub-parsers for repository management
    repository_parser = subparsers.add_parser('repository', help='Manage your repositories')
    repository_subparsers = repository_parser.add_subparsers(dest='subcommand')

    # Parser for listing repositories
    repository_list_parser = repository_subparsers.add_parser('ls', help='List your repositories')
    repository_list_parser.set_defaults(func=list_repositories)

    # Sub-parsers for task management
    task_parser = subparsers.add_parser('task', help='Manage your computational tasks')
    task_subparsers = task_parser.add_subparsers(dest='subcommand')

    # Parser for listing tasks
    task_list_parser = task_subparsers.add_parser('ls', help='List your current and past tasks')
    task_list_parser.set_defaults(func=list_tasks)

    # Parser for getting a task
    task_get_parser = task_subparsers.add_parser('get', help='Get the details of a specific task')
    task_get_parser.add_argument('task_id', help='ID of task to retrieve')
    task_get_parser.set_defaults(func=get_task)

    # Parser for constructing a task definition
    task_construct_parser = task_subparsers.add_parser('create', help='Create a task definition')
    task_construct_parser.set_defaults(func=construct_task)

    # Parser for submitting a task
    task_submit_parser = task_subparsers.add_parser('submit', help='Submit a single task')
    task_submit_parser.add_argument('task_definition', help='Definition of the task to submit')
    task_submit_parser.set_defaults(func=submit_task)

    # Parser for submitting many tasks
    task_submitmany_parser = task_subparsers.add_parser('submitmany', help='Submit many tasks at once')
    task_submitmany_parser.add_argument('task_list', help='List of tasks to submit')
    task_submitmany_parser.set_defaults(func=submit_tasks)

    args = parser.parse_args()
    if hasattr(args, 'func'):
        args.func(args)
    elif hasattr(args, 'command'):
        if args.command == 'repository':
            repository_parser.print_help()
        elif args.command == 'task':
            task_parser.print_help()
        else:
            parser.print_help()
    else:
        parser.print_help()
