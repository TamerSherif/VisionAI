## Inspiration

We have many inspirations, although the most prominent is that one of our team members' grandmother had vision issues at an old age which caused her to not be as motivated to perform activities. We were all very determined to complete this project even with all the issues we faced. A common theme for all of us is that we are extremely passionate about health and well being. This was a big project for us, and we can't be happier that we completed it.

## What it does

A wearable for the visually impaired. Our solution consists of a camera connected to a raspberry pi (only temporarily given the provided hardware) that will be on the person. A google home mini or any Android device with the Google Assistant will be used to issue commands in order to visualize the surrounding environment. It (currently) has two modes: 

1. A brief description of the surrounding environment, giving the user more sense of what is around him/her.
2. The ability to read typed or hand written text.

Voice commands will be sent through the Google home mini or Google Assistant on the user's phone which will then fetch data from the pi camera, process the data on a cloud server with two trained models through a secure gateway and respond appropriately with speech through another tunnel and API/endpoint.


## How we built it

There are many components to our project and a large number of moving parts. We programmed the Google Home Mini as well as the Google Assistant on phones to accept certain commands and do different actions depending on the command. If the user wants the first mode (describing the environment around them) a cloud server API will be hit by the Google assistant. The cloud server will then handle that request by hitting API #1 on the PI which captures an image and returns it to the cloud server. The picture is then sent through the environment description model. This model will output values which are then sent to API #2 on the PI where Google's text to speech handler resides.
A similar process occurs with text detection but with a different neural network architecture and trained model. 

## Challenges we ran into

Our project involved a lot of new concepts from Computer vision and natural language processing to networking and secure tunnels and gateways. Setting up the communication between the devices was one of the toughest parts as we had to perform reverse tunnelling and had to learn how to handle it properly. We had some trouble with sending and receiving get and post requests with Google Cloud and services but we managed to get around it after intense documentation reading.

## Accomplishments that we're proud of

We’re proud of how well the image processing on the remote server works for text detection and the scene description and the amount of work we put in.

## What we learned

We learned a lot about IoT, Computer Vision, APIs, NLP and networking.


## What's next for VisionAI

Improving on our product by making it more portable with a better IoT device. A better low cost camera is crucial as well to make it affordable. We also intend to add other modes that interact with one another dynamically.
An example: translating signs to native language if need be.

Check our Github at: https://github.com/TamerSherif/VisionAI

