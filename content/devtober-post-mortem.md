Title: Devtober Post Mortem
Date: 2020-11-04 22:09
Author: Thomas Stucky
Category: Game Development
Tags: devtober, game jam, kuiper
Slug: devtober-post-mortem
Status: published
Lang: en

# Objectives

For my first Devtober I set rather lofty goals, and met half of them. The game as I imagine it requires some complex systems that I've never built before, and along the way I encountered both pleasantly surprising results and discouraging setbacks. If you want to skip to the **Lessons Learned TLDR** that's at the bottom, please feel free to!

1.  **✔ Revamp destructible asteroids**
2.  **✔ Improve overall visuals**
3.  **✔ Add asteroid hopping and crawling mechanics**
4.  **Revamp accreting ice shells**
5.  **Make very simple AI to fight against**
6.  **Make playable as a HTML5 browser game (optional)**

# Revamping Destructible Asteroids

![](https://img.itch.zone/aW1nLzQ1NDU4ODIuZ2lm/original/pwhHD4.gif)

This was by far the biggest undertaking this month. To get the new and improved asteroids to act and look how they do now took half of my Devtober. I knew this would be a big piece going in, which is why I tackled it first. This was also blocker for revamping the accreting ice shell, since it would be built on top of the same system.

I am the most proud of my work on the asteroid break-up. I think it came out looking far better than I could have hoped, and performs much faster than I expected, even while still being coded in GDScript. The next steps are to get it fully coded into C++, which should prevent the frame stutter seen in the demo gif.

This part of the project also had some pleasant surprises along the way. For instance, while playing around with different ways to color the vertices of asteroid, I learned that by using a cubic color interpolation along the ordering of vertices of the Delaunay tessellation, I was able to very easily give the asteroids a nice frosted edge look. There was no reason for this to work aside from sheer luck, and I had no reason to try it aside from sheer curiosity and boredom. This experience taught me that aimless tinkering in moderation in game dev can yield serendipity.

One more lesson I gleamed from the asteroid revamp. The Fruit Ninja-esque chopping mechanic seen in the above gif was never meant to be in the game. It was just some debugging tool I made to test break-up, but as sometimes happens with debugging tools, I realize it's quite fun! I don't know what the mechanic will look like in it's final form, but I now know I have to find some excuse to give the player a similar power in-game!

# Adding Asteroid Hopping and Crawling Mechanics

![](https://img.itch.zone/aW1nLzQ1NDYwMTMuZ2lm/original/sOWJSl.gif)

Since asteroids had to be rebuilt from scratch, asteroid hopping and crawling wound up being the only true feature addition I had this month, and it's one I have yet to discuss the idea behind. When accreting ice shells are fully realized in Kuiper, it is possible for a player's ice shell to be chopped up/blown apart such that the player character is now unshelled and adrift in the cold void of the Kuiper Belt without any shielding, propulsion, or weapons. The player is now in E.S.A. mode (Extra Shellular Activity), a sort of "second chance" phase of gameplay, and must use their momentum and nearby asteroids to navigate to safety before they can start the process of rebuilding their protective ice shell.

![](https://img.itch.zone/aW1nLzQ1NDY4MDkuZ2lm/original/IwtveP.gif)

I dived into work on this feature immediately after I finished asteroid break-up; when I was reinvigorated by a hard fought victory and eager to start something I anticipated to be much simpler to implement. What I mean to say is I may have gone into tackling this feature with a little too much confidence right at the start. I vastly underestimated the time it would take, and I just assumed that the asteroid-ESA code interface would somehow work out. It didn't, and the feature took some amount of recoding on the asteroid end of things.

I also learned from this experience that player controls are hard, and to get asteroid crawling in particular to feel good on both analog stick and WASD is going to take some more time outside of Devtober. I am still proud of where the mechanic wound up, and during its testing I got around to building something I never even put in my objectives, but badly needed all the same: a PlayerFollowCam script.

# What Remains

Following the completion of asteroid hopping in the 3rd week of Devtober, and already knowing implementing AI and HTML5 might need to be held off until next month, I was onto the final feature: ice shell accretion. Up to this point I had been building everything in Godot's GDScript, which allows for very rapid prototyping, but is slow for expensive computation like a Poisson disk sampling algorithm or iterating through a 500 triangle tessellation in a single frame. In addition to being destructible like the asteroids, the ice shell must also be larger (more triangles to iterate over), and must accrete material (add triangles in response to water ice collisions), meaning the slowdown from doing this all in GDScript for the ice shell would be significant. I knew the destructible script would inevitably have to be re-coded in C++, but it was a step I hoped I could put off until after Devtober. Now this significant task had to be done in much less than a week if I were to have any hope of then extending it with a material accretion mechanic and finishing the accreting ice shell before the end of the month.

Over the final week of Devtober I worked tirelessly toward this end, and the results so far are very promising! The Poisson disk sampling saw a factor of 35x increase in speed, if I can get similar or better increases out of the remaining C++ re-code, then the game should run great on most any modern machine (keep in mind I intentionally do not develop on my gaming rig so that I know I'm developing something even low-end machines can handle).

In this final week of Devtober, my focus shifted from rapidly prototyping flashy features that make nice demo gifs towards making sure the implementation of those features are scalable and adaptable enough for what comes next. It was the work that I wanted to do later, but realized I absolutely needed to do now, and while it did not produce any new pretty demo gifs to post, it is building my confidence to see Kuiper through to the end.

# Conclusion

![](https://img.itch.zone/aW1nLzQ1NDY4MjUuZ2lm/original/kPIqgA.gif)

Kuiper is a game about being resourceful with what little you are given. Which is why I could stand to learn from it. At the beginning of the month I made a list of tasks that would get me to a vertical slice of the game, but I never took a moment to allocate time for each one. If I had, I am sure I would have removed some non-essential tasks from the list, and had a better idea of what to expect this month. There still would have been unexpected delays along the way, but with a scheduled list I would have stayed more focused on the task at hand rather than dreading what's to come or wondering what to do next.

I am extremely proud of the work I accomplished on the project this month. This is undoubtedly the most development I have been able to squeeze into a game project within single month, and it's taught me a lot along the way.

# Lessons Learned TLDR

What remains are summaries of what I learned this Devtober. Feel free to use these as a guide for your own game projects.

##### 1. Do the hard thing first

I'm glad asteroid break-up was the first thing I worked on, and it invigorated me to tackle what came next. Furthermore, if a problem winds up being too hard to tackle, it's better to learn early on in the project and re-scope then.

##### 2. Tinker!

Good things can happen when you toy with the systems of your game, even if you do it without a defined purpose.

##### 3. "Follow the Fun"

Follow the fun just means that if you find something that is unexpectedly fun, whether it was an intentional feature, debug tool (as in my case), or even a glitch, lean into it. Iterate on it. Can you improve or even rethink the game by incorporating it? This idea is not my own. Look up [Game Maker Toolkit's YouTube video on "Games that Designed Themselves"](https://www.youtube.com/watch?v=kMDe7_YwVKI) if you'd like to hear real examples of when "follow the fun" was practiced with success in the game industry.

##### 4. Give ample time to controls

This always seems to pop into my head every time I work on a control system. For any game the feel of the controls can make it or break it. Give ample time to both designing and iterating on controls. If you do not have ample time to commit to controls then write a prototype that at least works, and plan to improve the feel of it later on. Simple and readable code is always important, but realize that control systems that feel good to the player rarely take the form of simple. If your code for controls becomes monstrous, that might honestly be okay. When it comes to control code: Function \> Form.

##### 5. List and *schedule* objectives

In contrast to \#2, when you aren't toying with your project in moderation, it's good to work on a planned schedule. If you aren't the type to plan things a month out, like me, then at the very least try and do this: At the end of a day's work make a note. It could be a sticky note, an uncompileable sentence in your code, or a git commit message; just write it somewhere you'll notice it the next morning. Write what you were doing when you finished work, then write what you plan to do when you resume work. I'm not as consistent about it as I should be, but every time I practice this I find the overhead of starting up the next day to be far smaller.


# Thanks!

Thank you so much for reading this far! 😁 I will continue to work on Kuiper at the same pace until it I get the vertical slice I'm after. If you're curious about the project and want to follow along, please follow me on Twitter and keep checking for updates here.


