def calculate_bmi(weight, height):
    bmi = weight / (height ** 2)
    return bmi

# รับค่าน้ำหนัก (kg) และส่วนสูง (m)
weight = float(input("ป้อนน้ำหนักของคุณ (กิโลกรัม): "))
height = float(input("ป้อนส่วนสูงของคุณ (เมตร): "))

bmi = calculate_bmi(weight, height)
print(f"BMI ของคุณคือ: {bmi:.2f}")

# แสดงผลลัพธ์ตามเกณฑ์
if bmi < 18.5:
    print("น้ำหนักน้อยเกินไป")
elif 18.5 <= bmi < 24.9:
    print("น้ำหนักปกติ")
elif 25 <= bmi < 29.9:
    print("น้ำหนักเกิน")
else:
    print("อ้วน")
