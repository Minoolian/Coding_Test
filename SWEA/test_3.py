result=float('inf')

def dfs(s,end,dis,traps,re):
    global result
    
    if s in traps:
        for v,d,direction in dis[s]:
            dis[s].remove([v,d,1])
            dis[v].remove([s,d,0])
            dis[s].append([v,d,0])
            dis[v].append([s,d,1])
        
        for v,d,direction in dis[s]:
            if direction:
                if v==end:
                    result=min(result,re+d)
                    return
                dfs(v,end,dis,traps,re+d)
                
        for v,d,direction in dis[s]:
            dis[s].append([v,d,1])
            dis[v].append([s,d,0])
            dis[s].remove([v,d,0])
            dis[v].remove([s,d,1])
        
    else:
        for v,d,direction in dis[s]:
            if direction:
                if v==end:
                    result=min(result,re+d)
                    return
                dfs(v,end,dis,traps,re+d)
        

def solution(n, start, end, roads, traps):
    answer = 0
    dis=[[] for _ in range(n+1)]
    for u,v,d in roads:
        dis[u].append([v,d,1])
        dis[v].append([u,d,0])
        
    dfs(start,end,dis,traps,0)

    print(result)
    return answer
