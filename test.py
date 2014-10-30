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


def main():
    print(reverse_ing("thyme, dried"))
    print(reverse_ing("barbecue chicken, chopped"))


if __name__=="__main__":
    main()
