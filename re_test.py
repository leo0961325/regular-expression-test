import re

#第一位:
#姓名
last_name = "LNCARDHOLDER" 
first_name = 'FNIMA'

last_name_one = re.search('[^LN].+', last_name)
first_name_one = re.search('[^FN].+', first_name)
print(first_name_one,last_name_one)


#地址
address = '2570 24TH STREET ANYTOWN, CA 95818'
address_one = re.search('[^FN].+', address)
print(address_one)

#生日
birth = 'DOB 08/31/1977'
birth_one = re.search('[^DOB].+', birth)
print(birth_one)

#身高 

height = "HGT 5'-05"
height_one = re.search('[^HGT$].+', height)
print(height_one)

#第二位:
#姓名
last_name = "LN PARKER" 
first_name = 'FN TAMARRA'

last_name_one = re.search('[^LN].+', last_name)
first_name_one = re.search('[^FN].+', first_name)
print(first_name_one,last_name_one)


#地址
address = '3456 EAGLE DRIVE MARIN, CA 94956'
address_one = re.search('[^..].+', address)
print(address_one)

#生日
birth = 'DOB 05/30/1989'
birth_one = re.search('[^DOB].+', birth)
print(birth_one)

#身高 

height = "HGT 5'-08"
height_one = re.search('[^HGT$].+', height)
print(height_one)
