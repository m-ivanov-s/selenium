from main import check_words


# def test():
#     assert 'НЕВЕРНО' in check_words("НИВЕРНО")

def test(right_word, wrong_word):
    assert right_word in check_words(wrong_word)
