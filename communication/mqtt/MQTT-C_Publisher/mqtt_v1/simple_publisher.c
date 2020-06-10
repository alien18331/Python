
/**
 * @file
 * A simple program to that publishes the current time whenever ENTER is pressed. 
 */
#include <unistd.h>
#include <stdlib.h>
#include <stdio.h>

#include "mqtt.h"
#include "posix_sockets.h"

/**
 * @brief The client's refresher. This function triggers back-end routines to 
 *        handle ingress/egress traffic to the broker.
 * 
 * @note All this function needs to do is call \ref __mqtt_recv and 
 *       \ref __mqtt_send every so often. I've picked 100 ms meaning that 
 *       client ingress/egress traffic will be handled every 100 ms.
 */
void* client_refresher(void* client);


/**
 * A simple program to that publishes the current time whenever ENTER is pressed. 
 */
int main(int argc, const char *argv[]) 
{
    const char* addr = "127.0.0.1";
    const char* port = "1883";
    const char* topic = "STATUS";

    /* open the non-blocking TCP socket (connecting to the broker) */
    int sockfd = open_nb_socket(addr, port);

    /* setup a client */
    struct mqtt_client client;
    uint8_t sendbuf[2048]; /* sendbuf should be large enough to hold multiple whole mqtt messages */
    uint8_t recvbuf[1024]; /* recvbuf should be large enough any whole mqtt message expected to be received */
    mqtt_init(&client, sockfd, sendbuf, sizeof(sendbuf), recvbuf, sizeof(recvbuf));
    
    /* Create an anonymous session */
    const char* client_id = NULL;
    
    /* Ensure we have a clean session */
    uint8_t connect_flags = MQTT_CONNECT_CLEAN_SESSION;
    
    /* Send connection request to the broker. */
    mqtt_connect(&client, client_id, NULL, NULL, 0, NULL, NULL, connect_flags, 400);

    /* start a thread to refresh the client (handle egress and ingree client traffic) */
    pthread_t client_daemon;
    pthread_create(&client_daemon, NULL, client_refresher, &client);
    
    /* start publishing the time */
    printf("%s is ready to begin publishing the time.\n", argv[0]);
    printf("Press ENTER to publish the current time.\n");
    printf("Press CTRL-D (or any other key) to exit.\n\n");
    while(fgetc(stdin) == '\n') {
        /* get the current time */
        time_t timer;
        time(&timer);
        struct tm* tm_info = localtime(&timer);
        char timebuf[26];
        strftime(timebuf, 26, "%Y-%m-%d %H:%M:%S", tm_info);

        /* print a message */
        char application_message[256];
        snprintf(application_message, sizeof(application_message), "The time is %s", timebuf);
        printf("%s published : \"%s\"", argv[0], application_message);

        /* publish the time */
        mqtt_publish(&client, topic, application_message, strlen(application_message) + 1, MQTT_PUBLISH_QOS_0);

    }   

    /* disconnect */
    printf("\n%s disconnecting from %s\n", argv[0], addr);
    sleep(1);
}


void* client_refresher(void* client)
{
    while(1) 
    {
        mqtt_sync((struct mqtt_client*) client);
        usleep(100000U);
    }
    return NULL;
}
