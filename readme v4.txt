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
