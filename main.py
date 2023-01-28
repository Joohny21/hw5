# import concurrent.futures.process
from multiprocessing import cpu_count, Pool
# from concurrent.futures import ProcessPoolExecutor


# def find_divisors(num: int):
#     divisors = []
#     for i in range(1, num + 1):
#         if num % i == 0:
#             divisors.append(i)
#     return divisors
#
#
# def factorize(*number):
#     futures = []
#     with concurrent.futures.ProcessPoolExecutor(max_workers=cpu_count()) as executor:
#         for each in number:
#             futures.append(executor.submit(find_divisors, each))

def factorize(*number):
    for each in number:
        divisors = []
        for i in range(1, each + 1):
            if each % i == 0:
                divisors.append(i)
        return divisors


if __name__ == '__main__':
    with Pool(processes=cpu_count()) as pool:
        a, b, c, d = pool.map(factorize, [128, 255, 99999, 10651060])
    assert a == [1, 2, 4, 8, 16, 32, 64, 128]
    assert b == [1, 3, 5, 15, 17, 51, 85, 255]
    assert c == [1, 3, 9, 41, 123, 271, 369, 813, 2439, 11111, 33333, 99999]
    assert d == [1, 2, 4, 5, 7, 10, 14, 20, 28, 35, 70, 140, 76079, 152158, 304316, 380395, 532553, 760790, 1065106,
                 1521580, 2130212, 2662765, 5325530, 10651060]