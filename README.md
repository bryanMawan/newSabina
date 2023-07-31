# Tjejsatsningen

## Workflow Checklist”     

- [x] Fix static files (Friday, 2023-07-28 to Sunday, 2023-07-30)
- [x] Finalize successful page (Monday, 2023-07-31 to Wednesday, 2023-08-02)
- [ ] Make and add fohr logo (Thursday, 2023-08-03 to Saturday, 2023-08-05)
- [x] create use and first page for filepath assigning (Thursday, 2023-08-03 to Saturday, 2023-08-05)
- [ ] fix the popover and clipboard copy problem in the password modal
- [ ] refactor the code for best practices (Monday, 2023-08-07 to Saturday, 2023-08-09)


## About

...

## Code Review Checklist

### Discouraged Practices:

- [ ] **Avoid Global Variables:** Refrain from using global variables (`main_path`, `message`, `excel_password`) to prevent unintended side effects. Instead, pass variables explicitly to functions or use class-based views for handling state.

- [ ] **Avoid Hardcoded Primary Key Values:** Remove hardcoded primary key values (e.g., `pk=1`) when retrieving instances from models (`FilePath`, `password`). Consider using a more flexible approach, such as querying based on specific attributes or using `get_or_create()` if a default instance is needed.

- [ ] **Avoid Directly Accessing Form Fields:** In the `formPageView` class, refrain from directly accessing form fields using `form.Meta.fields`. This approach tightly couples the view to the specific form implementation. Use `get_form_kwargs` method to pass necessary fields or override `get_form_class` method if form class customization is required.

- [ ] **Use Proper Logging Mechanisms:** Instead of printing debug information to the terminal, use appropriate logging mechanisms for debugging. Remove any unnecessary print statements to keep the production code clean.

- [ ] **Stick to One Approach for URL Reverse:** Choose either `reverse` or `reverse_lazy` for URL reverse throughout the codebase for consistency. Typically, `reverse_lazy` is used for class-based views, while `reverse` is used for function-based views.

- [ ] **Include Proper Error Handling:** Add appropriate exception handling in the code to prevent potential crashes. Handle exceptions gracefully and provide meaningful error messages to users when required.

### Additional Recommendations:

- [ ] **Use Meaningful Variable and Function Names:** Improve the readability of the code by using descriptive and meaningful variable and function names that reflect their purpose.

- [ ] **Separate Views and Business Logic:** Consider separating business logic from views to promote code modularity and reusability.

- [ ] **Use Django Messages Framework:** Utilize Django's messages framework for displaying feedback to users instead of manually handling messages.

- [ ] **Use ModelForm:** Consider using Django's `ModelForm` instead of manually defining forms to leverage the built-in functionality and validations.

- [ ] **Follow Django Coding Standards:** Ensure that the code follows Django's coding standards and conventions for better consistency and maintainability.

- [ ] **Add Documentation:** Provide sufficient comments and documentation to explain the purpose and usage of classes, functions, and modules.

- [ ] **Unit Testing:** Write unit tests to validate the functionality of views, forms, and models.

- [ ] **Security Considerations:** If the code deals with sensitive data or user inputs, ensure proper security measures are implemented (e.g., input validation, CSRF protection).

- [ ] **Code Review:** Conduct a thorough code review to catch potential issues and improvements that may have been overlooked.

Note: This checklist summarizes the improvements needed in the provided code. It is crucial to address these points according to your specific project requirements and coding standards.


<!-- Add more information about your project below -->
