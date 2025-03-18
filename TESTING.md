Return to the [README.md](README.md) file.

## Table of Contents

<details>
<summary>Click here for Table of Contents</summary>

- [Validation](#validation)

- [Lighthouse](#lighthouse)

- [Manual Testing](#manual-testing)

- [Bugs](#bugs)

## Validation

### HTML

| Page | URL | Screenshot | Notes |
| :---: | :---: | :---: | :---: |
| landing | [W3C](https://validator.w3.org/) | ![screenshot](/documentation/validation/homepagevalid.png) | Passed all checks |
| about | [W3C](https://validator.w3.org/) | ![screenshot](/documentation/validation/aboutpagevalidation.png) | The django adminsitration created the about model using summernote and the model is being delivered from the backend to the frontend it's an issue that isnt to do with the html all of the html passes fine only the summernote has an error out of control. |
| FAQ | [W3C](https://validator.w3.org/) | ![screenshot](/documentation/validation/faqpage.png) | Passed all checks |
| contact | [W3C](https://validator.w3.org/) | ![screenshot](/documentation/validation/contactpagevalid.png) | Passed all checks |
| profile | [W3C](https://validator.w3.org/) | ![screenshot](/documentation/validation/profilevalid.png) | Passed all checks |
| storefront | [W3C](https://validator.w3.org/) | ![screenshot](/documentation/validation/storefrontvalid.png) | Passed all checks |
| product details | [W3C](https://validator.w3.org/) | ![screenshot](/documentation/validation/productdetailvalid.png) | Passed all checks |
| shopping bag | [W3C](https://validator.w3.org/) | ![screenshot](/documentation/validation/shoppingbagvalid.png) | Passed all checks |
| checkout | [W3C](https://validator.w3.org/) | ![screenshot](/documentation/validation/checkoutvalid.png) | Only error is due to the loading spinner which was taken from Boutique Ado |
| checkout success | [W3C](https://validator.w3.org/) | ![screenshot](/documentation/validation/checkoutsuccessvalid.png) | Passed all checks |



### CSS
| Page | Jigsaw URL | Screenshot | Notes |
| :---: | :---: | :---: | :---: |
| style.css | [Jigsaw](https://jigsaw.w3.org/css-validator/validator) | ![screenshot](/documentation/validation/stylecssvalid.png) | Passed all checks |
| checkout.css | [Jigsaw](https://jigsaw.w3.org/css-validator/validator) | ![screenshot](/documentation/validation/checkoutcssvalid.png) | Passed all checks |
| profile.css | [Jigsaw](https://jigsaw.w3.org/css-validator/validator) | ![screenshot](/documentation/validation/profilecssvalid.png) | Passed all checks |


### JavaScript

| Page | JS Hint URL | Screenshot | Notes |
| :---: | :---: | :---: | :---: |
| script.js | [BeautifyTools](https://beautifytools.com/javascript-validator.php) | ![screenshot](/documentation/validation/script.jsvalidation.png) | Passed all checks |

- script.js is the only file that I wrote custom js in. The other files in the project countryfield.js and stripe_elements.js are taken from Boutique Ado. 
- JSHint is down leading to me using BeautifyTools it would not load no matter what.
- ![screenshot](/documentation/validation/jshinterror.png)


### Python 

- There are many files to upload for this portion but I'll start by showing the pep8 validation process that Observastore underwent. 
![screenshot](/documentation/validation/pep8flake8.png)

- flake8 was used in the terminal to bring all of the pep8 errors into light so it can become easy to manage and fix. Most of the code already was fixed by myself while it was being created with the pep8 guidelines in my mind at all times. I really wanted to get the validation for pep8 correct this time and I believe I have done it. The following table will present the outcome of the pep8 validation. 

| File | URL | Screenshot | Notes |
| :---: | :---: | :---: | :---: |
| about/admin.py | [CI Python Linter](https://pep8ci.herokuapp.com/#) | ![screenshot](/documentation/validation/aboutadmin.png) | Passed all checks |
| about/urls.py | [CI Python Linter](https://pep8ci.herokuapp.com/#) | ![screenshot](/documentation/validation/abouturls.png) | Passed all checks |
| about/models.py | [CI Python Linter](https://pep8ci.herokuapp.com/#) | ![screenshot](/documentation/validation/aboutmodels.png) | Passed all checks |
| about/views.py | [CI Python Linter](https://pep8ci.herokuapp.com/#) | ![screenshot](/documentation/validation/aboutviews.png) | Passed all checks |
| storefront/admin.py | [CI Python Linter](https://pep8ci.herokuapp.com/#) | ![screenshot](/documentation/validation/storefrontadmin.png) | Passed all checks |
| storefront/urls.py | [CI Python Linter](https://pep8ci.herokuapp.com/#) | ![screenshot](/documentation/validation/storefronturls.png) | Passed all checks |
| storefront/models.py | [CI Python Linter](https://pep8ci.herokuapp.com/#) | ![screenshot](/documentation/validation/storefrontmodels.png) | Passed all checks |
| storefront/views.py | [CI Python Linter](https://pep8ci.herokuapp.com/#) | ![screenshot](/documentation/validation/storefrontviews.png) | Passed all checks |
| storefront/forms.py | [CI Python Linter](https://pep8ci.herokuapp.com/#) | ![screenshot](/documentation/validation/storefrontform.png) | Passed all checks |
| checkout/admin.py | [CI Python Linter](https://pep8ci.herokuapp.com/#) | ![screenshot](/documentation/validation/checkoutadmin.png) | Passed all checks |
| checkout/urls.py | [CI Python Linter](https://pep8ci.herokuapp.com/#) | ![screenshot](/documentation/validation/checkouturls.png) | Passed all checks |
| checkout/models.py | [CI Python Linter](https://pep8ci.herokuapp.com/#) | ![screenshot](/documentation/validation/checkoutmodel.png) | Passed all checks |
| checkout/forms.py | [CI Python Linter](https://pep8ci.herokuapp.com/#) | ![screenshot](/documentation/validation/checkoutform.png) | Passed all checks |
| checkout/signals.py | [CI Python Linter](https://pep8ci.herokuapp.com/#) | ![screenshot](/documentation/validation/checkoutsignals.png) | Passed all checks |
| checkout/views.py | [CI Python Linter](https://pep8ci.herokuapp.com/#) | ![screenshot](/documentation/validation/checkoutviews.png) | Passed all checks |
| webhook.py | [CI Python Linter](https://pep8ci.herokuapp.com/#) | ![screenshot](/documentation/validation/webhookspyvalid.png) | Passed all checks |
| webhook_handler.py | [CI Python Linter](https://pep8ci.herokuapp.com/#) | ![screenshot](/documentation/validation/webhookspy.png) | Passed all checks |
| bag/contexts.py | [CI Python Linter](https://pep8ci.herokuapp.com/#) | ![screenshot](/documentation/validation/bagcontexts.py.png) | Passed all checks |
| bag/admin.py | [CI Python Linter](https://pep8ci.herokuapp.com/#) | ![screenshot](/documentation/validation/bagurls.png) | Passed all checks |
| bag/views.py | [CI Python Linter](https://pep8ci.herokuapp.com/#) | ![screenshot](/documentation/validation/bagviews.png) | Passed all checks |
| contact/admin.py | [CI Python Linter](https://pep8ci.herokuapp.com/#) | ![screenshot](/documentation/validation/contactadmin.png) | Passed all checks |
| contact/forms.py | [CI Python Linter](https://pep8ci.herokuapp.com/#) | ![screenshot](/documentation/validation/contactform.png) | Passed all checks |
| contact/models.py | [CI Python Linter](https://pep8ci.herokuapp.com/#) | ![screenshot](/documentation/validation/contactmodel.png) | Passed all checks |
| contact/urls.py | [CI Python Linter](https://pep8ci.herokuapp.com/#) | ![screenshot](/documentation/validation/contacturls.png) | Passed all checks |
| contact/views.py | [CI Python Linter](https://pep8ci.herokuapp.com/#) | ![screenshot](/documentation/validation/contactview.png) | Passed all checks |
| faq/admin.py | [CI Python Linter](https://pep8ci.herokuapp.com/#) | ![screenshot](/documentation/validation/faqadmin.png) | Passed all checks |
| faq/models.py | [CI Python Linter](https://pep8ci.herokuapp.com/#) | ![screenshot](/documentation/validation/faqmode.png) | Passed all checks |
| faq/urls.py | [CI Python Linter](https://pep8ci.herokuapp.com/#) | ![screenshot](/documentation/validation/faqurl.png) | Passed all checks |
| faq/views.py | [CI Python Linter](https://pep8ci.herokuapp.com/#) | ![screenshot](/documentation/validation/faqview.png) | Passed all checks |
| profiles/forms.py | [CI Python Linter](https://pep8ci.herokuapp.com/#) | ![screenshot](/documentation/validation/profileform.png) | Passed all checks |
| profiles/models.py | [CI Python Linter](https://pep8ci.herokuapp.com/#) | ![screenshot](/documentation/validation/profilemodel.png) | Passed all checks |
| profiles/urls.py | [CI Python Linter](https://pep8ci.herokuapp.com/#) | ![screenshot](/documentation/validation/profileurl.png) | Passed all checks |
| profiles/views.py | [CI Python Linter](https://pep8ci.herokuapp.com/#) | ![screenshot](/documentation/validation/profileview.png) | Passed all checks |
| observastore/urls.py | [CI Python Linter](https://pep8ci.herokuapp.com/#) | ![screenshot](/documentation/validation/observastoreurl.png) | Passed all checks |
| observastore/views.py | [CI Python Linter](https://pep8ci.herokuapp.com/#) | ![screenshot](/documentation/validation/observastoreview.png) | Passed all checks |

