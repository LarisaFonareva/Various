n,m,k,x,y,z,t,a=[int(input()) for _ in range(8)]
two_books=n+m-x-t+m+k-y-t+n+k-z-t
one_book=n-t-(n+m-x-t)-(n+k-z-t)+m-t-(n+m-x-t)-(m+k-y-t)+k-t-(n+k-z-t)-(m+k-y-t)
zero_books=a-one_book-two_books-t
print(one_book,two_books,zero_books,sep='\n')