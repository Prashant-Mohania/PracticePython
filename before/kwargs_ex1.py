def func(name, **kwargs):
    if kwargs.get('reverse_str') == True:
        return [names[::-1].title() for names in name]
    else:
        return [names.title() for names in name]
l = ['prashant','kirti']
print(func(l,reverse_str = True))
print(func(l))