Title: Web App Camp
Date: 2014-09-07
Category: Notes
Tags: web, html
Author: Wray Mills
Summary: Camp notes for students

# Web Camp Sites Update

Most sites are up. Please watch your email -- I will send you an email when your site is ready. I do apologize for the delay, but we are spending some time doing additional customizations for each site. Also, in previous emails, I told you all to access the site using the username I put on the whiteboard the last day of camp. Instead, please use the username 'ec2-user' (referenced below). 

# Maintaining your site

I'll send you an email with your specific instructions. I am adding basic authentication to most sites (most everyone asked for it), so in that email will be a separate password for your site. Your login will be an "administrative" login -- other users may register, but they will be restricted on what they can do on your site. Once your site is up, you can maintain your site by connecting to the server like we did in class OR you can install ruby and ruby on rails on your own computer. Later, I'll include a brief overview of how to work on your own computer and then copy the files to the server. For now, you can use the server I have setup.

# Editing your files
If you have Koder installed on your tablet, you can edit files just like you did in class. You will need to create a new remote SFTP project where the username is the name of your site and the username/password is what I wrote on the whiteboard. Your project will be in the same directory location it was for class (e.g. /webappcamp/<your_app\>).

If you don't have Koder or want to use your computer, you can use [bbedit](http://www.barebones.com/products/bbedit/) on the Mac or use [WinSCP with Notepad++](http://www.thetechrepo.com/main-articles/542.html). Really, with WinSCP, you can use whatever editor you may already use.

# Accessing the console
If you have iSSH installed on your tablet, you can connect to the server using the same username/password I wrote on the whiteboard. On Windows, you can use [putty.exe](http://www.putty.org) to access the server and on Mac you can use the terminal with this command:

~~~~
ssh -l ec2-user <your_app>.techemstudios.com
~~~~

There are essentially two things you will need the access to do:

After you make changes, to reload your applicaiton and see the changes, you need to:

~~~~
cd /webappcamp/<your_app>
bundle exec rake assets:precompile
touch tmp/restart.txt
~~~~

If your site isn't working, you may want to review the application logfile (assume you are still in your app directory -- first command above):

~~~~
tail -500 log/production.log
~~~~


# An example of how to make changes

A student had the typical setup we created in camp: The main "articles" with the ability to "post" comments on an article. So, they have "articles" and "posts". He noted that when viewing a particular posted comment on an article that page has a link at the bottom of the page called "back". And when we generated the scaffold code, it assumed "back" from a post should take you back to the lists of posts. Well, in our case, we don't want that. We want "back" to go to the list of articles (really the home page in our case). So, we needed to go in and modify that link. Here is what we did:

 * Use a remote editor to open up the file /webappcamp/<your_app>/app/views/posts/show.html.erb
 * Change the line of code where it creates the back link to use "articles_path" instead of "posts_path".
 * Save the change.
 * Access the console as described above: enter the 3 unix commands.
 * Refresh your browser viewing the page and voila! Your change is there.

Please feel free to continue to comment and/or send me email if you have more questions. I'm very happy to help you all maintain your sites and work with you all to make it easier. In other words, now that you know what the actual unix commands are to reloaded your app on the EC2 user, I can provide you all with a simpler way to execute that in one command from your desktop or laptop. I do want you all to understand what is going on before we build out some of that automagic.



Some sites/apps we visited/used by day:

# Monday
  * [w3schools.com](http://www.w3schools.com/html/tryit.asp?filename=tryhtml_intro)
  * [koder](http://www.koderapp.com)


#
# Tuesday
  * [iSSH](http://www.zinger-soft.com/iSSH_features.html)
  * [Ruby](https://www.ruby-lang.org/en/)
  * [Ruby on Rails](http://rubyonrails.org)


#
# Wednesday
  * [Ruby on Rails tutorial (a blog)](http://guides.rubyonrails.org/getting_started.html)


#
# Thursday
  * [Ruby on Rails tutorial (creating a relation)](http://guides.rubyonrails.org/getting_started.html#adding-a-second-model)
  * [sorcery (authentication)](https://github.com/NoamB/sorcery)

