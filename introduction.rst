.. _introduction:

Introduction
============

VMPC2000XL is an emulator of the `Akai MPC2000XL <https://www.akaipro.com/mpc2000xl>`_ sampling sequencer. It is free and open source, and it works on the most popular platforms: Linux, MacOS and Windows. For all three platforms there is a standalone desktop application version. For Linux there are LV2 and VST3 plugins, for MacOS there are AU and VST3 plugins, and for Windows there's a VST3 plugin variety.

Conceived by Izmar, VMPC2000XL started early 2014 as a vehicle for learning how to program. The first iterations were `written in Java <https://github.com/izzyreal/vmpc-java>`_. Java's memory model, however, makes it inherently impossible to implement low-latency, glitch-free, realtime audio applications.

In 2016 an effort to port VMPC2000XL to C++ was initiated. The first ports were based on
`WDL OL <https://github.com/olilarkin/wdl-ol>`_ and then the VST2 SDK. Ultimately the project settled on `JUCE <https://juce.com/>`_, mainly for its ability to target all popular platforms and plugin formats.

Open Source
-----------

VMPC2000XL is Free and Open Source, with a GPL3 license. Check out the source code and issue tracking (for questions and support, reporting bugs and requesting features and improvements) at https://github.com/izzyreal/mpc/issues and https://github.com/izzyreal/vmpc-juce/issues.

Behavioral emulator
-------------------

VMPC2000XL is a *behavorial* rather than a *hardware* emulator.

Good examples of hardware emulators are the many game console and arcade machine emulators available today. These model the CPU and other relevant circuitry of consoles and arcade machines, allowing you to run any copy of a game ROM, cartridge or CD that would run on the original hardware.

The same can be done for the early MPCs. A crude implementation of the MPC3000 is being worked on `in MAME <https://github.com/mamedev/mame/blob/master/src/mame/drivers/mpc3000.cpp>`_.

VMPC2000XL, however, models the *behavior* of the MPC2000XL as a whole. The source code of VMPC2000XL knows nothing about the microprocessors, DACs and other hardware of the MPC2000XL. Contrary to the MAME implementation, VMPC2000XL is not capable of running the original MPC OS.

In this approach we essentially care more about *what* can be done, rather than *how* it is done. The idea is that at the cosmetic and functional levels the emulator is similar enough to substitute the original in certain conditions.

More than a hundred LCD screens have been reproduced, in most cases with pixel-precision. Their functionalities have been reverse engineered and implemented from scratch. The application is congruent with the main functional specifications of the original:

* 64-track sequencer
* 99 sequences in memory at once
* 32 simultaneous playback voices
* digital sampling of sound
* MIDI in/out

Additionally the MPC2000XL's native file formats have been reverse engineered, allowing exchange of SND, PGM, APS, MPC2000XL MID and ALL files. If you have a real MPC2000XL, you can load and modify its projects in VMPC2000XL and vice versa. This functionality can be combined with VMPC2000XL's :ref:`direct-to-disk recording <direct_to_disk_recording>` to solve the common problem of multi-tracking or "tracking out" to a DAW -- a common operation when working toward a final mixdown of a hiphop beat. Instead of hooking up your hardware MPC2000XL to an audio interface, you can now load your projects into VMPC2000XL and bounce them to up to 5 individual stereo WAV files in a matter of seconds.

Stability
---------

At the time of writing, the latest version of VMPC2000XL is 0.4. The project is still in a phase of taking shape and fixing crucial bugs, though much progress has been made in the past year.

VMPC2000XL 0.4 is stable enough for hobbyists who can forgive the odd crash. But before 1.0 has been reached, VMPC2000XL is not recommended for professional use, certainly not in a live setting.
