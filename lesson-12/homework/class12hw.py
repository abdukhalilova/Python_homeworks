import threading
from collections import Counter

# Exercise 1
def is_prime(n):
    if n < 2:
        return False
    for i in range(2, int(n ** 0.5) + 1):
        if n % i == 0:
            return False
    return True

def find_primes(start, end, primes):
    for num in range(start, end):
        if is_prime(num):
            primes.append(num)

def threaded_prime_checker(start, end, num_threads=4):
    threads = []
    primes = []
    step = (end - start) // num_threads

    for i in range(num_threads):
        t_start = start + i * step
        t_end = start + (i + 1) * step if i != num_threads - 1 else end
        thread = threading.Thread(target=find_primes, args=(t_start, t_end, primes))
        threads.append(thread)
        thread.start()

    for thread in threads:
        thread.join()

    print("Prime numbers:", sorted(primes))

threaded_prime_checker(10, 50, num_threads=4)

# Exercise 2
def count_words(lines, word_counts):
    local_count = Counter()
    for line in lines:
        local_count.update(line.strip().split())
    word_counts.append(local_count)

def threaded_word_count(filename, num_threads=4):
    with open(filename, 'r', encoding='utf-8') as file:
        lines = file.readlines()

    threads = []
    word_counts = []
    step = len(lines) // num_threads

    for i in range(num_threads):
        part = lines[i * step: (i + 1) * step] if i != num_threads - 1 else lines[i * step:]
        thread = threading.Thread(target=count_words, args=(part, word_counts))
        threads.append(thread)
        thread.start()

    for thread in threads:
        thread.join()

    total_count = Counter()
    for wc in word_counts:
        total_count.update(wc)

    print("Most common words:", total_count.most_common(10))

threaded_word_count(r"large_text_file.txt", num_threads=4)
