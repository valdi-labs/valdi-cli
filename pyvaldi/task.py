from pyvaldi.utils.TaskClient import TaskClient


def list_tasks(args):
    task_client = TaskClient()
    task_client.get_tasks()


def get_task(args):
    task_client = TaskClient()
    task_client.get_task(args.task_id)


def submit_task(args):
    print(f"Submit task {args.task_definition}")


def submit_tasks(args):
    print(f"Submit tasks in list {args.task_list}")
