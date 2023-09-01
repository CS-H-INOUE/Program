from janome.tokenizer import Tokenizer
from collections import Counter
import time
from tqdm import tqdm
import re
import requests
import io
import zipfile
from collections import defaultdict


def name_edit(original_text):
    first_sentence = '吾輩《わがはい》は猫である。名前はまだ無い。'
    last_sentence = '南無阿弥陀仏《なむあみだぶつ》南無阿弥陀仏。ありがたいありがたい。'
    
    #説明文書の削除（青空文庫）
    _, text = original_text.split(first_sentence)
    text, _ = text.split(last_sentence)
    text = first_sentence + text + last_sentence
    
    #不要な文字列を削除
    text = text.replace('｜', '').replace('　', '')
    text = re.sub('《\w+》', '', text)
    text = re.sub('［#\w+］', '', text)
    text = text.replace('\r', '').replace('\n', '')
    text = re.sub('[,「」?]', '', text)
    text = re.sub('（[^）]+）', '', text)
    text = re.sub('［[^］]+］', '', text)
    
    sentences = text.split('。')
    print('文の数', len(sentences))
    sentences[:10]

    return sentences

def name_list():
    # wagahaihanekodearu FileURL
    url = 'https://www.aozora.gr.jp/cards/000148/files/789_ruby_5639.zip'
    r = requests.get(url)
    content = r.content
    
    f = io.BytesIO(content)
    zipf = zipfile.ZipFile(f)
    namelist = zipf.namelist()
    data = zipf.read(namelist[0])
    original_text = data.decode('Shift_JIS')
    #print('original_text',original_text)

    edited_text = name_edit(original_text)  # name_edit の戻り値を受け取る
    return edited_text

def get_three_words_list(sentence):
    t = Tokenizer()
    BEGIN = '__BEGIN__'
    END = '__END__'
    words = list(t.tokenize(sentence, wakati=True))
    words = [BEGIN] + words + [END]
    three_words_list = []
    for i in range(len(words) -2):
        three_words_list.append(tuple(words[i:i+3]))
    return three_words_list

#マルコフ連鎖用辞書データの作成
def generate_markov_dict(three_words_count):
    markov_dict = {}
    for three_words, count in three_words_count.items():
        two_words = three_words[:2]
        next_words = three_words[2]
        if two_words not in markov_dict:
            markov_dict[two_words] = {'words': [], 'weights': []}
        markov_dict[two_words]['words'].append(next_words)
        markov_dict[two_words]['weights'].append(count)
    return markov_dict

#最初の単語を選択するための辞書データを作成する
def get_first_word_and_count(three_words_count):
    first_word_count = defaultdict(int)
    for three_words, count in three_words_count.items():
        if three_words[0] == BEGIN:
            next_word = three_words[1]
            first_word_count[next_word] += count

    return first_word_count                            

#最初の単語と出現数を取得
def get_first_words_weights(three_words_count):
    first_word_count = get_first_word_and_count(three_words_count)
    words = []
    weights = []
    for word , count in first_word_count.items():
        words.append(word)
        weights.append(count)

    return words, weights

if __name__ == "__main__":

    sentences = name_list()
    
    three_words_list = []    
    for sentence in tqdm(sentences):
        three_words_list += get_three_words_list(sentence)
    #3words 組の種類を確認
    three_words_count = Counter(three_words_list)
    print(len(three_words_count))

    #マルコフ連鎖用辞書データの作成
    markov_dict = generate_markov_dict(three_words_count)
    print('len(mrkov_dict):    ',len(mrkov_dict))
    first_words, first_weights = get_first_words_weights(three_words_count)
    print('len(first_words):    ',len(first_words))