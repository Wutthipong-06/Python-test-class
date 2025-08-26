def main():
    outfile = open('philosopher.txt', 'w') # เปิดไฟล์ในโหมดเขียน

    outfile.write('John Lacke\n')
    outfile.write('David Hume\n')
    outfile.write('Edmund Burke\n')

    outfile.close() # ปิดไฟล์เมื่อเลิกใช้งาน และส่งคืนให้ระบบ

    main()

    # \n เป็นการขึ้นบรรทัดใหม่