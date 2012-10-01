python-composed
=======================================

.. image:: https://secure.travis-ci.org/msabramo/python-composed.png
   :target: http://travis-ci.org/msabramo/python-composed

Python functional composition

Example usage
-------------

.. code:: python

    # composed_example.py

    from function_composition import compose

    def plus_2(x):
        return x + 2

    def times_3(x):
        return 3 * x

    print(compose(times_3, plus_2)(1))
    print(compose(times_3, plus_2)(2))
    print(compose(times_3, plus_2)(3))


    $ python composed_example.py
    9
    12
    15
