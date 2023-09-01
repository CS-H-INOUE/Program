from sklearn import datasets
from matplotlib import pyplot as plt

# X, y = datasets.load_iris(return_X_y=True)
X, y = datasets.load_digits(return_X_y=True)
print('x: ',X)
print('x.shape: ',X.shape)
print('y: ',y)
print('y.shape: ',y.shape)

X0 = X[0]
print('X0: ',X0)
print('X0.shape: ',X0.shape)

X0_square = X0.reshape(8,8)
X0_square = X0_square.astype('uint8')
print('8pixel square: ', X0_square)
print('x0_square.shape//check shape:')
print(X0_square.shape)

# plt.imshow(X0_square,cmap='gray')
# 白黒反転させてある。白が1、黒が0
fig,ax = plt.subplots(1,1,figsize=(8,8))
print('cmap:gray')
ax.imshow(X0_square,cmap='gray')

print('cmap:binayry')
# ax.imshow(X0_square,cmap='binary')
# plt.show()

#Otherdata choice
fig,ax = plt.subplots(1,1,figsize=(8,8))
X42 = X[42].reshape(8,8).astype('uint8')    # 42番目のデータを取り出す
ax.imshow(X42,cmap='gray')
plt.show()

#look at the value of the pixcel
X0_square[1][5]
print('X0_square[1][5]: ',X0_square[1][5])
X0_square[3][7]
print('X0_square[3][7]: ',X0_square[3][7])
X0_square[4][4]
print('X0_square[4][4]: ',X0_square[4][4])

