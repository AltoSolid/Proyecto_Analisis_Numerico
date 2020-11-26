function CubicSpline(x,y)
    if length(x)~=length(y)
        error1=["Error","cuantity of x is different to cuantity of y "];
        Error1=table(error1);
        writetable(Error1,"cubic.xlsx")
        return 
    end 
    
    n=length(x)-1;
    M=zeros(n*4);
    b=zeros(n*4,1);
    m=[];
    for i=1:4
        m(1,i)=i;
    end
    disp(m)
    M(1,m)=[((x(1))^3) ((x(1))^2)  x(1) 1];
    b(1)=y(1);
    for i=1:n
        M(i+1,[4*i-3 4*i-2 4*i-1 4*i])=[((x(1+i))^3) ((x(i+1))^2) x(i+1) 1];
        b(i+1)=y(i+1);    
    for i=2:n  
         M(n+i,4*i-7:4*i)=[((x(i))^3) ((x(i))^2) x(i) 1 -((x(i))^3) -((x(i))^2) -x(i) -1];
         b(n+i)=0;
    end
    
    disp(M)
    
    for i=2:n  
         M(n+(n-1)+i,4*i-7:4*i)=[(3*(x(i)^2)) (2*x(i)) 1 0 -(3*(x(i)^2)) -(2*x(i)) -1 0];
         b(n+(n-1)+i)=0;
    end 
    for i=2:n  
         M(3*n+(i-2),4*i-7:4*i)=[(6*x(i)) 2 0 0 -(6*x(i)) -2 0 0];
         b(3*n)=0;
    end 
    M((4*n)-1,1)=6*x(1); 
    M((4*n)-1,2)=2;
    b(4*n)=0;
    M(4*n,(4*n)-3)=6*x(n+1);  
    M(4*n,(4*n)-2)=2;
    b(4*n)=0; 
    S=M\b;
    disp(M);
    disp(b);
    disp(S);
    xlswrite('Cubico.xlsx',S,'hoja1','A1');
    end