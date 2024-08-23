# Testing

## Manual Testing

- I regularly tested elements as I completed them, using the site preview within gitpod I could write the code and then test the site to make sure links worked and the website was responsive.

- I published the page on Heroku and then tested the website on different sized devices as well as different brand devices (android/apple/amazon/desktop) 
 to check responsiveness. 

- Let friends and family visit and use the website and report back any unusual findings or problems. 

- I used Chrome Developer tools to simulate different screen sizes in order to test responsiveness.

## Bugs & Fixes

1. Intended Outcome - Have a modal appear when deleting either an item or a category warning the user that this cannot be undone.  
    - Issue:
        - Although the developers tools showed that the delete button linked to the modal I could not get the trigger to work to display the modal. 
    - Solution
        - I had to remove the modal temporarily due to time constraints and will revisit at a later date.  

# Post Development Testing

## Validator Testing

### HTML
No errors were returned when passing through the official W3C validator
- W3C Validator for [Toy Inventory](https://validator.w3.org/nu/?doc=https%3A%2F%2Ftoys-team-toy-inventory-80ed09c090ba.herokuapp.com%2F)

### CSS
I ran the validator and no errors were reported in my code - it did show some errors purely due to some of the code from the Materialize framework used but nothing that I could change 

- Jigsaw Validator for CSS [validation](https://jigsaw.w3.org/css-validator/validator?uri=https%3A%2F%2Ftoys-team-toy-inventory-80ed09c090ba.herokuapp.com%2F&profile=css3svg&usermedium=all&warning=1&vextwarning=&lang=en)

## Lighthouse score

Lighthouse score was run and everything was in the green, all scores came back over 90, with performance at 99.

## JSHint

When my JS was run through JSHint no errors were found, there were a few warnings but could not be changed without affecting my code. 

## Accessibility

As well as the accessibility score from lighthouse testing I also used [WAVE - Web accessability evaluation tool](https://wave.webaim.org/extension/) to check my pages for accessibility and no errors were found.

[Back to README.md](README.md)