function res = PSNR( x,y )
%PSNR Summary of this function goes here
%   Detailed explanation goes here
max_i = 1;
mserror = MSE(x,y);
res = 10*log10(max_i/(mserror));
end