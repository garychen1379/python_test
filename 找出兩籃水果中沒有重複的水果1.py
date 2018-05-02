iA = {"蘋果", "香蕉", "鳳梨", "芭樂"}
iB = {"鳳梨", "蘋果", "水梨", "蓮霧"}

u = iA.union(iB)
i = iA.intersection(iB)
ans = u - i
lst = list(ans)
lst.sort()
print(lst)
