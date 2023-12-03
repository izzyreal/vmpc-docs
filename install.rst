.. _install:

Install
=======
VMPC2000XL can be installed in Linux, macOS, iOS and Windows.

The recommended way to use VMPC2000XL is in standalone mode. The original is a complex piece of equipment with `a 200 page manual <https://www.platinumaudiolab.com/free_stuff/manuals/Akai/akai_mpc2000xl_manual.pdf>`_. `Roger Linn <https://en.wikipedia.org/wiki/Roger_Linn>`_ poured a tremendous amount of interconnecting functionality in the MPC2000XL's ancestors, the MPC60 and the MPC3000. A modern computer, let alone a full-on DAW, offers a lot of distraction from all this.

On the other hand, the usefulness of a DAW can't be denied -- it's great to load up an instrumental made on a real 2000XL and run it through your favorite software effects, via 10 individual mono outputs if you wish. You can also let VMPC2000XL control your software instruments via MIDI. Or maybe you want to add some of the MPC workflow to your projects just for parts of the beat.

By releasing VMPC2000XL in standalone, LV2, AU, AUv3 and VST3 formats it's completely up to you where and how you run it.

Install ZYpp packages (openSUSE, Ubuntu, Debian and Fedora)
-----------------------------------------------------------
Please follow the instructions below for

* `standalone <https://software.opensuse.org//download.html?project=multimedia%3Aproaudio&package=vmpc2000xl>`_ (openSUSE, Ubuntu, Debian and Fedora)
* `LV2 <https://software.opensuse.org//download.html?project=multimedia%3Aproaudio&package=lv2-vmpc2000xl>`_ (Fedora, openSUSE)
* `VST3 <https://software.opensuse.org//download.html?project=multimedia%3Aproaudio&package=vst3-vmpc2000xl>`_ (Fedora, openSUSE)

There are binaries available for x86_64, and for Tumbleweed aarch64 as well. There are also some Fedora binaries.

The :command:`VMPC2000XL` standalone executable will be installed in :command:`/usr/bin`.

On 64 bit systems the LV2 will be installed in :command:`/usr/lib64/lv2`, and the VST3 in :command:`/usr/lib64/vst3`.

On 32 bit systems the LV2 will be installed in :command:`/usr/lib/lv2`, and the VST3 in :command:`/usr/lib/vst3`.

.. _manual_installation_for_ubuntu:

Manual installation (Ubuntu 20)
-------------------------------
At the moment there is no package of VMPC2000XL for Ubuntu yet, but word on the street is it's in the making.

.. note::
   For Linux packager people: As per version 0.5.0, VMPC2000XL's Linux build process fully relies on CMake, and portable source packages suitable for offline builds can be generated with ease.

Some effort was put into making VMPC2000XL more attractive for the Linux community, for example by following the `XDG Base Directory Specification <https://specifications.freedesktop.org/basedir-spec/basedir-spec-latest.html>`_. Various self-contained standalone and LV2 Ubuntu builds are provided. Building from source should be straight-forward via `the vmpc-juce repo <https://github.com/izzyreal/vmpc-juce>`_.

Suggestions, or even better, contributions, to improve the Linux side of VMPC2000XL are welcome.

For now the recommended process for Ubuntu 20 is as follows:

* Visit https://izmar.nl/downloads
* Download the binary you need, place it where you should and run it
* Optionally download `the demo beats <https://github.com/izzyreal/mpc/tree/master/demo_data>`_ and save them into :file:`~/Documents/VMPC2000XL/Volumes/MPC2000XL`.

As per the `Filesystem Hierarchy Standard <https://www.pathname.com/fhs/pub/fhs-2.3.html#PURPOSE23>`_, the recommended location to store the portable `VMPC2000XL` executable is in :file:`/usr/local/bin`.

As per the `LV2 docs <https://lv2plug.in/pages/filesystem-hierarchy-standard.html>`_, the recommended location to store :file:`VMPC2000XL.lv2` is one of these:

