#include "/usr/include/python3.4/Python.h"
#include <stdio.h>

void print_hexn(const char *str, int n)
{
	int p = 0;

	for (; p < n - 1; ++p)
		printf("%02x ", (unsigned char) str[p]);

	printf("%02x", str[p]);
}
