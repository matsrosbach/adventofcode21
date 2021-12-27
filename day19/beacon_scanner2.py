
### Output from part 1. Took too long to run it again ;)

scanners = []
scanners.append([0, 0, 0])
scanners.append([-54, -1205, 34])
scanners.append([-1129, -1313, 51])
scanners.append([81, -2471, 53 ])
scanners.append([64, -3691, 46 ])
scanners.append([1089, -3554, -18 ])
scanners.append([-79, -3580, 1213 ])
scanners.append([-1208, -3707, 1217 ])
scanners.append([1162, -3686, 1163 ])
scanners.append([-1183, -4812, 1209 ])
scanners.append([1156, -4793, 50 ])
scanners.append([13, -4801, 1255 ])
scanners.append([-1316, -6106, 1274 ])
scanners.append([-96, -4931, -63 ])
scanners.append([82, -6059, 1187 ])
scanners.append([1229, -4908, 1131 ])
scanners.append([-1202, -5975, 36 ])
scanners.append([77, -7326, 1202 ])
scanners.append([-1267, -4757, 2436 ])
scanners.append([1242, -3739, 2459 ])
scanners.append([-100, -4762, -1171 ])
scanners.append([1089, -4924, 2450 ])
scanners.append([-106, -6008, 2451 ])
scanners.append([18, -6093, 99 ])
scanners.append([24, -7241, 2345 ])
scanners.append([-2431, -6016, 115 ])
scanners.append([-40, -5990, -1167 ])
scanners.append([-76, -7198, 3536 ])
scanners.append([-3677, -6107, 47 ])
scanners.append([-49, -8511, 2335 ])


largest = 0
for i in scanners:
    for j in scanners:
        if abs(i[0] - j[0]) + abs(i[1] - j[1]) + abs(i[2] - j[2]) > largest:
            largest = abs(i[0] - j[0]) + abs(i[1] - j[1]) + abs(i[2] - j[2])

print("The answer is: ", largest)
