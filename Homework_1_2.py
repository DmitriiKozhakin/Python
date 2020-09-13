time = int(input('Ввведите количество секунд '))
ss = time % 60
mm = (time - ss) % 60
hh = time // 3600
print('%02d:%02d:%02d' % (hh, mm, ss))
