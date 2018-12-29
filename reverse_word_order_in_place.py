# given a list of words separated by spaces, return the list of words in reverse order, 
# doing so in place.  that is, no additional space is available  
# question source : https://youtu.be/aotBpjJUqJo

def reverse_order(list):
  #this function reverse a string the same way a mirror reverses an image
  #the right-most character will be swapped with the left-most character
  #this will carry on until we reach the middle of the string
  for index in range(0,int(len(list)/2)):
      counter = len(list)-index -1
      list[index],list[counter]=list[counter],list[index]
  return list

def word_flip(list,k):
  #"i remixed a remix. it went back to normal" - mitch hedberg
  #now we go through the reversed string and separate words by space characters.  
  # once a word isfound, we reverse the 'reversed' and we're back to normal.
  for index in range(k,len(list)): #for each character in string
    if list[index] == " ": # once space is found, start swapping characters in word
      steps = (index-k)/2
      for counter in range(k,k+int(steps)):
        swap = (index - 1)-(counter-k)
        list[counter],list[swap]=list[swap],list[counter]
      k=index +1
      word_flip(list,k)
      break
    if index+1 == len(list): #edge case for end of list
      list[index],list[k]=list[k],list[index]
      break
  return list

string = ['h','i',' ','g','o','o','d',' ',' ','f','r','i','e','n','d','s']

reverse = reverse_order(string) #reverse the string entirely
flipped = word_flip(reverse,0) #reverse each substring within, separated by spaces
print(flipped)
