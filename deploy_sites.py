import subprocess,os

proc = subprocess.Popen('/usr/bin/git branch -a', stdout=subprocess.PIPE)
braches_raw = proc.stdout.read().split('\n')


for branch in branches_raw[1:]:
  branch = branch.lstrip("  origin/")
  print("Branch: " + branch)
  
  print    ("make github DOMAIN=" + branch + ".techemstudios.com")
  os.system("make github DOMAIN=" + branch + ".techemstudios.com")
  
  print    ("git remote remove origin")
  os.system("git remote remove origin")
  
  print    ("git remote add origin https://" + os.environ("GH_TOKEN") + "@github.com/techemstudios/" + branch)
  os.system("git remote add origin https://" + os.environ("GH_TOKEN") + "@github.com/techemstudios/" + branch)
  
  os.system("git push -f origin gh-pages")
