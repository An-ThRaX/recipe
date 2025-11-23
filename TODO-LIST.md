# Storage
- recipes shall contain fields id, category, title, description (instructions) (a list), ingredients (a list), OPTIONAL an image


# UI
- home page will display a docking bar, that will have the following elements:
    - Left side
        - Home btn - will return the user to root
        - Add new recipe
            - Shall open a modal, that will have the required fields
                - `done, it is wired to the BE`
                - `adds a new item, on Add, it refreshes the page and catalogue`
            - Shall NOT close when click around it - only cancel or add
                - `done`
            - Shall have Add and Cancel buttons
                - `done`
                - If fields are populated, the Cancel shall require confirmation
                    - `done; if the cancel is pressed while the form is partially filled, confirmation is required`
            - Shall have an option to load an image
                - it shall be resized (to be decided if and how)
        - Categories list - will show N main categories of recipes (e.g. favorites, desert, soup, main dish)
            - `done, new categories are added to the list`
        - Delete an existing recipe
            - Will require confirmation on deletion
    - Main screen will either hold latest viewed recipes, or a theme background, or favorites
    - On category selection, the main page will be populated with cards, 3 per row, with recipes linked by the selected category
    - The screen will hold 3.5 cards at a time on height axis
    - If the rows will exceed the screen height, they will be scrollable within that screen section
    - On recipe selection, the screen shall load the recipe details
        - The new screen shall have the recipe title on top
        - Mark as fav
        - The new screen shall be divided by two fine lines in 3 columns
            - ingredients (left column)
            - instructions (center and right column)

Brainstorming by Melania:
- handwriting to text 10000/10
- speech to text 8/10
- include images to recipes
- display the images at the bottom of recipe screen, scrollable on click enlarge
- search
- import export recipes as files