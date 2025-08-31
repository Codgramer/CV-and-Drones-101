import cv2
import numpy as np
import matplotlib.pyplot as plt


def hybrid(s1,s2):
    
    img1 = cv2.resize(s1,(256,256))
    img2 = cv2.resize(s2,(256,256))

    f_transform_img1 = np.fft.fft2(img1)
    fshift = np.fft.fftshift(f_transform_img1)
    f_transform_img2 = np.fft.fft2(img2)
    fshift2 = np.fft.fftshift(f_transform_img2)

# low pass filter
    # rows , cols = img1.shape
    # center_row , center_col = rows//2 , cols//2
    # square_size = 40
    # lpf = np.zeros((rows,cols) , dtype=np.uint8)
    # lpf[center_row - square_size//2 : center_row + square_size//2 ,
    #     center_col - square_size//2 : center_col + square_size//2] = 255
    center = (256//2 , 256//2)
    d = 10
    lpf = np.zeros_like(img1)
    lpf[center[0]-d:center[0]+d, center[1]-d:center[1]+d] = 1
    
# high pass filter
    # square_size = 10
    # hpf = np.ones((rows,cols) , dtype=np.uint8)*255
    # hpf[center_row - square_size//2 : center_row + square_size//2 ,
    #     center_col - square_size//2 : center_col + square_size//2] = 1
    hpf = np.ones_like(img2)
    hpf[center[0]-d:center[0]+d, center[1]-d:center[1]+d] = 0

# applting lpf and hpf in fourier of image
    f_transform_img1_lpf = (fshift*lpf)
    f_transform_img2_hpf = (fshift2*hpf)

# inverse fourier to get image back after filter
    img1_lpf = np.fft.fft2(np.fft.ifftshift(f_transform_img1_lpf)).real
    img1_lpf = cv2.rotate(img1_lpf,cv2.ROTATE_180)
    img2_hpf = np.fft.fft2(np.fft.ifftshift(f_transform_img2_hpf)).real
    img2_hpf = cv2.rotate(img2_hpf,cv2.ROTATE_180)

# combine lpf and hpf image
    hybrid_img = cv2.addWeighted(img1_lpf , 0.5 , img2_hpf , 0.5 , 0)
    # hybrid_img = cv2.rotate(hybrid_img,cv2.ROTATE_180)
    # hybrid_img = cv2.add(img1_lpf,img2_hpf)/2

    plt.figure(figsize=(20,20))


    plt.subplot(4,4,1) , plt.imshow(img1 , cmap='gray') , plt.title('image 1')
    plt.subplot(4,4,2) , plt.imshow(img2 , cmap='gray') , plt.title('image 2')
    plt.subplot(4,4,3) , plt.imshow(lpf , cmap='gray') , plt.title('Low-Pass_Filter')
    plt.subplot(4,4,4) , plt.imshow(20*np.log(np.abs(fshift) + 1) , cmap='gray') , plt.title('Fourier Transorm - Image 1')
    plt.subplot(4,4,5) , plt.imshow(np.log(np.abs(f_transform_img1_lpf) + 1) , cmap='gray') , plt.title('Filtered Fourier Transorm - Image 1')
    plt.subplot(4,4,6) , plt.imshow(img1_lpf , cmap='gray') , plt.title('Image 1 after lpf')
    plt.subplot(4,4,7) , plt.imshow(hpf , cmap='gray') , plt.title('High-Pass_Filter')
    plt.subplot(4,4,8) , plt.imshow(20*np.log(np.abs(fshift2) + 1) , cmap='gray') , plt.title('Fourier Transorm - Image 2')
    plt.subplot(4,4,9) , plt.imshow(np.log(np.abs(f_transform_img2_hpf) + 1) , cmap='gray') , plt.title('Filtered Fourier Transorm - Image 2')
    plt.subplot(4,4,10) , plt.imshow(img2_hpf , cmap='gray') , plt.title('Image 2 after hpf')
    plt.subplot(4,4,11) , plt.imshow(hybrid_img , cmap='gray') ,plt.title('Combined Hybrid Image')
    plt.show()

    # cv2.imshow('Low-Pass Filter', lpf)
    # cv2.imshow('Fourier Transform - Image 1', 20*np.log(np.abs(fshift) + 1).astype(np.uint8))
    # cv2.imshow('Filtered Fourier - Image 1', np.log(np.abs(f_transform_img1_lpf) + 1).astype(np.uint8))
    # cv2.imshow('Image 1 after LPF', img1_lpf)
    # cv2.imshow('High-Pass Filter', hpf)
    # cv2.imshow('Fourier Transform - Image 2', 20*np.log(np.abs(fshift2) + 1).astype(np.uint8))
    # cv2.imshow('Filtered Fourier - Image 2', np.log(np.abs(f_transform_img2_hpf) + 1).astype(np.uint8))
    # cv2.imshow('Image 2 after HPF', img2_hpf)
    # cv2.imshow('Combined Hybrid Image', hybrid_img)

    # cv2.waitKey(0)

image_1 = cv2.imread(r"C:\Users\Himanshu\Downloads\depositphotos_118245716-stock-photo-black-and-white-photo-of.jpg",cv2.IMREAD_GRAYSCALE)
image_2 = cv2.imread(r"C:\Users\Himanshu\Downloads\Albert_Einstein_Head.jpg",cv2.IMREAD_GRAYSCALE)
hybrid(image_1 , image_2)