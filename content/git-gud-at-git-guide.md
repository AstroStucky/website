---
author: Thomas Stucky
category: Project Management
date: 2025-01-06 13:41
lang: en
slug: git-gud-at-git-guide
status: draft
tags: git, security
title: Git Gud at Git Guide
...

***If you want to get straight to the point, skip to the "How to" sections.***

I saw an unfilled need for an approachable, game development focused guide for programmers, artists, audio engineers, and writers collaborating in small teams using git. This is that guide. We will cover git usage with both the command line tool *git* and one of the many GUI front-ends available for git: *GitHub Desktop*.

Here is our obligatory mention that git is not GitHub. Git is a free and open-source version control software originally developed by Linus Torvalds. GitHub is a development platform for hosting git repositories. Git can exist without GitHub. GitHub cannot exist without git.

# What is the purpose of this guide?
I do not claim to be an expert in git. Instead I have merely been a user of it for more years than I care to recall now. I have also done professional open-source development on GitHub. The knowledge I share here has been picked up from these experiences.

This guide is not to argue for any particular git best practices. If I demonstrate a particular branching workflow, that's just the way I have always done it and know well.

This guide is here to educate a user with zero git experience to a point where they can confidently contribute their code, art assets, sound tracks or whatever to a git repository without fear of mangled repository history or lost work. It also exists as a references for those who have minimal experience, but could use a refresher.

# What is version control?
Version control enables you to record snapshots of files on your computer at different epochs of development of those files, and enables you to go back to any of those past epochs at will for reference, to revert a change that's no longer needed, or to perform regression tests. Unlike a file backup systems, these snapshots are not created automatically, but instead intentionally by the user at logical development milestones.

For example, if you have just finished implementing a double jump movement ability into your platformer game and have tested and verified that it works well, that would be an ideal time to record this epoch of development into your version control software in case you ever need to go back to this point in the future. In git, this would be called a *commit*. A commit is a collection of changes made to files in a repository that may have a message (*e.g.* "Completed double-jump mechanic") and will always have a unique hash string associated with them, so that each commit can always be uniquely referenced at any point in the future. A git repository is effectively a sum of commits. Each one representing a small or large change and all together representing a recorded history of development on a collection of files.

## GitHub Credentials

***If you have never contributed to a GitHub project, do this first.***

As of August 13, 2021 GitHub no longer allows users to enter their GitHub password when they wish to push code to a server (push is git language for contributing your changes). This results in on-boarding new users to GitHub being slightly harder because they now have to setup their account to be capable of securely contributing code.

GitHub has its own guides to assist in this setup which I will link here for you to work through. The gist is you can either use SSH keys or a personal access tokens to verify your identity and access your GitHub repositories.

### SSH Keys

These are a cryptographic token pair. One lives on your computer and the other lives on GitHub's servers. Using Secure Shell (SSH) protocol, GitHub is capable of verifying your identity by validating the token that lives on your computer with the one that lives on their servers. This is the form of verification I use because I always use the same development machine, and I like not having to fuss with inputting credentials each time I push.

This method requires that you use the SSH URL for any repositories that you wish to contribute to. It will start with `git@github.com`.

