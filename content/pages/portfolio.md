---
author: Thomas Stucky
date: 2025-03-12 23:00
slug: portfolio
status: published
title: Portfolio
...

<head>
  <link rel="stylesheet" href="{static}/styles/additional.css"/>
</head>

  [Games Worked On](#games-worked-on)   
  [Open-Source Samples](#open-source-samples)

<p>
**Pong?**, **Orbit Toy**, **Pipeworks**, **Worm Rampage**, and **Kuiper** were all worked on solely by me. The projects listed on this page showcase my technical ability in game programming and game engines, in particular Godot. You can play most of the following games on my [Itch.io page](https://starrynitegames.itch.io/) and you can view any open-source code I have worked on at my [GitHub page](https://github.com/AstroStucky).
</p>

---

## Games Worked On

|     |     |     |
| --- | --- | --- |
| [<img class="thumbnailGrid" src="{static}/images/portfolio/thumbnail_thelastslice.png"/>](#the-last-slice) | [<img class="thumbnailGrid" src="{static}/images/portfolio/thumbnail_pong.png"/>](#pong)                | [<img class="thumbnailGrid" src="{static}/images/portfolio/thumbnail_orbittoy.png"/>](#orbit-toy) |
| [<img class="thumbnailGrid" src="{static}/images/portfolio/thumbnail_pipeworks.png"/>](#pipeworks)         | [<img class="thumbnailGrid" src="{static}/images/portfolio/thumbnail_wormrampage.png"/>](#worm-rampage) | [<img class="thumbnailGrid" src="{static}/images/portfolio/thumbnail_kuiper.png"/>](#kuiper)      |

### The Last Slice

<div class="verticalAlign">
  <iframe src="https://itch.io/embed/2301266?border_color=ffffff&amp;link_color=15A9DB" width="206" height="165" frameborder="0">  [The Last Slice by Starry, Helen Dinh, clickonbritt, MetaArcade, Ed Johnson](https://starrynitegames.itch.io/the-last-slice)
  </iframe>
  <p>
    As the director and lead programmer of *The Last Slice* I led a team of 5 others during a 2 week game jam for the [2023 Cozy Autumn Jam](https://itch.io/jam/cozy-autumn-game-jam-2023) to design and implement this cozy puzzle platformer that oozes with Autumn time vibes. I handled the tilemap implementation, character control, procedural animation, and the gameplay programming for each costume's unique abilities.
  </p>
</div>

[The game was very well received by Cozy Autumn Jam reviewers!](https://itch.io/jam/cozy-autumn-game-jam-2023/rate/2301266) It ranked **3rd for fun**, **5th for creativity**, and **6th place overall**.

<!-- TODO <div class="verticalAlign">
  <p>
    [The game was very well received by Cozy Autumn Jam reviewers!](https://itch.io/jam/cozy-autumn-game-jam-2023/rate/2301266) It ranked **3rd for fun**, **5th for creativity**, and **6th place overall**.
  </p>
  <span>
    ![]({static}/images/placeholder.png){width=400}
  </span>
</div>
 -->
<div style="text-align: center;">
![The player solves a platform puzzle using both the jack-o-lantern and ghost costume.]({static}/images/game-preview_the-last-slice.gif){width=400}
</div>

### Pong?

<div class="verticalAlign">
  <iframe src="https://itch.io/embed/2830850?border_width=0&amp;link_color=15A9DB" width="206" height="165" frameborder=0>
    [Pong? by Starry](https://starrynitegames.itch.io/pongq)
  </iframe>
  <p>
    For *Pong?* I developed an enemy AI based on simulated human-reaction time, cut my teeth on Godot's animation player, and implemented a weighted probability distribution for randomly selecting the next gameplay morph that also adjusts itself after each level to keep the player from seeing the same content too frequently.
  </p>
</div>

<div class="verticalAlign">
  <p>
    The game was made for the 8 day [Fox Hollow Jam 2](https://itch.io/jam/fox-hollow-jam-2) in which it took 2nd place.
  </p>
  <span>
    ![]({static}/images/FoxHollowJam2_2024_2ndplace_gold.png){width=400}
  </span>
</div>

<div style="text-align: center;">
![*Pong?* is Pong with a twist. Every time the player scores, a new big or small morph is applied to the game.]({static}/images/pongq-breakout.gif){width=400}
</div>

### Orbit Toy

<div class="verticalAlign">
  <iframe src="https://itch.io/embed/3393031?border_color=ffffff&amp;link_color=15A9DB" width="206" height="165" frameborder="0">  [Orbit Toy by Starry](https://starrynitegames.itch.io/orbit-toy)
  </iframe>
  <p>
    *Orbit Toy* is a demonstration instead of a full game. The environment is a 3D terrain shader wrapped around a half-sphere. It is capable of blending as many different noise and/or heightmap images together using addition, subtraction, multiplication, or division operations as needed to produce the desired terrain shape.
  </p>
</div>

The terrain albedo is rendered with a combination of height and normal texture blending to represent terrain walls, highlands, and lowlands. The minimap predicts the spacecraft's trajectory and reacts in real-time to adjustments by employing leap-frog integration, so that the prediction remains in tight agreement with Godot's physics engine result.

### Pipeworks

<div class="verticalAlign">
  <iframe src="https://itch.io/embed/1224282?border_width=0&amp;link_color=15A9DB" width="206" height="165" frameborder="0">
    [Pipeworks by Starry](https://starrynitegames.itch.io/pipeworks)
  </iframe>
  <p>
    For *Pipeworks* I built a simple but performant fluid effect with Godot's physics engine, about 50 circular rigid bodies, and the [metaball rending technique](https://en.wikipedia.org/wiki/Metaballs). The slosh forces are estimated simply by counting the number of particles within  the two bottom quadrants of the character's circular body, which manages to feel just like you are controlling a sloshy cylinder of fluid without the need for expensive computations.
  </p>
</div>

<div style="text-align: center;">
![Each level in Pipeworks begins with the player taking on coolant at a fill station. The player must then navigate to the nearest dump station, fighting the chaotic motion of their sloshy cargo along the way.]({static}/images/game-preview_pipeworks.gif){width=400}
</div>


### Worm Rampage

<div class="verticalAlign">
  <iframe src="https://itch.io/embed/1017063?border_width=0&amp;link_color=15A9DB" width="206" height="165" frameborder="0">
    [Worm Rampage by Starry](https://starrynitegames.itch.io/worm-rampage)
  </iframe>
  <p>
    For *Worm Rampage* I cut my teeth on procedural animation in Godot, line-of-sight based AI, navigation meshes, and Perlin noise terrain in 2D. I used the game as a case study for my talk about finite state machines in game development delivered to the SLC Game Dev community.
  </p>
</div>

<div style="text-align: center;">
  ![The player burrows through terrain in order to build up enough speed to breach and attack the surface.]({static}/images/game-preview_worm-rampage.gif){width=400}
</div>

### Kuiper


<div class="verticalAlign">
  <iframe src="https://itch.io/embed/371833?border_width=0&amp;link_color=15A9DB" width="206" height="165" frameborder="0">
    [Kuiper by Starry](https://starrynitegames.itch.io/kuiper)
  </iframe>
  <p>
    *Kuiper* was an experiment in destructible rigid bodies in 2D. Using the C++ GDNative library, I built a system for slicing up and blowing apart 2D meshes in real-time.
  </p>
</div>

<div style="text-align: center;">
  ![Demonstration of dynamic rigid body break-up built from scratch for Kuiper.]({static}/images/game-preview_kuiper.gif){width=400}
</div>

<!--
### Field Notes

<div class="verticalAlign">
  <iframe src="https://itch.io/embed/502778?border_width=0&amp;link_color=15A9DB" width="206" height="165" frameborder="0">
    [Field Notes by unrulycuriosity, Starry](https://unrulycuriosity.itch.io/fieldnotes)
  </iframe>
  <p>
    [Field Notes](https://unrulycuriosity.itch.io/fieldnotes) was a citizen science game concept prototyped for the [2019 Science Hackathon](http://sf.sciencehackday.org/hacks-2019/). The game had the player exploring planets and performing citizen science tasks on real-world science data in exchange for story progression. The game was rewarded "Best Interactive Hack".
  </p>
</div>

<div style="text-align: center;">
![In Field Notes you explore planets and complete real-world science classification tasks.]({static}/images/game-preview_field-notes.gif){width=400}
</div>
 -->
---

## Open-Source Samples

### OceanWATERS

<div class="verticalAlign">
  <img class="thumbnail" alt="" src="{static}/images/oceanwaters.jpg"/>
  <p>
    [*Ocean Worlds Autonomy Testbed for Exploration Research & Simulation* (*OceanWATERS*)](https://science.nasa.gov/science-research/science-enabling-technology/technology-highlights/towards-autonomous-surface-missions-on-ocean-worlds/) is an open-source 3D virtual robotics testbed for developing lander autonomy in a simulated Europa environment. [It is available on GitHub](https://github.com/nasa/ow_simulator).
  </p>
</div>

OceanWATERS helps enabled future exploration of outer solar system icy worlds. It is built on [ROS](https://www.ros.org/) and the simulation environment is based on [Gazebo](http://gazebosim.org/). My role on the project was to develop new features to increase fidelity of the physical simulation.

### Easy Fluid Sim

<div class="verticalAlign">
  <img class="thumbnail" alt="" src="{static}/images/portfolio-easyfluidsim.gif"/>
  <p>
    A demonstration of a quick and easy 2D fluid effect in Godot and [available on GitHub](https://github.com/AstroStucky/EasyFluidSim). It was presented to a meet-up of the SLC Game Devs at Millcreek Community Library in Millcreek, Utah, USA. [The original presentation, Fast and Easy 2D Fluid Simulation, is available on Google Drive](https://docs.google.com/presentation/d/1_LE85uojjjXCUUpGZrHOP-4MTcdNIx1tZ0nOZT4hfy4/edit?usp=sharing).
  </p>
</div>

### Flappy Goat

<div class="verticalAlign">
  <iframe src="https://itch.io/embed/2616570?border_width=0&amp;link_color=15A9DB" width="206" height="165" frameborder="0">
    [Flappy Goat by Starry, Tuckleberry Winn](https://starrynitegames.itch.io/flappy-goat)
  </iframe>
  <p>
    A Flappy Bird clone made to demonstrate building a 3D game in Godot using Blender file imports. [The code is available on GitHub](https://github.com/AstroStucky/FlappyGoat). It was presented to a meet-up of the SLC Game Devs at Millcreek Community Library in Millcreek, Utah, USA. [The game can be played on Itch.io](https://starrynitegames.itch.io/flappy-goat).
  </p>
</div>
