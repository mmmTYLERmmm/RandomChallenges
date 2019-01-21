def b10_b2(number): #base 10 to base 2
  result =""
  for index in range(7,-1,-1):
    if number / (2**index) >= 1:
      number-= 2**index
      result += "1"
    else: result += "0"
  return result

def b2_b10(number): #base2 to base10
  result = 0
  j=0
  for index in range(len(number)-1,-1,-1):
    result += (int(number[index]) * (2**j))
    j += 1
  return (number,result)

def bx_by(number,base_in,base_out,output_len):
  if base_in < 1 or base_out > 16:
    return "Error: Base_In and Base_Out must both be greater than 0 and less than 16"
  accepted_values = "0123456789ABCDEF"
  tmp_value = 0
  j=0
  result = ""
  #conver input to base10
  for index in range(len(number)-1,-1,-1):
    tmp_value += (accepted_values.index(number[index]) * (int(base_in)**j))
    j += 1
  #convert to base_out
  for index in range(output_len-1,-1,-1):
    if (tmp_value / base_out**index) >= 1:
      coef = int(tmp_value/base_out**index)
      if coef > base_out-1:
        return "Integer overflow... Please increase output length or output base."
      result += accepted_values[coef]
      tmp_value -= coef * base_out**index
    else: result += "0"
  return ("%s in base%s is = %s in base%s" % (number,base_in,result,base_out))

def main():
  for i in range (0,250):
    x = random.randint(4,16)
    print(bx_by(str(i),10,x,3))

import random
main()
