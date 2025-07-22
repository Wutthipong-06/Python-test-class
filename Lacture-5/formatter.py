def format_string(text, format_type="upper"):  # สร้างฟังก์ชันชื่อ format_string รับพารามิเตอร์ text และ format_type (ค่าเริ่มต้น "upper")
    
    if format_type == "upper":  # ตรวจสอบถ้า format_type เท่ากับ "upper"
        return text.upper()  # คืนค่าข้อความที่แปลงเป็นตัวพิมพ์ใหญ่แล้ว
    elif format_type == "lower":  # ตรวจสอบถ้า format_type เท่ากับ "lower"
        return text.lower()  # คืนค่าข้อความที่แปลงเป็นตัวพิมพ์เล็กแล้ว
    elif format_type == "remove_spaces":  # ตรวจสอบถ้า format_type เท่ากับ "remove_spaces"
        return text.replace(" ", "").upper()  # ลบช่องว่างทั้งหมด (แทนที่ " " ด้วย "") แล้วแปลงเป็นตัวพิมพ์ใหญ่
    elif format_type == "hyphenate":  # ตรวจสอบถ้า format_type เท่ากับ "hyphenate"
        return text.upper().replace(" ", "-")  # แปลงเป็นตัวพิมพ์ใหญ่ก่อน แล้วแทนที่ช่องว่างด้วยขีดกลาง (-)
    else:  # ถ้าไม่ตรงกับเงื่อนไขใดข้างต้น (กรณี format_type ไม่รู้จัก)
        return text  # คืนค่าข้อความต้นฉบับโดยไม่เปลี่ยนแปลง

def main():  # สร้างฟังก์ชันหลักชื่อ main   
    # ทดสอบการจัดรูปแบบต่างๆ
    test_strings = [  # สร้างลิสต์ของ tuples ที่มีข้อความทดสอบและประเภทการจัดรูปแบบ
        ("hello world this is a test", "remove_spaces"),  # tuple แรก: ข้อความ "hello world this is a test" กับ format "remove_spaces"
        ("python is fun", "remove_spaces"),  # tuple ที่สอง: ข้อความ "python is fun" กับ format "remove_spaces"
        ("hello world", "hyphenate")  # tuple ที่สาม: ข้อความ "hello world" กับ format "hyphenate"
    ]
    
    for text, fmt_type in test_strings:  # วนลูปผ่านแต่ละ tuple ในลิสต์ โดย text และ fmt_type จะเก็บค่าจาก tuple
        result = format_string(text, fmt_type)  # เรียกใช้ฟังก์ชัน format_string กับข้อความและประเภทการจัดรูปแบบ แล้วเก็บผลลัพธ์
        print(f"Input: '{text}' | Format: {fmt_type} | Output: {result}")  # แสดงผลลัพธ์ในรูปแบบ f-string

if __name__ == "__main__":  # ตรวจสอบว่าไฟล์นี้ถูกรันโดยตรง (ไม่ใช่ถูก import)
    main()  # เรียกใช้ฟังก์ชัน main()