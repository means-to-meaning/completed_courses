function res = MAE( x,y )
%MAE Summary of this function goes here
%   Detailed explanation goes here
    [size_x,size_y] = size(x);
    res = abs(x-y);
    res = (1/(size_x*size_y))*sum(res(:));
end