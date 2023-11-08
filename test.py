from sha1 import sha1
import hashlib


#Test1
message1 = "Distributed Lab"
my_impl1 = sha1(message1)
lib_impl1 = hashlib.sha1(message1.strip().encode()).hexdigest()

print("My implementation >> " + my_impl1)
print("Library implementation >> " + lib_impl1)

if my_impl1 == lib_impl1:
    print(">> Test succeed!")
else:
    print("Something wrong!")

#Test2
message2 = str([100101])
my_impl2 = sha1(message2)
lib_impl2 = hashlib.sha1(message2.strip().encode()).hexdigest()

print("My implementation >> " + my_impl2)
print("Library implementation >> " + lib_impl2)

if my_impl2 == lib_impl2:
    print(">> Test succeed!")
else:
    print("Something wrong!")

#Test3
message3 = "oirgjwerolitkngjksfngtbhikusrthilugjsndrfktgnhriduthjlesritgjnkdftgnbgthiuwsrthjlighlwjrktngsjkrthgiulertghwoiserjmnglknrtghiuejrltiohejrtftpgohkpoerjmklhndfkjgnbldfsghjnsrtfgihjn;doirftjhdlkfhg"
my_impl3 = sha1(message3)
lib_impl3 = hashlib.sha1(message3.strip().encode()).hexdigest()

print("My implementation >> " + my_impl3)
print("Library implementation >> " + lib_impl3)

if my_impl3 == lib_impl3:
    print(">> Test succeed!")
else:
    print("Something wrong!")
