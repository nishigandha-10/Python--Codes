s="pune"
for letter in s:
    print(letter)
y=["pune",34.56,100,67,"john"]
for element in y:
    print(y)
d=[1,2,3,4,5]
for number in d:
    print(number+10)
for number in d:
    if number==3:
        break
    print(number**3)
for number in range(0,18):
    print(number)
for number in range(0,10,2):
    print(number**2)
for number in range(0,10,-1):#not work
    print(number)
for number in range(10,0,-2):
    print(number)
#for number in range (5,11,1):
 #   print(number**2)
    for number in range(5,11,-2):
        print(number**2)
c='426547'
for num in c:
    print(c)
d=("mumbai",12,45,"pune",89)
for element in d:
    print(element)
x=[1,2,3,4,5,6,7,8,9]
print(len(x))
for number in (0,len(x)):
    print(number)#0,9
#print([2]*10)
k=[2]
#print(k[2])
for num in k:
    print(k*10)
x=[1,2,3,4,5,6,7,8,9]#45
sum=0
for i in x:
    sum+=i
print(sum)
x=[10,11,12,13,14,15]
'''sum=0
for number in x:
    sum+=element
    print(sum)'''
sub=1
for number in x:
    sub=sub*number
print(sub)
#print all even no in(0,50)
for  number in range(0,51):
    if number%2==0:
     print(number)

"""for number in range(0,51):
    if number%2!=0:
        print(number)
x=("leena")
for pune in range(0,5):
 print(x)
#for loop for dictionary:
r={"x":1,"y":2,"z":3}
print(r.keys())
for key in r.keys():
 print(key)
a={"c":1,"v":2,"b":3}
print(a.values())
for values in a.values():
 print(a.vlaues())
x="sam print onlyn the words that starts with  s in this sentence."
s=x.split()
print(s)
for word in s:
    if word.startswith("s"):
        print(word)
if word in s:
    if word[0]=="s":
        print(word)
r="print every word in this sentence that has an even number of letters"
a=r.spilt()
print(a)
for i in a:
    if len(i)%2==0:
      print(i)
s=r.split()
list=[]
for word in s:
    if len(word)%2==0:
     list.append(word)
print(list)"""

for number in range(0,101):
   if number%3==0 and number%2==0:
       print("FIZZBUZZ")
   elif number%3==0:
           print("FIZZ")
   elif number%5==0:
               print("BUZZ")
   else:
       print("number")

x=[12,45,1,23,89,0,575,78,3,200]
max_num=x[0]
for number in x:
    if number>max_num:
        max_num=number
print(max_num)
z="pune is well known for historical resion"
d={ }
for letter in z:
    if letter not in d.keys():
        d[letter]=1
    else:
        d[letter]=d[letter]+1
print(d)
p="nishigandha"
d={ }
for letter in p:
    if letter not in d.keys():
         d[letter]=1
    else:
        d[letter]=d[letter]+1
print(d)

















































































































