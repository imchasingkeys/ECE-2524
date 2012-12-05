#include "Process.h"

/* Initialize the process, create input/output pipes */
Process::Process(const vector<string> &args)
{
	if(pipe(writepipe) == -1)
	{
		cout << "pipe error" << endl;
		//some kind of error checking
	}
	if(pipe(readpipe) == -1)
	{
		cout << "pipe error" << endl;
		//some kind of error checking
	}	
	
	//Initialize the process
	m_pid = fork();
	
	if(m_pid == -1)
	{
		//some kind of error for forking
		cout << "Fork error" << endl;
	}
	
	//If process is child, connect pipes
	if(m_pid == 0)
	{	
		//Close standard in and make writepipe act as standard in
		//dup2(writepipe[0], STDIN_FILENO);
		close(0);
		dup(writepipe[0]);
		close(writepipe[0]);
		
		
		//Connect write end of readpipe to standard out
		close(1);
		dup(readpipe[1]);
		close(readpipe[1]);
		
		//Close write end of writepipe
		close(writepipe[1]);
		//Close read end of readpipe
		close(readpipe[0]);
		
		char *buf;
		buf = new char [args[0].size() + 1];
		strcpy(buf, args[0].c_str());
		
		//Exec consumer
		execve(buf, NULL, NULL);
	}	
}

/* Close any open file streams or file descriptors,
   insure that the child has terminated */
Process::~Process()
{
	close(writepipe[0]);	
	close(writepipe[1]);	
	close(readpipe[0]);	
	close(readpipe[1]);

	fclose(m_pread);	
}

/* write a string to the child process */
void Process::write(const string& mystring)
{
	char *buf;
	buf = new char [mystring.size() + 1];
	strcpy(buf, mystring.c_str());
	
	//Close read end of writepipe
	close(writepipe[0]);
	
	ssize_t thisSize = ::write(writepipe[1], buf, sizeof(buf));
	
	if(thisSize == -1)
	{
		//cout << "Write error" << endl;
		printf( "Write error: %s\n", strerror( errno ) );
	}
}

/* read a full line from the child process,
   if no line is available, block until one becomes available */
string Process::readline()
{
	char *line = NULL;
	size_t len = 0;
	ssize_t read;
	
	//Close the write end of the pipe
	close(readpipe[1]);
	
	m_pread = fdopen(readpipe[0], "r");
	
	if(m_pread == NULL)
	{
		printf( "fdopen fail: %s\n", strerror(errno));
	}
	
	read = getline(&line, &len, m_pread);
	
	if(read == -1)
	{
		printf( "Read error: %s\n", strerror(errno));
	}
	
	string lineString = line;
	
	free(line);
	
	return lineString;	
}
