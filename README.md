This is my first crack at posting on GitHub, so let me know if I'm missing anything!

This project finds 5 5-letter words which have 25 different letters between them. My original goal was to write a program that could solve the problem in under 50 minutes. On my current machine, the code runs in about 4 minutes.

Other strategies for further optimization in the future would be reordering of the original list of words to place rare letters before common ones, removing aneagrams from the original list, and implementing a faster comparison function like bitwise AND.

Let me know any further comments you may have on the project and how it works!



Note: The only required library is the english-words library. This can be bypassed by replacing the web2lower variable with another list of any enlgish words not containing uppercase or non-letter characters.
