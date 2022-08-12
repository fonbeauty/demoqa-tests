def resource(relative_path):
    import demo
    from pathlib import Path
    return (
        Path(demo.__file__)
            .parent
            .parent
            .joinpath('resources/')
            .joinpath(relative_path)
            .absolute()
            .__str__()
    )