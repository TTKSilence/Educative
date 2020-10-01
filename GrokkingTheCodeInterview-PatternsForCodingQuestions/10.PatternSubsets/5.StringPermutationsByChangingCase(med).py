#Given a string, find all of its permutations preserving the character sequence but changing case.
def StringPermutation(str):
    length=len(str)
    perm=[str]
    for i in range(length):
        '''Solution1
        if 64<ord(str[i])<91:
            temp=chr(ord(str[i])+32)
        elif 96<ord(str[i])<123:
            temp=chr(ord(str[i])-32)
        else:
            continue
        count=len(perm)
        for j in range(count):
            old=perm[j]
            perm.append(old[0:i]+temp+old[i+1:])
        '''
        #Solution2-Educative
        if str[i].isalpha():
            count=len(perm)
            for j in range(count):
                temp=list(perm[j])
                temp[i]=temp[i].swapcase()
                perm.append(''.join(temp))
    return perm

def main():
    print(StringPermutation('gtR-123'))
    print(StringPermutation('c63s'))
    print(StringPermutation('AMG63'))
    print(StringPermutation(''))

main()
