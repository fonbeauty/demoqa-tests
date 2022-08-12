def resource(relative_path):
    import demoqa
    from pathlib import Path
    return (
        Path(demoqa.__file__)
            .parent
            .parent
            .joinpath('resources/')
            .joinpath(relative_path)
            .absolute()
            .__str__()
    )