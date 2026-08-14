def flick_switch(lst):
    flick_bool = True
    r_lst = []
    for el in lst:
        if el == "flick":
            if flick_bool:
                flick_bool = False
            else:
                flick_bool = True
        r_lst.append(flick_bool)       
    return r_lst