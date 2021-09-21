Controls
========

There are 3 ways to control VMPC2000XL:

* Keyboard
* Mouse/touchscreen
* MIDI

It is **strongly recommended** to get familiar with :ref:`basic keyboard shortcuts <basic_operations>` rather than relying on the mouse. The more keyboard shortcuts you use, likely the greater the sense of immersion.

The other buttons are also mapped to keyboard shortcuts, but you can pick these up as you go.

.. note::

  The degree of MIDI controllability is the same as on the real MPC2000XL, i.e. not every button can be mapped to a MIDI control change parameter, and there's a limit to 4 mappings at a given moment.

Keyboard
--------

Below are the default keyboard shortcuts for most of the UI components.

Some letter keys are written in uppercase for disambiguation. For example, :code:`Record` is mapped to the letter :kbd:`L` and is written in uppercase to clarify it is not letter :kbd:`i` or number :kbd:`1`, so there is no need to press :kbd:`Shift` here.

In the same vein some special characters are clarified by appending their name in parentheses, for example :kbd:`; (semicolon)`.

.. note::

  The default keyboard mapping is geared towards US keyboard layout, but it's fully configurable. See :ref:`Configuring the keyboard <configuring_the_keyboard>` for instructions.

.. _basic_operations:

Basic operations
++++++++++++++++

================== ==================
Operation          Key(s)
================== ==================
Up/Down/Left/Right Up/Down/Left/Right
Data wheel up/down +/-
Numeric keypad     0 ... 9
Shift              Left shift
Record             L
Overdub            ; (semicolon)
Stop               ' (quote)
Play               Space
Play start         \\ (backslash)
F1 ... F6          F1 ... F6
Main screen        Escape
Open window        i
================== ==================

Pads
++++

+-+-+-+-+
|g|h|j|k|
+-+-+-+-+
|b|n|m|,|
+-+-+-+-+
|a|s|d|f|
+-+-+-+-+
|z|x|c|v|
+-+-+-+-+

Advanced operations
+++++++++++++++++++

====================== ======
Operation              Key(s)
====================== ======
Bank A                 Home
Bank B                 End
Bank C                 Insert
Bank D                 Delete
Previous step/event    q
Next step/event        w
Locate/Go to           e
Previous bar/Start     r
Next bar/End           t
Tape tempo/Note repeat y
Full level             o
16 levels              p
Next seq               [
Track mute             ]
====================== ======

VMPC-specific operations
++++++++++++++++++++++++

======================= ==================================
Operation               Key(s)
======================= ==================================
Direct-to-disk recorder Shift + Play start (defaults to L)
======================= ==================================

Mouse & touchscreen
-------------------

Pads
++++

The pads can be hit by by clicking them with the mouse, or, if you have a touchscreen, by touching them. The further away from the center of the pad, the lower the velocity. When a pad is hit, it will light up blue.

Buttons
+++++++

All buttons can be pressed by clicking them with the mouse, or, if you have a touchscreen, by touching them.

Data wheel
++++++++++

The data wheel can be turned by dragging or scrolling. Precise, single-step changes can be performed by holding any of the modifier keys (Shift, Ctrl, Alt/Option) while dragging.

Slider/Rec gain/Main volume
+++++++++++++++++++++++++++

These controls can be operated by dragging or scrolling.

.. note::

  If your mouse or touchpad emits momentum/inertia events, VMPC2000XL will process these accordingly. The data wheel, slider, rec gain and main volume controls will come to a gradual stop.

MIDI
----

Please refer to the `MPC2000XL manual <https://www.platinumaudiolab.com/free_stuff/manuals/Akai/akai_mpc2000xl_manual.pdf>`_ (p185) to see the details of assigning MIDI Continuous Controllers to MPC2000XL functionality.
