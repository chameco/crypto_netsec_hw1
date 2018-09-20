This is the README.MD for Crypotgraphy and Network Security 1 for HW1 in Fall '18 taught by Professor Bulent Yener and written by Samad Farooqui (faroos3@rpi.edu). 

I'm going to get started with this homework! It is to implement a TOY DES to transpot one file to another (in our case, a 8 bit one). According to the Professor, we have to implement slides 72, 73, and 74 in lecture 1.2. 

The very first thing is to take the input and convert it into binary. As for input, I am just going to take a string of plaintext for now. I guess we can provide any number of bits, convert to binary, break it up into 8 bit pieces, stick them in the encryptor, combine them, and that's the ciphertext? I'll ask in office hours tomorrow. 

I used this in order to convert my input into binary: https://stackoverflow.com/questions/7396849/convert-binary-to-ascii-and-vice-versa. It's returning it in a string, I may have to go through and change every bit to an int while actually doing calculations in order to do the math. 

First, we need to do the initial permutation of the 8-bit plain text. I could also be implementing the part in the middle for the key. What is the initial key though? 

I went to office hours! The initial key is user input according to mentor John. I also get how to bitwise operate using python strings now, so I'll be using that. 

The result of the leftshift on the 5-bit pieces also needs to be 5-bit, I need to account for that. I was doing it in 8 bits at first.


Honestly, some of the functions for generating the cipher are a lot faster to write now that the key generation code is finished. 

I got my sboxes working! I'm oddly proud of them.

I think I got the decryption and encryption, but it's not decrypting the right way. Now I need to figure out what's wrong.

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