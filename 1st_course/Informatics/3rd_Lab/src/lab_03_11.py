from collections import Counter, namedtuple
import heapq


class Node(namedtuple("Node", ["left", "right"])):
    def walk(self, code, acc):
        self.left.walk(code, acc + "0")
        self.right.walk(code, acc + "1")


class Leaf(namedtuple("Leaf", ["char"])):
    def walk(self, code, acc):
        code[self.char] = acc or "0"


def encodeHuffman(fileIn, fileOut):
    my_input = open(fileIn, 'r')
    s = ""
    for line in my_input:
        s += line
    my_input.close()
    h = []
    for ch, freq in Counter(s).items():
        h.append((freq, len(h), Leaf(ch)))

    heapq.heapify(h)

    count = len(h)
    while len(h) > 1:
        freq1, _cpunt1, left = heapq.heappop(h)
        freq2, _cpunt1, right = heapq.heappop(h)
        heapq.heappush(h, (freq1+freq2, count, Node(left, right)))
        count += 1
    code = {}
    if h:
        [(_freq, _count, root)] = h
        root.walk(code, "")
    out = "".join(code[ch] for ch in s)
    my_output = open(fileOut, 'w')
    my_output.write(out+"\n")
    for i in code:
        my_output.write("{} {} \n".format(i, code[i]))
    my_output.close()


def decodeHuffman(fileIn, fileOut):
    my_input = open(fileIn, 'r')
    en = ""
    code = {}
    c = True
    for line in my_input:
        if c:
            en += line
            c = False
        else:
            trash = line.split(" ")
            code.update([(trash[0], trash[1])])
    en = en[:(len(en)-1)]
    my_input.close()
    pointer = 0
    encoded_str = ''
    while pointer < len(en):
        ok = False
        for ch in code.keys():
            if en.startswith(code[ch], pointer):
                encoded_str += ch
                pointer += len(code[ch])
                ok = True
        else:
            if not ok:
                return False
    my_output = open(fileOut, 'w')
    my_output.write(encoded_str)
    my_output.close()
    return True


def encodeLZ(fileIn, fileOut):
    global kLZ
    file1 = open(fileIn, 'r')
    data = file1.read().strip()
    kLZ = len(data)
    file1.close()

    file2 = open(fileOut, 'r+')
    if len(data) == 0:
        return False
    seq = ['', data[0]]
    warn = []
    file2.write('0'+ data[0])

    for i in range(1, len(data)):
        if i in warn:
            continue
        if data[i] in seq:
            cur = data[i]
            for j in range(i + 1, len(data)):
                prev = cur
                cur += data[j]
                if cur not in seq:
                    warn.append(j)
                    seq.append(cur)
                    file2.write(str(seq.index(prev)) + cur[len(cur) - 1])
                    break
                else:
                    prev = cur
                    warn.append(j)
        else:
            seq.append(data[i])

    file2.close()
    test = open(fileOut, 'r')
    kLZ = kLZ/len(test.read().strip())


def decodeLZ(fileIn, fileOut):
    file1 = open(fileIn, 'r')
    data = file1.read().strip()
    file1.close()
    file2 = open(fileOut, 'w')

    code = ['']
    numbers = ['1', '2', '3', '4', '5', '6', '7', '8', '9', '0']

    for i in range(1, len(data), 2):
        subst = code[int(data[i - 1])]
        code.append(subst + data[i])

    for i in data:
        if i in numbers:
            file2.write(code[int(i)])
        else:
            file2.write(i)
    file2.close()

    beg = open(fileOut, 'r')
    fin = open('dataLZ.txt', 'r')
    if beg.read().strip() == fin.read().strip():
        return True
    else:
        return False


def main():
    encodeHuffman(input("Path to input file: "), input("Path to output file: "))
    encodeLZ(input("Path to input file: "), input("Path to output file: "))
    # encodeHuffman("C:\Projects\Lab3\src\input_huf.txt", "C:\Projects\Lab3\src\output_huf.txt")
    # decodeHuffman("C:\Projects\Lab3\src\output_huf.txt", "C:\Projects\Lab3\src\input_huf.txt"))


main()
