from pyvaldi.utils.RepositoryClient import RepositoryClient


def list_repositories(args):
    repo_client = RepositoryClient()
    repo_client.get_repositories()
