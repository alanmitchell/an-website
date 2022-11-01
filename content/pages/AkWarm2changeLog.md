Title: AkWarm Change Log
URL: /AkWarm/AkWarm2changeLog.html
Save_As: AkWarm/AkWarm2changeLog.html

This page describes the changes that have occurred in the various releases of
AkWarm 2. The versions are listed from the most recent to the oldest.
#### Version 2.11.0 (October 31, 2022)
1. Miscellaneous Bug Fixes
2. New "Supplemental - Pre" and "Supplemental - Post" rating types.


#### Version 2.10.0 Beta (March 27, 2019) and Final (April 16, 2019)
1. New Energy Library.
2. New formula for required ventilation to meet new BEES/IECC requirements.
3. Additional input for 'Living Space' blower door test result.
4. Additional input for living space/garage common wall area.
5. Minor formatting changes on Rating Certificate report.
6. Require As-Is and Post ratings to be uploaded to ARIS before printing as 'official'.
7. Fix bug for combo-type DHW efficiencies.
8. Update HomeEnergyScore interface to use new API.

#### Version 2.9.0 Beta (April 19, 2018) and Final (April 30, 2018)
1. For official BEES, require a client's email. Add a checkbox for no email service.
2. Prompt user to enter a price per ton of wood pellets, if this type of system is selected.
3. Several changes to the spot and whole-house ventilation section of the Air tab.
4. For older files that did not have a Max. Flow Rate: On opening in the new version, populate the Mechanical Ventilation Flow Rate from the Design Heat Loss Inputs section into the Max Flow Rate section of the Mechanical Ventilation on the Air Tab.
5. Add identification for 'high temp' and 'low temp' distribution for hydronic heating to match IOR recommendation.
6. Side Arm Efficiency: if a side-arm unit is selected, auto-populate the energy factor based on the standard de-rate (EF=Primary System Efficiency -5%); Flag files for review if user override value is input.  Include popup if user entry ‘justification of sidearm efficiency required if library value is not used'.
7. Allow multiple file uploads at a time when using 'Add Image'.
8. Improved hpxml and HomeEnergyScore integration (still in beta).
9. Fix AHRI Links on Heater and DHW tabs (the old links were broken).

#### Version 2.8.0 Beta (Sepember 7, 2017) and Final (September 27, 2017)
1. Added an Above-Grade Masonry Wall shell component.
2. Disabled the "Unconditioned Space" option for DHW location.
3. Added a "Garage Heater" option for HealthSafetyAppliance inspections
4. Disabled the Oven and Range CO input boxes for non-oven HealthSafetyAppliances.
5. Added a (beta) menu option to export the current AkWarm file to hpxml. Most, but not all, of the content from the AkWarm inputs are mapped to the hpxml output. We are interested in feedback from users about if/how this is used and could be improved.
6. Added a (beta) menu option and dialog to submit the current AkWarm file through the HomeEnergyScore API. This feature has not yet been approved for producing official HomeEnergyScore labels, and the use of this feature requires a username/password. Contact AHFC if you are interested in helping to test this feature.

#### Version 2.7.1 (March 28, 2017)
1. New Climate Data in Energy Library
2. Updated Fuel and Electricity Prices in Energy Library
3. Ability to itemize a subset of all lights/appliance loads and have AkWarm fill in the remaining electricity consumption based on standard AkWarm Low/Medium/High Appliance usage.
4. Bug fix to code that determines whether a file has changed or not.
5. Updated error handling for ARIS uploads.
6. Modify Ventilation warning language.
7. Modify the language in the "Additional Information" section to remove the WH EF notification.
8. Modify the language in the CSR for Wx files to be "Assessor" and "Weatherization Operations Manual".

#### Version 2.6.1 (August 12, 2016)
  1. Files must now be first uploaded to ARIS before they can be Saved as Official.
  2. Energy savings in MMBtu are now shown on the Audit Report for AkWarm-Commercial.
  3. If an SHGC value is manually entered, a corresponding U-Value must also be manually entered.
  4. Miscellaneous changes related to BEES compliance.
  5. A new August 9, 2016 Energy Library with updated Fuel and Electric prices is included.

