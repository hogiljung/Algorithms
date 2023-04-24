def solution(M, N):
    if (M-1)==0:
        return (N-1)
    
    if (N-1)==0:
        return (M-1)
    
    return M*N-1