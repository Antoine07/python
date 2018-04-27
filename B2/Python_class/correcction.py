

def multiply(*m):
    m1, m2 = m 

    # lancer une exception arrête les programme
    if len(m1) != len(m2):
        raise "Attention les listes ne sont pas égales"
    
    return sum( m1[i]*m2[i] for i in range(len(m1)) )

print(multiply([1,2,3], [2,3,4]))

