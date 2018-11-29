==========================
Cards Against Humanity Bot
==========================

This is a Discord bot to create cards against humanity games. 

I'm not affiliated with the official Cards Against Humanity game or the web app in any way. Don't sue me.


Usage
~~~~~
You'll need python3 and pip::

    pip3 install selenium discord --user

    # install the firefox browser driver thing

    python3 main.py


Bot Usage
~~~~~~~~~
``!newgame`` creates a new game. Please wait up to 3 or four seconds for the bot to make the game. 
The CAH web app is really slow and also I don't want to send too many requests per second and break stuff.
Also all the button presses and stuff have to be handled in an emulated browser which is really slow.
Just an endpoint I could ping would be great.

The bot will then reply with something like this:

    **Cards Against Humanity**
    Game Created! Join and add any reaction to start game
    *password*
    ``h``

Click the link (the title) and input the password to join the game. Once enough people have joined, click
the 👍 icon under the message to start the game. The bot will attempt to start a game, and then disconnect
and close the virtual browser session to preserve my prescious server space.