def split_and_join(line):
    a=line.split(" ")
    result=""
    for index in range(len(a)-1):
        result+=a[index]+"-"
    result+=a[-1]
    return result
if __name__ == '__main__':
    line = input()
    result = split_and_join(line)
    print(result)
