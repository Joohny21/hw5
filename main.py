import concurrent.futures.process
from multiprocessing import cpu_count
from concurrent.futures import ProcessPoolExecutor


def find_divisors(num: int):
    divisors = []
    for i in range(1, num + 1):
        if num % i == 0:
            divisors.append(i)
    print(divisors)


def factorize(*number):
    futures = []
    print(number)
    with concurrent.futures.ProcessPoolExecutor(max_workers=cpu_count()) as executor:
        for each in number:
            futures.append(executor.submit(find_divisors, each))



if __name__ == '__main__':
    factorize(128, 255, 99999, 10651060)
