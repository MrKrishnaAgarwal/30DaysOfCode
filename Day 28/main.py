import random
num_list= [1,2,3,4,5,6,7,8,9,10]
print("List before using shuffle:",num_list)
random.shuffle(num_list)
print("List after using shuffle method:",num_list)
num_list.reverse()
print("List after using reverse method on shuffled list:",num_list)
