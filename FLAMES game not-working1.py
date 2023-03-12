# wrong logic

name1 = input("PLayer 1, enter your name : ")
name2 = input("Player 2, enter your name : ")

lis_name1 = list(name1)
lis_name2 = list(name2)

for letter in lis_name1 :
    if letter in lis_name2 :
        lis_name1.remove(letter)
        lis_name2.remove(letter)
print("Non-repeating letters of your names: ",lis_name1 + lis_name2)        
count = len(lis_name1)+len(lis_name2)

root = "FLAMES"
root_list = ['F','L','A','M','E','S']
result = { 'F':'Friend' , 'L':'Love', 'A':'Affection','M':'Marriage','E':'Enemy','S':'Sister'}
start_pos = 1
end_pos = 0
for i in range(1,6):
    end_pos = start_pos + count - 1
    while end_pos > len(root_list) :
         end_pos = end_pos - (6-start_pos+1) 
    while root_list[end_pos-1]==0:
        end_pos+=1
        if end_pos>len(root_list):
            end_pos=1
    root_list[end_pos-1]= 0
    print("Removed letters : ",root[end_pos-1],end=" ")
    
    start_pos=end_pos+1
    if start_pos > len(root_list):
        start_pos=1
    while root_list[start_pos-1]==0:
        start_pos+=1
        
for i in range(len(root_list)):
    if root_list[i]!=0 :
        print("Relation between you both : ", result[root_list[i]])    
        break