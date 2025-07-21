# ฟังก์ชันที่มีการใช้เงื่อนไขภายใน
def check_even_odd(number):
    if number % 2 == 0:
        return "เลขค่"
    else:
        return "เลขคี่"
# เรียกใช้ฟังก์ชันและแสดงผลลัพธ์
result = check_even_odd(7) # เปลี่ยนเลข 7 เป็นเลขที่ต้องการตรวจสอบ
print(result)