import random
import string
import datetime


#letters according to number + digits according to number [e.g. L-3 D-5 = GKU51230]
def random_alpha_numeric_id(letters_count, digits_count):
    sample_str = ''.join((random.choice(string.ascii_uppercase) for i in range(letters_count)))
    sample_str += ''.join((random.choice(string.digits) for i in range(digits_count)))
    sample_list = list(sample_str)
    final_string = ''.join(sample_list)
    return final_string

#passed fixed letter + digits according to passed number [e.g. Fixed_L-JSS, D-4 = JSS5032 ]
def fixed_alpha_random_number_id(letters, digits_count):
    sample_str = letters
    sample_str += ''.join((random.choice(string.digits) for i in range(digits_count)))
    sample_list = list(sample_str)
    final_string = ''.join(sample_list)
    return final_string


#Fixed letters JSS  + last 2 digit of current year + random sigle letter + digits according to passed number [e.g. Fixed_L-JSS, D-4 = JSS5032 ]


def random_alpha_numeric_id_with_currentYear(letters_count, digits_count):
    brand_name = 'JSS'
    cy = datetime.datetime.today()
    current_year = cy.strftime("%y")
    rndm_letter = ''.join(random.choice(string.ascii_uppercase) for i in range(letters_count))
    rndm_number = ''.join(random.choice(string.digits) for i in range(digits_count))
    rndm_alph_num = str(rndm_letter) + str(rndm_number)  
    rndm_id_tupple = (brand_name, current_year, rndm_alph_num)
    random_id_str = "-".join(rndm_id_tupple)
    return random_id_str