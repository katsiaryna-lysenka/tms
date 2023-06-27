Parent1 = type('Parent1', (object,), {'a': 5})
Parent2 = type('Parent2', (object,), {'b': 10})
Child = type('Child', (Parent1, Parent2), {'c': 15})
