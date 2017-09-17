img_path = 'Cameraman256_week9.bmp';
img_path_enc = 'Cameraman256enc_week9.bmp';

img_orig = im2double(imread(img_path));
imwrite(img_orig,img_path_enc,'jpg','quality',10);
img_enc = im2double(imread(img_path_enc));
PSNR(img_enc, img_orig)

