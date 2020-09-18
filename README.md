# ENGS 108 Fall 2020 Repository
Included in this repository are assignment notebooks and datasets that will be used throughout the class. They provide a skeleton for your coding assignments so that hopefully concepts are enforced over debugging. Although these assignments have been curated throughout the years, this delivery format is experimental, so if anything doesn't work as it should please let the TAs know as soon as possible. 

# Getting Setup

This semester we will be using Github to host datasets and assignment notebooks and Google Colab to run all of our code. The process for getting setup is pretty straightforward and you will be aided considerably if you install the following tools:
1. Github Desktop (Available on Windows and MacOS)
1. Google Drive Backup and Sync (So that you can access your Google Drive on your computer)

## Installing GitHub Desktop
Navigate to the `Code` button on the righthand side of this screen and click `Open with GitHub Desktop`. You will be taken to another screen where you can download and install the application.

## Installing Google Drive Backup and Sync
Navigate to [Google's website](https://www.google.com/drive/download/) and download and install the Google Drive Backup and Sync Application. You should also be using your Dartmouth Account for this as it has unlimited storage in case we play around with some larger datasets.

## Cloning the Class Repository. 
Now that we have GitHub Desktop and Google Drive Backup and Sync installed, we'll now setup our repo.
1. Open GitHub Desktop.
1. Navigate to File > Clone Repository...
1. Click the tab labeled URL.
1. Type in the URL address of this repo, i.e. yakaboskic/ENGS_108_Fall_2020
1. Choose your Google Drive Folder as your Local Path (Very Important!). I also like to have a folder of my Git repos something like 'Google Drive/git/'
1. Then click Clone. Your're done with the hardest part!

# Save a Google Drive copy of the code skeleton to your Colab Notebooks Folder.
We want to make things as easy as possible as well as making sure your homework code is not accidently overwritten.
1. On this GitHub repo, open your notebook skeleton of choice.
1. Click open in Google Colab.
1. Then click Save a copy in Drive.
1. This will open up a new notebook and save a copy to MyDrive/Colab Notebooks. You can check the location by going to File > Locate in Drive.
1. Now you have a copy of the skeleton in your Colab Notebook folder, seperated from your Git Repo.
1. **This is important in case I have to update a skeleton for some reason it won't accidently overwrite work that you have already done.**

# Accessing Everything From Google Colab
Now that we have everything loaded up in Google Drive accessing Colab is a breeze. **Make sure you've saved a notebook copy as stated above.**
1. Navigate to [Google Colab](https://colab.research.google.com/notebooks/intro.ipynb)
1. If you're new, maybe look at the intro notebook to get yourself familiar.
1. If you're not signed in, make sure to sign into your appropriate Google Account.
1. Now click File > Open Notebook. 
1. Click on the Google Drive Tab, and you should see your Notebooks appear. 
1. Load your respective notebook and get started on the assignment.

## Mounting your Google Drive in Colab
When we work with datasets, you will need to have access to files in the repository we cloned with all the datasets. This procedure is called mounting. 
1. After opening your desired notebook, click on the little folder icon on the lefthand side.
1. Three icons will now appear on the top of this Files Panel.
1. Click on the rightmost icon (When you hover it should say Mount Drive).
1. That's it. You should be able to see all your Drive contents in the '/content/Drive/MyDrive' directory. 
*Note: If there is any data loading code make sure to change your base file path to what it should be on your particular system.*

# Submitting Homework
Please do not deviate far from the assignment code skeleton. If you find a significant error or have concerns please reach out to the TAs.
The homework development process should be as follows:
1. Run all the setup that is described here.
1. Answer all assignment code inside your Colab notebook via code or Markdown. If you are unsure about writing in Markdown view this [guide](https://colab.research.google.com/notebooks/markdown_guide.ipynb#scrollTo=tPqPXAKKkzaM). It's actually quite easy.
1. Upon completion of your assignment, download your completed notebook to your computer (File > Download .ipyb) and rename it. (Although it's saved in your Google Drive as well, I find this to be the best method.
1. Then submit your completed jupyter notebook to Canvas.
