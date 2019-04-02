ia,ib,ic=list(map(int, input().split()))
"""
if ia == ib:
    print(ic)
elif ia == ic:
    print(ib)
elif ic == ib:
    print(ia)
    """
print(ia*(ib==ic)+ib*(ic==ia)+ic*(ia==ib) if not (ia==ib==ic) else ia)