phonebook1 = {'123-45-67', '234-56-78', '345-67-89'}
print(phonebook1)
print(type(phonebook1))

phonebook1 = {'123-45-67', '234-56-78', '345-67-89'}
print(phonebook1)
set_len = len(phonebook1)
print("The length of phonebook1 is :", set_len)
print("The given phonebook1 is :", phonebook1)

a = {'124525' , '454565'}
print(a)
print(type(a))
print(len(a))
print("The llength of above is", len(a))

ages = [23, 19, 18, 21, 18, 20, 21, 23, 22, 23, 19, 20]
print("The data is the list named ages will have: ", ages)
print("The length of original list name ages is : ", len(ages))
ages_set = set(ages)
print("After converting a list into set we get :", ages_set)
print("Now the lenght of the converted list which is now set is : ", len(ages_set))
ages = list(ages_set)
print("Now converted again set into list :", ages)
print("Remember: It will rearrange the order items. ")


Phonebook1 = {'123-45-67' , '234-56-89' , '345-56-89' , '897-56-12' , '123-45-78'}
print(Phonebook1)
print('123-45-67' in Phonebook1)
print('033-45-89' in Phonebook1)
print('345-56-12' in Phonebook1)


few_of_my_students = {'Muhammad Rashid' , 'Muhammad Kashif' , 'Waqas Mansha' , 'Shahzeb Hussain',
'Owais ali' , 'Asad mansha' , 'Shshid Rasool' , 'Saqib Rasool' , 'Ali Ahmed' , 'Naeem ali' , 'Tau' ,
'Shahzeb' , 'ali ahmed' , 'arsalan' , 'samiullah' , 'Haris Khattak' , 'Muhammad ALi' , 'Rafey' ,
'Rearamg' , 'Muhammad Bassam' , 'Javed Mansoor' ,'Muhammad Rashid' , 'Muhammad Kashif' , 'Waqas Mansha' , 'Shahzeb Hussain',
'Owais ali' , 'Asad mansha' , 'Shshid Rasool' , 'Saqib Rasool' , 'Ali Ahmed' , 'Naeem ali' , 'Tau' ,
'Shahzeb' , 'ali ahmed' , 'arsalan' , 'samiullah' , 'Haris Khattak' , 'Muhammad ALi' , 'Rafey' ,
'Rearamg' , 'Muhammad Bassam' , 'Javed Mansoor' , 'Muhammad Rashid' , 'Muhammad Kashif' , 'Waqas Mansha' , 'Shahzeb Hussain',
'Owais ali' , 'Asad mansha' , 'Shshid Rasool' , 'Saqib Rasool' , 'Ali Ahmed' , 'Naeem ali' , 'Tau' ,
'Shahzeb' , 'ali ahmed' , 'arsalan' , 'samiullah' , 'Haris Khattak' , 'Muhammad ALi' , 'Rafey' ,
'Rearamg' , 'Muhammad Bassam' , 'Javed Mansoor' , 'Muhammad Rashid' , 'Muhammad Kashif' , 'Waqas Mansha' , 'Shahzeb Hussain',
'Owais ali' , 'Asad mansha' , 'Shshid Rasool' , 'Saqib Rasool' , 'Ali Ahmed' , 'Naeem ali' , 'Tau' ,
'Shahzeb' , 'ali ahmed' , 'arsalan' , 'samiullah' , 'Haris Khattak' , 'Muhammad ALi' , 'Rafey' ,
'Rearamg' , 'Muhammad Bassam' , 'Javed Mansoor' , 'Muhammad Rashid' , 'Muhammad Kashif' , 'Waqas Mansha' , 'Shahzeb Hussain',
'Owais ali' , 'Asad mansha' , 'Shshid Rasool' , 'Saqib Rasool' , 'Ali Ahmed' , 'Naeem ali' , 'Tau' ,
'Shahzeb' , 'ali ahmed' , 'arsalan' , 'samiullah' , 'Haris Khattak' , 'Muhammad ALi' , 'Rafey' ,
'Rearamg' , 'Muhammad Bassam' , 'Javed Mansoor'}

print('Here is list the list of few of my students' , few_of_my_students)
print("lets count the number of students in the set" , len(few_of_my_students))

Phonebook1 = {'123-45-67' , '234-56-78' , '345-67-89' , '123-45-67' , '345-67-89'}
Phonebook3 = {'345-67-89' , '456-78-90'}
print("Phonebook1 is :", Phonebook1)
print("Phonebook3 is :", Phonebook3)
print("Is phonebook1 is equal to ", Phonebook1 == Phonebook3)
print("Phpnebook1 is not eqaul to Phonebook3", Phonebook1 != Phonebook3)

Phonebook1 = {'123-45-67' , '234-56-78' , '345-67-89' , '123-45-67' , '345-67-89'}
anotherphonebook = {'123-45-67' , '234-56-89'}
print("Phonebook1:" , Phonebook1)
print("Anotherphonebook", anotherphonebook)
print("Comparing anotherphonebook with phonebook1 :", anotherphonebook <= Phonebook1)