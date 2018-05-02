N = eval(input())

if N <= 540000:
    J = 5
    K = N*J/100
    L = 0
    M = K - L
    print('%d'%(J),'%',' %.0f %d %d '%(K,L,M),sep='')
elif 540001 <= N <= 1210000:
    J = 12
    K = N*J/100
    L = 37800
    M = K - L
    print('%d'%(J),'%',' %.0f %d %d '%(K,L,M),sep='')
elif 1210001 <= N <= 2420000:
    J = 20
    K = N*J/100
    L = 134600
    M = K - L
    print('%d'%(J),'%',' %.0f %d %d '%(K,L,M),sep='')
elif 2420001 <= N <= 4530000:
    J = 30
    K = N*J/100
    L = 376600
    M = K - L
    print('%d'%(J),'%',' %.0f %d %d '%(K,L,M),sep='')
elif 4530001 <= N <= 10310000:
    J = 40
    K = N*J/100
    L = 829600
    M = K - L
    print('%d'%(J),'%',' %.0f %d %d '%(K,L,M),sep='')
else:
    J = 45
    K = N*J/100
    L = 1345100
    M = K - L
    print('%d'%(J),'%',' %.0f %d %d '%(K,L,M),sep='')
    
