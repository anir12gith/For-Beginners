#issuperset

#Is set 1 larger than set 2 ? = true

set1 = {1,2,3,4,5}
set2 = {1,2,3,4}
print(set1.issuperset(set2)) 

#Is set 3 larger than set 4 ? = false
set3 = {1,2,3,4}
set4 = {1,2,3,4,5}
print(set3.issuperset(set4)) 

#=========================
print("="*50)
#========================


#issubset

#Is set 5 smaller than set 6 ? = false
set5 = {1,2,3,4}
set6 = {1,2,3}
print(set5.issubset(set6)) 

#Is set 7 smaller than set 8 ? = true
set7 = {1,2,3}
set8 = {1,2,3,4}
print(set7.issubset(set8)) 

print("="*50)

#dictionary


user = {
    "name": "anir",
    "age": 16,
    "country": "morroco",
    "lun": ["Html","CSS","JS"],
    "name": "bouzid",
    "age": 17
}

print(user)


print(user["lun"]) 


#================
print("="*50)
#================


# two - dimensional dictionary

luang = {
    "One":{
        "name":"Html",
        "prograsse":"80%"
    },
    "tow":{
        "name":"css",
        "prograsse":"90%"
    },
    "three":{
        "name":"JS",
        "prograsse":"100%"
    }
}

luang.clear() #clear all dictionary
print(luang)  #Result = {}