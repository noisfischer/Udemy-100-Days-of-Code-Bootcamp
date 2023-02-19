def caesar_cipher(text_input, shift_input, direction_input):
    text_input = [*text_input]
    delete_first_half = len(text_input)
    total_in_alphabet = len(alphabet)
    
    if direction_input == 'encode':
      for x in range(len(text_input)):
        
        if alphabet.count(text_input[x]) == 0:
          text_input.extend(text_input[x])
  
        else:
          index = alphabet.index(text_input[x])
          
          if (index + shift_input) < total_in_alphabet:
            text_input.extend(alphabet[index + shift_input]) 
           
          else: 
            text_input.extend(alphabet[(index + shift_input) - total_in_alphabet])
          
      for x in range(delete_first_half): 
        text_input.pop(0)
    
      text_input = ''.join(text_input)
    
      print(f"The encoded text is {text_input}")
    
  
    elif direction_input == 'decode':
      
      for x in range(len(text_input)):
  
        if alphabet.count(text_input[x]) == 0:
          text_input.extend(text_input[x])
        else:
          index = alphabet.index(text_input[x])
        
          if (index + shift_input) < total_in_alphabet:
            text_input.extend(alphabet[index - shift_input])
             
          else:
            text_input.extend(alphabet[(index - shift_input) + total_in_alphabet])
        
      for x in range(delete_first_half): 
        text_input.pop(0)
        
      text_input = ''.join(text_input)
      print(f"The decoded text is {text_input}")
  
    else:
      print("Please return 'encode' or 'decode'. Try again.")
  
  

alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']

restart = "yes"

while restart == "yes":

  direction = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n")
  text = input("Type your message:\n").lower()
  shift = int(input("Type the shift number:\n"))
  
  if shift > 26:
    shift = shift % 26
  
  
  caesar_cipher(text_input = text, shift_input = shift, direction_input = direction)

  restart = input("\nType 'yes' to go again or 'no' to end: ")

  if restart == "no":
    print("Goodbye")

