import cv2


def get_image_from_path(path, filename):
    # with cv2.imread(path+filename) as image:
    #     cv2.write(path+"newImage.jpg",image)
    image = cv2.imread(path + filename)
    cv2.imwrite(path + "newImage.jpg", image)


def main():
    get_image_from_path("./OPENCV/ImageData/", "test.jpg")


if __name__ == '__main__':
    main()