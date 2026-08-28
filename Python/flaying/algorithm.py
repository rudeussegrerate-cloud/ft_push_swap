
def is_path(path: dict) -> tuple[bool, list[str]]:
    left = []
    for key in path:
        try:
            path[key]
        except KeyError:
            if (key == 'goal'):
                return(False, left)
        else:
            left.append(path[key])
            if (path[key] == 'goal'):
                break
    return (True, left)