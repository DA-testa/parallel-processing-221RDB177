from typing import List, Tuple

def parallel_processing(n: int, data: List[int]) -> List[Tuple[int, int]]:
    output: List[Tuple[int, int]] = []
    threads: List[int] = [0] * n

    for t in data:
        how_soon = min(threads)
        soon_thread = threads.index(how_soon)
        output.append((soon_thread, how_soon))
        threads[soon_thread] += t

    return output

def main() -> None:
    n = int(input().split()[0])
    data = list(map(int, input().split()))

    result = parallel_processing(n, data)

    for i, j in result:
        print(i, j)

if __name__ == "__main__":
    main()