#### Version 2.5.3 (March 10, 2016)
  1. Renewable Energy Systems are now included in the energy analysis and Energy Rating.  Both thermal and electrical production systems can be included.
  2. Substituted a BEES-specific Rating certificate for BEES ratings.
  3. Added a Combustion Safety Report and refined the Combustion Safety Inputs, ensuring that tests are present for all combustion appliances.
  4. Remove the prior PUR-101 report and the BEES Checklist.
  5. Implemented tests for Spot Ventilation that are required for BEES ratings.
  5. Require a user-entered U-Value for a window if a user-entered SHGC is provided.
  6. Fixed a bug related to HRVs that caused them to be evaluated as Unbalanced ventilation systems in certain circumstances.
  7. Fixed the AkWarm Installer to work properly on computers that have not had a prior version of AkWarm installed.
  8. Changed the Ductwork insulation level to R-19 (previously was R-3).
  9. Allowed Self-Generation as a choice for every location.
  10. Added the 2016-03-07 library with new fuel/utility prices and four new garage doors.

#### Version 2.4.1 (April 1, 2015)
  1. For any rating that uses the new 3/30/2015 Energy Library or a future library, the domestic hot water usage assumption was changed to 15.2 gallons/person/day.  The old assumption of 20.0 gallons/person/day will still be used for old ratings so that their rating score will be unaffected.
  2. The Energy Star Home Performance logo was added to the Rating Certificate for ratings other than BEES and Ratings from Plans.
  3. If the heating system is more than 25% oversized in a BEES rating, a BEES Warning is issued, as opposed to a BEES failure.
  4. The Setback Thermostat BEES compliance test was removed (including removal from the checklist).
  5. Three other items were removed from the required BEES checklist: air handler leakage test, Energy Efficiency certificate posting, high efficiency lighting.
  6. Editing of the summary improvements table in the Improvement Options Report was disabled.
  7. The required amount of ventilation for ASHRAE 62.2 compliance is displayed in the Ventilation Inputs section.
  8. Fixed a bug that erroneously reverted changes to the "Ventilation System has controls..." checkbox.
  6. A new installer was created that should support remote install.
  7. The 3/30/2015 Energy Library was added with updated Fuel and Electric prices and an increase in three DHW Energy Factors to comply with RESNET DHW efficiency minimums.

#### 2/4/2015 Energy Library (February 4, 2015)
  1. Released a new Energy Library that has two equipment choices for Steam and Hot Water District Heat.  These were inadvertantly lost after the 9/24/2013 Library.

#### Version 2.3.3.1 (December 17, 2014)
  1. AkWarm-Commercial Bug Fixes
    1. Fixed a bug that caused a crash when there were no improvements in the file or no cost-effective improvements.
    2. The Setup program failed to install the Long Audit Report template file.  Now fixed.
    3. Greatly sped up Calculate time for files that include Generic Loads.
    4. Fixed a bug that disabled the ability to edit the Lighting Equipment description when an "Other" lamp is selected.

#### Version 2.3.3.0 (December 9, 2014)
  1. Substantially changed the content and formatting of the PUR 101 report for BEES Ratings.
  2. For homes with mechanical ventilation systems, the maximum flow rate of the system can now be entered. This flow is then compared against the BEES required ventilation flow rate for the home.
  3. Design Heat Load Analysis
    1. For the Primary Heating System, the user can choose to include the garage heat load and the Domestic Hot Water heat load if the primary system serves those loads.  The total load served by the primary heating system is now calculated and displayed in the Design Heat Loss report.
    2. The domestic hot water heat load is now explicitly calculated if it is being served by the primary heating system.
    3. The main home ventilation rate can now be tied to the ventilation inputs in on the "Air" tab.
    4. The heating output capacity of the existing primary heating system can be entered, and this output is compared against the results from the Design Heat Load analysis.  The same comparison is used to determine whether the heating system complies with the 25% oversizing limit for BEES ratings.
  2. Increased the estimated seasonal efficiency of ground-source heat pumps, to be more consistent with the efficiency estimation approach used for other heating systems.
  3. User entry of a window U-value now also requires entry of an SHGC value for the window, since both are available on the rating label.
  2. The default computer window size for the application has been increased due to the prevalence of high resolution screens.
  3. Edited the Improvement descriptions and the user-selectable boilerplate that is included in the Improvement Options Report.
  3. Energy Library Changes
    1. Updated fuel and utility prices.
    1. Increased the default efficiencies for numerous heating system types to make these efficiencies more consistent with the actual savings observed from heating system retrofits.
  2. Bug Fixes
    1. When changing from a oil or gas heating system to a Heat Pump, a combustion test efficiency entered for the fuel-fired heating system would override the efficiency calculation for the heat pump, causing the efficiency used for the heat pump to be too low.  This has been fixed.
    1. Entering 0" into an arithmetic expression caused the expression to be improperly evaluated.  This has been fixed.
  2. AkWarm-Commercial changes
    1. Added Before-Improvement and After-Improvement Fuel Use to the Executive Summary of the Long Report.
    1. Added a summary table on the Improvements Results screen totaling important values for all improvements and for all cost-effective improvements. Totals are also displayed for any set of improvements that the user selects on the screen.
    1. CO2 savings were added to improvement summary tables in the long report.

