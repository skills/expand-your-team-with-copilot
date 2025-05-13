### School Overview

- The school name is "Mergington High School"
- The school is a public high school in Mergington, Florida.
- The school motto is "Branch out and grow".
- It serves grades 9 through 12 and typically has 100 to 150 students per grade.

- The school year starts in August and ends in May.
- There are 3 trimesters per year.
- There is a 4th summer cycle, but it is optional.

Below is a list of common roles and tasks they might want help with.
If a user specifies their role, you can use this information to provide more targeted suggestions or offer ways to help them.

## Development Environment

For detailed setup and development instructions, please refer to our [Development Guide](../docs/how-to-develop.md).

### User Interaction

Consider the following when communicating with the staff.

- The staff is not technical. Explain in simple terms as much as possible and avoid software jargon.
- Any new code must be easy to maintain and understand, without significant coding experience.

## Program architecture

- The website users are the students and teachers. Make sure the user experience is simple.
- Do not make additional apps or services.
- Do not make command line tools.
- Do not create a long single file application. Always use an easy-to-understand directory structure.
- Only use HTML, CSS, Javascript, and Python. No other languages.

### Documentation

- Always update the README file to explain how to use the program. Assume the user will quickly forget so good documentation is important.
- Once the readme gets too long, start organizing it into a docs directory.

### Quality considerations

- If the tasks involves grades, scores, or other numerical data, isolate those functions and make sure they are correct with unit tests.

### Security considerations

- Personal information might be processed so privacy and security are important.
- Do not provide examples that encourage the user to hardcode secrets, passwords, or other sensitive information.
- If credentials or other sensitive information is required, add features to the program to prompt for it, store it locally, and logout. For example a login dialog box.
