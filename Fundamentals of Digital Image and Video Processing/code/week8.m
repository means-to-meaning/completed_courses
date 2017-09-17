question5 = -(0.2*log2(0.2) + 0.3*log2(0.3) + 0.5*log2(0.5))

img_path = 'Cameraman256_week8.bmp';
img = imread(img_path);
img_dbl = im2double(img);
[a,b]=hist(img_dbl(:),unique(img_dbl(:)));
rel_freq = a./length(img_dbl(:));
entrpy = -sum(rel_freq.*log2(rel_freq))