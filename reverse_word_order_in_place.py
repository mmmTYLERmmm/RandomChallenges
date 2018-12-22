# give a list of words separated by spaces, return the list of words in reverse order, 
# doing so in place.  that is, no additional space is available  
# question source : https://youtu.be/aotBpjJUqJo

def reverse_order(list):
  for index in range(0,int(len(list)/2)):
      counter = len(list)-index -1
      list[index],list[counter]=list[counter],list[index]
  return list

def word_flip(list,k):
  for index in range(k,len(list)):
    if list[index] == " ":
      steps = (index-k)/2
      for counter in range(k,k+int(steps)):
        swap = (index - 1)-(counter-k)
        list[counter],list[swap]=list[swap],list[counter]
      k=index +1
      word_flip(list,k)
      break
    if index+1 == len(list) and (index-k)== 1: #edge case for end of list
      list[index],list[k]=list[k],list[index]
      break
  return list



string = ['h','i',' ','g','o','o','d',' ',' ','f','r','i','e','n','d','s']

reverse = reverse_order(string)
flipped = word_flip(reverse,0)
print(flipped)