* :file:`~/.lv2/`
* :file:`/usr/local/lib/lv2/`
* :file:`/user/lib/lv2/`

As per the `VST3 docs <https://steinbergmedia.github.io/vst3_dev_portal/pages/Technical+Documentation/Locations+Format/Plugin+Locations.html#on-linux-platform>`, the recommended location to store :file:`VMPC2000XL.vst3` is in one of these:

* :file:`~/.vst3/`
* :file:`/usr/local/lib/vst3/`
* :file:`/user/lib/vst3/`

The standalone is built with JACK support, which is the recommended driver type to use for getting the lowest latency. Alternatively use ALSA. PulseAudio also works, but it is the option with the highest latency.

Builds for other distributions can be requested, or made by yourself.

Building from source
--------------------
You should be able to build VMPC2000XL on many platforms, for example most Linux distributions.

If you wish to build VMPC2000XL from source, please follow `the instructions here <https://github.com/izzyreal/vmpc-juce>`_.

Additionally the project has been set up in such a way that alternative front-ends can be implemented. Start exploring `the source code <https://github.com/izzyreal/vmpc-juce>`_ of the JUCE implementation, which, in this context, serves as a reference implementation.

The main idea for an alternative front-end is to do what `vmpc juce <https://github.com/izzyreal/vmpc-juce>`_ is doing, i.e. exchange audio i/o with, and direct controller input into, `mpc <https://github.com/izzyreal/mpc>`_, and present the state of this library's core entity, :code:`Mpc`, and its children, to the user. This presentation can be for example an ASCII display, a hardware LCD or a `vector GUI <https://github.com/izzyreal/vmpc>`_, and the controller input can come from a dedicated MPC-like board. A `somewhat functional VR concept <https://github.com/izzyreal/vmpc-unreal-plugin>`_ was implemented in Unreal.

Install using the installers (macOS/Windows)
--------------------------------------------
* Visit https://izmar.nl/downloads
* Download the installer you need and run it
* Follow the installer's instructions

The installers allows you to select which formats (standalone, VST3 and AU) to install. After installation you can move plugins from their default directories (see below) to anywhere you like.

macOS
+++++
The macOS installer deploys Universal 2 binaries of VMPC2000XL standalone, VST3 and AU. When you install the standalone variety, the AUv3 comes with it -- it is embedded in the application. You need to run the standalone application at least once before AUv3 hosts pick up on it. The other plugins are installed in :file:`/Users/you/Library/Audio/Plug-Ins`.

Windows
+++++++
The Windows installer deploys 64 bit binaries on 64 bit systems, and 32 bit binaries on 32 bit systems, in standalone and VST3 formats. The VST3 is installed into :file:`C:\\Program Files\\Common Files\\VST3` on 64 bit systems, :file:`C:\\Program Files (x86)\\Common Files\\VST3` on 32 bit systems.

.. admonition:: Important note for Windows users

    If you experience missing DLL errors when attempting to run VMPC2000XL after a successful installation procedure, you are probably missing a Microsoft update which you can grab from here: https://support.microsoft.com/en-us/help/2977003/the-latest-supported-visual-c-downloads

Update
------
If you have installed VMPC2000XL before, the installer may offer various options to migrate your previous configuration and user data. Please run the installer to see what applies to your system.

It is recommended to regularly backup your data, especially right before updating VMPC2000XL.

Moreover, the update process may not always succeed in cleaning up the old application files. Please refer to the Uninstall section below if you come across any files you'd like to delete, or simply want to clean up what can be.

Uninstall
---------
Linux
+++++
See :ref:`Manual installation (Ubuntu 20) <manual_installation_for_ubuntu>` for the likely locations where you can :command:`rm` any VMPC2000XL binaries.

macOS
+++++
Remove :file:`/Applications/VMPC2000XL.app`.

