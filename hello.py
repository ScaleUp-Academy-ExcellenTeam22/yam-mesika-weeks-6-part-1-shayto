def words_length(sentence: str) -> list[int]:
    """
    This function receives a sentence, splits the sentence to words (including punctuation)
    This function returns a list of all words length.
    :param sentence: The sentence to split into words and check their lengths.
    :return: List of the lengths of the words.
    """
    words = sentence.split()
    return [len(word) for word in words]


if __name__ == "__main__":
    print(words_length("Toto, I've a feeling we're not in Kansas anymore"))