#### Version 2.3.2.1 (April 16, 2014)
  1. Released 2014-04-11 Energy Library, which updates fuel and utility rates.  Also included in the Library are a number of air-source and ground-source heat pumps.  AkWarm now automatically adjusts heat pump efficiencies for the climate where the home is located.  A number of Heat Pump replacement improvements are included in the library.  
  2. All LED lamps in the commercial lamp table in the Energy Library were increased in efficacy to 100 lumens/Watt.
  3. Metlakatla and Larsen Bay are now designated as Special Hydro cities.
  4. A few user actions that could cause false "Did Not Calculate" warnings were fixed.
  5. A "Generic Load" model was added to the Commercial version, which allows modeling of heat-consuming end uses such as heated community water supply, heated water storage tanks, sidewalk snowmelt systems, and swimming pools.

#### Version 2.3.1.0 (September 24, 2013)

  1. Changed the format of the Energy Rating Certificate.
  2. Added a PUR 101 report for BEES certification.
  3. Added Space Heating Equipment selections compatible with the District Steam and Hot Water fuel types.

#### Version 2.3.0.1 (July 1, 2013)

  1. Changed the threshold for 5 star to 89 points. Added a 6 star level at 95 points. Allowed Rating Points to goes as high as 110 points.
  2. Implemented changes related to the 2012 BEES standard, including setting compliance to the 5 star 89 point level, requiring air tightness of less than 4 ACH at 50 Pa, and providing a checklist of mandatory items for compliance.
  3. Changed the Southcentral Alaska reference house to have the same reference R-value for walls and floors as Southeast Alaska.
  4. Added an Energy Efficiency Sticker report.
  5. Fixed a bug that caused an erroneous setting of the "Did Not Calculate Flag" in the AkWarm file.
  6. Fixed a bug in the Design Heat Loss section that could crash AkWarm.
  7. Fixed a bug that affected AkWarm-Commerical files containing schedules with a date that only occurs during Leap Years.

#### Version 2.2.0.4 (August 14, 2012)

  1. Fixed a bug that caused the Rating Date (Residential) and the Audit Date (Commercial) to display as today's date instead of the actual date previously entered by the user.
  2. Clarified the description of results in the Residential Design Heat Loss Report.
  3. Added the 8/6/2012 Energy Library with updated fuel and utility prices.

