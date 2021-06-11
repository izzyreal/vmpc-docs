.. _install:

Install
=======

VMPC2000XL can be installed in Linux, MacOS and Windows. The current version should run reliable enough to satisfy enthousiasts and hobbyists, given the fact that they can `report bugs and request features <http://izmar.nl/index.php/bug-reports-feature-requests>`_ by contacting the author. 

Stability is roughly equal for the standalone and plugin versions, though your best bet is the standalone version. Standalone is the recommended way to use VMPC2000XL for other reasons too -- the original is a complex piece of equipment with `a 200 page manual <https://www.platinumaudiolab.com/free_stuff/manuals/Akai/akai_mpc2000xl_manual.pdf>`_. `Roger Linn <https://en.wikipedia.org/wiki/Roger_Linn>`_ poured a tremendous amount of interconnecting functionality in the MPC2000XL's ancestors, the MPC60 and the MPC3000. A modern computer, let alone a full-on DAW, offers a lot of potential distraction from all this.

On the other hand, the usefulness of a DAW can't be denied -- it's great fun to load up an instrumental you made on a real 2000XL and run it through your favorite software effects, via 10 individual mono outputs if you wish. Let VMPC2000XL control your software instruments via MIDI. Or maybe you want to add some of the MPC workflow to your projects just for parts of the beat.

By exposing VMPC2000XL in standalone, LV2, AU and VST3 formats it is completely up to you.

.. _manual_installation_for_ubuntu:

Manual installation (Ubuntu 18)
-------------------------------

At the moment there is no package of VMPC2000XL for any Linux distribution. If all goes well and the project is in good enough shape, and if enough Linux audio users ask for packages, these will hopefully become available.

Some effort was put into making VMPC2000XL more attractive for the Linux community, for example by following the `XDG Base Directory Specification <https://specifications.freedesktop.org/basedir-spec/basedir-spec-latest.html>`_. Various self-contained standalone and LV2 Ubuntu builds are provided. You can `generate ninja and Make build files <https://github.com/izzyreal/vmpc-workspace>`_.

Suggestions, or even better, contributions, to improve the Linux side of VMPC2000XL are welcome.

For now the recommended process for Ubuntu 18 is as follows:

* Visit http://izmar.nl/index.php/downloads
* Download what you need, place it where you want and run it
* Optionally download `the demo beats <https://github.com/izzyreal/mpc/tree/master/demo_data>`_ and save them into :file:`~/Documents/VMPC2000XL/Volumes/MPC2000XL`.

As per the `Filesystem Hierarchy Standard <https://www.pathname.com/fhs/pub/fhs-2.3.html#PURPOSE23>`_, the recommended location to store the portable `VMPC2000XL` executable is in :file:`/usr/local/bin`.

As per the `LV2 docs <https://lv2plug.in/pages/filesystem-hierarchy-standard.html>`_, the recommended location to store :file:`VMPC2000XL.lv2` is one of these:

* :file:`~/.lv2`
* :file:`/usr/local/lib/lv2`
* :file:`/user/lib/lv2`

The standalone is built with JACK support, which is the recommended driver type to use.

The LV2 has run successfully in Carla.

Builds for other distributions can be requested, or made by yourself.

Building from source
--------------------

You should be able to build VMPC2000XL on many platforms, for example most Linux distributions.

If you wish to build the VMPC2000XL JUCE implementation as is, which is the implementation used for the available binaries, please follow `the instructions here <https://github.com/izzyreal/vmpc-workspace>`_.

Additionally the project has been set up in such a way that alternative front-ends can be implemented. Start exploring `the source code <https://github.com/izzyreal/vmpc-workspace>`_ of the JUCE implementation.

The main idea for an alternative front-end is to do what `vmpc juce <https://github.com/izzyreal/vmpc-juce>`_ is doing, i.e. exchange audio i/o with and direct controller input into `mpc <https://github.com/izzyreal/mpc>`_ and present the state of this library's core entity, :code:`Mpc`, and its children, to the user. This presentation can be for example an ASCII display, a hardware LCD or a `vector GUI <https://github.com/izzyreal/vmpc>`_, and the controller input can come from a dedicated MPC-like board. A `somewhat functional VR concept <https://github.com/izzyreal/vmpc-unreal-plugin>`_ was implemented in Unreal.

Install using the installers (MacOS/Windows)
--------------------------------------------

* Visit http://izmar.nl/index.php/downloads
* Download the installer you need and run it
* Follow the installer's instructions

The installers allows you to select which format(s) (standalone, VST3 and AU) you want to install. After installation you can place move plugins from their default directories (see below) to anywhere you like.

MacOS
+++++
The MacOS installer deploys universal binaries, compatible with Intel and Apple Silicon systems, in standalone, VST3 and AU formats. Plugins are installed in :file:`/Users/you/Library/Audio/Plug-Ins`.

Windows
+++++++
The Windows installer deploys 64 bit binaries on 64 bit systems, and 32 bit binaries on 32 bit systems, in standalone and VST3 formats. The VST3 is installed into :file:`C:\\Program Files\\Common Files\\VST3` on 64 bit systems, :file:`C:\\Program Files (x86)\\Common Files\\VST3` on 32 bit systems.

.. admonition:: Important note for Windows users

    If you experience missing DLL errors when attempting to run VMPC2000XL after a successful installation procedure, you are probably missing a Microsoft update which you can grab from here: https://support.microsoft.com/en-us/help/2977003/the-latest-supported-visual-c-downloads

