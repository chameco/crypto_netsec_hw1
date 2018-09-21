This is the README.MD for Crypotgraphy and Network Security 1 for HW1 in Fall '18 taught by Professor Bulent Yener and written by Samad Farooqui (faroos3@rpi.edu). 

Usage for server: python3 server.py "message.txt" 1000000001
Usage for client: python3 client.py  output.txt 1000000001

To close the server, use Ctrl C. Otherwise, it will just keep listening, connecting, and sending out encrypted messages.

The last part can be any 10-bit key, as long as it is the same. 

I'm going to get started with this homework! It is to implement a TOY DES to transpot one file to another (in our case, a 8 bit one). According to the Professor, we have to implement slides 72, 73, and 74 in lecture 1.2. 

The very first thing is to take the input and convert it into binary. As for input, I am just going to take a string of plaintext for now. I guess we can provide any number of bits, convert to binary, break it up into 8 bit pieces, stick them in the encryptor, combine them, and that's the ciphertext? I'll ask in office hours tomorrow. 

I used stack overflow to look into how I can convert strings to binary and then binary back to those strings. It's returning it in a string, I may have to go through and change every bit to an int while actually doing calculations in order to do the math. 

First, we need to do the initial permutation of the 8-bit plain text. I could also be implementing the part in the middle for the key. What is the initial key though? 

I went to office hours! The initial key is user input according to mentor John. I also get how to bitwise operate using python strings now, so I'll be using that. 

The result of the leftshift on the 5-bit pieces also needs to be 5-bit, I need to account for that. I was doing it in 8 bits at first.


Honestly, some of the functions for generating the cipher are a lot faster to write now that the key generation code is finished. 

I got my sboxes working! I'm oddly proud of them.

I think I got the decryption and encryption, but it's not decrypting the right way. Now I need to figure out what's wrong. I'm going to try adding proper format strings to everywhere that returns a binary. 

Well, I tried that and it did not fix my problem. I'm going to take a look at the Feistel Cycle, Sboxes, and any potential off-by-one errors.

I got it working!! The problem was in my Feistel, like I was suspecting. Made sure that was good. 

Now to work on the networking part. Basically, the server is going to take a file as user input, then read it, decrypt it, and send it if someone connects. Then, a client can connect to an open port, take it, decrypt it, and output the message to the console and write it to a file. Both will also take the key as input because I trust my users with input (for better or for worse). 

I'm going to use a TCP connection. The connection would be secure. 

If you'd like to modify the message being sent, change it in message.txt and make sure to adjust the recv and send calls in client.py and server.py accordingly, otherwise errors may occur. 

Overall, this homework was very cool! It took a little bit to figure out the Sboxes and the Feistel Cycle bug I was having, but it eventually just came down to following the slides. 

In detail, the program is composed of three main parts, a client, a server, and the toy_des. The server binds localhost:9095 to be a TCP server, so ensure that the port is free. It takes a message and encrypts it, and sends it out to anyone listening after connecting. The client will listen for connections on localhost:9095 and can recieve messages. After it is done receiving the message, it decrypts it, outputs it, and writes it to a file. The encryption and decryption parts are written in toy_des.py. That file implements the DES that we were told from the slides. A lot of the functions and features are written into their own sections. The biggest function is the F_function function. Features like S-boxes, permutations, and the splitting of bits are broken up. Then, the encryption and decryption algorithms just string everything together. Key generation is handled the same way, with features being a bunch of tiny functions and then strung together in the end.

Issues with this work ended up being the bugs I encountered on the way, and not knowing what to do at first. I was not sure how S-boxes worked, but went to office hours and managed to get help. I also had issues with my Feistel Cycle, as documented above, and managed to get that to work by re-visting the slides and double checking what had to be done. 

If I were to do this work again, I would start earlier. I would also go to office hours sooner, and will be taking advantage of that resource throughout the course of the class. 

Again, this homework was fun once I knew what I was doing. Thanks for the help! 

Eliyah also said to put ascii art. Here's one of my favorites. 

            ▄              ▄
                  ▌▒█           ▄▀▒▌
                  ▌▒▒█        ▄▀▒▒▒▐
                 ▐▄▀▒▒▀▀▀▀▄▄▄▀▒▒▒▒▒▐
               ▄▄▀▒░▒▒▒▒▒▒▒▒▒█▒▒▄█▒▐
             ▄▀▒▒▒░░░▒▒▒░░░▒▒▒▀██▀▒▌
            ▐▒▒▒▄▄▒▒▒▒░░░▒▒▒▒▒▒▒▀▄▒▒▌
            ▌░░▌█▀▒▒▒▒▒▄▀█▄▒▒▒▒▒▒▒█▒▐
           ▐░░░▒▒▒▒▒▒▒▒▌██▀▒▒░░░▒▒▒▀▄▌
           ▌░▒▄██▄▒▒▒▒▒▒▒▒▒░░░░░░▒▒▒▒▌
          ▌▒▀▐▄█▄█▌▄░▀▒▒░░░░░░░░░░▒▒▒▐
          ▐▒▒▐▀▐▀▒░▄▄▒▄▒▒▒▒▒▒░▒░▒░▒▒▒▒▌
          ▐▒▒▒▀▀▄▄▒▒▒▄▒▒▒▒▒▒▒▒░▒░▒░▒▒▐
           ▌▒▒▒▒▒▒▀▀▀▒▒▒▒▒▒░▒░▒░▒░▒▒▒▌
           ▐▒▒▒▒▒▒▒▒▒▒▒▒▒▒░▒░▒░▒▒▄▒▒▐
            ▀▄▒▒▒▒▒▒▒▒▒▒▒░▒░▒░▒▄▒▒▒▒▌
              ▀▄▒▒▒▒▒▒▒▒▒▒▄▄▄▀▒▒▒▒▄▀
                ▀▄▄▄▄▄▄▀▀▀▒▒▒▒▒▄▄▀
                   ▒▒▒▒▒▒▒▒▒▒▀▀