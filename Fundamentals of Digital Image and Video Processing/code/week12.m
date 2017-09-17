n=10;
Acol = repmat(1:1:n,n,1);
Arow = repmat([1:1:n]',1,n);
D = sin(Acol + Arow);
I = diag(n);
A = normc(D + I);

S = 3;
b = [-2,-6,-9,1,8,10,1,-9,-4,-3]';
r = b;
Omega = [];

while sum(xomg ~= 0) < S
    x=zeros(n,1);
    valid_idx=setdiff(1:n,Omega);
    for j = valid_idx
        x(j) = A(:,j)'*r
    end
    [~,i] = max(abs(x));
    Omega = [Omega,i];
    Aomg = A(:,Omega);
    xomg = pinv(Aomg'*Aomg)*(Aomg'*b);
    r = b - Aomg*xomg;
end
Omega
x
