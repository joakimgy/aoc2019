import itertools

filename = "day14input.txt"
with open(filename) as f:
    inputarray = [line.rstrip() for line in f]


def maskPlusValue(mask, val):
    bitValue = 1
    for bit in reversed(mask):
        if (bit == "1"):
            val = val | bitValue
        if (bit == "0"):
            val = val & ~bitValue
        bitValue *= 2
    return val


def task1():
    bitmask = ""
    mem = {}
    for op in inputarray:
        if "mask" in op:
            bitmask = op.split(" = ")[1]
            continue
        val = int(op.split(" = ")[1])
        memPos = op.split("[")[1].split("]")[0]
        mem[memPos] = maskPlusValue(bitmask, val)
    return sum(mem.values())


def maskPlusAddress(mask, address):
    floating = []
    bitValue = 1
    for bit in reversed(mask):
        if (bit == "X"):
            floating.append(bitValue)
            address = address & ~bitValue
        if (bit == "1"):
            address = address | bitValue
        bitValue *= 2
    return (address, floating)


def task2():
    bitmask = ""
    mem = {}
    for op in inputarray:
        if "mask" in op:
            bitmask = op.split(" = ")[1]
            continue
        val = int(op.split(" = ")[1])
        address = int(op.split("[")[1].split("]")[0])
        (memPos, floating) = maskPlusAddress(bitmask, address)
        mem[memPos] = val
        for i in range(1, len(floating)+1):
            for subList in itertools.combinations(floating, i):
                mem[memPos+sum(subList)] = val
        for pos in floating:
            mem[memPos+pos] = val
    return sum(mem.values())


print("Task 1 result: ", task1())
print("Task 2 result: ", task2())
