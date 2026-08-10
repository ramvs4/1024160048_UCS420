# Q1
l="1024160048"
L=[int(i)*10 for i in l]
print(L)

L.append(30)
print(L) # we appended 30 at the end of the list
L.insert(1,90)
print(L) # we inserted 90 at the specific index of 1
# deletion
L.remove(30)
print(L)
L.pop(2)
print(L)
# sorting 
L.sort()
print(L)
L.sort(reverse=True)
print(L)
# slicing
print(L[:3])
print(L[7:])
# greater than avg
avg=sum(L)/len(L)
new_list=[i for i in L if i >avg]
print(new_list)

#Q5
my_dict={"name":"Ram Varshney","roll_no":"1024160048","branch":"CSE","age":"19","city":"Jaipur"}
my_dict["location"] = my_dict.pop("city")
print(my_dict)

my_dict["CGPA"]="10"
print(my_dict)
my_dict["age"]=int(my_dict["age"])+1
print(my_dict)
dict_1=my_dict.copy()
dict_2=my_dict.copy()
branch_1=dict_1.pop("branch")
print(branch_1)
print(dict_1)

del dict_2["branch"]
print(dict_2)

for i in my_dict:
    print(i,"->",my_dict[i])

print(my_dict.items())

for key, value in my_dict.items(): 
    print(key , "->", value)

if "email" in my_dict:
    print(my_dict["email"])
else:
    print("email not found")

friend_dict={"name":"Bhagya","roll_no":"1024160050","branch":"ECE","age":29,"location":"Delhi"}

merged={**my_dict, **friend_dict}
print(merged)

string_dict={k:v for k,v in my_dict.items() if type(v)==str}
print(string_dict)

# Q2
l="1024160048"
L=[int(i)*10 for i in l]
scores=tuple(L[:8])
print(scores)

highest=max(scores)
print(highest, scores.index(highest))

lowest=min(scores)
print(lowest, scores.count(lowest))

reversed_list=list(scores[::-1])
print(reversed_list)

x=int(input("Enter a score: "))
if x in scores:
    print(scores.index(x))
else:
    print("not present")

try:
    scores[0]=100
except TypeError as e:
    print(e)

first, second, *rest = scores
print(first, second, rest)

#Q3
import random
random.seed(1024160048)

nums=[random.randint(100,900) for i in range(100)]
print(nums)

odd=[i for i in nums if i%2!=0]
print(len(odd))

even=[i for i in nums if i%2==0]
print(len(even))

def is_prime(n):
    if n<2:
        return False
    for i in range(2,n//2+1):
        if n%i==0:
            return False
    return True

primes=[i for i in nums if is_prime(i)]
print(len(primes))
print(primes)

most_common=max(set(nums), key=nums.count)
print(most_common, nums.count(most_common))

# Q4
l="1024160048"
digits=[int(i) for i in l[:8]]

A={i*7 for i in digits}
B={i*9 for i in digits}
print(A)
print(B)

print(A.union(B))
print(A.intersection(B))
print(A.difference(B))
print(B.difference(A))
print(A.symmetric_difference(B))
print(A.issubset(B))
print(B.issuperset(A))

x=int(input("Enter a value: "))
A.discard(x)
print(A)