#### Version 2.2.0.3 (May 29, 2012)

  1. Added checkbox for identfiying whether a storm door is installed. Prior to this feature, the Energy Library was forced to contain many combinations of door types both with and without storm doors.
  2. Added inputs for directly entering certified U-values of Entry Doors and Garage Doors.
  3. For the Residential software only:
    1. Included detailed inputs and a new report for calculating the Design Space Heating Load for the home.
    2. Garage components can now be entered at Garage temperature instead of Living Space temperature. This improves the accuracy of the energy estimates, design heat loss estimates, and improvement savings estimates while not affecting the rating score assigned to the home.
    3. Added inputs to allow for the recording of CO and pressure health and safety measurements for combustion appliances.
    4. Added inputs and graphs to allow the user to compare actual fuel and electric usage to the fuel usage predicted by AkWarm.
  4. For the Commercial software only:
    1. Added the ability to specify operation and maintenance savings and improvement lifetime for Ventilation improvements.
    2. Added the Actual Fuel Use versus AkWarm-predicted Fuel Use graphs to an appendix in the Long Energy Audit Report.
    3. Software now allows improvement lives up to 50 years. Prior limit was 30 years.
    4. If maintenance cost savings are entered for an improvement, that input is shown in the Short and Long Audit Reports.
    5. Added a feature to fill out a custom Excel template with data from AkWarm. This feature can be used to create custom graphs and tables using AkWarm inputs and calculated results.
    6. Added the ability to export an AkWarm file to XML format, a standard format readable by many other software packages.
    7. For determining average utility cost ($/kWh and $/ccf) in the Fuel Cost dialog, used a higher assumed usage in the calculation to produce more accurate results for rate structures with large customer charges.
  5. Energy Library Changes (4/6/2012 Library)
    1. Removed door types that included storm doors, since there is a new checkbox input for indicating whether a door has a storm door.
    2. Added "Polyurethane - Agribalance" as an insulation option.
    3. Added an uninsulated wood sectional garage door.
  6. Fixed bugs, including:
    1. Have included data validation so that entering an Improvement Life beyond the acceptable range (now 50 years) does not cause a crash.
    2. Fixed a bug causing erratic improvement calculation restults that occurred in the Commercial software when the "Uncontrolled Heat Output" input was non-zero and heat gains from disribution fans and pumps were significant.
    3. Fixed a bug that only affected results archived in ARIS; the bug resulted in multiple calculated fuel use records to be archived instead of just the last set of calculations (only affected Commercial software).
    4. Reduced the memory required to process files with large image attachments.
    5. Fixed a problem with the Log Diamter input that caused a new value not to be stored properly.
    6. Fixed a problem where Commercial Electrical Load Retrofit Life input was not visible when using large screen fonts.
    7. Put in the correct Zip Code for Kongiganak.
    8. Fixed a bug where files having a filename containing one of the five characters: & > < ' " would always fail the "File not Calculated" test.

#### Version 2.1.4 (February 27, 2012)

  1. Provided a checkbox input that allows the user to identify the walls that contain windows and doors. As part of this change, the user now can tell AkWarm to deduct windows and doors from the above-grade portion of below-grade walls.
  2. Added a warning that triggers when AkWarm is exited that tells the user that they have changed inputs and not recalculated results. Leaving the AkWarm file in this state means that the inputs are not consistent with the last-calculated results.
  3. When the User brings up the dialog that allows direct entry of fuel and utility prices, the average utility prices shown were based on using 1,000 units (kWh or CCF) of the fuel per month. Now, 500 units of usage are assumed for the Residential software, and 1,500 units are assumed for the Commercial software.
  4. For the Commercial software only:
    1. Added inputs to allow the specification of the life of the HVAC, cooking, and clothes drying improvements.
    2. Added an on-screen table and a section in the Long Audit Report to display electrical peak demand.
    3. Added Glycol and Steam as choices for the heat transfer medium for heating/cooling plants.
    4. Included internal gains as an offset in the Design Heating Load calculation.
    5. Included the AkWarm and Energy Library version numbers at the end of the Long and Short Audit reports.
    6. More accurately estimated the contribution of internal gains to cooling loads.
  5. Energy Library Changes
    1. Updated Fuel and Utility prices and price escalation rates.
    2. Additional Types of EPS rigid foam listed and updated R-values.
    3. Various Commercial door types added and inclusion of a Tree control for easier selection of the door type.
    4. More R-value levels for the rigid foam below-grade floor improvement.
    5. Added a Broken or Missing Glazing Glass type.
  6. Fixed bugs, including:
    1. The contribution of cooling plants to electrical peak demand was being overestimated in most situations. The error was largest when large wattage distribution systems were present. This bug was fixed.
    2. Fixed a bug related to the validation of shell component inputs.

