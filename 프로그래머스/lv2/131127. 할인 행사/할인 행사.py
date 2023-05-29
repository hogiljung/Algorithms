from collections import Counter
def solution(want, number, discount):
    wishlist={w:n for w,n in zip(want, number)}
    ans=0

    wishlistLen= sum(wishlist.values())
    wishlist=Counter(wishlist)

    for i in range(0,len(discount)-wishlistLen+1):
        dislist=Counter(discount[i:i+wishlistLen])
        checklist=wishlist-dislist
        if sum(checklist.values())==0:
            ans+=1
    return ans
