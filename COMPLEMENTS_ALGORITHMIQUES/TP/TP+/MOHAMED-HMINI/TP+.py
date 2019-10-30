#!/usr/bin/env python
# coding: utf-8

# ## EXERCICE 1/2:

# In[ ]:


used_combs = []

def not_used(comb, used_combs):
    return not(comb in used_combs)   
    pass

def roll_dice(n, nbd, comb):
    
    new_comb = comb.copy()
    sorted_new_comb = sorted(new_comb)
    _not_used = not_used(sorted_new_comb, used_combs)

    if not _not_used :
        return 0
    
    used_combs.append(sorted_new_comb)    
    total_sum = sum(new_comb)

    s = 1 if total_sum == n else 0    
    
    if s == 0:
        for i in range(nbd):
            if comb[i] < 6:
                new_comb[i] += 1
                s += roll_dice(n, nbd, new_comb)
            
            
    return s
    
    pass

if __name__ == "__main__":
    n, nbd = int(input("LOOK FOR NUMBER : ")), int(input("NUMBER OF DICES : "))
    len_slt_space = roll_dice(n, nbd, [1]*nbd)
    print("LENGTH OF THE SOLUTION SPACE : " + str(len_slt_space))
    #print("SOLUTION SPACE : " + str(combs))


# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:




