Welcome to Misclassification by PSD
author: Katie Ballard
date:8/29/19
purpose: Find the missclassification error of neutrons to gammas and gammas to neutrons 
           based on two gaussian curves that are fitted to PSD data, by detector and energy

How to use this code:
    First, open psdConstants.py and choose the slice demensions, what channels 
    should be elxuded, the mode wanted for the discrimination line, and the 
    location of where you want things saved.  
    
    Then open psdMisclassification. This will be where the code is run from. 
    You will need to set "path" "minFile" and "maxFile" to where the data is coming
    from, what the lowest number of the files is, and what the highest number of the 
    files is. Make sure that the code is importing the correct type of data with 
    the correct attributes. You will need: "PSD", "Integral" and "Channel" data
    to run the code. 
    
    The code will gather the data in chunks and will save the data's PSD in a large array 
    based on the data's channel and energy. It will then use the array to go through the 
    rest of the code. 
    
    This code will produce a lot of graphs that are not shown, to see them go to the location of your save path. 
    If the code is run another time these graphs will be changed if they are not put in a seperate folder or if the 
    save path was not changed. The last graph printed can be useful to look at if problem 1 occurs. 
    

How to make graphs of specific sections of data:
           Open psdAnalysis and set the types of graphs you want to 'True'.
           psdConstants will need to be set up with 'Rows' equal to the amount of data that you want,
           and 'SAVEPATH' set to where you want the graphs to be saved. 
           
           You will have to change 'raw graph' in psdAnalysis to set up different types of graphs. 
           
           'density plot' is preset to do a plot of psd vs integral. If you want to plot something else
           open densityPlot_v4 and change what x and y equal. 

strengths:
    Can be run without data after the inital run with data, as long as the bin sizes
        are not changed. This can cut down on the time it takes the code to process. 
    Only psdConstants and psdMisclassification have to be changed run different things. 

weaknesses:
    There is a dependance on having close to correct center guesses, idealy we 
        would have a list of ideal centers for each seperate graph. 
    The gaussians are graphed seperately instead of at the same time. 
    
Probelm Checks:
   1 "optimal perameters not found.... 800":
        centers are off, write "thisChannel" in the terminal
        if thisChannel is below 40:
            change centers 0 or 1 
        if above 40:
            change centers 2 or 3
        new centers can be tested by copying all of line 87 in 
        psdMisclassification into the terminal, if the error reoccurs continue 
        trying new centers
    
    
    