#### Version 2.1.3 (December 21, 2011)

  1. For the Commercial software, added a menu item on the File menu to remove any schedules that are not currently being used.
  2. For the Commercial software, added an input for Maintenance Cost Savings associated with an improvement. The input is present for the HVAC improvement, all Electrical Load improvements, Cooking improvements, and Clothes Drying improvements.
  3. For the Residential software, if the user itemizes lights and appliances, they are included in the energy calculations and the analysis of improvements. Itemized lights and appliances do not affect the rating score.
  4. Included the ability to add Images and PDFs to be stored in the Residential AkWarm file.
  5. Added the ability to select the sections to include in the Residential Improvement Options report, if the report is printed from the Reports tab.
  6. Added an optional Solar Heat Gain Coefficient (SHGC) input for windows. NFRC window labels generally have this tested value.
  7. Improved the below-grade heat loss algorithm and made it more consistent with ASHRAE recommended methods.
  8. Fixed various bugs. A parial list is:
    1. For pumps and fans using the "On Time Schedule" control strategy, the selected schedule would reset back to the first schedule in the list if the pump/fan dialog was reopened. This bug was fixed.
    2. Added the missing Refrigeration end use to the Commercial Long and Short Audit reports.
    3. Allowed the last retrofit heating plant, cooling plant, and distribution system to be fully visible on the screen.
    4. Fixed a bug that would cause an error when the same PDF file was opened twice in a row from the list of images/PDFs.
    5. Fixed a bug related to the Expand button used for the HVAC retrofit description.
    6. Fixed a bug related to the HVAC Retrofit Same as Existing checkbox causing an error.
    7. Stopped RTF reports from printing out multiple copies in some situations.

#### Version 2.1.2 (September 7, 2011)

  1. Added a detailed Lights and Appliances module to the Residential software that allows Raters to record individual lights and appliances in the home. Currently, the module does not affect energy use or rating calculations, and therefore is only useful for data collection purposes. In a future release, the lights and appliances information will be used in the energy use calculation.
  2. Added a detailed Energy Audit Report to the Commercial Software that provides more energy analysis results and explanatory text than the current short audit report.
  3. Added an ARIS Location ID field to the Commercial software.
  4. Includes the new 8/25/2011 Energy Library with updated fuel and utility prices.
  5. Fixed various bugs:
    1. The View/Adjust library cost feature did not work for Setback thermostats and caused an application crash if invoked. This bug was fixed.
    2. The View/Adjust library cost feature would cause an application crash if the home/building's city was not first selected. Now, a message appears telling the user that a city must be selected prior to using the feature.
    3. Fixed a memory exhaustion error that occurred when many pumps/fans were entered. Fixing the problem also improved performance of the feature. Applied this same fix to a number of other list entry components, such as Building Spaces and Images.
    4. Allowed natural gas appliances to be used in cities without a natural gas utility in the Energy Library, since the user can directly enter a natural gas price in that situation.

#### Version 2.1.1 (August 1, 2011)

  1. Added a feature to view and easily adjust the improvement costs that come from the Energy Library. The feature also allows the user to deselect any R-value levels or heating efficiency levels that the user does not want to be recommended by the improvement analysis process.
  2. For Residential homes, allowed the use of Natural Gas in all communities, since the user can manually enter a Natural Gas price if one is not present in the Energy Library.
  3. For Commercial buildings, removed unused energy end uses from the end use bar graph present in the Short Audit Report.
  4. For Commercial buildings, fixed a bug related to not storing the building's energy use after improvements are applied.

#### Version 2.1.0 (July 11, 2011)

  1. Combined AkWarm Commercial into the standard AkWarm Residential program so both Residential Ratings and Commercial Audits can be performed with the same program.
  2. Relative to AkWarm Residential version 2.0.6.1, the following changes were made:
    1. The Design Heat Loss after implmentation of each improvement is included in both the Weatherization and Rater IOR reports.
    2. The Fuel Prices used in the analysis are shown on the Rating screen and in both the Weatherization and Rater IOR reports.
    3. Any fuel prices can now be entered by the User, even if those prices are present in the Energy Library. For situations where the User must enter a fuel price, the fuel price dialog does *not* appear every time the Calculate button is clicked; it is now a pop-up dialog invoked from the Client screen.
    4. The Savings-to-Investment-Ratio, SIR, is shown on the Improvements screen and in the Weatherization IOR report.
    5. The Life of each improvement measure is shown on the Weatherization IOR report.
    6. The Weatherization IOR report now includes a table showing the MMBtu of Fuel Use by Fuel Type for the As-Is home and the home with all Improvements.
    7. The "Notes to the Homeowner" are now printed in both the Weatherization and Rating IOR reports.
  3. Relative to AkWarm Commercial version 1.1.1, the following changes were made:
    1. The images in the audit report now print in the order they were entered.
    2. Fixed a bug related to losing the Notes entry for an image.
    3. Fixed a bug related to setting the air tightness improvement method of entry.
  4. For both Residential and Commercial versions:
    1. The loading of the Energy Library at program start-up is much faster.
    2. Fixed a bug in the Arithmetic Expression evaluator related to handling of inches.

