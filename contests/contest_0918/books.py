from typing import ChainMap


def readable(n, book):
    read = [0 for _ in range(n+1)]
    read[0] = 1
    reads = loop = 0
    last_reads = 0
    while reads != n:
        last_reads = reads
        for index, chapter in enumerate(book):
            if not read[index]:
                can_read = True
                for pr in chapter:
                    if read[pr] != 1:
                        can_read = False
                        break
                if can_read:
                    read[index] = 1  
                    reads += 1
        loop += 1
        if last_reads == reads:
            break
    
    if reads != n:  return(-1)
    else:           return(loop)


    

t = int(input())

for _ in range(t):
    n = int(input())
    book = [[]]
    for _ in range(n): 
        chapter = list(map(int, input().split()))
        if len(chapter) != 1:   chapter = chapter[1:]
        book.append(chapter)

    #print(book)
    print(readable(n, book))


