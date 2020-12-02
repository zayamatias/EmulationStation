EmulationStation
================

This is a fork of a fork EmulationStation for RetroPie.
EmulationStation is a cross-platform graphical front-end for emulators with controller navigation. 

HOWTO (for RPI4):

Clone Git & Compile Emulationstation:

`cd`  
`git clone --recursive https://github.com/RetroPie/EmulationStation.git`  
`cd EmulationStation`  
`cmake -DUSE_MESA_GLES=On -DRPI=On  .`  
`make`  

Copy `emu.py` to your home directory:

`cp /home/pi/EmulationStation/emu.py /home/pi/.`

Copy `default.jpg` to your home directory:

`cp /home/pi/EmulationStation/default.jpg /home/pi/.`

Backup autostart (so you can go to your normal emulationstation afterwards)

`sudo cp  /opt/retropie/configs/all/autostart.sh  /opt/retropie/configs/all/autostart.sh.old`

Edit your autostart and change 

`emulationstation #auto` (or something similar) to `/home/pi/emu.py`

Oh, and you will net to get fim (image viewer)

`sudo apt install fim` 

`reboot`

Considerations:
===============

Two import things:

System marquees should be present in the theme you're using as (theme.xml):
`<theme>
    ...
    <view name="system">
        <image name="marquee">
            <path>./art/system.png</path>
         </image>
     ...`

Which also means marquees for system can be specific for each theme, hopefully nice theme makers will pick up this feature

Game marquees should be defined in the gamelist.xml file as:

`<gameList>
     <game>
      ....
         <marquee>/home/pi/RetroPie/roms/3do/marquees/1C4E0F77EB28C0B4FAA49CE4C866E8791C563A83-marquee.png</marquee>
       ....
       </game>`
       
If no marquee is found, it will display the default marquee (default.jpg from here, but feel free to change it)

Extras
======

As you can see emu.py receives the names of the marquees to display, so if you modify emu.py you could do whatever you want, send them to anotehr pi, turn off lights, you name it...


For game marquees downloading, see my scraper https://github.com/zayamatias/sscraper, it will download the marquees if avaiable and add them to the gamelist.xml
