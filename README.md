# Skyfear Launch Script
This repository contains the source code of Skyfear's launch script, as well as the complete set of tools used to compile and ship it. I am making this part of the game open source in the interest of trust, security, and improvements to accomodations making the game runnable.

## History
Skyfear was made in a source-compiled version of Unreal Engine 4.21, which did not support a change made by Intel on their SHA references to OpenSSL -- very nuanced and annoying type of bug. There are two articles about this issue included here, https://dovetailgames.freshdesk.com/en/support/solutions/articles/80000968751-intel-10th-gen-cpus-causing-crashes-on-older-ue4-games, https://www.intel.com/content/www/us/en/developer/articles/troubleshooting/openssl-sha-crash-bug-requires-application-update.html, and I've included pdf copies of these articles in this repository in case they ever went offline in the future. Reasons why I cannot fix this in the game engine itself are complicated, Skyfear is very intertwined with the 4.21 version and changing that would be several months of work - leaving the rest of the game untouched.

## Solution
The solution was to create a script that attempts to straighten out any issues like this before running the game, and because this will be in a script format and open source, I hope that this can serve as a platform to address any future compatibility issues as well.

## Issues, Collaboration
I encourage any programmer to look for improvements to this script that may improve its trustworthyness and flexibilty. Please use the issue tracker to submit anything you've got. For *security issues specifically*, please do that privately - send to `protoriastudios@gmail.com`, or hit me up on Discord `@telekrex`.