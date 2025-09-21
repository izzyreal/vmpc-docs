.. _install:

Install
=======
VMPC2000XL can be installed in Linux, macOS, iPadOS and Windows.

The recommended way to use VMPC2000XL is in standalone mode. The original is a complex piece of equipment with `a 200 page manual <https://www.platinumaudiolab.com/free_stuff/manuals/Akai/akai_mpc2000xl_manual.pdf>`_. `Roger Linn <https://en.wikipedia.org/wiki/Roger_Linn>`_ poured a tremendous amount of interconnecting functionality in the MPC2000XL's ancestors: the MPC60 and the MPC3000. A modern computer, let alone a full-fledged DAW, offers a lot of distraction from all this, leading to a more superficial understanding of the MPC.

On the other hand, the usefulness of a DAW can't be denied, and it's great to load an instrumental beat that was made on a real 2000XL, and run it through your favorite software effects, via 10 individual mono outputs if you wish. You can also let VMPC2000XL control your software instruments via MIDI. Or maybe you want to add some of the MPC workflow to your projects just for some parts of the beat.

Because VMPC2000XL is available in standalone, LV2, AU, AUv3 and VST3 formats, it's completely up to the user where and how to run it.

Linux package installation (openSUSE, Ubuntu, Debian, Raspbian, Mageia and Fedora)
----------------------------------------------------------------------------------
Please follow the instructions below for

* `standalone <https://software.opensuse.org//download.html?project=multimedia%3Aproaudio&package=vmpc2000xl>`_ (openSUSE, Ubuntu, Debian, Raspbian, Mageia and Fedora)
* `LV2 <https://software.opensuse.org//download.html?project=multimedia%3Aproaudio&package=lv2-vmpc2000xl>`_ (Fedora, Mageia, openSUSE)
* `VST3 <https://software.opensuse.org//download.html?project=multimedia%3Aproaudio&package=vst3-vmpc2000xl>`_ (Fedora, Mageia, openSUSE)

There are binaries available for x86_64/amd64, and in some cases aarch64/arm64.

The :code:`VMPC2000XL` standalone executable will be installed in :code:`/usr/bin`.

On 64 bit systems the LV2 will be installed in :code:`/usr/lib64/lv2`, and the VST3 in :code:`/usr/lib64/vst3`.

On 32 bit systems the LV2 will be installed in :code:`/usr/lib/lv2`, and the VST3 in :code:`/usr/lib/vst3`.

.. _manual_installation_for_ubuntu:

Manual installation (Ubuntu 20)
-------------------------------

#. Visit https://izmar.nl/downloads.
#. Download the binary you need.
#. Optionally download `the demo beats <https://github.com/izzyreal/mpc/tree/master/demo_data>`_ and save them into :file:`~/Documents/VMPC2000XL/Volumes/MPC2000XL`.

As per the `Filesystem Hierarchy Standard <https://www.pathname.com/fhs/pub/fhs-2.3.html#PURPOSE23>`_, the recommended location to store the portable `VMPC2000XL` executable, is in :file:`/usr/local/bin`.

As per the `LV2 docs <https://lv2plug.in/pages/filesystem-hierarchy-standard.html>`_, the recommended location to store :file:`VMPC2000XL.lv2` is one of these:

* :file:`~/.lv2/`
* :file:`/usr/local/lib/lv2/`
* :file:`/user/lib/lv2/`

As per the `VST3 docs <https://steinbergmedia.github.io/vst3_dev_portal/pages/Technical+Documentation/Locations+Format/Plugin+Locations.html#on-linux-platform>`_, the recommended location to store :file:`VMPC2000XL.vst3` is one of these:

* :file:`~/.vst3/`
* :file:`/usr/local/lib/vst3/`
* :file:`/user/lib/vst3/`

Building from source
--------------------

If you wish to build VMPC2000XL from source, please follow `the instructions here <https://github.com/izzyreal/vmpc-juce>`_.

Additionally the project has been set up in such a way that alternative front-ends can be implemented. See `the source code <https://github.com/izzyreal/vmpc-juce>`_ of the JUCE implementation, for a reference implementation.