[GitHub Docs - Adding a new SSH key to your GitHub account](https://docs.github.com/en/authentication/connecting-to-github-with-ssh/adding-a-new-ssh-key-to-your-github-account)

### Personal Access Tokens

These are like a long password that you will have to enter (or copy and paste) into the password field each time you push changes to a remote repository (although you can also cache the token for some amount of time so it does not ask for it again). This method enables you to use HTTPS URLs to access your git repository. I do not personally use these, but if for whatever reason your development machine is constantly changing, this might be your best option.

[GitHub Docs - Managing your personal access tokens](https://docs.github.com/en/authentication/keeping-your-account-and-data-secure/managing-your-personal-access-tokens)

## How to download a remote repository (clone)

We will not go over how to create a repository from scratch because this is a practical guide that makes the assumption there is another on your team with expertise to create the initial repository and host it on a repository server, such as GitHub. So in this section we will skip right to the point where a remote repository already exists on a server and you wish to download it to view its files and make contributions.

Remote repositories are accessed via a URL provided by your repository admin. GitHub provides 2 methods of accessing a remote repository and each come with their own style of URL: HTTPS and SSH. Your choice of which one ultimately does not matter so long as you have setup your GitHub credentials on both your account and your development machine accordingly (see the **GitHub Credentials** section above for more information).

With a web browser navigate to the repository's webpage on GitHub, which will open in the **Code** tab. Click blue "<> Code" button next to the About section. A drop down will show where you will select the style of URL you wish to use (either HTTPS or SSH). Copy one of those URLs to your clipboard and proceed to either of the next two sections depending on which git front-end you are using.

![]({static}/images/post_git-gud-at-git-guide/GitHub-clone-prompt.png)

### Download remote repository with CLI in a terminal

Your first download of a remote repository using the command-line is simple. While in your terminal, navigate to where you want the repository's directory to live on your computer. And execute the following command where `REPOSITORY_URL` is the URL you got from the GitHub page.
```
git clone REPOSITORY_URL
```

### Download remote repository with GitHub Desktop

Open up GitHub Desktop. Click on "Clone a repository from the Internet...". If you have used your GitHub account to log into GitHub Desktop, you will already see all of your repositories and respositories you are a collaborators on available to clone. If you see the correct repo there, go ahead and use it. In case you do not, you can also enter the URL manually, but clicking the URL tab in this prompt and pasting the URL acquired from GitHub in the previous section.

Do not forgot to modify the local path so the repository saves in the intended location on your computer. Click clone to initiate the download.

~![]({static}/images/post_git-gud-at-git-guide/GitHubDesktop-clone-remote.png)

## How to update from a remote repository (pull)

Now that the remote repository has been cloned onto your machine, you have what is known as a local repository. Should you need to update your local files form the remote repository because you collaborator recently pushed important changes to it, this is what you do.

### Update from remote repository using CLI in a terminal

Simply run the command
```
git pull
```

What has happened is git has accesses the remote repository to download all commits applied to it since your last pull or fetch and applied (merged) those commits into your local repository workspace. A pull is simply a compound operation of a fetch and a merge. Should you get an error about unstaged changes that would conflict with your pull, see the section **How to contribute your changes (commit)**.

### Update from remote repository using GitHub Desktop

In GitHub Desktop you can simply navigate in the top menu to Repository > Pull to update files on your local machine. Github Desktop will also automatically perform what is known as a fetch, which downloads new commits without merging those commits into your current local respository workspace. This is just so users can stay automatically updated as to changes occurring in the remote.

## How to view your local changes (status)

The most important part of working with git is changing files. That's what it's all about. So lets say you have just implemented your new game mechanic, which required modifying an existing file and creating a new file. Before committing anything it is always good practice to see exactly what has changed. Should you see additional files that you did not intend to change. They have either been changed by mistake or automatically by whatever development tools you may have been using. It is important to know the difference and to avoid contributing changes to the repository that you did not intend to contribute. This is why we view what has changed before doing anything else.

Another extremely powerful tool that will be talked about in this section is a file differential, or *diff* for short. This uses a similarity algorithm to infer which new lines have replaced old lines (if any) and show at a glance what in the file is new and what is modified. It is important to remember diffs are really only useful for viewing changes in text based files. Modified binary files will not produce a diff.

### View local changes using CLI in a terminal

```
git status -s
```

The `-s` is optional. I just prefer it for brevity. Feel free to explore that status commands other options with `git help status`.

This will display a list of all modified files, new files, and new directories since the last commit known about by your local repository.

```
M  player.script
?? new_mechanic.script
```

Where `M` and `??` should be red, assuming you are using a colorized terminal.

To view the diff of the modifications made to the `player.script` file use the command
```
git diff player.script
```
This will show you exactly what lines were added or modified.

```
diff --git a/player.script b/player.script
index 6962432..998eb5f 100644
--- a/player.script
+++ b/player.script
@@ -4,4 +4,6 @@ func walk():
 func jump():
   # Code for player jumping

+func new_mechanic():
+  # implement code for mechanic here
```

### View local changes using GitHub Desktop

In GitHub Desktop a summary of local changes will be updated as you work and displayed in the left pane under "Changes".

![]({static}/images/post_git-gud-at-git-guide/GitHubDesktop-changes-pane.png)

Assuming the change is a modification of an existing file, represented in the GUI by the yellow square with a dot inside it, you can click on the change line item to see the diff right there in GitHub Desktop.

## How to stage your local changes (add)

Once you are sure you have made the changes you want to make, they must be staged before they can be turned into a commit. This tells git specifically what files you want to be in the commit, which enables you to exclude other changes you do not wish to be in the commit.

### Stage your local changes using CLI in a terminal

Call the `add` command followed by a list of the files you wish to add.

```
git add player.script new_mechanic.script
```

Wildcards can be used. The following command would have accomplished the same thing

```
git add *.script
```

I would strongly advise against using `git add .` while in the root directory of the repository. This would simply add everything that has changed. As was pointed out in the previous section, you should be intentional about what gets staged, and using blindly adding all changes is an easy way to get into the habit of cluttering the repository with changes that were not necessary.

After the add command, a `git status -s` will look like so

```
A  new_mechanic.script
M  player.script
```

Notice that staged changes are represented by green `A` and `M`, instead of the red `??` and `M`. The reason the `new_mechanic.script` file is now tagged with a green `A` is because the file was previously untracked, or in other words, unknown to the local repository. Now that it is stage, the file is ready to be tracked, which is signified by the green `A`, which stands for add.

### Stage your local changes using GitHub Desktop

In GitHub Desktop the concept of staging is represented simply by ticked or unticked check boxes next to each change line item in the "Changes" left pane, where ticked means the item is staged.

## How to contribute your changes (commit)

You can now commit your staged changes, which will *immortalize* them into your local repository's history. Remember that a commit should be made at logical development milestones, or in other words, when you have finished something. It is good practice to commit often, which means your commits may be small, and that is perfectly fine.

### Contribute your changes using CLI in a terminal

The following command will save any staged changes you have into the local repository.

```
git commit
```

If you have forgotten to stage any changes, this will produce an error message. Empty commits are not allowed by git.

The above command will result in a terminal text editor popping up in which you can type a brief and descriptive message about what has changed in this commit. Do not skimp on these messages, as they are very helpful ways of documenting your project's development history. It is good practice to use the first line of the commit message as a summary for all the changes, and then, if necessary, writing about those changes in more detail in the following lines. Small commits that only use the first line for summary are fine too.

You can also type a commit message in the same command you create the commit with

```
git commit -m "New mechanic added"
```

### Contribute your changes using GitHub Desktop

Underneath the "Changes" left pane is the commit pane. The summary should be a brief description of what has changed in the commit, and the description may go into more detail. When the correct changes have been checked (staged), type your commit message summary and description into the commit pane, and click "Commit to BRANCH", where BRANCH is whatever branch you are currently working on. We will go into details about these later.

![]({static}/images/post_git-gud-at-git-guide/GitHubDesktop-commit.png)

## How to update the remote repository with your contributions (push)

The local repository has now committed your changes to its history, but this history needs to be updated on the remote repository as well. This is known as a push. When a push has been completed the local repository and remote repository should contain the same history.

### Update the remote repository with your contributions using CLI in a terminal

A push is done simply enough with the command

```
git push
```

Assuming you have commit that are not yet known by the remote repository, this will result in an upload of those commits.

### Update the remote repository with your contributions using GitHub Desktop

To push on GitHub Desktop, navigate to the top menu and click Repository > Push.

# More to come...

There is so much more I want to go over in this guide, including branching and merging. Branching is like creating an alternate history in your repository that moves forward at its own pace one commit at a time. Merging is the method by which these alternate histories can be combined into one. Stand by, and I will hopefully have more guidance to add here.

I hope this has been helpful. Please reach it you have advice on how it can be more helpful.
