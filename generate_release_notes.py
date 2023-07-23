from subprocess import check_output, CalledProcessError


def get_release_notes() -> str:
    """
    Fetch release notes using git commands.

    Returns:
        A string of commit messages between the latest tag and HEAD.
    """
    cmd = "git describe --tags --abbrev=0"
    try:
        latest_tag = check_output(cmd.split(), text=True).strip()
    except CalledProcessError:
        latest_tag = ""

    cmd = f"git log --oneline {latest_tag}..HEAD"
    try:
        commit_messages = check_output(cmd.split(), text=True).strip()
    except CalledProcessError:
        commit_messages = ""

    return commit_messages


if __name__ == '__main__':
    print(get_release_notes())