import string
from collections.abc import Generator


def words(text: str) -> Generator[str]:
    """
    This generator receives text, splits it in to words without punctuations.
    :param text: The text.
    :return: The words without punctuations.
    """
    text = text.split()
    for word in text:
        new_word = ''.join(character for character in word if character.isalnum())
        yield new_word


def count_words(text: str) -> dict:
    """
    This function receives text and returns a dictionary with each word and its length.
    :param text: The text to make dictionary from.
    :return: Dictionary of word and length.
    """
    return {word: len(word) for word in words(text)}


if __name__ == "__main__":
    my_text = """
    You see, wire telegraph is a kind of a very, very long cat.
    You pull his tail in New York and his head is meowing in Los Angeles.
    Do you understand this?
    And radio operates exactly the same way: you send signals here, they receive them there.
    The only difference is that there is no cat.
    """
    print(count_words(my_text))
