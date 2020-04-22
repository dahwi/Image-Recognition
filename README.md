# Image-Recognition
All work is from the tutorial "Image Recognition and Python" by sentdex
## Overview
Image Recognition is used for all sores of things such as facial recognition, identifying what picture contains, etc 

## Goal of the Project
Begin to use machine learning, in form of pattern recognition, to teach our program what text looks like


## Requirements
<ul>
<li>  Python 2.7.5 </li>

<ul>
<li> numpy </li>
<li> matplotlib </li>
<li> PIL or pillow </li>
</ul>

<li> Images to test our program </li>

<ul>
<li> Download from sentdex.com/tutorialimages.zip </li>
</ul>

</ul>

## Problem faced
Using default python 2.7.5 installed in Linux CentOS 7, you need to install <strong> subprocess32</strong> and <strong> tkinter</strong> manually to fully operate <strong> matplotlib </strong> using
`pip install tkinter && pip install subprocess32`

If you are using CentOS 7 minimal, you need to download GNOME GUI on your CentOS 7 to display the plot using `yum groupinstall "GNOME Desktop" "Graphical Administration Tools"
` and `ln -sf /lib/systemd/system/runlevel5.target /etc/systemd/system/default.target`(reboot your machine afterwards)

Matplotlib chooses Xwindows backend by default. You need to set matplotlib to not use the Xwindows backend using
`echo "backend: qt4agg" > ~/.config/matplotlib/matplotlibrc
`

`ValueError: assignment destination is read-only` is raised when assigning new values to numpy array meaning that you can only access but cannot modify them. This problem is fixed by downgrading numpy using `pip install numpy==1.15.4` and setting a flag parameter using `your_array_name.setflags(write = 1)` 
