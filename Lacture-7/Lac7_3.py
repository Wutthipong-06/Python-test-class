set1 = {1,2,3}
set2 = {4,5,6}
set3 = {7,8,9}

print(set1.union(set2,set3)) #การรวมสมาชิก

print(set1.intersection(set2,set3)) #หาสมาชิกที่มีร่วมกัน

print(set1.difference(set2,set3)) #หาสมาชิกแรกที่ไม่มีในสมาชิกสอง

print(set1.symmetric_difference(set2 ,set3)) #หาสมาชิกที่อยู่ในเซตใดเซตหนึ่งเท่านั้น
