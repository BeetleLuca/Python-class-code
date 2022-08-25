'''
某医院内科有a,b,c,d,e,f,g七位医生，他们在一星期内每天值一次班，根据排班要求打印出值班表。
'''
# 用列表结构列出Monday~Sunday
days=["Monday","Tuesday","Wednesday","Thursday","Friday","Saturday","Sunday"]
for a in range(7):
    for b in range(7):
        if a!=b:
            for c in range(7):
                if (c!=a) and (c!=b):
                    for d in range(7):
                        if (d!=a) and (d!=b) and (d!=c):
                            for e in range(7):
                                if (e!=a) and (e!=b) and (e!=c) and (e!=d):
                                    for f in range(7):
                                        if (f!=a) and (f!=b) and (f!=c) and (f!=d) and (f!=e):
                                            for g in range(7):
                                                if (g!=a) and (g!=b) and (g!=c) and (g!=d) and (g!=e) and (g!=f):
                                                    # 用条件表达式表示出符合要求的排班
                                                    if (a == c+1) and (d == e+2) and (b == g-3) and (f > b) and (f < c) and (f==3):(#不可以填days[f]=="Thursday")
                                                        # 打印输出每个医生的排班结果
                                                        print("a医生:",days[a],'\n')
                                                        print("b医生:",days[b],'\n')
                                                        print("c医生:",days[c],'\n')
                                                        print("d医生:",days[d],'\n')
                                                        print("e医生:",days[e],'\n')
                                                        print("f医生:",days[f],'\n')
                                                        print("g医生:",days[g],'\n')
