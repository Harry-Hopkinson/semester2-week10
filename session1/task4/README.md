# Task 4

`pgm_tools.c` contains the PGM image manipulation program seen in earlier
weeks of the module.

1. Compile the program with minimal optimization, timing how long this takes:

       time gcc -O0 pgm_tools.c

   Make a note of the results.

2. Check the size in bytes of the executable. You can do this with

       wc -c a.out

3. Repeat Steps 1 & 2 above, using `-O3` instead of `-O0`. You should find
   that compilation takes longer and the resulting executable is slightly
   larger.

4. Repeat Steps 1 & 2, using `-Os` instead of `-O0`, to optimize for space.
   You should see that the resulting executable is significantly smaller
   than before.
