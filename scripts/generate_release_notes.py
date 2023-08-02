from subprocess import check_output, CalledProcessError, SubprocessError


def is_git_directory():
    try:
        check_output(["git", "status"])
        return True
    except SubprocessError:
        return False


def get_release_notes() -> str:
    """
    Fetch release notes using git commands.

    Returns:
        A string of commit messages between the latest tag and HEAD.
    """
    # Initialize commit messages variable
    commit_messages = ""

    # Only run commands if inside a Git repository
    if is_git_directory():
        cmd = ["git", "describe", "--tags", "--abbrev=0"]
        try:
            latest_tag = check_output(cmd, text=True).strip()
        except CalledProcessError:
            # If fails to fetch latest tag, it means there are no tags yet,
            # We can directly fetch all the logs till HEAD in this case
            latest_tag = 'HEAD'
        except OSError:
            print("The command could not be executed.")
            return commit_messages

        cmd = ["git", "log", "--oneline", f"{latest_tag}..HEAD"]
        try:
            commit_messages = check_output(cmd, text=True).strip()
        except CalledProcessError:
            commit_messages = ""
        except OSError:
            print("The command could not be executed.")

    else:
        print("This directory is not a Git repository.")

    return commit_messages


if __name__ == '__main__':
    print(get_release_notes())
