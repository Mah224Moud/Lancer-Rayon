# coding=utf-8
from util import *


def tof(contact):
        if is_num(contact) : 
                return contact
        else:
                if not(type(contact) is tuple):
                        return contact.t 

 
def purge(l):
        if None == l:
                return None
        ((a1, a2), qa)=(hd(l), tl(l))
        if (None == qa):
                if a1==a2:
                        return None
                else:
                        return cons((a1, a2), None)
        if(a1 != a2):
                return cons((a1, a2), purge(qa))
        else:
                return purge(qa)

def purge1D(liste):
        return purge(liste)


def merge(l):
        if None == l:
                return None;

        ((a1, a2), q1) = (hd(l),tl(l))
        if (None == q1):
                return cons((a1, a2), None)
        else:
                ((a3, a4), q2) = (hd(q1),tl(q1))
                if None == q2:
                        if a2 >= a3:
                                return cons((a1, a4), None)
                        else:
                                temp=cons((a1, a2), (a3, a4))
                                return cons(temp, None)
                else:
                        if a2 >= a3:
                                return merge(cons((a1, a4), q2))
                        else:
                                return cons((a1, a2), merge(cons((a3, a4), q2)))
def merge1D(liste):
        return merge(liste)     


def simplify1D(liste):
        return purge1D(merge1D(liste))
def simplify(intervalles):
    if None == intervalles or None == tl(intervalles):
        return intervalles
    else:
        a = (a1, a2) = hd(intervalles)
        (b1, b2) = hd(tl(intervalles))
        if a2 == b1:
            return simplify(cons((a1, b2), tl(tl(intervalles))))
        else:
            return cons(a, simplify(tl(intervalles)))
def inter( a, b):
        
        if None==a or None==b :
                return None
        else:
                ((a1,a2), qa) = (hd(a), tl(a))
                ((b1,b2), qb) = (hd(b), tl(b))
                assert( tof( a1) <= tof( a2))
                assert( tof( b1) <= tof( b2))
                if tof( a1) > tof( b1) :
                        return inter(b, a)
                elif tof( a2) < tof( b1) :
                        return inter( qa, b)
                elif tof( b2) <= tof( a2) :
                        return cons((b1, b2), inter( a, qb))
                else:
                        return cons((b1, a2), inter( qa, b))


def inter1D(a, b):
        return simplify1D(inter(a, b))


def union( a, b):
        if None==b:
                return a
        elif None==a:
                return b
        else:
                ((a1,a2), qa) = (hd(a), tl(a))
                ((b1,b2), qb) = (hd(b), tl(b))
                assert( tof( a1) <= tof( a2))
                assert( tof( b1) <= tof( b2))
                if (tof(a1) >= tof(b1)) and (tof(a2) <= tof(b2)):
                        return cons((b1, b2), union(qa, qb))
                elif tof(b2) <= tof(a1):
                        return cons((b1, b2), union(a, qb))
                elif tof(a2) <= tof(b1):
                        return cons((a1, a2), union(qa, b))
                elif (tof(a1) <= tof(b1)) and (tof(a2) >= tof(b2)):
                        return cons((a1, a2), union(qa, qb))
                elif (tof(a1) <= tof(b1)) and (tof(a2) <= tof(b2)) and (tof(b2) >= tof(a1)):
                        return cons((a1, b2), union(qa, qb))
                elif (tof(a1) >= tof(b1)) and (tof(a2)  >= tof(b2)) and (tof(b2) >= tof(a1)):
                        return cons((a1, b2), union(qa, qb)) 
def union1D( a, b):
        return simplify1D(union(a, b))

def differ(a, b):
        if None==b:
                return a
        elif None==a:
                return None
        else:
                ((a1,a2), qa) = (hd(a), tl(a))
                ((b1,b2), qb) = (hd(b), tl(b))
                assert( tof( a1) <= tof( a2))
                assert( tof( b1) <= tof( b2))
                if (tof(a1) >= tof(b1)) and (tof(a2) <= tof(b2)):
                        btemp=cons((a2, b2), qb)
                        return differ(qa, btemp)
                elif tof(b2) <= tof(a1):
                        return differ(a, qb)
                elif tof(a2) <= tof(b1):
                        return cons((a1, a2), differ(qa, b))
                elif (tof(a1) <= tof(b1)) and (tof(a2) >= tof(b2)):
                        atemp=cons((b2, a2), qa)
                        return cons((a1, b1), differ(atemp, qb))
                elif (tof(a1) <= tof(b1)) and (tof(a2) <= tof(b2)) and (tof(b2) >= tof(a1)):
                        btemp=cons((a2, b2), qb)
                        return cons((a1, b1), differ(qa, btemp))
                elif (tof(a1) >= tof(b1)) and (tof(a2)  >= tof(b2)) and (tof(b2) >= tof(a1)):
                        atemp=cons((b2, a2), qa)
                        return differ(atemp, qb)
def differ1D(a, b):
        return simplify(differ(a, b))



"""a=vtol( [(1, 4), (6, 20), (24, 36)])
b=vtol( [(2, 7), (10, 14), (16, 22), (23, 40), (50, 100)])
print(union1D(a,  b)) """