Plugins can be removed from :file:`/Library/Audio/Plug-Ins`.

.. note::
   If you are an existing user and the last time you tried VMPC2000XL was a while ago, you might have a :file:`vMPC.app`, which should also be removed.

iOS
+++
Tap and hold the VMPC2000XL icon in your Home Screen and tap "Remove App".

Windows
+++++++
Run the VMPC2000XL uninstaller you have in Add/Remove Programs.

Assuming you have installed VMPC2000XL into its default location, you can manually delete :file:`C:\\Program Files\\VMPC2000XL` afterwards. On 32 bit systems, and some v0.2 and older installations on 64 bit systems, you can delete :file:`C:\\Program Files (x86)\\VMPC2000XL`.

VST3 plugins can be removed from :file:`C:\\Program Files\\Common Files\\VST3`, :file:`C:\\Program Files (x86)\\Common Files\\VST3` or any other locations where you store plugins.

.. note::
   If you are an existing user and the last time you tried VMPC2000XL was a while ago, you might have a :file:`vMPC` directory in your :file:`Program Files`/:file:`Program Files (x86)`, which can also be removed.

Cleanup
+++++++
For a full cleanup including demo beats, configuration files and user data (your sounds, sequences, etc.), refer to the `File Locations`_ section below and delete from those what you wish.

File Locations
--------------
For locations of the executable and plugin binaries, refer to the `Uninstall`_ section above. The discussion below is restricted to all other files that are installed and generated by VMPC2000XL. Each of the files mentioned here are safe to delete, and VMPC2000XL will regenerate sane defaults.

There are two categories of files:

#. **Documents**
     * Everything you create: :file:`VMPC2000XL/Volumes/MPC2000XL`
     * Direct-to-disk recordings: :file:`VMPC2000XL/Recordings`
     * Log file: :file:`VMPC2000XL/vmpc.log`
     * MIDI control presets: :file:`VMPC2000XL/MidiControlPresets`
     * Auto-save data: :file:`VMPC2000XL/AutoSave`

#. **Configuration files**
    * Keyboard mapping: :file:`config/keys.txt` (only present when you have changed the default mapping)
    * NVRAM data (main screen user defaults): :file:`config/nvram.vmp`
    * VMPC2000XL-specific: :file:`config/vmpc-specific.ini`
    * Audio/MIDI configuration: :file:`VMPC2000XL.settings`
    * USB volumes: :file:`volumes.json`

Demo beats are bundled into the executables and plugins. When you start VMPC2000XL, a check is performed to see if a :file:`DEMOS` directory exists in your user data directory. If not, a fresh copy of the original demo data will be placed in :file:`VMPC2000XL/Volumes/MPC2000XL/DEMOS`.

Resources that are absolutely required by the application, such as LCD background images and the metronome click PCM WAV data, are also bundled into the executables and plugins, making VMPC2000XL fully portable and self-contained. Hence you will not find such files anywhere in your filesystem.

Linux
+++++
**Documents** :file:`~/Documents/VMPC2000XL`

**Configuration files** :file:`~/.config/VMPC2000XL/config` and :file:`~/.config/VMPC2000XL.settings`

macOS
+++++
**Documents** :file:`/Users/you/Documents/VMPC2000XL`

**Configuration files** :file:`/Users/you/Library/Application Support/VMPC2000XL/config` and :file:`/Users/you/Library/Application Support/VMPC2000XL.settings`

iOS
+++
**Documents standalone** :file:`On My iPad/VMPC2000XL`

**AUv3** Not visible due to a limitation beyond my control, subject to change

**Configuration files** Unknown

Windows
+++++++
**Documents** :file:`C:\\Users\\you\\Documents\\VMPC2000XL`

**Configuration files** :file:`C:\\Users\\you\\AppData\\Roaming\\VMPC2000XL\\config` and :file:`C:\\Users\\you\\AppData\\Roaming\\VMPC2000XL\\VMPC2000XL.settings`
