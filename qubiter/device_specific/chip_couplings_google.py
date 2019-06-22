

# from cirq/google/known_devices.py
# Positions with - are empty.
# Letters at row, col = (r, c) are connected
# to letters with
# (r+1, c),
# (r-1, c),
# (r, c+1),
# (r, c-1).


BRISTLECONE_GRID = \
"""
-----AB-----
----ABCD----
---ABCDEF---
--ABCDEFGH--
-ABCDEFGHIJ-
ABCDEFGHIJKL
-CDEFGHIJKL-
--EFGHIJKL--
---GHIJKL---
----IJKL----
-----KL-----
"""

"""
>>> import cirq
>>> print(cirq.google.Bristlecone)
                                        
                                             (0, 5)....(0, 6)
                                    (1, 4)...(1, 5)....(1, 6)....(1, 7)
                           (2, 3)...(2, 4)...(2, 5)....(2, 6)....(2, 7)...(2, 8)     
                  (3, 2)...(3, 3)...(3, 4)...(3, 5)....(3, 6)....(3, 7)...(3, 8)...(3, 9)
         (4, 1)...(4, 2)...(4, 3)...(4, 4)...(4, 5)....(4, 6)....(4, 7)...(4, 8)...(4, 9)...(4, 10)
(5, 0)...(5, 1)...(5, 2)...(5, 3)...(5, 4)...(5, 5)....(5, 6)....(5, 7)...(5, 8)...(5, 9)...(5, 10)...(5, 11)
         (6, 1)...(6, 2)...(6, 3)...(6, 4)...(6, 5)....(6, 6)....(6, 7)...(6, 8)...(6, 9)...(6, 10)
                  (7, 2)...(7, 3)...(7, 4)...(7, 5)....(7, 6)....(7, 7)...(7, 8)...(7, 9)
                           (8, 3)...(8, 4)...(8, 5)....(8, 6)....(8, 7)...(8, 8)
                                    (9, 4)...(9, 5)....(9, 6)....(9, 7)
                                             (10, 5)...(10, 6)
"""
