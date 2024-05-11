from timeit import timeit

from fibonacci import go, python


def bench_fast(num: int) -> None:
    print(f"{num} GoPy fast: {timeit(lambda: go.fast_find_fibonacci_num(num))} sec")
    print(f"{num} Python fast: {timeit(lambda: python.fast_find_fibonacci_num(num))} sec")


def bench_recursive(num: int) -> None:
    print(f"{num} GoPy recursive: {timeit(lambda: go.recursive_find_fibonacci_num(num))} sec")
    print(f"{num} Python recursive: {timeit(lambda: python.recursive_find_fibonacci_num(num))} sec")


def main() -> None:
    bench_fast(100)
    bench_fast(200)
    bench_fast(300)

    bench_recursive(10)
    bench_recursive(15)
