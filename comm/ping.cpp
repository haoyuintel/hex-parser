#include <iostream>
#include <cstring>
#include <cstdlib>
#include <cstdio>
#include <cerrno>
#include <unistd.h>
#include <arpa/inet.h>
#include <netinet/ip_icmp.h>
#include <sys/types.h>
#include <sys/socket.h>
#include <netdb.h>
#include <chrono>

#define PACKET_SIZE 64

using namespace std;

unsigned short checksum(void *b, int len)
{
    unsigned short *buf = (unsigned short *)b;
    unsigned int sum = 0;
    unsigned short result;

    for (; len > 1; len -= 2)
    {
        sum += *buf++;
    }

    if (len == 1)
    {
        sum += *(unsigned char*)buf;
    }

    sum = (sum >> 16) + (sum & 0xffff);
    sum += (sum >> 16);

    result = ~sum;

    return result;
}


void send_ping(int fd, struct sockaddr_in * addr)
{
    struct icmp icmp_hdr;
    char packet[PACKET_SIZE];

    memset(&icmp_hdr, 0, sizeof(icmp_hdr));

    icmp_hdr.icmp_type = ICMP_ECHO;
    icmp_hdr.icmp_cksum = checksum(&icmp_hdr, sizeof(icmp_hdr));
    icmp_hdr.icmp_code = 0;
    icmp_hdr.icmp_hun.ih_idseq.icd_id = getpid();
    icmp_hdr.icmp_hun.ih_idseq.icd_seq = 0;

    auto start = chrono::high_resolution_clock::now();

    if(sendto(fd, packet, sizeof(packet), 0, (struct sockaddr*)addr, sizeof(*addr)) <= 0) 
    {
        perror("sendto");
        return;
    }

    struct sockaddr_in rcv_addr;
    socklen_t rcv_addr_len = sizeof(rcv_addr);
    if (recvfrom(fd, packet, sizeof(packet), 0, (struct sockaddr*)&rcv_addr, (socklen_t*)&rcv_addr_len) <= 0)
    {
        perror("recvfrom");
        return;
    }

    auto end = chrono::high_resolution_clock::now();
    auto elapsed = end - start;

    cout << "ping to: [" << addr->sin_addr.s_addr << "], successfully, use for " << elapsed.count() * 1000 << "ms" << endl;
    
}

int main(int argc, char *argv[]) 
{
    if (argc != 2)
    {
        cerr << "Usage: " << argv[0] << endl;
        return 1;
    }

    const char* ip_addr = argv[1];

    int sockfd;
    struct sockaddr_in addr;

    int sockfd = socket(AF_INET, SOCK_RAW, IPPROTO_ICMP);
    if (sockfd < 0) 
    {
        perror("socket");
        return 1;
    }

    memset(&addr, 0, sizeof(addr));
    addr.sin_family = AF_INET;
    addr.sin_addr.s_addr = inet_addr(ip_addr);

    

    close(sockfd);
    return 0;
    
}