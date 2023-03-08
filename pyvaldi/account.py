from pyvaldi.utils.AuthorizationClient import AuthorizationClient


def configure(args):
    AuthorizationClient(reconfigure=True)
