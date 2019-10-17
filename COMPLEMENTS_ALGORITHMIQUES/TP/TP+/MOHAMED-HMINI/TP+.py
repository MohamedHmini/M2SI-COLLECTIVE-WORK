#!/usr/bin/env python
# coding: utf-8

# ## EXERCICE 1/2:

# In[7]:


def not_used(comb, used_combs):
    
    try:
        used_combs.index(sorted(comb))
        return False
    except:
        return True
        pass
    
    pass

def roll_dice(n, nbd, comb, used_combs = []):
    
    new_comb = comb.copy()
    _not_used = not_used(new_comb, used_combs)
    total_sum = sum(new_comb)
    if total_sum == n and _not_used:
        used_combs.append(sorted(new_comb))
        s = 1
        pass
    else:
        s = 0
        pass
    
    
    if s == 0:
        for i in range(nbd):
            if comb[i] < 6:
                new_comb[i] += 1
                s += roll_dice(n, nbd, new_comb, used_combs)[0]
            
            
    return s,used_combs
    
    pass


n, nbd = int(input("LOOK FOR NUMBER : ")), int(input("NUMBER OF DICES : "))
len_slt_space, combs = roll_dice(n, nbd, [1]*nbd)
print("LENGTH OF THE SOLUTION SPACE : " + str(len_slt_space))
print("SOLUTION SPACE : " + str(combs))
