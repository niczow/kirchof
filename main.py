v1 = 24
r = []
for i in range(5):
    x = int(input(f'Podaj R{i+1}: '))
    r.append(x)

r.append(500)
z = [
    [r[1]+r[4]+r[5], r[4] + r[5], r[5]],
    [r[5], r[0]+r[5], r[0]+r[3]+r[5]],
    [-1*r[1], r[0]+r[2], r[0]]
]

wg = z[0][0] * z[1][1] * z[2][2] + z[0][1] * z[1][2] * z[2][0] + z[0][2] * z[1][0] * z[2][1] - z[0][2] * z[1][1] * z[2][0] - z[0][1] * z[1][0] * z[2][2] - z[0][0] * z[1][2] * z[2][1]
w2 = v1 * z[1][1] * z[2][2] + z[0][1] * z[1][2] * 0 + z[0][2] * v1 * z[2][1] - z[0][2] * z[1][1] * 0 - z[0][1] * v1 * z[2][2] - v1 * z[1][2] * z[2][1]
w3 = z[0][0] * v1 * z[2][2] + v1 * z[1][2] * z[2][0] + z[0][2] * z[1][0] * 0 - z[0][2] * v1 * z[2][0] - v1 * z[1][0] * z[2][2] - z[0][0] * z[1][2] * 0
w4 = z[0][0] * z[1][1] * 0 + z[0][1] * v1 * z[2][0] + v1 * z[1][0] * z[2][1] - v1 * z[1][1] * z[2][0] - z[0][1] * z[1][0] * 0 - z[0][0] * v1 * z[2][1]

i2 = round(w2*1000/wg, 1)
i3 = round(w3*1000/wg, 1)
i4 = round(w4*1000/wg, 1)
i1 = i3 + i4
i5 = i2 + i3
i6 = i4 + i5

print(f"""
I1 = {round(i1, 1)} mA
I2 = {i2} mA
I3 = {i3} mA
I4 = {i4} mA
I5 = {round(i5, 1)} mA
I6 = {round(i6, 1)} mA
""")