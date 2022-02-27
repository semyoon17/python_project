
duration = 1540

ss = duration % 60
mm = duration // 60
hh = duration // 3600
mm1 = duration//60 - hh*60
dd = duration // 86400
hh1 = duration // 3600 - dd*24

if duration < 60:
    print(duration, f'сек')
elif 60 <= duration < 3600:
    print(mm, f'мин', ss, f'сек')
elif 3600 <= duration < 86400:
    print(hh, f'ч', mm1, f'мин', ss, f'сек')
else:
    print(dd, f'дн', hh1, f'ч', mm1, f'мин', ss, f'сек')






