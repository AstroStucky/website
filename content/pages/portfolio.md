---
author: Thomas Stucky
date: 2021-11-15 15:33
slug: portfolio
status: published
title: Portfolio
...

![]({static}/images/portfolio-collage.gif)

All games listed here are works in progress and some are further along in development than others. **Kuiper**, **Pipeworks**, and **Worm Rampage** were all worked on solely by me. The projects listed on this page showcase my technical ability in game programming and game engines. You can play most of the following games on their [Itch.io page](https://starrynitegames.itch.io/) and you can view any open-source code I have worked on at my [GitHub page](https://github.com/AstroStucky).

# The Last Slice

[![](http://astrostucky.com/wp/wp-content/uploads/2024/01/jackolantern_jump.gif){.aligncenter .wp-image-334 width="400" height="299"}](https://starrynitegames.itch.io/the-last-slice)

The Last Slice is a laid-back puzzle platformer built in only 2 weeks for the [2023 Cozy Autumn Jam](https://itch.io/jam/cozy-autumn-game-jam-2023). You play as a *pumpkignome* who has been charged with the task of uncovering who ate the last slice of pumpkin pie on the day of the autumn celebration. Along the way you acquire the ability to change into different forms in order to traverse through the world.

[The game was well received by Cozy Autumn Jam reviewers!](https://itch.io/jam/cozy-autumn-game-jam-2023/rate/2301266) Of the 126 submissions our game ranked **3rd for fun**, **5th for creativity**, and **6th place overall**.

`<iframe src="https://itch.io/embed/2301266?bg_color=161616&amp;fg_color=e5e5e5&amp;border_color=161616" width="208" height="167" frameborder="0">`{=html}[The Last Slice by Starry, Helen Dinh, clickonbritt, MetaArcade, Ed Johnson](https://starrynitegames.itch.io/the-last-slice)`</iframe>`{=html}

# OceanWATERS

![](http://astrostucky.com/wp/wp-content/uploads/2022/02/lander_europa-1024x576.jpg){.wp-image-324 width="656" height="368"}

[*Ocean Worlds Autonomy Testbed for Exploration Research & Simulation* (*OceanWATERS*)](https://github.com/nasa/ow_simulator#ocean-worlds-autonomy-testbed-for-exploration-research--simulation-oceanwaters) is an open-source 3D virtual robotics testbed for developing lander autonomy in a simulated Europa environment. OceanWATERS helps enabled future exploration of outer solar system icy worlds. It is built on [ROS](https://www.ros.org/) and the simulation environment is based on [Gazebo](http://gazebosim.org/). My role on the project was to develop new features to increase fidelity of the physical simulation.

# Kuiper

![Demonstration of dynamic rigid body break-up built from scratch for Kuiper.](http://astrostucky.com/wp/wp-content/uploads/2021/11/102920_kuiper_devtober29_particles.gif){.wp-image-293 width="400" height="278"}

Resources are scarce out on the fringe. People have to make their spacecraft with whatever they can find, and in Kuiper, ice is by and large the most abundant and versatile resource there is. The player is given the power to bend ice to their will. They will use this power to dynamically construct a protective hull around themselves, and use fragments of that hull to attack enemies and propel themselves throughout the Kuiper Belt.

[Kuiper](https://starrynitegames.itch.io/kuiper) is an idea inspired by time spent at NASA Ames Research Center researching ice in its surprisingly numerous forms, and in particular how it behaves at extreme low temperature and pressure.

`<iframe src="https://itch.io/embed/371833?bg_color=161616&amp;border_color=161616" width="208" height="167" frameborder="0">`{=html}[Kuiper by Starry](https://starrynitegames.itch.io/kuiper)`</iframe>`{=html}

# Pipeworks

![Each level in Pipeworks begins with the player taking on coolant at a fill station. The player must then navigate to the nearest dump station, fighting the chaotic motion of their sloshy cargo along the way.]({static}/images/game-preview_pipeworks.gif)


[Pipeworks](https://starrynitegames.itch.io/pipeworks) was prototyped during the [49th Ludum Dare 72-hour Game Jam](https://ldjam.com/events/ludum-dare/49/) for the theme "Unstable". You are a coolant delivery bot tasked with toting your sloshy cargo from one point to another inside a vast underground reactor complex.

The fluid simulation is done with 100 rigid bodies interacting in Godot's physics engine. The rigid bodies are rendered as metaballs to give the appearance of a fluid. [From this design I created an educational demonstration that is open-sourced on GitHub](https://github.com/AstroStucky/EasyFluidSim).

Using the collisions of the metaballs against the interior body of the bot resulted in movement that was far too unstable, so instead a cheap and simple technique is used to calculate the slosh force whereby every fluid body below the midway point imposes a torque on the bot equal to its weight multiplied by its horizontal distance from the bot's center.

`<iframe src="https://itch.io/embed/1224282?border_width=0&amp;bg_color=161616" width="206" height="165" frameborder="0">`{=html}[Pipeworks by Starry](https://starrynitegames.itch.io/pipeworks)`</iframe>`{=html}

# Worm Rampage

![Cover Art by [\@butterstoch\_workshop](https://www.instagram.com/butterscotch_workshop/)]({static}/images/game-art_worm-rampage.jpg)


![In Worm Rampage the player burrows through terrain in order to build up enough speed to breach and attack the surface.](http://astrostucky.com/wp/wp-content/uploads/2021/11/042621_worm_ldcomplete-1.gif){.wp-image-297 width="400" height="233"}

[Worm Rampage](https://starrynitegames.itch.io/worm-rampage) was prototyped during the [48th Ludum Dare 72-hour Game Jam](https://ldjam.com/events/ludum-dare/48/) for the theme "Deeper and Deeper". The concept is that you are a massive tunnel burrowing worm wreaking havoc on surface dwellers.

`<iframe src="https://itch.io/embed/1017063?border_width=0&amp;bg_color=161616" width="206" height="165" frameborder="0">`{=html}[Worm Rampage by Starry](https://starrynitegames.itch.io/worm-rampage)`</iframe>`{=html}

# Field Notes

![In Field Notes you explore planets and complete real-world science classification tasks.](http://astrostucky.com/wp/wp-content/uploads/2022/02/hYjgWe.gif){.wp-image-325 width="435" height="253"}

[Field Notes](https://unrulycuriosity.itch.io/fieldnotes) was a citizen science game concept prototyped for the [2019 Science Hackathon](http://sf.sciencehackday.org/hacks-2019/). The game had the player exploring planets and performing citizen science tasks on real-world science data in exchange for story progression. The game was rewarded "Best Interactive Hack".

`<iframe src="https://itch.io/embed/502778?border_width=0&amp;bg_color=161616" width="206" height="165" frameborder="0">`{=html}[Field Notes by unrulycuriosity, Starry](https://unrulycuriosity.itch.io/fieldnotes)`</iframe>`{=html}

# Golfpocolypse

Goflpocolypse was an unannounced Unity project made in collaboration with a mostly remote team of artists, game designers, and programmers. It served as my first introduction to the Unity game engine. I built several different versions of a golf ball shooting mechanic, and coded all the level instancing and physics engine adjustments.
