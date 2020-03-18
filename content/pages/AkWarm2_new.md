Title: What's New in AkWarm 2 compared to AkWarm 1.03
URL: /AkWarm/AkWarm2_new.html
Save_As: AkWarm/AkWarm2_new.html

Although the primary objective of Phase 1 of the AkWarm Modernization Project
was to replicate the functionality of the original AkWarm software program
(version 1.03d) using modern software development tools, some new features are
available in the AkWarm 2 release. A listing of most of those features is
below.

#### Microsoft Vista Compatibility

Unlike the AkWarm 1.03d, AkWarm 2 runs on the Microsoft Vista operating
system, as well as running on Windows XP Service Pack 2 (SP2) or later.

#### Select Energy Library to Use

From the opening screen in AkWarm 2 where you can start a new Rating or open
an existing one, you also have the option to pick which Energy Library you
want to use when calculating Ratings. This feature is available as the "Switch
Library ..." option on the File menu. If you don't utilize this option, the
most recent Energy Library will be used for calculations. However, see the
next paragraph for a situation where using an older Energy Library is useful.

The new 3/13/2009 Energy Library for AkWarm 2 (and the 2/12/2009 Library for
AkWarm 1.03d) has a more accurate efficiency rating for a Conventional Natural
Gas Boiler. For a rating done with a prior version of the Library involving
this type of heating system, the Rating Points will be different if calculated
with AkWarm 2. To be fair, you can use the older library efficiency values to
do a Post rating on such a home. The "Switch Library" feature makes it easy to
utilize an older Energy Library in a rating.

#### Long File Names

File names are no longer limited to only 8 characters. Up to 255 characters can be
used for the directory path plus file name.

#### Multiple Homes can be Open

More than one home can be open simultaneously in the AkWarm program. This
facilitates comparisons between different homes.

#### Built-In Retrofit Reporter

The Retrofit Reporter software, which allows creation of a detailed and nicely
formatted Improvement Options report in Microsoft Word format, is now built
into the main AkWarm software instead of being a separate add-on program.

#### Ventilation Improvement Available

As one of the standard improvement options, you can analyze the addtion of a
ventilation system without heat recovery or a heat recovery ventilator.

#### Sophisticated Area and Volume Calculator

The Shell Component Area and Home Volume input boxes have a number of new
useful features. First, you are not limited to two lines of entry; expressions
can be entered on many separate lines for clarity. Second, labels ending in a
colon can appear at the beginning of each line to help you remember what part
of the component or home the expression refers to. Finally, feet and inches
can be used in the expressions using the standard ' and " notations. An
example of a valid Volume entry is:
    
    First Floor: 40 * 30 * 8
    Second Floor: 30 * 30 * 8'6"
    Third Floor: 20'4" * 24'6" * 8'3"

#### Garage Wizard Complies with Rating Policy

The Garage Wizard now creates all of its components at the Living Space
temperature, in compliance with Rating policy. Relative to AkWarm 1, this
reduces workload and diminishes the chance for error.

#### CFM at 50 Pascals is Primary Blower Door Input

Instead of Air-change-per-hour being the primary blower door test input, CFM
at 50 Pascals is used. Changes in the volume input will not cause the CFM @ 50
Pa input to change.

#### Better Editing and Display of Shell Components

All editing of Shell components now occurs on the main screen, without the
need for pop-up editing dialogs. Components are now organized by type; for
example, all Wall components appear together in the list of shell components.
Also, the list of shell components contains calculated R-values and areas,
performing the function of the "Summmarize" button in the old AkWarm.

#### Simpler Selection of Heating and Hot Water Systems

The list of space heating and domestic hot water heating systems are now
organized into categories (e.g. forced air, hydronic, direct) to facilitate
finding the correct system. Also, a preview of the assumed AFUE or Energy
Factor for each system is shown.

#### Improved Editing of Improvement Information

The description of the Location of an improvement can now be edited by the
user. Also, Notes, Location, and Boilerplate to include can be edited from
both the input screens and from the list of improvements on the output screen.

#### Rating Number Line Shows Plus Levels

Plus levels are now shown on the Rating Number Line graphic shown on the
output screen and on the Rating Certificate, making it easier to see how close
a home is to the next higher Rating level.

#### Reporting/Printing Improvements

Any printer can be selected prior to printing AkWarm reports. The Energy Cost
and Features report now fits on one page in most situations. The Energy Flows
report is now nicely formatted with clear column alignment. Reports are more
ink-efficient through use of cross-hatching instead of solid fills for bar
graphs.

#### No Log-In Screen at Startup

A log-in screen does _not_ appear at start up. Instead, log-in is only
required when you attempt to save a rating as an Official Rating, which is
accomplished through a button on the Rating output screen. Also, there is no
need to manually enter an Official Rating Point total.

#### Much Improved Error Tolerance and Reporting

If an unexpected error occurs in the application, the user is given a chance
to enter a comment and send the problem file to the developers. Also, the user
can return to the program and save their work.

Also, rating inputs are checked real-time for validity; improper inputs are
marked with red exclamation points if they need attention.

#### Smaller Energy Library Files

Energy library files are now only about 100 KB in size, instead of nearly 1
MB, facilitating faster download and e-mail of the files.

