def nested_sum(list1):
  for item in list1:
     if isinstance(item,list):
        for x in item:
          list2.append(x)
     else:
        list2.append(item)
 


list1=[1,2,3,[4,5,6]]
list2=[]
nested_sum(list1)

tot=0
for x in list2:
 tot= tot+ x

print(tot)


