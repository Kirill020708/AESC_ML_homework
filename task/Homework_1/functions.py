import numpy as np

def prod_non_zero_diag(x):
    """Compute product of nonzero elements from matrix diagonal.

    input:
    x -- 2-d numpy array
    output:
    product -- integer number


    Not vectorized implementation.
    """
    sum=1
    for i in range(min(x.size,x[0].size)):
        if x[i][i]!=0:
            sum*=x[i][i]

    return sum

    pass


def are_multisets_equal(x, y):
    """Return True if both vectors create equal multisets.

    input:
    x, y -- 1-d numpy arrays
    output:
    True if multisets are equal, False otherwise -- boolean

    Not vectorized implementation.
    """
    if len(x)!=len(y):
        return False
    x.sort()
    y.sort()
    for i in range(len(x)):
        if x[i]!=y[i]:
            return False
    return True
    pass


def max_after_zero(x):
    """Find max element after zero in array.

    input:
    x -- 1-d numpy array
    output:
    maximum element after zero -- integer number

    Not vectorized implementation.
    """
    mx=0
    for i in range(1,x.size):
        if x[i-1]==0:
            mx=max(mx,x[i])
    return mx
    pass


def convert_image(img, coefs):
    """Sum up image channels with weights from coefs array

    input:
    img -- 3-d numpy array (H x W x 3)
    coefs -- 1-d numpy array (length 3)
    output:
    img -- 2-d numpy array

    Not vectorized implementation.
    """
    ans = np.zeros((np.size(img,axis=0),np.size(img,axis=1)))
    for i in range(np.size(img,axis=0)):
        for j in range(np.size(img,axis=1)):
            for k in range(coefs.size):
                ans[i][j]+=img[i][j][k]*coefs[k]
    return ans
    pass


def run_length_encoding(x):
    """Make run-length encoding.

    input:
    x -- 1-d numpy array
    output:
    elements, counters -- integer iterables

    Not vectorized implementation.
    """
    a=0
    kl=0
    nmb=[]
    rep=[]
    for i in range(x.size):
        if i==0 or x[i-1]==x[i]:
            a=x[i]
            kl+=1
        else:
            nmb.append(a)
            rep.append(kl)
            a=x[i]
            kl=1

    return (np.array(nmb),np.array(rep))
    pass


def pairwise_distance(x, y):
    """Return pairwise object distance.

    input:
    x, y -- 2d numpy arrays
    output:
    distance array -- 2d numpy array

    Not vectorized implementation.
    """
    ans = np.empty((np.size(x,axis=0),np.size(y,axis=0)))
    for i in range(np.size(x,axis=0)):
        for j in range(np.size(y,axis=0)):
            ans[i][j]=math.sqrt((x[i][0]-y[j][0])**2+(x[i][1]-y[j][1])**2)
    return ans
    pass
