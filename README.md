# cs182-f17-psets

Welcome to CS182! This repository will house your homework assignments.

If you are reading this, the name of the repository should be cs182-f17-psets-YourGithubID. If that's what you see, you should already be logged into your Github account and have your own private repository (this one) for your homeworks. You're good to read on.

If you don't see your Github ID at the end of the repository name, you need to find the link on [Canvas](https://canvas.harvard.edu/courses/29895) to create your own private repository.

If you don't know what any of this means, contact [Brian Plancher](mailto:brian_plancher@g.harvard.edu), who administers the Github Classroom. These instructions only apply to your private repo.

## How this repository works
This repository is a copy of a "seed" repository maintained by the TFs. Right now there should be six folders in this repository. Throughout this semester, your TFs will add assignments to the seed repository, and you will be responsible for copying them into your repository (using "fetch" and "merge", in git-speak). Assuming you've already cloned your repository locally, you can get the new files by:
```
git remote add seed_repo https://github.com/Harvard-CS182/cs182-f17-psets.git # only needs to be done once
git fetch seed_repo
git merge seed_repo/master -m "Fetched new assignment"
```
These commands (1) tell your local git repository where the seed repo is (and calls it "seed_repo"), (2) gets that repo from github.com, and (3) merges it with your local files. A final, fourth, step would be to push to your remote repository so it shows up on the web and your TFs can see it.

In fact, try that now to make sure you don't get any errors, and contact us via [Piazza](https://piazza.com/class/j6mi3zytbdh4h3) if you do.

## Problem set rules
Each problem set will consist of a written and programming portion. You are welcome to work alone or in pairs on the programming portion, but *the written portion must be done individually*. If you worked with someone for the programming portion, you must identify each other in your submitted materials. 

## Problem set submission
For each assignment you will be given a number of files. When you complete the assignments you should always push to this repository, and we will tell you which files need to be submitted on Canvas as well.

## Finally
If you are having any trouble, please reach out to us on Piazza. We're here to help!
