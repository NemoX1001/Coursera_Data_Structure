# python3
import random

def read_input():
    return (input().rstrip(), input().rstrip())

def print_occurrences(output):
    print(' '.join(map(str, output)))

def hash_func(s, p, x):
    ans = 0
    for c in reversed(s):
        ans = ((ans * x + ord(c)) % p + p) % p
    return ans

def precompute_hashes(pattern, text, p, x):
    result = [None] * (len(text) - len(pattern) + 1)
    S = text[(len(text)-len(pattern)):len(text)]
    result[len(text)-len(pattern)] = hash_func(S, p, x)

    y = 1
    for i in range(1, len(pattern) + 1):
        y = (y * x) % p
    for i in range(len(text) - len(pattern) - 1, -1, -1):
        result[i] = (x * result[i+1] + ord(text[i]) - y * ord(text[i + len(pattern)])) % p

    return result

def get_occurrences(pattern, text):
    _prime = 1000000007
    x = random.randint(0, _prime)
    hashes = precompute_hashes(pattern, text, _prime, x)
    result = []
    pHash = hash_func(pattern, _prime, x)
    for i in range(0, len(text) - len(pattern) + 1):
        if pHash != hashes[i]:
            continue
        if text[i:i+ len(pattern)] == pattern:
            result.append(i)
    return result

if __name__ == '__main__':
    print_occurrences(get_occurrences(*read_input()))