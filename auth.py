import os


def get_auth():
    """
    Gets basic authorization credentials.
    :return: Tuple consisting of a username and password. Example: ('me@example.com', 'pas5w0rd')
    """
    with open(os.path.join('basic_auth', 'credentials.txt'), mode='r') as f:
        credentials = f.readline().split(':')
    return credentials[0], credentials[1]
