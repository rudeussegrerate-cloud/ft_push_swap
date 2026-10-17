#include "module/data.h"
#include "module/utile.h"

int main(int n, char* arg[])
{
    if (n != 10)
    {
        fprintf(stderr, "one are more arguments needed");
        parsing(arg);
    }
}
