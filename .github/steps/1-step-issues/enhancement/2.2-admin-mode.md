# Admin Mode

## Problem

Students are removing each other to free up space for themselves in the activities.

## Recommended Solution

Add a user icon in the top right. When clicked it shows a login button. When the login button is clicked, it presents a window to enter a username and password.

- Only the teachers (logged in) have the ability to register and unregister students to activities.

- The students (not logged in) can still view who is registered.

- There is no need for an account maintenance page. Teachers will be assigned passwords.

## Context

Since there is no database yet, please store the teacher usernames and passwords in a `json` file that is checked by the backend.
