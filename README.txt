This repository holds source code for Skyfear's launch script. I made this public in the interest of trust, security, and accomodations making the game runnable.

Why does this exist?
Skyfear was made in a source-compiled version of Unreal Engine 4.21, which does not support a change made by Intel on their SHA references to OpenSSL in newer CPUs. There are two articles about this here, https://dovetailgames.freshdesk.com/en/support/solutions/articles/80000968751-intel-10th-gen-cpus-causing-crashes-on-older-ue4-games, https://www.intel.com/content/www/us/en/developer/articles/troubleshooting/openssl-sha-crash-bug-requires-application-update.html, and I've included .pdf copies of these articles in this repository in case the original pages are gone someday. Reasons why I cannot fix this in the game engine itself are complicated, Skyfear is very intertwined with the 4.21 version and changing that would be months-a year of work.

The solution was a script that generates a compatible environment to straighten out any issues like this before running the game. What `launcher.py` does is it creates a shell session in which the troublesome environment variable(s) are corrected, and runs the game through that. This happens non-destructively, the user's device does not need to make any system changes.

Collaboration:
I encourage programmers to look for improvements that may improve trustworthyness and flexibilty. Please use the issue tracker for this.

Security:
To report security issues specifically, please do not use the public issue tracker. Instead, please contact protoriastudios@gmail.com or @telekrex on Discord.