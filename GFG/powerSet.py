def gen_subset(s, curr, index, pw_set):
    
    if index == len(s):
        pw_set.append(curr)
    else:    
        gen_subset(s, curr + s[index],index + 1, pw_set)
        gen_subset(s, curr, index + 1, pw_set)


def powerSet(s):

    pw_set = list()
    gen_subset(s, "", 0, pw_set)

    return pw_set

def main():
    
    s = "abc"
    pw_set = powerSet(s)
    pw_set.sort()
    print(pw_set)

if __name__ == '__main__':
    main()
    