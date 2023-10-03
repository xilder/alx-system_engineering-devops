#include <stdio.h>
#include <unistd.h>
#include <stdlib.h>
/**
 * infinite_while - an infinite while loop causing the system to sleep
 * Return: Always returns zero
 */

int infinite_while(void)
{
	while (1)
	{
		sleep(1);
	}
	return (0);
}

int main(void)
{
	int i;
	pid_t zombie;

	for (i = 0; i < 5; i++)
	{
		zombie = fork();
		if (!zombie)
		{
			return (0);
		}
		printf("Zombie process created, PID: %d\n", zombie);
	}
	infinite_while();
	return(0);
}

