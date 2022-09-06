from string import ascii_lowercase

def get_distance(ch1, ch2):
    if ch1 > ch2:
        ch1, ch2 = ch2, ch1
    idx1 = ascii_lowercase.index(ch1)
    idx2 = ascii_lowercase.index(ch2)
    return min(
        idx2 - idx1,
        len(ascii_lowercase) - idx2 + idx1)

def prepare(chars):
    distances = [
        get_distance(chars[i], chars[i - 1])
        for i in range(len(chars))]
    return distances

def z_function(s):
    z = [0] * len(s)
    l = r = 0
    n = len(s)
    for i in range(1, n):
        if i <= r:
            z[i] = min(z[i - l], r - i + 1)
        while i + z[i] < n and s[i + z[i]] == s[z[i]]:
            z[i] += 1
        if r < i + z[i] - 1:
            r = i + z[i] - 1
            l = i
    return z

def search_kmp(pattern, text, marker='%'):
    zf = z_function(pattern + marker + text)
    ps = len(pattern)
    ts = len(text)
    for i in range(ts - ps + 1):
        if zf[i + ps + 1] == ps:
            return i
    return -1

n = int(input())
t = input()
s = input()

t_a = prepare(t)
s_a = prepare(s)

idx = search_kmp(s_a, t_a * 2, marker=[-1])

if idx == -1:
    print('Impossible')
else:
    print('Success')
    k = 0 if idx == 0 else n - idx
    print(k, ord(s[0]) - ord(t[idx]))