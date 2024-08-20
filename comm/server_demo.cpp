#include <sys/epoll.h>
#include "includes/defines.h"
#include <fcntl.h>

class server_processor
{
private:
    void init();
    void set_non_blocking(int fd);
public:
    server_processor(/* args */);
    ~server_processor();
};

server_processor::server_processor(/* args */)
{
}

server_processor::~server_processor()
{
}


server_processor::server_processor() 
{
    init();
}

void server_processor::init() 
{
    int fd = epoll_create1(EPOLL_CLOEXEC);
}

void set_non_blocking(int fd)
{
    fcntl(fd, F_GETFL, 0);
}