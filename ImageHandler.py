import cv2 as cv
import os


class ImageHandler:

    def __init__(self, path, log_folder):
        self.path = os.path.realpath(path)
        self.img = cv.imread(self.path, cv.IMREAD_GRAYSCALE)[3:, 3:]
        self.img_c = cv.imread(self.path, cv.IMREAD_COLOR)[3:, 3:]
        self.step_log = os.path.normpath(os.path.join(os.path.realpath(__file__), f'../{log_folder}'))


    def draw_middle_line(self, color=(0, 0, 255), thickness=2, offset=5, mid_x=215):
        if mid_x != 215:

            max_x = 0
            min_x = 600

            for x in range(self.img.shape[1]):
                for y in range(self.img.shape[0]):
                    if self.img[y, x] == 0:
                        if x > max_x:
                            max_x = x
                        if x < min_x:
                            min_x = x

            mid_x = int((max_x + min_x) / 2)

            print(f'Left: {min_x}\tRight: {max_x}\tMiddle: {mid_x}')

        cv.line(self.img_c, (mid_x, 5), (mid_x, self.img.shape[0] - 5), color, thickness=thickness)
                

    def draw_center_of_mass(self, color=(255, 0, 255), thickness=-1, radius=5):
        com_x = 0
        com_y = 0
        n = 0

        for x in range(self.img.shape[1]):
            for y in range(self.img.shape[0]):
                if self.img[y, x] < 255:
                    n += 1
                
                    com_x += ((255 - self.img[y, x]) / 255) * x
                    com_y += ((255 - self.img[y, x]) / 255) * y

        com_x = int(com_x / n)
        com_y = int(com_y / n)

        print(f'X_COM: {com_x}\tY_COM: {com_y}')

        image = cv.circle(self.img_c, (com_x, com_y), radius, color, thickness)


    def save_color(self, filename):
        log = os.path.normpath(os.path.join(self.step_log, filename))
        cv.imwrite(log, self.img_c)

    
    def save_raw(self, filename):
        log = os.path.normpath(os.path.join(self.step_log, filename))
        cv.imwrite(log, self.img)


    def show_color(self, name=None):
        if name is None:
            name = self.path

        cv.imshow(f'{name} color', self.img_c)
        cv.waitKey(0)   


    def show_raw(self, name=None):
        if name is None:
            name = self.path

        cv.imshow(f'{name} raw', self.img)
        cv.waitKey(0)  