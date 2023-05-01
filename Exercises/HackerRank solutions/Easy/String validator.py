if __name__ == '__main__':
    s = input()
    
    has_alphanumeric = any(ch.isalnum() for ch in s)
    has_alphabetical = any(ch.isalpha() for ch in s)
    has_digits = any(ch.isdigit() for ch in s)
    has_lowercase = any(ch.islower() for ch in s)
    has_uppercase = any(ch.isupper() for ch in s)
    
    # print statements
    print(has_alphanumeric)
    print(has_alphabetical)
    print(has_digits)
    print(has_lowercase)
    print(has_uppercase)
