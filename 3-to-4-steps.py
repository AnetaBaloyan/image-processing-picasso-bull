import cv2 as cv
import os

# The files and directories to be used.
plate3 = os.path.realpath('Picasso-bull-plates/picasso_bull_plate_9.jpg')
plate4 = os.path.realpath('Picasso-bull-plates/picasso_bull_plate_10.jpg')
step_log = os.path.normpath(os.path.join(os.path.realpath(__file__), '../entry-4'))
# print(step_log)

bull3 = cv.imread(plate3, cv.IMREAD_GRAYSCALE)
bull3 = bull3[:, 26:] # I measured manually that to precisely align the two plates, plate 3 must be shifted 3 pixels upwards and to thr right. And plate 9 must be shifted 26 pixels to the right.
# cv.imshow('Bull3', bull3)
bull4 = cv.imread(plate4, cv.IMREAD_GRAYSCALE)
# cv.imshow('Bull4', bull4)

# Adjust the sizes.
h = min(bull3.shape[0], bull4.shape[0])
w = min(bull3.shape[1], bull4.shape[1])

bull3 = bull3[:h, :w]
bull4 = bull4[:h, :w]

# Overlay to plates to see the difference.
alpha = 0.3
beta = (1.0 - alpha)
overlay = cv.addWeighted(bull3, alpha, bull4, beta, 0.0)

# Save the state.
log_overlay = os.path.normpath(os.path.join(step_log, 'overlay.jpg'))
# print(log_overlay)
cv.imwrite(log_overlay, overlay)

# cv.imshow('Progress', overlay)

# cv.waitKey(0)