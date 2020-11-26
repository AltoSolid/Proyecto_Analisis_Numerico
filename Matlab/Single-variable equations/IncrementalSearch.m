%This program finds an interval where f(x) has a change of sign (root)
%using the incremental search method

syms x
x0 = -3
delta= 0.5
f = log(sin(x)^2+1)-1/2
itera = 100
c=1
x1=x0+delta
while c<=itera
    f1=subs(f,x0);
    f2=subs(f,x1);
    if f1==0
        fprintf("There is a root in: %12.10f\n",x0)
    elseif f2==8
        fprintf("There is a root in: %12.10f\n",x1)
    elseif f1*f2<0
        fprintf ("There is a root in: (%12.10f,%12.10f)\n",x0,x1)
    end
    x0=x1;
    x1=x1+delta;
    c=c+1;
end