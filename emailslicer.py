import re
regex = r'\b[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Z|a-z]{2,7}\b'
email_input = ""

def main():
    print("Welcome to the email slicer")
    print("")
    global email_input
    email_input = input("Enter your email address: ")
    return email_check(email_input)

def email_spil():
    global email_input
    (username, domain) = email_input.split("@")
    (domain, extension) = domain.split(".")


    print("Username: ", username)
    print("Domain: ", domain)
    print("Extension", extension)



def email_check(email_input):
    
    if(re.fullmatch(regex, email_input)):
        return email_spil()
    else:
        print("invalid Input. Try again")
        return main()



main()

