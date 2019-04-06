a=[int(input()) for _ in range(6)]
analMEGA =min(a[1],a[2],a[3],a[4],a[5])
print( 5 + a[0] // analMEGA if a[0] % analMEGA != 0 else 5 + a[0] // analMEGA -1)