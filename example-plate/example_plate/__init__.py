def setup(app):
    from .extension import ExampleAdmonition
    app.add_directive("example", ExampleAdmonition)
    return {"version": "0.1", "parallel_read_safe": True}