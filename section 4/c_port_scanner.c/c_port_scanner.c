#include <stdio.h>
#include <string.h>
#include <arpa/inet.h>
#include <unistd.h>

// Function to scan a single port
void scan_port(int port) {
    int sock;
    struct sockaddr_in target;

    // Create socket
    sock = socket(AF_INET, SOCK_STREAM, 0);

    if (sock < 0) {
        printf("Socket creation failed\n");
        return;
    }

    // Configure target
    target.sin_family = AF_INET;
    target.sin_port = htons(port);
    target.sin_addr.s_addr = inet_addr("127.0.0.1");

    // Try to connect
    if (connect(sock, (struct sockaddr*)&target, sizeof(target)) == 0) {
        printf("Port %d: OPEN\n", port);
    } else {
        printf("Port %d: CLOSED\n", port);
    }

    close(sock);
}

// Main function
int main() {
    int ports[] = {22, 80, 443, 3306};

    printf("Scanning localhost (127.0.0.1)...\n\n");

    for (int i = 0; i < 4; i++) {
        scan_port(ports[i]);
    }

    return 0;
}
