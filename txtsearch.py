def brute_force(pat,txt):
    for pos in range(0,len(txt)):
        flag = True
        for i in range(0,len(pat)):
            if txt[pos+i] != pat[i]:
                flag = False
                break
        if flag:
            return pos
    return str(-1)

def computeLPSArray(pat, M, lps):
	len = 0 
	lps[0] 
	i = 1
	while i < M:
		if pat[i]== pat[len]:
			len += 1
			lps[i] = len
			i += 1
		else:
			if len != 0:
				len = lps[len-1]
			else:
				lps[i] = 0
				i += 1

def KMP(pat,txt):
    M = len(pat)
    N = len(txt)
    lps = [0]*M
    j = 0
    computeLPSArray(pat, M, lps)
    i = 0
    
    while i < N:
        if pat[j] == txt[i]:
            i+=1
            j+=1
        if j == M:
            return str(i-j)
        elif i<N and pat[j] != txt[i]:
            if j!= 0:
                j = lps[j-1]
            else:
                i+=1
    return str(-1)

def RKarp(pat,txt,q = 101):
    d = 256
    M = len(pat)
    N = len(txt)
    i = 0
    j = 0
    p = 0
    t = 0
    h = 1
   
    for i in range(M-1):
        h = (h * d)% q
    for i in range(M):
        p = (d * p + ord(pat[i]))% q
        t = (d * t + ord(txt[i]))% q
        
    for i in range(N-M + 1):
        if p == t:
            for j in range(M):
                if txt[i + j] != pat[j]:
                    break
            j+= 1
            if j == M:
                return str(i)
        if i < N-M:
            t = (d*(t-ord(txt[i])*h) + ord(txt[i + M]))% q
            if t < 0:
                t = t + q
    return str(-1)







                
