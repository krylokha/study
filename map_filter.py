def my_map(f, arr):
    for x in arr:
        yield f(x)

def my_filter(f: Callable[[Any], bool], arr: list[Any]) -> list[Any]:
    for x in arr:
        if f(x):
            yield x

for x in my_map(lambda x: x * 3, [1, 2, 3]):
    print(x)

