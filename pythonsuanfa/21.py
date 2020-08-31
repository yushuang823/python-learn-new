"""
两个乒乓球队进行比赛，各出三人。甲队为a,b,c三人，乙队为x,y,z三人。已抽签决定比赛名单。有人向队员打听比赛的名单。
a说他不和x比，c说他不和x,z比，请编程序找出三队赛手的名单。
> 先进行排列组合，再挑选符合要求的组合。
"""
m = ('a', 'b', 'c')
n = ('x', 'y', 'z')
res = []
for i in m:
    for j in n:
        if (i == m[0] and j == n[0]) or (i == m[2] and j == n[0]) or (i == m[2] and j == n[2]):
            continue
        res.append((i, j))
print(res)

