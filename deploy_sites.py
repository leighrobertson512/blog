import os

branches_raw = os.system('git branch -a').split("\n")

for branch in branches_raw[1:]:
  branch = branch.lstrip('  origin/')
  os.system("make github DOMAIN=" + branch "+.techemstudios.com")
  os.system("git remote remove origin")
  os.system("git remote add origin https://" + os.environ('GH_TOKEN') + "@github.com/techemstudios/" + branch)
  os.system("git push -f origin gh-pages")
