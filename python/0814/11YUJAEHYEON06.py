# 케라스를 사용하여 MNIST 데이터셋을 이용해 간단한 다층 퍼셉트론 모델을 구축하고, 모델을 학습한 후, 
# 테스트 데이터셋에 대한 정확도를 출력하시오. 

import tensorflow as tf
from tensorflow.keras import layers, models

# MNIST 데이터셋 로드
mnist = tf.keras.datasets.mnist
(x_train, y_train), (x_test, y_test) = mnist.load_data()

# 데이터 전처리: 이미지를 1차원 벡터로 펼치고, 0-1 범위로 정규화
x_train = x_train.reshape((x_train.shape[0], -1)).astype('float32') / 255
x_test = x_test.reshape((x_test.shape[0], -1)).astype('float32') / 255

# 레이블을 원-핫 인코딩
y_train = tf.keras.utils.to_categorical(y_train, 10)
y_test = tf.keras.utils.to_categorical(y_test, 10)

# 모델 구축
model = models.Sequential([
    layers.Dense(512, activation='relu', input_shape=(784,)),
    layers.Dense(256, activation='relu'),
    layers.Dense(10, activation='softmax')
])

# 모델 컴파일
model.compile(optimizer='adam',
              loss='categorical_crossentropy',
              metrics=['accuracy'])

# 모델 학습
model.fit(x_train, y_train, epochs=5, batch_size=128, validation_split=0.2)

# 테스트 데이터셋에 대한 정확도 평가
test_loss, test_acc = model.evaluate(x_test, y_test)
print(f'Test accuracy: {test_acc}')