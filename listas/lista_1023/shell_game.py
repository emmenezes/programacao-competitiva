fi = open("input.txt", 'r')
fo = open("output.txt", 'w')

def swap(i, a, b):
    if i == a:
        return b
    if i == b:
        return a
    return i

def main():
    i = fi.readline().rstrip()

    for _ in range(3):
        a, b = fi.readline().rstrip().split()
        i = swap(i, a, b)

    fo.write(i)
    fi.close()
    fo.close()

if __name__ == "__main__":
    main()