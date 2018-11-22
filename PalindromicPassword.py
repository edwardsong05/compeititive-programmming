N = int(input())


def palindrome(n):
    if int(n / 100000) == n % 10:
        n %= 100000
        n -= n % 10
        if int(n/10000) == (n % 100)/10:
            n %= 10000
            n -= n % 100
            if int(n/1000) == (n % 1000)/100:
                return True
            else:
                return False
        else:
            return False
    else:
        return False


for i in range(N):
    inp = input()
    if inp == "".join(reversed(inp)):
        print(inp)
    else:
        original = int(inp)

        # check increase
        temp1 = original
        while True:
            temp1 += 1
            if palindrome(temp1):
                break
        check1 = temp1 - original

        # check decrease
        temp2 = original
        while True:
            temp2 -= 1
            if palindrome(temp2):
                break
        check2 = original - temp2

        if int(temp1 / 1000000) != 0:
            print(temp2)
        elif int(temp2 / 100000) == 0:
            print(temp1)
        elif check2 <= check1:
            print(temp2)
        else:
            print(temp1)


