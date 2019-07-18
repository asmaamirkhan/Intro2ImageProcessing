# @author: Asmaa ~ 2019
# TRAFFIC SIGNS CLASSIFICATION - MVP version
############################################

import os
import skimage.data
import skimage.transform
from matplotlib import pyplot as plt
import tensorflow as tf
import numpy as np
import random

os.environ['TF_CPP_MIN_LOG_LEVEL'] = '2'

# !Data loading function
def load_dataset(dataset_dir):

    # get all directories in data set folder
    # !REMEMBER that each folder name represents a label
    dirs = [d for d in os.listdir(dataset_dir) if os.path.isdir(
        os.path.join(dataset_dir, d))]

    # create arrays to store images and labels
    labels = []
    images = []

    # loop through directories, get data and store it in the arrays

    for dir in dirs:
        # get label name
        label = os.path.join(dataset_dir, dir)
        # get each image name
        # the result is an array of files
        file_names = [os.path.join(label, f)
                      for f in os.listdir(label) if f.endswith('.ppm')]

        # for each label (directory name) load its images and store in the array
        for file1 in file_names:
            # open image and store it and its corresponding label
            images.append(skimage.data.imread(file1))
            labels.append(int(dir))
    return images, labels

# !Data display function


def display_images_and_labels(images, labels):
    """Display the first image of each label."""
    unique_labels = set(labels)
    plt.figure(figsize=(15, 15))
    i = 1
    for label in unique_labels:
        # Pick the first image for each label.
        image = images[labels.index(label)]
        plt.subplot(8, 8, i)  # A grid of 8 rows x 8 columns
        plt.axis('off')
        plt.title("Label {0} ({1})".format(label, labels.count(label)))
        i += 1
        _ = plt.imshow(image)
    plt.show()


# load data
images, labels = load_dataset('traffic_dataset_train')

# print data info
print('#images', len(images), '#labels', len(
    labels), '#unique labels', len(set(labels)))

# display sample data
#display_images_and_labels(images, labels)


# !PreProcessing
# resize images to get 32X32 images
resized_images = [skimage.transform.resize(image, (32, 32), mode='constant')
                  for image in images]

# display sample resized data
#display_images_and_labels(resized_images, labels)


# convert images into numpy arrays
labels_a = np.array(labels)
images_a = np.array(resized_images)

# !Data is ready to use, set trainig model properties
# create a tensorflow graph
tgraph = tf.Graph()

with tgraph.as_default():

    # create placeholders for inputs(images) and labels
    # [batch size, height, width, channels]
    image_ph = tf.placeholder(tf.float32, [None, 32, 32, 3])
    label_ph = tf.placeholder(tf.int32, [None])

    # flatten images
    flat_images = tf.contrib.layers.flatten(image_ph)

    # generate logits
    logits = tf.contrib.layers.fully_connected(flat_images, 62, tf.nn.relu)

    # convert logits into indices (integers)
    predicted_labels = tf.argmax(logits, 1)

    # choose a  loss function
    loss = tf.reduce_mean(tf.nn.sparse_softmax_cross_entropy_with_logits(
        logits=logits, labels=label_ph))

    # create training optimizer
    train_model = tf.train.AdamOptimizer(learning_rate=0.001).minimize(loss)

    # initialize variables before start training
    init = tf.global_variables_initializer()

    # print model propetires
    print("images_flat: ", flat_images)
    print("logits: ", logits)
    print("loss: ", loss)
    print("predicted_labels: ", predicted_labels)


# !START TRAINING
# we create a session to start training
sess = tf.compat.v1.Session(graph=tgraph)

# initialize all variables (return value is not important)
_ = sess.run([init])

# start training loop 300 iterations
for i in range(201):
    _, loss_value = sess.run([train_model, loss],
                             feed_dict={image_ph: images_a, label_ph: labels_a})
    if i % 10 == 0:
        print("Loss: ", loss_value)

# !Model is ready, we can use it
# first use it on training set
# pick random samples from training set
s_indices = random.sample(range(len(resized_images)), 10)
s_images = [resized_images[i] for i in s_indices]
s_labels = [labels[i] for i in s_indices]

# run the model on the sample
predicted = sess.run([predicted_labels],
                     feed_dict={image_ph: s_images})[0]

print(s_labels)
print(predicted)


# Display the predictions and the ground truth visually.
fig = plt.figure(figsize=(10, 10))
for i in range(len(s_images)):
    truth = s_labels[i]
    prediction = predicted[i]
    plt.subplot(5, 2, 1+i)
    plt.axis('off')
    color = 'green' if truth == prediction else 'red'
    plt.text(40, 10, "Truth:        {0}\nPrediction: {1}".format(truth, prediction),
             fontsize=12, color=color)
    plt.imshow(s_images[i])
plt.show()

# !Evaluation, try test data
# load test data
images_t, labels_t = load_dataset('traffic_dataset_test')

# resize test data
resized_test_images = [skimage.transform.resize(image, (32, 32), mode='constant')
                       for image in images_t]


# Run predictions against the full test set.
predicted = sess.run([predicted_labels],
                     feed_dict={image_ph: resized_test_images})[0]

# Calculate how many matches we got.
match_count = sum([int(y == y_) for y, y_ in zip(labels_t, predicted)])
accuracy = match_count / len(labels_t)
print("Accuracy: {:.3f}".format(accuracy))

r = []
for m in range(10):
    r.append(random.randint(30, 2000))

print(r)

for i in range(10):
    truth = labels_t[r[i]]
    prediction = predicted[r[i]]
    plt.subplot(5, 2, 1+i)
    plt.axis('off')
    color = 'green' if truth == prediction else 'red'
    plt.text(40, 10, "Truth:        {0}\nPrediction: {1}".format(truth, prediction),
             fontsize=12, color=color)
    plt.imshow(resized_test_images[r[i]])
plt.show()

# Best obtained accuracy: 0.649 :'(
print(accuracy)