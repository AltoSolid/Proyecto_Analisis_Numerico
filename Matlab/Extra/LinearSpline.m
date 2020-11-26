x=input('Enter vector X: ');
y=input('Enter vector Y: ');
n=length(X)-1;
M=zeros(n,2);

for i=1:n
    for j=1:2
        if (j==1)
            M(i,j)=((Y(i+1,1)-Y(i,1))/(X(i+1,1)-X(i,1)));
        end
        if (j==2)
           M(i,j)=Y(i+1,1)+((M(i,1)))*(-(X(i+1,1)));
        end
    end
end
 
N=length(x)-1;
pos=1;
valor=length(x);
valor1=1;
valor2=2;
fprintf('The corresponding sections are: %g \n',N);
    
for i=1:(length(x)-1) 
    fprintf('\nBetween xi and xf : %g and %g\n\n',x(pos),x(pos+1));
    for j=valor1:(valor2)
        a=M(i,j);
        disp(a);
    end
    pos=pos+1;
end
