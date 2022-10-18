.. _introduction:

Introduction
============
VMPC2000XL is an emulator of the `Akai MPC2000XL <https://www.akaipro.com/mpc2000xl>`_ sampling sequencer. It is free and open source, and it works on the most popular platforms: Linux, macOS, iOS and Windows. For all four platforms there is a standalone application version. For Linux there are LV2 and VST3 plugins, for MacOS there are AU and VST3 plugins, for iOS there is an AUv3 version, and for Windows there's a VST3 plugin variety. Experimental LV2 support for macOS and Windows is on its way.

Conceived by Izmar, VMPC2000XL started early 2014 as a vehicle for learning how to program. The first iterations were `written in Java <https://github.com/izzyreal/vmpc-java>`_. The fact that Java has a garbage collector, however, doesn't make it very suitable for low-latency, glitch-free, realtime audio applications. Almost no professional audio software is written in garbage-collecting languages for this reason, and the same goes for domains like realtime video and high-frequency trading.

For that reason in 2016 an effort to port VMPC2000XL to C++ was initiated. The first ports were based on
`WDL OL <https://github.com/olilarkin/wdl-ol>`_ and a bit later the VST2 SDK. Ultimately the project settled on `JUCE <https://juce.com/>`_, mainly for its ability to target all popular platforms and plugin formats.

Open Source
-----------
VMPC2000XL is Free and Open Source, with a GPL3 license. Check out the source code and issue tracking (for questions and support, reporting bugs and requesting features and improvements) at https://github.com/izzyreal/mpc/issues and https://github.com/izzyreal/vmpc-juce/issues.

Behavioral emulator
-------------------
VMPC2000XL is a *behavorial* rather than a *hardware* emulator.

Good examples of hardware emulators are the many game console and arcade machine emulators available today. These model the CPU and other relevant circuitry of consoles and arcade machines, resulting in a virtual machine. This virtual machine allows you to run any unmodified copy of a game ROM, cartridge or CD that would run on the original hardware.

The same can be done for the early MPCs. A crude implementation of the MPC3000 is being worked on `in MAME <https://github.com/mamedev/mame/blob/master/src/mame/drivers/mpc3000.cpp>`_.

VMPC2000XL, however, models the *behavior* of the MPC2000XL as a whole, rather than its parts that make it a computer: the CPU, memory, BIOS and so on. The source code of VMPC2000XL knows nothing about the microprocessors, DACs and other hardware that resides inside the MPC2000XL. Contrary to the MAME implementation of the MPC3000, VMPC2000XL is not, and does not aim to be, capable of running the original MPC OS.

In this approach we essentially care more about *what* can be done, rather than *how* it is done. The idea is that at the cosmetic and functional levels the emulator is similar enough to substitute the original in certain conditions.

More than a hundred LCD screens have been reproduced, in most cases with pixel-precision. Their functionalities have been reverse engineered and implemented from scratch. VMPC2000XL is congruent with the main functional specifications of the original:

* 64-track sequencer
* 99 sequences in memory at once
* 32 simultaneous playback voices
* digital sampling of sound
* MIDI in/out

Very little functionality has been altered or added, so in most cases to know something about VMPC2000XL equals knowing something about the MPC2000XL.

Additionally the MPC2000XL's native file formats have been reverse engineered, allowing exchange of SND, PGM, APS, MPC2000XL MID and ALL files. If you have a real MPC2000XL, you can load and modify its projects in VMPC2000XL and vice versa. This functionality can be combined with VMPC2000XL's :ref:`direct-to-disk recording <direct_to_disk_recording>` to solve the common problem of multi-tracking or "tracking out" to a DAW -- a common operation when working toward a final mixdown of a hiphop beat. Instead of hooking up your hardware MPC2000XL to an audio interface, you can now load your projects into VMPC2000XL and bounce them to up to 5 individual stereo WAV files in a matter of seconds.

Stability
---------
At the time of writing, the latest version of VMPC2000XL is 0.5.0. A huge amount of effort for this release has gone into ironing out bugs and making behaviour more like the original. Moreover, all causes of crashes that I'm aware of have been addressed.
