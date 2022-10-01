import orjson  # https://github.com/ijl/orjson

# this demonstrates wrapping orjson json parsing library
# (wrapping required since orjson decodes to bytes)
# other json libraries can often be used directly


def loads(o, **kwargs):
    return orjson.loads(o)


def dumps(o, **kwargs):
    return orjson.dumps(o).decode("utf-8")
