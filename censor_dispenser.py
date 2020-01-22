# These are the emails you will be censoring. The open() function is opening the text file that the emails are contained in and the .read() method is allowing us to save their contexts to the following variables:
email_one = open("email_one.txt", "r").read()
email_two = open("email_two.txt", "r").read()
email_three = open("email_three.txt", "r").read()
email_four = open("email_four.txt", "r").read()

proprietary_terms = ["she", "personality matrix", "sense of self", "self-preservation", "learning algorithms", "herself", "her" ]
proprietary_terms_replacement = ["it", "ability", "system", "security", "systems", "itself", "it\'s"]
negative_words = ["concerned", "behind", "danger", "dangerous", "alarming", "alarmed", "out of control", "help", "unhappy", "bad", "upset", "awful", "broken", "damage", "damaging", "dismal", "distressed", "distressed", "concerning", "horrible", "horribly", "questionable"]
less_negative_words = ["", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", ""]


def clean_text(text):
    new_text_list = []
    new_text = ''
    new_text_list = text.split(' ')
    new_text_list_cleaned = []

    for i in new_text_list: 
        i = i.strip()
        if i == '':
            continue
        elif '\n\n\n\n\n' in i:
            new_text_list_cleaned.append(i.replace('\n\n\n\n\n', '\n\n'))
            new_text = ' '.join(new_text_list_cleaned)
        else:
            new_text_list_cleaned.append(i)
            new_text = ' '.join(new_text_list_cleaned)
            
    return new_text


def censor_word(word1, word2, text):
    new_text = ''
    if word1 in text:
        text = text.replace(word1, word2)
    new_text = clean_text(text)
    return new_text

#print(censor_word("learning algorithms", "discovery mechanisms", email_one))

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
    new_text = clean_text(new_text)
    return new_text

censored_data_from_censor_list = censor_list(proprietary_terms, proprietary_terms_replacement, email_three)

def censor_if_word_occured_twice(lst1, lst2, text):
    #new_text = ''
    w_count = []
    for i in range(len(lst1)):
        if lst1[i] in text:
            w_count = text.count(lst1[i])
            if w_count > 2:
                text = text.replace(lst1[i], lst2[i])
    
    new_text = censor_list(proprietary_terms, proprietary_terms_replacement, text)

    new_text = clean_text(new_text)
    return new_text

  
test_3 = censor_if_word_occured_twice(negative_words, less_negative_words, email_three)

print(test_3)