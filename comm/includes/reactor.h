#ifndef REACTOR_H
#define REACTOR_H

#include "defines.h"
#include "event.h"

struct reactor
{
    u32 fd;
    struct event *events;
};



#endif