#### Version 2.0.6 (Apr 6, 2010)

  1. Includes a report to determine whether the home complies with the Federal $2,000 Homebuilder Tax Credit program. This report is temporarily disabled, pending approval of AkWarm by the IRS.
  2. Has the ability to print the Cost by Component graph and add a note to the printed report to describe the graph. This print feature is accessed by a print button on the Cost by Component screen.
  3. Peforms Automatic Energy Library updates. If any new Energy Libraries are released, they will be automatically downloaded from the Internet and installed by the AkWarm program. AkWarm checks for updates each time it starts up, assuming an Internet connection is available.
  4. Notifies the user if the version of AkWarm is out of date. Each time AkWarm starts up, it will notify the user if a more current version of the AkWarm program is available for download. The user must still manually initiate the download and installation of the new version.
  5. Includes a cooling model to estimate the energy use of a cooling system. Cooling energy use is now incorporated into many of the AkWarm reports. The addition of the cooling model was required for determining compliance with the Federal Homebuilder Tax Credit.
  6. Makes it possible to have a Below-Grade Wall component that is totally above-grade. This allows the unique wall construction types that were only available to below-grade walls to be used for above-grade walls.
  7. Includes a Rater signature line on the Rating certificate. Fixes problems with printing overlap in the footer of the Rating certificate.
  8. Has the ability to enter a second client/homeowner name.
  9. Adds new rating types, including Weatherization As-Is, Weatherization Post, Public Housing As-Is, and Public Housing Post.
  10. Has the floor area of the garage as an input, clearly separated from the entry of the living space floor area.
  11. Eliminates the warning about a differing number of perimeter and center below-grade floor components, because such a situation frequently occurs.
  12. Changes to the Improvement Options Report include:
    1. For Weatherization rating types, includes estimated improvement costs but still hides costs for other rating types.
    2. Indicates that Increased Rating Points are only estimates, with exact values determined by a Post rating.
    3. If the same Boilerplate item is included multiple times in a report, it is only printed once; subsequent instances of the boilerplate item refer back to the first printed instance.
  13. The 3/24/2010 Energy Library is included in the release and is updated as follows:
    1. Fuel costs and utility rates are updated, including their projected price escalation factors.
    2. The R-values of garage doors (and replacement door improvements) are reduced to comport with test data that measures the performance of the entire door.
    3. Adds DHW system options for a sidearm tank off of a wood boiler.
    4. Makes the Wood Stove replacement improvements consistent with the wood stove efficiencies in the Energy Library. Allows for three different replacements: non-catalytic stove, catalytic stove, and pellet stove.
    5. Includes a more complete set of heat distribution options for Ground-Source heat pumps and electric resistance heat.
  14. Various Bug Fixes:
    1. Eliminates an AkWarm error that was caused by blanking out entries in the Floor Area Calculator.
    2. Corrects an error where AkWarm, in certain situations, would erroneously suggest to use an older Energy Library when a file was being opened. The correct Energy Library is now suggested or automatically used.
    3. Until now, changing the fuel type of the dryer or cooking range has affected the Energy Rating score. For ratings using the 3/24/2010 Energy Library or later, the fuel type of the dryer or range will not affect the rating score.

