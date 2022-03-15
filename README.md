Very simple Caesar Cipher encryption/decryption program.

Created while working on some challenges and while I was going to a website to solve these I thought about how I would write my own, and so here we are.

The code is documented to explain function arguments, althought I can't stress enough how simple the functionality is. 

1. Generate Cipher Key
   - Generates the actual letter cipher based on a numerical input. 26 is the middle of the canvas. In a traditional sense of a caesar cipher, the key is notated as +1 or -3, etc.
     A +1 would take 27 as the numerical argument. a -3 would take 23 as the numerical argument. Even though this isn't the normal way to express this, I like the simplicity of it.
     It's simple to translate and I may get around to it.

2. Encrypt Text
    - Takes a string of text and a key. Returns encrypted text. Not good at handling uppercase characters. I may get around to it.

3. Decrypt Text
    - Takes a string of encrypted text and a key. Returns decrypted text. Also not good at handling uppercase characters. Again I may get around to it.

4. Bruteforce Decrypt Text
    - Takes a string of encrypted text as the only argument. Decrypts the text 26 times with every possible key. Outputs all 26 decryptions. Again not good at uppercase.s
