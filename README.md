# `CMPSC 302` Web Development, Week 3: Basic Style (Exercises, aka: golf)

* Assigned: 14 March 2022, 1:30 PM
* Due: 27 March 2022, 11:59 PM

## Fore things

Today we're going to test a bit of our knowldge about positioning by _playing golf_. That's right: golf, a subject
that I know nothing about except that it has lakes, sand, grass, and, occasionally, polite claps.

We're going to experience this through _positioning_, a topic that were going to cover broadly at the beginning
and dive deeper into over the course of the week. We're also going to review some more about CSS selectors and, in the process
learn about how we can position things _relative_ to other things.

If that weren't enough, we're also going to work with our on-going garden lab as we learn more about positioning and how to 
make columns from text and `div`s. 

Overall, an action packed week that has us doing something like..._fore_ (4) things.

## Making a GitHub Pages page

This assignment also requires you to make your work available via GitHub Pages. For a primer on where to find it
and how to do it:

- [ ] locate and click the `Settings` tab at the top of the screen
- [ ] from the menu at the left, select `Pages`
- [ ] locate the "Source" heading; set the "Branch" as `main`, and change the second drop-down to `/docs`
- [ ] click `Save`
- [ ] One last step: make the page _public_ by setting `GitHub Pages visibility` to `Public`
  * This step is _required_ for your HTML and CSS to pass validation!
A green box will appear at the top of the page listing the random URL that you've been assigned. This is your
URL!

## Accepting the assignment

- [ ] Using either the link posted to our class Discord or the [course schedule](https://cmpsc302.chompe.rs)
- [ ] Click the link provided for the lab assignment and accept it in GitHub classroom
- [ ] Once the assignment finishes building, click the link to go to your personal repository assignment

## "Cloning" a repository

### Using the correct download link

- [ ] On this repository's page, click the `Clone or download` button in the upper right hand corner
* You may need to scroll up to see it
- [ ] In the upper right corner of the box that appears, click `Use SSH`
- [ ] Copy the link that appears in the textbox below the phrase "Use a password with a protected key."

#### Cloning

* [ ] Type `ls` in your terminal window
* You should be in your `~` directory
- [ ] Find the folder you've made to hold class assignments (may involve `cd`ing)
- [ ] Once there, "clone" the repository using the link copied above
  * If I (the instructor) were to clone my own repository, I'd enter (your link will look different):

```
git clone git@github.com:Allegheny-ComputerScience-302-S2022/cmpsc-302-week-2-basic-style-exercises.git
```

## Wrap-up

### Submitting the assignment/saving progress

The GitHub platform is a place to store your work. So, it makes some sense that should be able to _clone_ (download) from it, and push back (upload) to it. Here, we'll learn this second part.

- [ ] `cd` to your `~` folder
- [ ] Locate your `cmpsc-302-week-2-basic-style-exercises` folder and `cd` to it.

Once in this folder, we need to tell git that there have been changes.

- [ ] Type `git add -A` and press `Enter`
* This tells git to look through the _entire_ folder structure for new changes and "stage" them

- [ ] Type `git commit -m "YOUR COMMIT MESSAGE"` to "label" the commit
* This is typically something like `git commit -m "Fixing a typo"` -- the message in quotes should be as descriptive as possible, while still remaining somewhat short

- [ ] To send all changes to the server, type `git push`
- [ ] At the prompt, input the password associated with the `SSH Key` you created earlier in this exercise (yesterday)

Once the process finishes successfully, we're done!
