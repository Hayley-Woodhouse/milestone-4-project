
# Testing

# Contents

* [MANUAL TESTING](#manual-testing)
    * [User Stories](#user-stories)
        * [Guest User](#guest-user)
        * [Registered User](#registered-user)
        * [Admin](#admin)
    * [Responsive](#responsive)
    * [Browsers](#browsers)
* [AUTOMATED TESTING](#automated-testing)
    * [Lighthouse](#lighthouse)
    * [W3C Validator](#w3c-validator)
    * [W3 Jigsaw](#w3-jigsaw)
    * [JS Hint](#js-hint)
    * [PEP8](#pep8)
* [Bugs](#bugs)
    * [Allauth](#allauth)
* [Furture Updates](#future-updates)
___
# MANUAL TESTING
Manual testing is when project designers and developers to inspect software for defects. It requires the devloper to play the role of an end user where by they use most of the application's features to ensure correct behaviour.

[Back to top](#contents)

___
# User Stories

To test user stories a screen shot and brief description is provided as evidence that the criteria has been met.

## Guest User

As casual/first time user – As a site user that has not created an account, I want to be able to:

| Find out more about Lakeside Art Prints and to navigate it. |
|----| 
| To find out information about the site its delivery and returns and contact information, this can be found in collapsible buttons in the footer.|
![about us](assets/readme-images/about_userstory.png)


| Search for specific artist and art |
|----|
|The search option in the navbar will render data linked to the searched criteria. By art name, artist name, price, art style and date.|
![search by artist](assets/readme-images/search-artist.png)
![search by art](assets/readme-images/search-art-name.png)
|Using the drop down tab the data display can be refind by art styles and all products.|
![search bt category](assets/readme-images/search-cat.png)
![refine category search](assets/readme-images/search-category.png)

| Find detailed information retaining to the art and artist |
|----|
| When clicking on the selected product the details on the art name, style, artist and date of art work are displayed. |
![product details](assets/readme-images/detail-user.png)

| View estimated delivery and costs |
|----|
| Delivery costs are calculated in the shoppping bad. A total cost is visible on under the basket icon in the navbar. The free delivery threshold is also calculated for user to see how much more they could spend to achieve free delivery. | 
![delivery cost](assets/readme-images/delivery-cost.png)

| Add items to basket |
|----|
| When an item is selected the user continue to add the product to the bag by clicking the add to bag button |
![add item to bag](assets/readme-images/add-to-bag-user.png)

| Review and edit and delete basket items |
|----|
| The update button enables the user to change the quantity of item. Doing so would also update the cost and delivery implications. The remove button can delete the product from the bag. If it was the only product in the bag the user will be directed to the empty bag page. |
![update and delete bag](assets/readme-images/edit-delete-user.png)
![empy bag](assets/readme-images/empty-bag-user.png)

| Make purchases as a guest user |
|----|
| Guest users can make purchaces and confirmation page will display the full order, cost and delivery address details. Also a confirmation email detail will display above the form. |
![payment form](assets/readme-images/payment-form.png)
![payment form](assets/readme-images/payment-confirmation.png)

| Create an account if I want to do more |
|----|
| An account can be created via the my account drop down in the navbar. Alternativly a registration link is provided before checkout. |
![profile registration form](assets/readme-images/register-user.png)

| Contact Lakeside Art Prints to report, query, and rectify and problems |
|----|
| Contact details are avalible in collapsible button in the footer |
![payment form](assets/readme-images/payment-confirmation.png)

[Back to top](#contents)

## Registered User

As a site user that has created an account, I want to be able to:

| Do all that a casual user can |
|----|
| All requirements are met in the user stories |

| Easily register for an account |
|----|
| An account can be created via the my account drop down in the navbar. Alternativly a registration link is provided before checkout. |
![profile registration form](assets/readme-images/register-user.png)

| Log in and out with ease |
|----|
| A simple sign in form, once completed, will direct the user to their profile page. Using the link in the navbar the user can re-view thier page and log out |
![profile sign in](assets/readme-images/sign-in-user.png)
![profile sign out](assets/readme-images/sign-out-user.png)

| Edit my profile and update details, change of address, name etc |
|----|
| The user can update their contact number and delivery details. Also when the user makes payment the delivery details will auto fill with their profile details |
![profile page](assets/readme-images/profile-user.png)
![profile autofill](assets/readme-images/profile-autofill-user.png)

| View my full purchase history |
|----|
| When the account user makes a purchace the order details will be logged on the profile page order history. Additionally clicking on the order number will display the full order details.
![profile purchase history](assets/readme-images/profile-order-summary-user.png)

| Retrieve or reset forgotten passwords |
|----|
| Given the project time scale this has been marked as an immediate update |

[Back to top](#contents)

## Admin 

As the shop admin, I want to be able to:

| Add products to the shop |
|----|
| Simply select products and add product. From there fill in the required fields and save. The product details will be added to the product list.|
![add product admin](assets/readme-images/add-product-admin.png)

| Edit/ update a product & Delete a discontinued product |
|----|
| Selecting an individual project and the field can be altered and saved. The detete button will also remove the product completely. |
![update and delete products admin](assets/readme-images/edit-product-admin.png)

[Back to top](#contents)

___
# Responsive

The sites responsive design was tested using Google Crome and firefox devTools

|| Small Mobile | Med Mobile | Tablet | Laptop | Large Laptop | Desktop |
| --- | --- | --- | --- | --- | --- | --- | 
| site | Pass |Pass | Pass | Pass | Pass | Pass |
| images | Pass |Pass |Pass |Pass |Pass |Pass |

[Back to top](#contents)
___
# Browsers

- [Google Chrome](https://en.wikipedia.org/wiki/Google_Chrome) *'is a cross-platform web browser developed by Google.'*
- [Microsoft Edge](https://en.wikipedia.org/wiki/Microsoft_Edge) *'is a cross-platform web browser created and developed by Microsoft.'*
- [Safari](https://en.wikipedia.org/wiki/Safari_(web_browser)) *'is a graphical web browser developed by Apple.'*
- [Mozilla Firefox](https://en.wikipedia.org/wiki/Firefox) *'is a free and open-source web browser developed by the Mozilla Foundation and its subsidiary, the Mozilla Corporation.'*

[Back to top](#contents)

___
# AUTOMATED TESTING

Automated testing is the use of a software separate from the software being tested to control the execution of tests and the comparison of actual outcomes with predicted outcomes.

[Back to top](#contents)

___
# Lighthouse
*'An open-source, automated tool for measuring the quality of web pages.'* - [Wikipedia Google Lighthouse](https://en.wikipedia.org/wiki/Google_Lighthouse)
![Lighthouse testing](assets/readme-images/lighthouse-test.png)

[Back to top](#contents)

___
# W3 validator
*'is a validator by the World Wide Web Consortium (W3C) that allows Internet users to check pre-HTML5 HTML and XHTML documents for well-formed markup against a document type definition.'* - [ Wikipedia W3 validator](https://en.wikipedia.org/wiki/W3C_Markup_Validation_Service)
![Html testing](assets/readme-images/html-test.png)

Testing html was used in fragments as python code displayed errors. With these pieces of codes ignored the code past validation.

[Back to top](#contents)

___
# W3 Jigsaw
*'is a CSS validator and free software developed by W3C, and a free online service.'* - [W3 Jigsaw](https://www.w3.org/wiki/CssValidator)
![Css testing error](assets/readme-images/css-test.png)

Css testing displayed a single error stating an anchor in a comment didnt have a closing tag. With the closing tag added, the code past validation.
![Css testing pass](assets/readme-images/css-test2.png)

[Back to top](#contents)

___
# JS Hint
*'is a static code analysis tool used in software development for checking if JavaScript source code complies with coding rules.'* - [Wikipedia JS Hint](https://en.wikipedia.org/wiki/JSHint)
![JS testing](assets/readme-images/js-test.png)
With two minor warnings the code passed validation.

[Back to top](#contents)

___
# PEP8
*'is a python validating tool used in software development.'* - [PEP8](http://pep8online.com/)
![Python testing](assets/readme-images/python-test.png)

 [Back to top](#contents)   

___
# Bugs

| Test number | Description | Expectation | Outcome | Pass/Fail | Comments |
| --- | --- | --- | --- | --- | --- |
| 1 | css mobile nav miss-aligned | expected inline links | links stack forcing the navbar to extend down the page | Fail | test 1 |
| 2 | css mobile nav miss-aligned | expected inline links | reduced padding at mobile query | pass | test 1-review |
| 3 | admin login | login to admin account | login failed error | fail | test 2 |
| 4 | admin login | login to admin account | temporary commented out signal, logged into admin via html login page, reactivated signal | pass | test 2- review|

## Allauth
Authentication using django allauth

Testing that allauth has been setup correctly.
![allauth](assets/readme-images/allauth_testing.png)
manually creating a user email address via admin and enabling authentication.
![allauth](assets/readme-images/allauth2.png)
The error messsage shows that the redirct (success) has worked and that authentication is running correctly.
![allauth](assets/readme-images/allauth3.png)

[Back to top](#contents)

## Payment testing
Strip payment testing. To ensure that strip payment was set up and that payment was received to strip payment system.
![Strip payment](assets/readme-images/payment-testing.png)


___
# Future Updates

- Create a superuser for admin to add, update and remove products via the page login.

- Add delete function for the registered users to delete their user account.

[Back to top](#contents)
