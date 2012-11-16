//Dispatcher.cpp

/*
Description:

	Connects consumer and generator programs
*/

#include <stdlib.h>
#include <iostream>
#include<unistd.h>
#include <string.h>
#include <stdio.h>
#include <sys/wait.h>
#include <sys/types.h>


using namespace std;

int main()
{
	int pipefd[2];
	pid_t cpid;
	
	if(pipe(pipefd) == -1)
	{
		perror("pipe");
		exit(EXIT_FAILURE);
	}
	
	cpid = fork();
	if(cpid == -1)
	{
		perror("fork");
		exit(EXIT_FAILURE);
	}
	
	//If process is child, connect its output to write end of pipe
	if(cpid == 0)
	{	
		//Connect standard out to write end of the pipe
		dup2(pipefd[1], STDOUT_FILENO); 
		
		//Close the read end of the pipe
		close(pipefd[0]); 
		
		//Exec the generator
		execve("./generator", NULL, NULL);
	}
	
	//Now call fork a second time
	pid_t cpid2;
	
	cpid2 = fork();
	if(cpid2 == -1)
	{
		perror("fork");
		exit(EXIT_FAILURE);
	}
	
	//If process is child, connect its input to the read end of pipe
	if(cpid2 == 0)
	{	
		//Connect read end of pipe to standard in
		dup2(pipefd[0], STDIN_FILENO);
		
		//Close the write end of the pipe
		close(pipefd[1]);
		
		//exec the consumer
		execve("./consumer", NULL, NULL);
	}
	
	//Now sleep for one second
	sleep(1);
	
	
	//Now use kill to send SIGTERM signal to child running generator
	int worked;
	worked = kill(cpid, SIGTERM);
	if(worked  == -1)
	{
		cerr << "Kill signal wasn't sent" << endl;
		exit(EXIT_FAILURE);
	}
	
	//Wait for generator child process to terminate
	int* status = NULL;
	waitpid(cpid, status, 0);
	
	//Print message to standard error indicating child exited
	cerr << "child[" << cpid << "] exited with status " << status << endl;
	
	//Close all pipes
	close(pipefd[0]);
	close(pipefd[1]);
	
	//Now wait for the consumer process to exit
	waitpid(cpid2, status, 0);
	
	//Print message to standard error indicating child exited
	cerr << "child[" << cpid2 << "] exited with status " << status << endl;
	
	return 0;
}
		
