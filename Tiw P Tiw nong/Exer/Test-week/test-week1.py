n = input()

# เก็บตัวอักษรที่ไม่ซ้ำ ตามลำดับ (ยกเว้น '.')
format = []
for i in n:
    if i != '.' and i not in format:
        format.append(i)

# เก็บลำดับตัวอักษรทั้งหมด (ยกเว้น '.')
old = [c for c in n if c != '.']

print(format)
print(old)

# ถ้า format == old → รูปแบบลำดับเหมือนกัน (False)
if format == old:
    print(False)
else:
    print(True)