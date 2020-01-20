# These are the emails you will be censoring. The open() function is opening the text file that the emails are contained in and the .read() method is allowing us to save their contexts to the following variables:
email_one = open("email_one.txt", "r").read()
email_two = open("email_two.txt", "r").read()
email_three = open("email_three.txt", "r").read()
email_four = open("email_four.txt", "r").read()

proprietary_terms = ["she", "personality matrix", "sense of self", "self-preservation", "learning algorithms", "her", "herself"]
proprietary_terms_replacement = ["it", "ability", "system", "security", "systems", "it\'s","itself"]

new_text = ''

def censor_list(lst1, lst2, text):
    
    for i in range(len(lst1)):
        print(i)
        if lst1[i] in text:
            new_text = text.replace(lst1[i], lst2[i])


    return new_text

test = censor_list(proprietary_terms, proprietary_terms_replacement, email_two)

print(test)
