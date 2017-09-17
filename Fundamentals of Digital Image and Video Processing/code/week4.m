img_path1 = 'digital-images-week4_quizzes-frame_1.jpg';
img_path2 = 'digital-images-week4_quizzes-frame_2.jpg';

img1 = imread(img_path1);
img2 = imread(img_path2);

I1 = im2double(img1);
I2 = im2double(img2);

block = I2(65:96,81:112);

[size_x,size_y] = size(I1);
block_size_x=32;
block_size_y=32;

min_mae = 1000000000;
min_row = 0;
min_col= 0;
for row=1:(size_x-block_size_x)
    for col=1:(size_y-block_size_y)
        block_try = I1(row:(row+block_size_x-1),col:(col+block_size_y-1));
        this_mae = MAE(block_try, block);
        if this_mae < min_mae
           min_mae = this_mae;
           disp(min_mae);
           min_row = row;
           min_col = col;
        end
    end
end

disp([min_row, min_col]);