Update
------

If you have installed VMPC2000XL before, the installer may offer various options to migrate your previous configuration and user data. Please run the installer to see what applies to your system.

In general it is recommended to regularly backup your data, especially before right updating VMPC2000XL.

Additionally the update process may not always succeed in cleaning up the old application files. Please refer to the Uninstall section below if you come across any files you'd like to delete, or simply want to clean up what can be.

Uninstall
---------

MacOS
+++++
Remove :file:`/Applications/VMPC2000XL.app` for v0.3 and later. Remove :file:`/Applications/vMPC.app` if you have v0.2 or older.

Plugins can be removed from :file:`/Library/Audio/Plug-Ins`.

Windows
+++++++
Run any VMPC2000XL and vMPC uninstallers you have in Add/Remove Programs.

Assuming you have installed VMPC2000XL into its default location, you can manually delete :file:`C:\\Program Files\\VMPC2000XL` and :file:`C:\\Program Files\\vMPC` afterwards. On 32 bit systems, and some v0.2 and older installations on 64 bit systems, you can delete the same directories from :file:`C:\\Program Files (x86)`.

VST3 plugins can be removed from :file:`C:\\Program Files\\Common Files\\VST3`, :file:`C:\\Program Files (x86)\\Common Files\\VST3` or any other locations where you store plugins.

Linux
+++++
As per the `Filesystem Hierarchy Standard <https://www.pathname.com/fhs/pub/fhs-2.3.html#PURPOSE23>`_, you have likely placed your portable :file:`VMPC2000XL` executable in :file:`/usr/local/bin`.

As per the `LV2 docs <https://lv2plug.in/pages/filesystem-hierarchy-standard.html>`_, you likely have your :file:`VMPC2000XL.lv2` in one of these locations and can remove it from there:

* :file:`~/.lv2`
* :file:`/usr/local/lib/lv2`
* :file:`/user/lib/lv2`

Cleanup
+++++++
For a full cleanup including demo beats, configuration files and user data (your sounds, sequences, etc.), refer to the `File Locations`_ section below and delete from those what you wish.


File Locations
--------------

For locations of the executable and plugin binaries, refer to the `Uninstall`_ section above. The discussion below is restricted to all other files that are installed and generated by VMPC2000XL.

There are three categories of files:

#. **Demo recovery data:** Demo beats that are never modified by VMPC2000XL
#. **Documents:**
    * Everything you create: :file:`VMPC2000XL/Volumes/MPC2000XL`
    * Direct-to-disk recordings: :file:`VMPC2000XL/Recordings`
    * Log file: :file:`VMPC2000XL/vmpc.log`
#. **Configuration files:**
    * Keyboard mapping: :file:`config/keys.txt`
    * NVRAM data (main screen user defaults): :file:`config/nvram.vmp`
    * VMPC2000XL-specific: :file:`config/vmpc-specific.ini`
    * Audio/MIDI configuration and auto-save data: :file:`VMPC2000XL.settings`

On MacOS and Windows, demo data is bundled into the installer, which places it in a safe location from which it can always be restored. When you start VMPC2000XL, a check is performed to see if a :file:`DEMOS` directory exists in your user data directory. If not, a fresh copy of the original demo data will be placed in :file:`VMPC2000XL/Volumes/MPC2000XL/DEMOS`.

Resources that are absolutely required by the application, such as background images and the metronome click PCM WAV data, are bundled into the executables and plugins, making them fully portable and self-contained. Hence you will not find such files anywhere in your filesystem.

Linux
+++++
**Demo recovery data** Unavailable

**Documents** :file:`~/Documents/VMPC2000XL`

**Configuration files** :file:`~/.config/VMPC2000XL/config` and :file:`~/.config/VMPC2000XL.settings`

MacOS
+++++
**Demo recovery data** :file:`/Library/Application Support/VMPC2000XL/DemoData`

**Documents** :file:`/Users/you/Documents/VMPC2000XL`

**Configuration files** :file:`/Users/you/Library/Application Support/VMPC2000XL/config` and :file:`/Users/you/Library/Application Support/VMPC2000XL.settings`

Windows
+++++++
**Demo recovery data** :file:`C:\\Users\you\\AppData\\Roaming\\VMPC2000XL\\DemoData`

**Documents** :file:`C:\\Users\\you\\Documents\\VMPC2000XL`

**Configuration files** :file:`C:\\Users\\you\\AppData\\Roaming\\VMPC2000XL\\config` and :file:`C:\\Users\\you\\AppData\\Roaming\\VMPC2000XL\\VMPC2000XL.settings`


File Locations (v0.3 and lower)
-------------------------------

In older releases most non-application files are stored in :file:`/Users/you/vMPC` on MacOS and Windows. 

On Linux most non-application files are stored in :file:`/home/you/vMPC`.

When you are cleaning up, you can remove this :file:`vMPC` directory completely, or you can backup your sounds, sequences, programs and so on from :file:`vMPC/Stores/MPC2000XL`.

On Windows audio/MIDI preferences are saved in :file:`C:\\Users\\you\\AppData\\Roaming\\vmpc.settings`.

On MacOS this is :file:`/Users/you/Library/Application Support/vmpc.settings`.

On Linux it is :file:`~/.config/vmpc.settings`.
