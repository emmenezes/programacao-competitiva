w = list(map(int, input().split()))
b1 = list(map(int, input().split()))
b2 = list(map(int, input().split()))

aw = (w[2] - w[0])*(w[3] - w[1])
# print(aw)

awb1_base = min(w[2], b1[2]) - max(w[0], b1[0])
awb1_height = min(w[3], b1[3]) - max(w[1], b1[1])
if awb1_base > 0 and awb1_height > 0:
    awb1 = awb1_base*awb1_height
else:
    awb1 = 0

awb2_base = min(w[2], b2[2]) - max(w[0], b2[0])
awb2_height = min(w[3], b2[3]) - max(w[1], b2[1])
if awb2_base > 0 and awb2_height > 0:
    awb2 = awb2_base*awb2_height
else:
    awb2 = 0

ab_base = min(w[2], b1[2], b2[2]) - max(w[0], b1[0], b2[0])
ab_height = min(w[3], b1[3], b2[3]) - max(w[1], b1[1], b2[1])
if ab_base > 0 and ab_height > 0:
    ab = ab_base*ab_height
else:
    ab = 0


aw = aw - awb1 - awb2 + ab
# print(aw, awb1, awb2, ab)
if aw > 0:
    print("YES")
else:
    print("NO")