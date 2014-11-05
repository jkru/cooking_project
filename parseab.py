import BeautifulSoup
from nltk import FreqDist
import string

#############################################################
# =>look at using the last word of a multi-word expression  #
# as the word that carries the most information             #
# maybe use the other words to subclass??                   #
#############################################################


def reverse_ing(ing_string):
    list_ing = ing_string.split()
    first_ing = list_ing.pop(0)
    list_ing.append(first_ing)
    rev_string = ""
    for item in list_ing:
        rev_string = rev_string+" "+item

    if list_ing[-1][-1] == ",":
        rev_string = rev_string[:-1]
        return rev_string
    else:
        return reverse_ing(rev_string)


list_files = open("ab/recipes.txt", 'r')
allthethings = {}
allwords = []

for afile in list_files:
    soup_file = "ab/"+afile
    soup_file = soup_file.strip()
    soup = open(soup_file, "r")
    soup = BeautifulSoup.BeautifulSoup(soup)
    ingr = soup.findAll("li",{"itemprop":"ingredients"})
    
    bag_of_words = []
    for item in ingr:
        single_ingr = item.getText()
        single_ingr = single_ingr.encode("ascii")
        ingr_string = ""
        for achar in single_ingr:
            commaflag = False
            if achar not in string.punctuation and achar not in string.digits:
                ingr_char = achar
            elif achar == ",":
                commaflag = True
                ingr_char = "  "
            else:
                ingr_char = "  "
            ingr_string += ingr_char
        single_ingr = ingr_string
        if commaflag == True:
            single_ingr = reverse_ing(ingr_string)
            commaflag = False
            
        #need to strip out things
        if "spoon" in single_ingr:
            if single_ingr[:5] == "table":
                list_single_ingr = single_ingr.split()
 
        bag_of_words.append(single_ingr)
        allwords.append(single_ingr)
    
    allthethings[soup_file] = bag_of_words

stuff = FreqDist(allwords)
print stuff.most_common(20)
