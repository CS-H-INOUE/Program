from sklearn import datasets
from sklearn.linear_model import LogisticRegression
from matplotlib import pyplot as plt
from PIL import Image
from PIL import ImageEnhance  # 画像の明るさを変えるために必要(明暗の調整)
from PIL import ImageOps  # 画像の反転を行うために必要(白黒反転)
import matplotlib.pyplot as plt
import numpy as np

import os

class ImagePreprocessor:
    def __init__(self, image_filename):
        self.image_filename = image_filename
        
    def load_image(self):
        current_directory = os.getcwd()
        image_path = os.path.join(current_directory, self.image_filename)
        return Image.open(image_path)
    
    def enhance_brightness(self, factor):
        image = self.load_image()
        enhancer = ImageEnhance.Brightness(image)
        enhanced_image = enhancer.enhance(factor)
        return enhanced_image

    def gray(self, enhanced_image):
        im_gray = enhanced_image.convert('L')
        return im_gray

    def rs(self, im_gray):
        im_8x8 = im_gray.resize((8,8),Image.LANCZOS)
        return im_8x8

    def inv(selfm, im_8x8):
        im_inverse = ImageOps.invert(im_8x8)
        return im_inverse

    def convert_to_feature_vector(self, image):
        # asarray() は、入力として与えられたオブジェクトがNumPy配列であれば、
        # そのオブジェクトをコピーせずにそのまま返します。
        # もし入力がNumPy配列でない場合、新しいNumPy配列を作成して返します。
        # image_array = np.asarray(image) 

        # array()は、常に新しいNumPy配列を作成して返します。
        # 元々がNumPy配列であっても、新しい配列が作成されます。
        # したがって、元のデータとは別のメモリ領域にコピーが作成されるため、メモリ使用量が増加します。
        image_array = np.array(image)  # 画像をnumpy配列に変換
        X_im1d = image_array.reshape(-1)  # 画像を1次元の特徴ベクトルに変換
        
        print('x_im1d array:',X_im1d)
        print('x_im1d array length:',len(X_im1d))

        feature_vector = X_im1d * (16 / 255) # 画像の各ピクセルの値を0から15の範囲に変換
        return feature_vector

    def show_image(self, image):
        fig, ax = plt.subplots(1, 1, figsize=(8, 8))
        ax.imshow(image, cmap='gray')
        plt.show()

class CustomLogisticRegression:
    def __init__(self):
        # 慣習的にclf = classifierとする
        self.clf = LogisticRegression(random_state=0, solver='liblinear', multi_class='auto')
    
    def train(self):
        X, y = datasets.load_digits(return_X_y=True)
        self.clf.fit(X, y)
    
    def predict(self, X_test):
        print('X_test:',X_test)
        print("X_test length:", len(X_test[0]))
        return self.clf.predict(X_test)[0]
    
    def predict_proba(self, X_test):
        return self.clf.predict_proba(X_test)[0]

if __name__ == "__main__":
    # クラスのインスタンス化と学習
    model = CustomLogisticRegression()
    model.train()

    # 画像のパスを指定
    image_filename = 'moji.jpg'
    
    # 画像前処理クラスのインスタンス化
    preprocessor = ImagePreprocessor(image_filename)
    
    # 画像の読み込みと表示
    original_image = preprocessor.load_image()
    # preprocessor.show_image(original_image)

    # 画像の明るさを変更
    enhanced_image = preprocessor.enhance_brightness(1)  # 例として明るさを2.0倍に変更

    # GrayScaleに変換
    im_gray = preprocessor.gray(enhanced_image)

    #文字の縮小
    im_8x8 = preprocessor.rs(im_gray)

    #白黒反転
    im_inverse = preprocessor.inv(im_8x8)
    
    # preprocessor 後の画像の表示
    preprocessor.show_image(im_8x8)
    preprocessor.show_image(im_inverse)
    
    # 特徴ベクトルに変換
    feature_vector = preprocessor.convert_to_feature_vector(im_inverse)
    print("Feature Vector:", feature_vector)
    print("Feature Vector length:", len(feature_vector))

    # 予測のデモ
    prediction = model.predict([feature_vector])
    print("Prediction:", prediction)

    # 予測確率のデモ
    probabilities = model.predict_proba([feature_vector])
    print("Predicted Probabilities:", probabilities)