#### Version 2.0.5 (Sep 23, 2009)

  1. A substantial upgrade to the shape-based Area Calculator was done. The new calculator can model any shape with straight sides (e.g. octagons), calculating both perimeter and center areas. The shape is now stored with the shell component it is associated with so that future edits to the shape can be made.
  2. When an old file is opened that used a prior Energy Library, AkWarm stops to ask if the user wants to continue to use the original Energy Library with the rating or wants to use the most current library. This feature replaces the "Switch Library" feature that was in the prior version of AkWarm. Note that only historical AkWarm 2 Energy Libraries are available for use; if the rating was done with an AkWarm 1 library, the best matching AkWarm 2 library is used if the user wants to continue to use a historical library.
  3. A report is now available on the File menu that prints all of the user-entered inputs to the AkWarm rating.
  4. Various changes to the Improvement Options Report were made including:
    1. For ratings performed with the current Energy Library, estimated improvement cost information is no longer shown, due to the large uncertainty in the cost estimates. If a rating is performed with a library of version 4/10/2009 or earlier, the cost estimates are shown in order to closely replicate the Improvement Options Report that was originally presented to the homeowner.
    2. An explanatory note was added to explain that the points shown on the report for each measure assume that all prior measures are completed.
    3. All references to brand names were removed from the report.
  5. A new Energy Library, version 9/5/2009, was produced including updated fuel and utility costs, more insulation levels for some shell improvements, and more accurate data for improvements that add insulation to attics.
  6. The Design Heat Loss calculation results on the Energy Flows report are described more accurately, and the estimate of Heating System _Input_ size was removed. The design heat loss of the conditioned space is still calculated; only the estimate of the input rating of the heating system has been removed.
  7. The Rating Type (e.g. As-Is, Post Improvement) is now printed in the footer of the Rating Certificate.
  8. Dates when the AkWarm file was created, last saved, and last saved as Official are included in the AkWarm file for use by data archiving systems.
  9. Miscellaneous Bug Fixes including:
    1. Corrected bug that made it impossible to enter in an insulation thickness less than the cavity thickness.
    2. Fixed bug that disabled Save as Official button on some computers for homes that have no improvments selected.
    3. Fixed bug that affected points and energy use for the perimeter section of slab-on-grade components where Insulation Quality was marked worse than OK.
    4. Allowed the entry of a rise in excess of the run in the Slope calculator.
    5. Cleaned out control characters from the Notes field of old AkWarm files, which previously created an error in AkWarm 2.
    6. Fixed the shell area to floor area warning calculation to more accurately account for garage floor area.
    7. Fixed a bug in the control that is used to enter numbers.

#### Version 2.0.4 (Apr 10, 2009)

  1. Made the flat-to-sloped converter available for Ceiling with Attic shell components.
  2. Changed flat-to-sloped calculator to apply slope multiplier to all lines in an area expression and apply multiplier to all parts of complicated expressions.
  3. Fixed a problem with the shape-based floor/ceiling area calculator that was causing measurements to be rounded to nearest integer.
  4. Installed three page Data Collection Worksheet during the AkWarm installation process. The worksheet is available on the "Start, Programs, AkWarm" menu.
  5. Enabled Right-Click Copy, Cut and Paste menu for the Improvement Notes.
  6. Created the 04/10/2009 Energy Library, which eliminates the R-14 door recommendation when the exterior door replacement improvement is analyzed.
  7. Added a Warning explaining that changing the Name of a shell component after it has been initially set will not affect the Improvements report. Instead, the entry for the Location of the improvement must be changed.
  8. Changed destination of GAMA link to go to the GAMA web site instead of directly to the AHRI web site, which has the product efficiency database.
  9. Implemented error checking that requires an entry for the equipment type of the Primary Heating System and requires an entry for the construction type of an Other Wall.
  10. Miscellaneous Bug Fixes, including:
    * Fixed a problem with the command that activates Microsoft Word after the Improvements Report is created.
    * Fixed a problem where blanking out the average ceiling height did not actually affect the entry.
    * Fixed a Null Reference Error that would sometimes occur when creating a new shell component.
    * Eliminated an error that occurred when clicking on column headings of the Heater Upgrade grid when there were no upgrades in the grid.
  11. Added the ability to view Version and Debug information by using the Ctrl-D keyboard shortcut.

#### Version 2.0.3 (Mar 20, 2009)

  1. Removed requirement for a User ID entry when saving official ratings.
  2. In some scenarios where there were no changes to file and a "Save as Official" was done, the rating was not changed to Official. This bug was fixed.

#### Version 2.0.2 (Mar 19, 2009)

Original Release
