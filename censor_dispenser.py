# These are the emails you will be censoring. The open() function is opening the text file that the emails are contained in and the .read() method is allowing us to save their contexts to the following variables:
email_one = open("email_one.txt", "r").read()
email_two = open("email_two.txt", "r").read()
email_three = open("email_three.txt", "r").read()
email_four = open("email_four.txt", "r").read()

proprietary_terms = ["she", "personality matrix", "sense of self", "self-preservation", "learning algorithms", "herself", "her" ]
proprietary_terms_replacement = ["it", "ability", "system", "security", "systems", "itself", "it\'s"]

new_text = ''

def censor_word(word1, word2, text):
    if word1 in text:
        text = text.replace(word1, word2)
    return text

print(censor_word("learning algorithms", "discovery mechanisms", email_one))

def censor_list(lst1, lst2, text):
    new_text = ''
    uppercase_lst1 = []
    uppercase_lst2 = []

    for i in range(len(lst1)):
            uppercase_lst1.append(' '.join(w.capitalize() for w in lst1[i].split()))
            uppercase_lst2.append(' '.join(w.capitalize() for w in lst2[i].split()))  
    
    for i in range(len(lst1)):
        if lst1[i] in text:
            text = text.replace(lst1[i], lst2[i])
            if uppercase_lst1[i] in text:
                text = text.replace(uppercase_lst1[i], uppercase_lst2[i])

    new_text = text
    return new_text

test = censor_list(proprietary_terms, proprietary_terms_replacement, email_two)

print(test)
