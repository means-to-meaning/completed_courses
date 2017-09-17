img_path = 'digital-images-week5_quizzes-noisy.jpg';
img = imread(img_path);
I = im2double(img);

img_path_smooth = 'original_week5.jpg';
img_smooth = imread(img_path_smooth);
I_smooth = im2double(img_smooth);


imshow(I);
imshow(I_smooth);

I_filt = medfilt2(I);
I_filt2 = medfilt2(I_filt);

imshow([I, I_filt, I_filt2]);

psnr1=PSNR(I_smooth, I)
psnr2=PSNR(I_smooth, I_filt)
psnr3=PSNR(I_smooth, I_filt2)