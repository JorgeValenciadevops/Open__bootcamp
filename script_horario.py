
import time

s = time.localtime()
print('-------------------------------')
if s.tm_hour <= 6:
    h = s.tm_hour - 6
    m = s.tm_min-60
    s = s.tm_sec - 60
    print(f'Faltan {abs(h)}h {abs(m)}m {abs(s)}s')
else:
    print('Hora de ir a casa ')

print('-------------------------------')
