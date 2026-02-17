# Notes on replication of RQ2

To replicate RQ2 on original dataset, you would need to download the full dataset, then use the steps 4-5 provided by the original authors to run the projects and get the results.

## Requirements

We recommend using Eclipse IDE, OS Linux and Java 11 to run the scripts to ensure the best compatibility. Note, that Step 4.1 requires you to use GitHub OAuth Token, not the personal token (although it might work, we do not guarantee it for the sake of replication accuracy).

## Step-by-Step Guide

Here are the detailed step-by-step overview of the steps to do:

1. After downloading the original data, navigate to the folder `Step 4 Extract the Code Readability Issues identified by SonarQube ASAT/4.1 Download the before after github`.
2. As it was noted in `datasets`, original dataset contains errors that prevent downloading, use our changed dataset in the following way:
   copy the `Selected Merged PRs with code readabiliy improvements (copy).csv` dataset to the `data` and replace the original `.csv` inside of the Eclipse project.
3. After replacing the dataset, run the script according to the `README.md` left by the authors to download the full dataset.
4. Warning: Note that step 4.2 and step 5 requires you to use folder that you get <b>inside</b> the temp folder you have used in 4.1, which will be named `fileTemp`. E.g., if you have used a path such as `/home/<username>/tmp`, the path you provide to the scripts in 4.2 and 5 will be `/home/<username>/tmp/fileTemp`.
5. Navigate to step 4.2, change the path as it was stated before, to use the `fileTemp`, run the script as a `JavaApplication`, not as the test (despite the file and class named as the test, it is in fact an application).
6. Now you can run the step 5, which is just a one-file java script, to get the count of issues in the repo. Note that console outputs are not on English, so you most likely would want to translate it if you don't know the language. Do not forget to change the path to the `fileTemp` as it was stated before.

## Changes Introduced

There were no changes introduced to the original scripts, nor additional scripts added to replicate the RQ2. The only change was cleaning the dataset, which was done iteratively by removing and checking manualy each failed dataset entry from `.csv` file after running the script from 4.1 step.