The main idea for an alternative front-end is to do what `vmpc-juce <https://github.com/izzyreal/vmpc-juce>`_ (i.e. the mainline VMPC2000XL release, whose manual you're reading now) is doing. It exchanges audio i/o with, and directs controller input into, `mpc <https://github.com/izzyreal/mpc>`_. It also presents a view on the state of this library's core entity, :code:`mpc::Mpc`, and its children, to the user. This presentation can be for example an ASCII terminal or a hardware LCD, and the controller input can come from a custom-built MPC-like controller.

Install using the installers (macOS/Windows)
--------------------------------------------

#. Visit https://izmar.nl/downloads.
#. Download the installer you need and run it.
#. Follow the installer's instructions.

The installers allow you to select which formats (standalone, LV2, VST3 and AU) to install. After installation you can move plugins from their default directories (see below) to anywhere you like.

macOS
+++++
The macOS installer deploys Universal 2 binaries of VMPC2000XL standalone, LV2, VST3 and AU. When you install the standalone variety, the AUv3 comes with it -- it is embedded in the application. You need to run the standalone application at least once in order for AUv3 hosts to detect the AUv3. The other plugin formats are installed in :file:`/Users/you/Library/Audio/Plug-Ins`.

.. admonition:: Important note regarding AUv3 on macOS

    Currently the AUv3 implementation is lacking a way to import and export documents (sounds, sequences and other files that make up your projects). The iPadOS AUv3 implementation has this functionality, and it will come to macOS as well, but it's currently not certain when. This renders the macOS AUv3 less interesting for many serious applications. If you are affected by this, for now it is recommended to use the AUv2 implementation. If your host only reveals the AUv3, and not the AUv2, even though you have both installed, you can remove either the complete :file:`VMPC2000XL.app` standalone bundle from :file:`/Applications`, or you can remove the AUv3 :file:`PlugIns` directory that is embedded in :file:`/Applications/VMPC2000XL.app/Contents/PlugIns`. In some hosts, it's not obvious which format of VMPC2000XL you're currently running. To verify which format you're running, see :ref:`The About window <the_about_window>`.

Windows
+++++++
The Windows installer deploys 64 bit binaries on 64 bit systems, and 32 bit binaries on 32 bit systems, in standalone, LV2 and VST3 formats. The LV2 is installed into :file:`C:\\Program Files\\Common Files\\LV2` on 64 bit systems, :file:`C:\\Program Files (x86)\\Common Files\\LV2` on 32 bit systems. The VST3 is installed into :file:`C:\\Program Files\\Common Files\\VST3` on 64 bit systems, :file:`C:\\Program Files (x86)\\Common Files\\VST3` on 32 bit systems.

.. admonition:: Important note for Windows users

    If you experience missing DLL errors when attempting to run VMPC2000XL after a successful installation procedure, you are probably missing a Microsoft update which you can grab from here: https://support.microsoft.com/en-us/help/2977003/the-latest-supported-visual-c-downloads

Update
------
If you have installed VMPC2000XL before, the installer may offer various options to migrate your previous configuration and user data. Please run the installer to see what applies to your system.

It is recommended to regularly backup your sounds, programs, sequences and other VMPC2000XL documents, especially right before updating VMPC2000XL.

Moreover, the update process may not always succeed in cleaning up the old application files. Please refer to the Uninstall section below if you come across any files you'd like to delete, or simply want to clean up what can be.

Uninstall
---------

Linux
+++++

If you have installed VMPC2000XL as a package, use your package manager (:code:`apt`, :code:`dnf`, etc.) to uninstall it.

For manual installations, see :ref:`Manual installation (Ubuntu 20) <manual_installation_for_ubuntu>` for the likely locations where you can :code:`rm` any VMPC2000XL binaries.

macOS
+++++
Remove :file:`/Applications/VMPC2000XL.app`.

Plugins can be removed from :file:`/Library/Audio/Plug-Ins`.

iPadOS
++++++

Tap and hold the VMPC2000XL icon in your Home Screen and tap "Remove App".

Windows
+++++++

Run the VMPC2000XL uninstaller you have in Add/Remove Programs.

Assuming you have installed VMPC2000XL into its default location, on 64 bit systems you can manually delete the empty directory :file:`C:\\Program Files\\VMPC2000XL` afterwards. On 32 bit systems, you can delete :file:`C:\\Program Files (x86)\\VMPC2000XL`.

VST3 plugins can be removed from :file:`C:\\Program Files\\Common Files\\VST3`, :file:`C:\\Program Files (x86)\\Common Files\\VST3` or any other locations where you store plugins.

Cleanup
+++++++

For a full cleanup including demo beats, configuration files and user data (your sounds, sequences, etc.), refer to the `File Locations`_ section below and delete from those what you wish.

File Locations
--------------

For locations of the executable and plugin binaries, refer to the `Uninstall`_ section above. The discussion below is limited to all other files that are installed and generated by VMPC2000XL. Each of the files mentioned here are safe to delete, and VMPC2000XL will regenerate sane defaults.

There are two categories of files, each in their platform-specific locations. These platform-specific locations are discussed in detail further below, but first we take a look at the categories and which files are in it:

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
    * Audio/MIDI configuration (only for standalone, not plugins): :file:`VMPC2000XL.settings`
    * USB volumes: :file:`volumes.json`

Demo beats are bundled into the application. When you start VMPC2000XL, a check is performed to see if a :file:`DEMOS` directory exists in your user data directory. If not, a fresh copy of the original demo data will be placed in :file:`VMPC2000XL/Volumes/MPC2000XL/DEMOS`.

Resources that are absolutely required by the application, such as LCD background images and the metronome click PCM WAV data, are bundled into the application as well, making VMPC2000XL fully portable and self-contained.

Linux
+++++

**Documents** :file:`~/Documents/VMPC2000XL`

**Configuration files** :file:`~/.config/VMPC2000XL/config` and :file:`~/.config/VMPC2000XL.settings`

macOS
+++++

**Documents** :file:`/Users/you/Documents/VMPC2000XL`

**Documents (AUv3)** :file:`~/Library/Containers/nl.izmar.vmpc2000xl.vmpc2000xlAUv3/Data/Documents`

**Configuration files** :file:`/Users/you/Library/Application Support/VMPC2000XL/config` and :file:`/Users/you/Library/Application Support/VMPC2000XL.settings`

**Configuration files (AUv3)** :file:`~/Library/Containers/nl.izmar.vmpc2000xl.vmpc2000xlAUv3/Data/Library/Application Support/VMPC2000XL/config`

iPadOS
++++++

**Documents standalone and AUv3** App group sandbox. The exact location is undisclosed (by iPadOS) and the only way to access these is via VMPC2000XL itself. You can share documents (via AirDrop or to save them to Files) via the :ref:`Export button <export_share_files_and_folders>`. You can listen to, and remove, your direct-to-disk recordings via the :ref:`Recording Manager button <manage_recordings>`.

**Configuration files** App group sandbox.

Windows
+++++++

**Documents** :file:`C:\\Users\\you\\Documents\\VMPC2000XL`

**Configuration files** :file:`C:\\Users\\you\\AppData\\Roaming\\VMPC2000XL\\config` and :file:`C:\\Users\\you\\AppData\\Roaming\\VMPC2000XL\\VMPC2000XL.settings`
