# pool_ops.py
#
# Usage: python3 pool_ops.py c_in h_in w_in n_filt h_filt w_filt s p
#  script to determine the output shape and operation count of a convolution layer
# Parameters:
# c_in: input channel count
# h_in: input height count
# w_in: input width count
# h_pool: average pooling kernel height count
# w_pool: average pooling kernel width count
# s: stride of average pooling kernel
# p: amount of padding on each of the four input map sides
# Output:
# c_out: output channel count
# h_out: output height count
# w_out: output width count
# adds: number of additions performed
# muls: number of multiplications performed
# divs: number of divisions performed

# Written by Jack Rathert
# Other contributors: None

## imports---------------------------------------------------------------------------
import sys

## Functions--------------------------------------------------------------------------
def poolops(c_in:int,h_in:int,w_in:int,h_pool:int,w_pool:int,s:int,p:int):
   c_out = c_in 
   h_out = (h_in+2*p-h_pool)/s + 1
   w_out = (w_in+2*p-w_pool)/s + 1
   adds = h_out*w_out*c_in*(h_pool*w_pool-1)
   muls = 0
   divs = c_in*h_out*w_out
   return c_out,h_out,w_out,adds,muls,divs
   
# Arguments---------------------------------------------------------------------------
# initilization
c_in = int(0.0)
h_in = int(0.0)
w_in = int(0.0)
h_pool = int(0.0)
w_pool = int(0.0)
s = int(0.0)
p = int(0.0)

# parsing
if len(sys.argv)==8:
   c_in = int(sys.argv[1])
   h_in = int(sys.argv[2])
   w_in = int(sys.argv[3])
   h_pool = int(sys.argv[4])
   w_pool = int(sys.argv[5])
   s = int(sys.argv[6])
   p = int(sys.argv[7])
else:
  print(\
   'Usage: '\
   'python3 pool_ops.py c_in h_in w_in h_pool w_pool s p'\
  )
  exit()

## Function Calls ----------------------------------------------------------------------
c_out, h_out, w_out, adds, muls, divs = poolops(c_in,h_in,w_in,h_pool,w_pool,s,p)

print(int(c_out)) # output channel count
print(int(h_out)) # output height count
print(int(w_out)) # output width count
print(int(adds))  # number of additions performed
print(int(muls))  # number of multiplications performed
print(int(divs))  # number of divisions performed