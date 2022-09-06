def read_arr():
    return [int(i) for i in input().split()]

n = int(input())
seconds_in_day = 24 * 60 * 60

def to_seconds(arr):
    return (arr[0] * 60 + arr[1]) * 60 + arr[2]

class Section:
    def __init__(self, *pairs):
        self.pairs = sorted(pairs)

    def common(self, section):
        i = 0
        new_pairs = []
        for pair in section.pairs:
            while i != len(self.pairs) and pair[0] >= self.pairs[i][1]:
                i += 1
            if i == len(self.pairs):
                break
            start = max(pair[0], self.pairs[i][0])
            end = min(pair[1], self.pairs[i][1])
            new_pairs.append((start, end))
        self.pairs = new_pairs

sec = Section((0, seconds_in_day))

for i in range(n):
    arr = read_arr()
    a = to_seconds(arr[:3])
    b = to_seconds(arr[3:])
    if a == b:
        continue
    elif a < b:
        sec1 = Section((a, b))
    else:
        sec1 = Section((0, b), (a, seconds_in_day))
    sec.common(sec1)

s = 0

for pair in sec.pairs:
    s += pair[1] - pair[0]

print(s)