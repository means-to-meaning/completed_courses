function res = MSE( x,y )
%MSE Summary of this function goes here
%   Detailed explanation goes here
[size_x,size_y]=size(x);
d = (x - y);
res = (1/(size_x*size_y))*sum(d(:).^2);
end