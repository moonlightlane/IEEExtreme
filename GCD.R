GCD <- function(N,V,X) {
  new_V <- V/X;
  int_V <- vector();
  for (i = 1; i < N; i++) {
    if (new_V(i) - floor(new_V(i)) < 0.00000001) {
      int_V(i) <- new_V(i);
    }
  }
  print(int_V)
}

GCD(5,c(2,3,5,6,6,6),2)
