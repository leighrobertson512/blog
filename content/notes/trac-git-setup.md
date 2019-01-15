Title: Trac setup with GitHub
Date: 2014-08-18
Category: Notes
Tags: trac, git
Author: Wray Mills
Summary: Trac server setup with Git

This entry documents the setup for the Trac/SVN server -- using git (on github) as the primary remote repository instead of the hosted svn.

We are using a server that hosts both SVN as well as several trac instances. This server resides within our internal restricted network. We'll refer to the trac/svn server as trac-1.

Essentially, the Trac-Git setup is detailed [here](http://trac.edgewall.org/wiki/TracGit).

I went through the process of adding a git repository (as the default) to an existing Trac project. The configuration essentially points to a locally cloned git repository (local on the Trac server). And this works well, but sort of assumes that this local repository is either an integrated git remote repository (one where all developers are syncing their changes) or that itself is being synced separately. And while I can setup post-receive hooks on the repository, these won't work unless developers are pushing to this repository or someone is fetching from the integrated repository (in github in our case). So, while not the best solution, I've setup a cron job to fetch from the github repository every 15 minutes. So far this seems to work out fairly well.

Definitely open to suggestions here.

I will be setting up some post-receive hooks to enhance the integration, so I may run across a better solution.
