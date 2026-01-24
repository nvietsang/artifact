import pycryptosat as cs
import argparse
import sys

# Building the clauses following [Sin05] https://www.carstensinz.de/papers/CP-2005.pdf
def upperbound(sSat,vesId,size_word,hwmax,startextra):
    sSat.add_clause([-(vesId[0]), startextra])
    for j in range (2,hwmax+1):
        sSat.add_clause([-(startextra+j-1)])
    for i in range(2,size_word):
        sSat.add_clause([-(vesId[i-1]),
                         startextra+(hwmax)*(i-1)])
        sSat.add_clause([-(startextra+(hwmax)*(i-2)),
                         startextra+(hwmax)*(i-1)])
        for j in range(2,hwmax+1):
            sSat.add_clause([-(vesId[i-1]), 
                             -(startextra+hwmax*(i-2)+j-2), 
                             startextra+(i-1)*hwmax+j-1])
            sSat.add_clause([-(startextra+hwmax*(i-2)+j-1), 
                             startextra+(i-1)*hwmax+j-1])
        sSat.add_clause([-(vesId[i-1]), 
                         -(startextra+hwmax*(i-2)+hwmax-1)])
    sSat.add_clause([-(vesId[size_word-1]), 
                     -(startextra+hwmax*(size_word-2)+hwmax-1)])
    startextra+=(size_word-1)*hwmax

if __name__ == "__main__":

    print('''
    Find the minimum number of CPA runs by SAT solver.
    Note that the indexes in tuples of solution may be different when rerun. 
    However, the number of tuples is always the same.
    ''')

    parser = argparse.ArgumentParser()
    parser.add_argument("-n",
                        dest="n",
                        help="This defines the universe [0,n-1]. In our case, n=64 by default.",
                        type=int,
                        default=64)
    parser.add_argument("--first-shift",
                        dest="s1",
                        help="The first shift index in the tuple: s1=19 for k0, s1=61 for k1.",
                        type=int,
                        required=True)    
    parser.add_argument("--second-shift",
                        dest="s2",
                        help="The second shift index in the tuple: s1=28 for k0, s1=39 for k1.",
                        type=int,
                        required=True)         
    parser.add_argument("--max",
                        dest="ub",
                        help="Upper bound for the number of tuples.",
                        type=int,
                        required=True)  
    
    config = parser.parse_args()
    n  = config.n
    s1 = config.s1
    s2 = config.s2
    ub = config.ub

    list_set=[]
    for i in range(n):
        list_set.append([i,(i+s1)%n,(i+s2)%n])
    list_set_to_have=list(range(n))

    sSat=cs.Solver()

    #Each t subset of variable should appear 
    for i in list_set_to_have: 
        clause_presence=[]
        for j in list_set:
            if i in j:
                clause_presence += [list_set.index(j)+1]
        sSat.add_clause(clause_presence)        
    upperbound(sSat,
               list(range(1,len(list_set)+1)),
               len(list_set),
               ub,
               len(list_set)+1)

    satq,solution=sSat.solve()
    print(f"Is the SAT problem solvable: {satq}")
    if(satq):
        # Verify that the tuples cover the universe
        veritab = [False] * 64
        for i in range(1,len(list_set)+1):
            if solution[i]:
                for idx in list_set[i-1]:
                    veritab[idx] = True
        assert sum(veritab) == 64

        # Print solution
        print("[Table 3.6, page 35]")
        print("The solution is:")
        for i in range(1,len(list_set)+1):
            if solution[i]:
                (i0, i1, i2) = list_set[i-1]
                print(f"({i0:2d}, {i1:2d}, {i2:2d})")
        

