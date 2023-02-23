total = 0
for m in range(1,6):
    for n in range(1,15):
        for k in range(1,99,2):
            if 10 * m + 5 * n + 0.5 * k == 100 and n+m+k==100:
                total += 1
                print('n =', n, 'k =', k, 'm =', m)
print('Общее количество натуральных решений =', total)