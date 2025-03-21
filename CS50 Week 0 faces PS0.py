def convert(smiley):
    smiley = smiley.replace(":)", "🙂")
    smiley = smiley.replace(":(", "🙁")
    return smiley

def main():
    convert_smile = input(str("Please type a sentence: "))
    print(convert(convert_smile))

main()

