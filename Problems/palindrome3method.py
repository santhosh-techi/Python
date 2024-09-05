def is_panlindrome(input):
    min=0
    max=len(input)-1

    #converting all the characters of the string into smaller case for the easy comparision
    input=input.lower()

    while min<max:
        if input[min]==input[max]:
            min=min+1
            max=max-1
        else:
            return False
            break
        
        return True

print(is_panlindrome('abcdcba'))