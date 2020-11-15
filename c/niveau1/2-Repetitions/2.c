#include <stdio.h>
#define repeat(nb) for (int _loop = 1, _max = (nb); _loop <= _max; _loop++)
int main()
{
   repeat(13)
   {
      printf("9 * 8 = 72\n");
   }
}