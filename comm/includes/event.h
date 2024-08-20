#ifndef EVENT_H
#define EVENT_H

#include "defines.h"

struct event
{
    u32 fd;
    u32 event_type;
    void* args;
    u32 callback(u32 fd, u32 event_type, void* args);
};


#endif