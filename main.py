import wikipedia as wk
from wikipedia.wikipedia import page


def choose_language():

    languages = {
        "Bulgarian": "bg",
        "English": "en",
        "Korean": "ko",
        "Japonese": "ja"
    }
    for lang in languages:
        print(f"Type {lang} to change the language")

    print("You selected: ", end="")
    lang_choice = input()
    if lang_choice not in languages:
        raise ValueError

    return wk.set_lang(languages[lang_choice])


def choose_page():
    print("Enter a")
    keywords = input()

    try:
        possible_pages = wk.search(str(keywords), results=10, suggestion=False)
    except wk.DisambiguationError:
        print("Be more specific")
    except wk.PageError:
        print(f"{keywords} Does not match any articles in the database.")

    for count, articles in enumerate(possible_pages):
        print(f"Type {count} to open {articles} article.")
    try:
        print("Selecting: ", end="")
        article_number = int(input())
        if article_number > len(possible_pages):
            raise IndexError
    except ValueError:
        print("You did not enter a number")

    page_selected = wk.page(str(possible_pages[article_number]))

    print(page_selected.content)


def main():
    choose_language()
    choose_page()


if __name__ == '__main__':
    main()
