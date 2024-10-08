---
author: Thomas Stucky
date: 2024-07-30 18:00
slug: portfolio
status: published
title: Portfolio
...

# Game Development Portfolio

<div style="text-align: center;">
![]({static}/images/portfolio-collage.gif){width=600}
</div>

**Kuiper**, **Pipeworks**, and **Worm Rampage** were all worked on solely by me. The projects listed on this page showcase my technical ability in game programming and game engines, in particular Godot. You can play most of the following games on my [Itch.io page](https://starrynitegames.itch.io/) and you can view any open-source code I have worked on at my [GitHub page](https://github.com/AstroStucky).

## The Last Slice

<div style="text-align: center;">
![The player solves a platform puzzle using both the jack-o-lantern and ghost costume.]({static}/images/game-preview_the-last-slice.gif){width=400}
</div>

The Last Slice is a laid-back puzzle platformer built in only 2 weeks for the [2023 Cozy Autumn Jam](https://itch.io/jam/cozy-autumn-game-jam-2023). You play as a *pumpkignome* who has been charged with the task of uncovering who ate the last slice of pumpkin pie on the day of the autumn celebration. Along the way you acquire the ability to change into different forms in order to traverse through the world.

[The game was well received by Cozy Autumn Jam reviewers!](https://itch.io/jam/cozy-autumn-game-jam-2023/rate/2301266) Of the 126 submissions our game ranked **3rd for fun**, **5th for creativity**, and **6th place overall**.

<div style="text-align: center;">
  <iframe src="https://itch.io/embed/2301266?border_color=fff" width="206" height="165" frameborder="0">  [The Last Slice by Starry, Helen Dinh, clickonbritt, MetaArcade, Ed Johnson](https://starrynitegames.itch.io/the-last-slice)
  </iframe>
</div>

<!--
## OceanWATERS

![]({static}/images/oceanwaters.jpg){width=400}

[*Ocean Worlds Autonomy Testbed for Exploration Research & Simulation* (*OceanWATERS*)](https://github.com/nasa/ow_simulator##ocean-worlds-autonomy-testbed-for-exploration-research--simulation-oceanwaters) is an open-source 3D virtual robotics testbed for developing lander autonomy in a simulated Europa environment. OceanWATERS helps enabled future exploration of outer solar system icy worlds. It is built on [ROS](https://www.ros.org/) and the simulation environment is based on [Gazebo](http://gazebosim.org/). My role on the project was to develop new features to increase fidelity of the physical simulation.
 -->

---

## Pong?

<div style="text-align: center;">
![Pong? is Pong with a twist. Every time the player scores, a new big or small morph is applied to the game.]({static}/images/pongq-breakout.gif){width=400}
</div>

[Pong?](https://starrynitegames.itch.io/pongq) operates like a rogue-like version of Pong. Each time there is a score, the rules of the game are morphed in some way to always keep the players on their toes. Some morphs can even occur in combination with other morphs. The game also features multiplayer, so grab a friend and give it a try!

<div style="text-align: center;">
  ![Pong? was made for the [Fox Hollow Jam 2](https://itch.io/jam/fox-hollow-jam-2
) and won the second place prize. Everything in the game was made in only 8 days by myself.]({static}/images/FoxHollowJam2_2024_2ndplace_gold.png){width=300}
</div>

<div style="text-align: center;">
  <iframe src="https://itch.io/embed/2830850?border_width=0&amp;border_color=fff" width="206" height="165" frameborder=0>
    [Pong? by Starry](https://starrynitegames.itch.io/pongq)
  </iframe>
</div>

---

## Pipeworks

<div style="text-align: center;">
![Each level in Pipeworks begins with the player taking on coolant at a fill station. The player must then navigate to the nearest dump station, fighting the chaotic motion of their sloshy cargo along the way.]({static}/images/game-preview_pipeworks.gif){width=400}
</div>

[Pipeworks](https://starrynitegames.itch.io/pipeworks) was prototyped during the [49th Ludum Dare 72-hour Game Jam](https://ldjam.com/events/ludum-dare/49/) for the theme "Unstable". You are a coolant delivery bot tasked with toting your sloshy cargo from one point to another inside a vast underground reactor complex.

The fluid simulation is done with 50 rigid bodies interacting in Godot's physics engine. The rigid bodies are rendered as metaballs to give the appearance of a fluid. [From this design I created an educational demonstration that is open-sourced on GitHub](https://github.com/AstroStucky/EasyFluidSim).

Using the collisions of the metaballs against the interior body of the bot resulted in movement that was far too unstable, so instead a cheap and simple technique is used to calculate the slosh force whereby every fluid body below the midway point imposes a torque on the bot equal to its weight multiplied by its horizontal distance from the bot's center.

<div style="text-align: center;">
  <iframe src="https://itch.io/embed/1224282?border_width=0" width="206" height="165" frameborder="0">
    [Pipeworks by Starry](https://starrynitegames.itch.io/pipeworks)
  </iframe>
</div>

---

## Worm Rampage

<div style="text-align: center;">
![In Worm Rampage the player burrows through terrain in order to build up enough speed to breach and attack the surface.]({static}/images/game-preview_worm-rampage.gif){width=400}
</div>

[Worm Rampage](https://starrynitegames.itch.io/worm-rampage) was prototyped during the [48th Ludum Dare 72-hour Game Jam](https://ldjam.com/events/ludum-dare/48/) for the theme "Deeper and Deeper". The concept is that you are a massive tunnel burrowing worm wreaking havoc on surface dwellers.

<div style="text-align: center;">
  <iframe src="https://itch.io/embed/1017063?border_width=0" width="206" height="165" frameborder="0">
    [Worm Rampage by Starry](https://starrynitegames.itch.io/worm-rampage)
  </iframe>
</div>

---

## Kuiper

<div style="text-align: center;">
  ![Demonstration of dynamic rigid body break-up built from scratch for Kuiper.]({static}/images/game-preview_kuiper.gif){width=400}
</div>

Resources are scarce out on the fringe. People have to make their spacecraft with whatever they can find, and in Kuiper, ice is by and large the most abundant and versatile resource there is. The player is given the power to bend ice to their will. They will use this power to dynamically construct a protective hull around themselves, and use fragments of that hull to attack enemies and propel themselves throughout the Kuiper Belt.

[Kuiper](https://starrynitegames.itch.io/kuiper) is an idea inspired by time spent at NASA Ames Research Center researching ice in its surprisingly numerous forms, and in particular how it behaves at extreme low temperature and pressure.

<div style="text-align: center;">
  <iframe src="https://itch.io/embed/371833?border_width=0" width="206" height="165" frameborder="0">
    [Kuiper by Starry](https://starrynitegames.itch.io/kuiper)
  </iframe>
</div>

---

## Field Notes

<div style="text-align: center;">
![In Field Notes you explore planets and complete real-world science classification tasks.]({static}/images/game-preview_field-notes.gif){width=400}
</div>

[Field Notes](https://unrulycuriosity.itch.io/fieldnotes) was a citizen science game concept prototyped for the [2019 Science Hackathon](http://sf.sciencehackday.org/hacks-2019/). The game had the player exploring planets and performing citizen science tasks on real-world science data in exchange for story progression. The game was rewarded "Best Interactive Hack".

<div style="text-align: center;">
  <iframe src="https://itch.io/embed/502778?border_width=0" width="206" height="165" frameborder="0">
    [Field Notes by unrulycuriosity, Starry](https://unrulycuriosity.itch.io/fieldnotes)
  </iframe>
</div>
