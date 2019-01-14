Title: Craft of Minecraft (Winter 2015)
Date: 2015-03-16
Category: Classes
Tags: minecraft, python, bukkit
Author: Wray
Summary: The promised blog page that goes along with the winter Craft of Minecraft

### Minecraft PE Server

We started the class discussing servers and clients and the networking involved to make games like minecraft work. We setup a minecraft PE server (that is actually still running). If you are interested in running a PE server for your own home network, you can find a fairly stable version here:

[Get PocketMine](http://www.pocketmine.net)

The instructions are relatively straightforward and this server acts similar to the PC server version in that it will create several configuration files after the first time the server is run. However, please keep in mind the following pros and cons when it comes to running this server vs. simply sharing your PE world with others on your network (essentially Minecraft PE can run as a "server" for others on your network).

* Good
    * PocketMine will support more players (especially if you have an i7 machine with 8+ GB ram).
    * PocketMine will allow op commands at the console so you have more control over your world.
    * Just like the PC edition, PocketMine has access controls (whitelist) to constrain access.
    * Just like the PC edition, PocketMine will support some plugins.
    * If you expose your PocketMine server to the Internet (port forward), users outside your network can join your server.

* Bad
    * PocketMine is not as stable and can get glitchy and force reconnects, etc.
    * PocketMine does require a separate laptop/pc running it on the network so its not as easy to create an "ad-hoc" world.
    * PocketMine is not quite as up-to-date as Minecraft PE and certainly behind the PC edition.

Another [nice article](http://www.howtogeek.com/202961/how-to-run-a-local-minecraft-pe-server-for-fun-and-persistent-world-building/) to read with information on PocketMine and configuring it.

So, the other thing we covered in class is how you can actually get another app that works with Apple's Game Center that allows you to expose your PocketMine PE world outside of your network. This is actually pretty cool, but a little tricky to setup. Furthermore, there are so many people just waiting for new PE worlds to be exposed that your world can quickly be invaded by TNT wielding and lava toting fire starters! The app's site does an ok job explaining how to set things up, but feel free to shoot me an email or comment here if you have some issues:

[Multiplayer for Minecraft PE](https://itunes.apple.com/us/app/multiplayer-for-minecraft-pe/id609704981?mt=8)

### Minecraft PE powered rails and redstone

We also spent some time on minecraft PE showing how one can use powered rails and build binary logic gates! There is a [good YouTube resource](https://www.youtube.com/watch?v=bLK58PRzaSU) for doing that.

We didn't get to doing this in PC redstone, but I would encourage that you all try this at home (and let us know how it goes). In fact, once we move our newer server (and the world they played in the last day), it would be awesome if some of the students could build some logic gates in that world to share with other students. We will definitely give them credit for providing instructional materials!!

![Winter 2015 Minecraft class]({filename}/images/minecraft-class1.jpg)

### Minecraft Bukkit server and Python

So, we also did quite a bit with a version of minecraft known as Bukkit. This is the same version that runs on the raspberry pi and it worked well for the group we had in our class -- allowing us to make server modifications using Python. Here are roughly the steps we went through (and the students should mostly remember how this goes).

* Go to the "AdventuresInMinecraft" directory
* Run the StartBukkit command
* Launch Minecraft
* Make sure your Minecraft profile is using version 1.6.4 (yes, bukkit is not near the latest version)
* Choose multiplayer, direct connect, with a host of "localhost"
* Launch the Python 2.* "IDLE" application
* Open up any of the modules we created in the "AdventuresInMinecraft/MyAdventures" directory
* The IDLE application has the option to "Run Module" which will run the python code that connects to your running bukkit server and whose results you should see in your running Minecraft application.
* Remember, building large structures (like a sphere of size 100 or greater) will take some time. Build this out of TNT and light and you will likely bog down your server for an hour or so!
* If your world is lagging due to some large build, you can go into "AdventuresInMinecraft/Bukkit" and delete your world! Of course, you are *deleting your world*, so test your builds before you build in a world you want to keep.

![Winter 2015 Minecraft class]({filename}/images/minecraft-class2.jpg)

### Thank you

Thanks again. I probably learned more than you all did and I appreciate that. Please comment here or send me email if you need anything else. For those of you who were using our laptops and want to do the Bukkit server on your own, let me know if you need more detailed instructions and I'll work with you all. Check out our Spring session and Summer Camps coming up. We are combining raspberry pi and minecraft for some fun projects -- I know you all would do great in these classes and I'm happy to talk to you in advance if you have specific objectives in mind for your next minecraft/pi projects.





 
