from os import path


def remove_comments(filepaths):
    """
    Remove comments from given files.

    Mainly intended for files with ignore directive for linting/formatting surrounding
    "{{ cookiecutter }}" expressions.
    """
    for filepath in filepaths:
        with open(filepath, "r+") as f:
            lines = f.readlines()
            # remove comments
            lines = [line for line in lines if not line.strip().startswith("#")]
            f.seek(0)
            f.write("".join(lines))
            f.truncate()


if __name__ == "__main__":
    remove_comments(
        path.join("{{ cookiecutter.python_module_name }}", "environment.yml")
    )
