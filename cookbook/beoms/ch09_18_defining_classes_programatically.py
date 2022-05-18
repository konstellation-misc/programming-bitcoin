
def prepare_class(name, bases=(), kwds=None):
    """Call the __prepare__ method of the appropriate metaclass.
    Returns (metaclass, namespace, kwds) as a 3-tuple
    *metaclass* is the appropriate metaclass
    *namespace* is the prepared class namespace
    *kwds* is an updated copy of the passed in kwds argument with any
    'metaclass' entry removed. If no kwds argument is passed in, this will
    be an empty dict.
    """
    if kwds is None:
        kwds = {}
    else:
        kwds = dict(kwds) # Don't alter the provided mapping
    if 'metaclass' in kwds:
        meta = kwds.pop('metaclass')
    else:
        if bases:
            meta = type(bases[0])
        else:
            meta = type

    # SIMPLIFIED
    assert isinstance(meta, type)

    if hasattr(meta, '__prepare__'):
        ns = meta.__prepare__(name, bases, **kwds)
    else:
        ns = {}
    return meta, ns, kwds


def new_class(name, bases=(), kwds=None, exec_body=None):
    """Create a class object dynamically using the appropriate metaclass."""
    # SIMPLIFIED
    assert len(bases) == 0
    resolved_bases = bases

    meta, ns, kwds = prepare_class(name, resolved_bases, kwds)
    if exec_body is not None:
        exec_body(ns)
    if resolved_bases is not bases:
        ns['__orig_bases__'] = bases
    return meta(name, resolved_bases, ns, **kwds)


######## Manually define class

def __init__(self, name, shares, price):
    self.name = name
    self.shares = shares
    self.price = price


def cost(self):
    return self.shares * self.price

cls_dict = {
        '__init__' : __init__,
        'cost' : cost,
}

Stock = new_class('Stock', (), {}, lambda ns: ns.update(cls_dict))
