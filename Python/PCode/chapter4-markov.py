import requests
import io
import zipfile
import re
from collections import defaultdict, Counter
from janome.tokenizer import Tokenizer
from tqdm import tqdm
import random
import pickle

#このようにメソッド内で self を使用することで、クラス内の他のメソッドや属性にアクセスできます。
class MarkovTextGenerator:
    def __init__(self):
        self.BEGIN = '__BEGIN__'
        self.END = '__END__'
        self.tokenizer = Tokenizer()

    def download_and_extract_text(self, url):
        response = requests.get(url)
        if response.status_code != 200:
            raise Exception(f"Failed to download content from {url}")
        
        content = response.content
        zip_stream = io.BytesIO(content)
        
        with zipfile.ZipFile(zip_stream) as zipf:
            namelist = zipf.namelist()
            data = zipf.read(namelist[0])
            original_text = data.decode('Shift_JIS')
        
        return original_text

    def preprocess_text(self, original_text):
        first_sentence = '吾輩《わがはい》は猫である。名前はまだ無い。'
        last_sentence = '南無阿弥陀仏《なむあみだぶつ》南無阿弥陀仏。ありがたいありがたい。'
        
        _, text = original_text.split(first_sentence)
        text, _ = text.split(last_sentence)
        text = first_sentence + text + last_sentence
        
        text = text.replace('｜', '').replace('　', '')
        text = re.sub('《\w+》', '', text)
        text = re.sub('［#\w+］', '', text)
        text = text.replace('\r', '').replace('\n', '')
        text = re.sub('[,「」?]', '', text)
        text = re.sub('（[^）]+）', '', text)
        text = re.sub('［[^］]+］', '', text)
        
        sentences = text.split('。')
        return sentences

    def get_three_words_list(self, sentence):
        words = list(self.tokenizer.tokenize(sentence, wakati=True))
        words = [self.BEGIN] + words + [self.END]
        three_words_list = []
        for i in range(len(words) - 2):
            three_words_list.append(tuple(words[i:i+3]))
        return three_words_list

    def create_entry(self):
        return {'words': [], 'weights': []}

    def generate_markov_dict(self, three_words_count):    
        markov_dict = defaultdict(self.create_entry)
        for three_words, count in three_words_count.items():
            two_words = three_words[:2]
            next_word = three_words[2]
            markov_dict[two_words]['words'].append(next_word)
            markov_dict[two_words]['weights'].append(count)
        return markov_dict

    def get_first_words_weights(self, three_words_count):
        first_word_count = Counter()
        for three_words, count in three_words_count.items():
            if three_words[0] == self.BEGIN:
                next_word = three_words[1]
                first_word_count[next_word] += count
        return first_word_count

    def build_model(self, url):
        original_text = self.download_and_extract_text(url)
        sentences = self.preprocess_text(original_text)
        
        three_words_list = []
        for sentence in tqdm(sentences):
            three_words_list += self.get_three_words_list(sentence)
        
        three_words_count = Counter(three_words_list)
        markov_dict = self.generate_markov_dict(three_words_count)
        first_words_weights = self.get_first_words_weights(three_words_count)
        
        return markov_dict, first_words_weights

    def generate_sentence(self, markov_dict, first_words_weights):
        current_words = [self.BEGIN]
        while current_words[-1] != self.END:
            if current_words[-1] == self.BEGIN:
                next_word = self.choose_first_word(first_words_weights)
            else:
                next_word = self.choose_next_word(markov_dict, current_words[-2:])
            current_words.append(next_word)
        
        generated_sentence = ''.join(current_words[1:-1])
        return generated_sentence

    def choose_first_word(self, first_words_weights):
        words, weights = zip(*first_words_weights.items())
        return random.choices(words, weights=weights)[0]

    def choose_next_word(self, markov_dict, prev_words):
        if tuple(prev_words) in markov_dict:
            next_words = markov_dict[tuple(prev_words)]
            return random.choices(next_words['words'], weights=next_words['weights'])[0]
        else:
            return self.END

if __name__ == "__main__":
    url = 'https://www.aozora.gr.jp/cards/000148/files/789_ruby_5639.zip'
    generator = MarkovTextGenerator()
    markov_dict, first_words_weights = generator.build_model(url)
    
    generated_sentence = generator.generate_sentence(markov_dict, first_words_weights)
    print(generated_sentence)

    # ロックオブジェクトを含まないようにデータを整理してから保存
    markov_dict_copy = defaultdict(dict)
    for key, value in markov_dict.items():
        markov_dict_copy[key]['words'] = value['words']
        markov_dict_copy[key]['weights'] = value['weights']
        # 不要なロックオブジェクトを削除
    markov_dict_copy = dict(markov_dict_copy)

    with open('markov_dict.pickle', 'wb') as f:
        data = (markov_dict, first_words_weights)
        pickle.dump(data, f)
