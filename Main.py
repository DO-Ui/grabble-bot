from selenium.webdriver.common.keys import Keys
import unscramble
from selenium import webdriver
import itertools
import random

args = webdriver.ChromeOptions()
args.add_argument("--mute-audio")

driver = webdriver.Chrome(chrome_options=args)

driver.get("https://grabble.coolmathgames.com/new-home")

previous = []

d = unscramble.GetDic()
ind = unscramble.Ints2Dic(d)


while True:
    try:
        tiles = driver.find_elements_by_css_selector("[class='tile']")

        word_elements = driver.find_elements_by_css_selector("[class='word']")

        current_words = []
        letters = []
        found = []
        found_words_to_steal = []

        for i in range(0, len(word_elements)):
            current_words.append(word_elements[i].text)
        for i in range(0, len(tiles)):
            letters.append(tiles[i].text)

        # STEALING FUNCTION

        if previous != letters:
            for word in current_words:
                for i in range(1, len(word + ''.join(letters))+1):
                    for combination in itertools.combinations(letters, i):
                        v = unscramble.Vect2Int(unscramble.Word2Vect(
                            ''.join(filter(str.isalnum, str(combination)+str(word)))))
                        tp = ind.get(v)
                        if tp != None:
                            for p in tp:
                                found_words_to_steal.append(p)

        found_words_to_steal = list(dict.fromkeys(found_words_to_steal))

        if len(found_words_to_steal) > 0:
            print(found_words_to_steal)
            for i in found_words_to_steal:
                driver.find_element_by_id("inputWord").click()
                driver.find_element_by_id("inputWord").send_keys(i)
                driver.find_element_by_id("inputWord").send_keys(Keys.RETURN)

        # NEW WORDS

        if previous != letters:
            for i in range(1, len(''.join(letters))+1):
                for combination in itertools.combinations(''.join(letters), i):
                    v = unscramble.Vect2Int(unscramble.Word2Vect(
                        ''.join(filter(str.isalnum, str(combination)))))
                    tp = ind.get(v)
                    if tp != None:
                        for p in tp:
                            found.append(p)

        found = list(dict.fromkeys(found))

        if len(found) > 0:
            # print(found)
            for i in found:
                driver.find_element_by_id("inputWord").click()
                driver.find_element_by_id("inputWord").send_keys(i)
                driver.find_element_by_id("inputWord").send_keys(Keys.RETURN)

        previous = letters
    except:
        pass
