# ETS2Manual

A Manual Randomizer for Euro Truck Simulator 2, for use with the [Archipelago Manual](https://github.com/ManualForArchipelago) Project.

## Setup and How to Play

What you need:

- A fresh save file and the base game of ETS2. If you own DLCs that add/expand countries, you can enable them with yaml options, but base game is all you need to play.
- Start your save in any city of Germany, or in the country you got the key for at startup if you set the starting_country option to random

You collect checks as you discover cities or interact with collectibles on the map.

- For cities, you can claim the check whenever the [CITY NAME] DISCOVERED popup appears;
- For photo trophies, you can claim the check whenever the Steam achievement pops up after using the in-game Photo option (Media -> Photo Mode) and taking a picture in front of the point of interest marked in the map (it will show its name on screen).
- For viewpoints, you can claim the check after the cutscene starts playing when you interact with it in-game.

## Locations

Note: The quantity of locations listed below will vary depending on which DLC's you enable with yaml options.

- Cities
- Photo Trophies (with Photosanity enabled)
- Viewpoints (with Viewpointsanity enabled)

## Items

- Country Keys
  - You cannot enter or traverse through countries you do not have access to. Each country will have its corresponding key on the pool and receiving these will unlock access to said country.
- Delivery Tokens
  - Collect these tokens to win. You can configure the number of Delivery Tokens needed to win as a yaml option.

## Scout hints

If you enable scout hints in the options, all locations will have a "scout" button appended in the Manual client. When you click them, you will know what item is under them. You can use that in several ways, to prevent aimless wandering across your hundreds of locations:

- Awarding yourself a hint for every delivery completed
- Scout hinting on every offered delivery
- Hinting all locations within a country when you get its key
- ...or whatever narrative you'd like!

## Things to know

- It's not mandatory to be hauling cargo at the time of claiming the check. This is a very slow-paced game and requiring the player to always be on jobs makes it even more slow. You can play in free roam for as long as you can, but be reminded that you'll eventually need to earn money to pay for all those tickets :)
- Strongly suggest the use of [Universal Tracker](https://github.com/FarisTheAncient/Archipelago/releases) alongside the Manual Client as it'll help you understand what's in logic at the time with the items you have.
- Ferry boats are logically considered as borders between countries, because these will give you access from one country to another. Take this information in consideration when you unlock access to a country but are unsure how to reach it.
