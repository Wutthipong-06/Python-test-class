import unittest  # นำเข้า module unittest สำหรับการทดสอบ
from formatter import format_string  # นำเข้าฟังก์ชัน format_string จากไฟล์ formatter.py

class TestStringFormatter(unittest.TestCase):  # สร้างคลาสทดสอบที่สืบทอดจาก unittest.TestCase
    """Unit tests สำหรับทดสอบการทำงานของ Dynamic String Formatter"""
    
    def test_upper_case_formatting(self):  # เมธอดทดสอบการแปลงตัวพิมพ์ใหญ่
        """ทดสอบการแปลงเป็นตัวพิมพ์ใหญ่"""
        result = format_string("hello world", "upper")  # เรียกใช้ฟังก์ชัน format_string กับ "hello world" และ "upper"
        self.assertEqual(result, "HELLO WORLD")  # ตรวจสอบว่าผลลัพธ์เท่ากับ "HELLO WORLD" หรือไม่
    
    def test_lower_case_formatting(self):  # เมธอดทดสอบการแปลงตัวพิมพ์เล็ก
        """ทดสอบการแปลงเป็นตัวพิมพ์เล็ก"""
        result = format_string("HELLO WORLD", "lower")  # เรียกใช้ฟังก์ชัน format_string กับ "HELLO WORLD" และ "lower"
        self.assertEqual(result, "hello world")  # ตรวจสอบว่าผลลัพธ์เท่ากับ "hello world" หรือไม่
    
    def test_remove_spaces_formatting(self):  # เมธอดทดสอบการลบช่องว่าง
        """ทดสอบการลบช่องว่างและแปลงเป็นตัวพิมพ์ใหญ่"""
        result = format_string("hello world this is a test", "remove_spaces")  # ทดสอบกับข้อความยาว
        self.assertEqual(result, "HELLOWORLDTHISISATEST")  # ตรวจสอบว่าผลลัพธ์ถูกต้อง (ไม่มีช่องว่างและเป็นตัวใหญ่)
        
        result2 = format_string("python is fun", "remove_spaces")  # ทดสอบกับข้อความที่สอง
        self.assertEqual(result2, "PYTHONISFUN")  # ตรวจสอบว่าผลลัพธ์ถูกต้อง
    
    def test_hyphenate_formatting(self):  # เมธอดทดสอบการใส่ขีดกลาง
        """ทดสอบการแทนที่ช่องว่างด้วยขีดกลาง"""
        result = format_string("hello world", "hyphenate")  # เรียกใช้ฟังก์ชันกับ "hyphenate"
        self.assertEqual(result, "HELLO-WORLD")  # ตรวจสอบว่าได้ "HELLO-WORLD" (ตัวใหญ่และมีขีดกลาง)
    
    def test_default_formatting(self):  # เมธอดทดสอบกรณี format_type ไม่รู้จัก
        """ทดสอบการจัดรูปแบบแบบ default (ไม่เปลี่ยนแปลง)"""
        result = format_string("Hello World", "unknown")  # ส่ง format_type ที่ไม่มีในฟังก์ชัน
        self.assertEqual(result, "Hello World")  # ตรวจสอบว่าข้อความไม่เปลี่ยนแปลง
    
    def test_empty_string(self):  # เมธอดทดสอบกับข้อความว่าง
        """ทดสอบกับข้อความว่าง"""
        result = format_string("", "upper")  # ส่งข้อความว่างเข้าไป
        self.assertEqual(result, "")  # ตรวจสอบว่าผลลัพธ์ยังคงเป็นข้อความว่าง

if __name__ == "__main__":  # ตรวจสอบว่าไฟล์นี้ถูกรันโดยตรง (ไม่ใช่ถูก import)
    # รัน unit tests
    unittest.main()  # เรียกใช้ unittest.main() เพื่อรันการทดสอบทั้งหมดในคลาส