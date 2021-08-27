# Scam Avenger
Saransh Rakshak
srakshak@berkeley.edu


PROJECT DESCRIPTION:

Scammers primarily target the elderly and young children - two age groups who are the most likely to succumb to high-pressure scam tactics and lose hundreds if not thousands. I have personally been bombarded by calls, asking to get a 'refund for my auto insurance' or 'court order house arrest unless payment by gift card', and I can see how it can easily excite or alarm somebody who may be unaware of the scam. 

The initial call is automated, but the call back number almost always transfers to a call center in India or Nigeria. As they are spoofing for local area codes(so it doesn't show as 'scam likely') the number frequently changes, and cannot be reached after they leave a few voicemails and change to a new number.

This project will work towards calling back these numbers immediately, and talking to the scammers for as long as possible using Pydub & SpeechRecognition, pre-recorded responses in different voice accents such as an old man and a child, as well as volume and Sentiment analysis information to see the 'anger level' of the scammer. (I've always wanted to be a voice actor for TV shows so I'm having a lot of fun with the voices).

My goal is, the more time the scammers talk to pre-recordings of me, the less they can spend scamming actual people for money.


As most scammers follow a very similar script, I generally know the two main procedures they use:

1) Upon calling back the victim will be told either that they have won some sort of reward/refund- or- they will be threatened with legal action if they are unable to pay in gift cards. 

2) The scammer will proceed to persuade the victim to log onto a desktop computer or laptop and will convince the victim to remotely share access to the victim's computer.

3) The scammer will either ...

A. (Visual Scam) Ask the victim to log into bank account, and using inspect element to change the visual values of their account funds, and stating the money will be withheld without payment

B. (Visual Scam) Ask the victim to log into a bank account, where the scammer will transfer money quickly between savings and credit, giving the appearance of money loss, then stating money will be withheld without payment.

C. (Refund Scam) Scammer will run a program on the Terminal/Command line that gives the appearance of money refund taking place, and that the victim has full control of the money transfer (no actual money transfer takes place). When the victim enters the amount to be refunded, an additional 0 will be added to the input giving the appearance that the victim has transferred x10 the asked for refund from the scammers account to the victims personal account. The scammer will then desperately beg the victim to transfer the money back via gift cards, stating that the victim cannot simply transfer back the 'money' via the old command line method or a bank transfer method, and will often negotiate a smaller amount in gift cards out of desperation for getting anything. Scammer may also use the inspect element on bank account webpage to edit the appearance that money has been transferred.

D. (Refund Scam) Ask the victim to log into bank account, and using inspect element to show that scammer has sent too much money and will lose their job, and that the victim must transfer gift cards to help the scammers family survive (or any other desperate situation the scammer thinks up of).  

E. (Stolen Info Scam) Scammer will hide all files from the user's desktop, and state that the victim's comp files/ personal information/bank account/etc. will be withheld until gift card payment is given. 

F. (Legal Action Scam) Scammer will call the victim threatening . May pull up a fake webpage or inspect elements on victims bank account page stating money will be withheld without gift card payment similar to the Refund Scam, or may hide files like in the Stolen Info Scam. This is probably the most barbaric method in comparison to the others, but is still one of the most effective nonetheless. 

4) Scammer will then ask the victim to drive to a nearby store to purchase gift cards, and will stay on the phone with the victim throughout the process (I will play fake driving sounds and extend the drive time to increase conversation time).

5) Once the victim returns home, the scammer will ask the victim to reopen their desktop and continue sharing access to the victim's computer. Scammers will tell the victim to open up Notepad or other text writing app to type gift card numbers into. Scammer will then redeem gift card numbers into his or her own account, completing the scam. Most scammers will hang up right after getting and using the gift card numbers.

6) Few scammers will stay on the phone and give the appearance of keeping 'honest' with their agreement by refreshing the victim's bank account page (which they had edited using inspect element) thus returning the actual values in the victim's bank account, or will retransfer the victim's computer files which the scammer had hidden in a different folder, back to desktop.




By using NLTK for sentiment analysis (mainly VADER) & volume, I can extend the stalling conversation more precisely- complying with the scammer if he seems too angry or about to hang up -or- avoiding instructions from the scammer & stalling when they are in a calmer mood, further agitating them and driving up the call time.

I am planning on using multiple google numbers and essentially waiting for scam calls for call back numbers (I was hoping you might know of a more efficient process for scam number data collection). I am also still in the works of creating a program that will listen to the call or voicemail, verify it's a scam via keywords and the presence of an automated voice, and pull both the call back number and information about the type of scam.

I'm also utilizing previously recorded scam calls on youtube, there are a few famous YouTubers (such as KitBoga and Jim Browning) who frequently call back scammers and mess with them (I highly recommend checking Jim Browning out; he is an amazing person). I am taking YouTube's auto-generated subtitles from these channels and grouping common trigger words that are used by the scammer(from scammers script or general template), to train the proper pre-recorded responses from the same voice actor. 

Additionally, I will set up a virtual machine, so that I can give the appearance of complying with the scammers instructions while they run the scam. I am also in the process of creating a fake web page for a bank to log into while talking to the scammer. 



######
## FIGURE SHIT OUT ABOUT SECURITITTY
#


