# You are given an array strarr of strings and an integer k.
# Your task is to return the first longest string consisting of k consecutive strings taken in the array.
# Example: longest_consec(["zone", "abigail", "theta", "form", "libe", "zas", "theta", "abigail"], 2) --> "abigailtheta"
# n being the length of the string array, if n = 0 or k > n or k <= 0 return "".

def longest_consec(strarr, k):
    res = ''
    try:
        maxlen = max(*list(map(len, strarr)))
        for s in strarr:
            if len(s) == maxlen:
                for a in range(strarr.index(s), strarr.index(s) + k):
                    if a < len(strarr):
                        res += strarr[a]
                break
    except: pass
    return res


s = longest_consec(["zone", "abigail", "theta", "form", "libe", "zas", "theta", "abigail"], 2)

print(s)