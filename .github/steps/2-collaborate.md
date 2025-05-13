## Step 2: Collaborate with Copilot

As you saw, Copilot created a Pull Request, the perfect place to work collaboratively. This pull request is very similar to your normal collaboration strategy, but Copilot provides some options to help with collaboration.

- **Pull Request Description** - Copilot will keep a concise overview of its goal and implementation.
- **Timeline** - Copilot will provide high-level notes about starting working sessions and commits.
- **Session History** - A detailed log of the steps Copilot took to implement the issue.
- **Comments** - Add a comment on the pull request conversation.
- **Reviews** - Combine multiple comments in a pull request review.
- **@ mentions** - You can tag Copilot in a comment just like a coworker.

Adding **comments** or a **review** will trigger Copilot to continue its work.

All work created by Copilot is committed with the assignee as a co-contributor (keeping your contribution graph safe).

#### Important Considerations

- All of Copilot's work is done on a branch with the convention `copilot/*`
- Push activity from Copilot doesn't trigger Actions workflows.
- Pull requests created by Copilot do still trigger Actions workflows, but they need human approval before running.
- Rulesets and similar protections are enforced.

### ⌨️ Activity: View Copilot's progress

1. In the issue, click on the reference link to the pull request. Alternately, use the **Pull Requests** tab in the top navigation.

   <img width="350" src="https://github.com/user-attachments/assets/40245540-e717-43b3-b2be-90f25cc494d0" />

1. Wait a moment for Copilot to complete its work and request a review from you.

1. Review the pull request description created by Copilot summarizing the work. Notice that it provides 3 things:

   - A summary of the original request.
   - A summary of the actions taken.
   - A link to the original issue.

   <img width="500" src="https://github.com/user-attachments/assets/acd70a53-b703-493e-9be3-ddfad9ff6d38" />

1. Scroll down slightly to view the timeline and high-level notes provided by Copilot. Click the **View session** button.

   <img width="500" src="https://github.com/user-attachments/assets/088260e6-bae0-40af-8186-864eb3e7b8a2" />

1. The new page shows a journal of Copilot's work. The left navigation is a list of each working session.

   <img width="500" src="https://github.com/user-attachments/assets/e54cfaf0-fabc-4c17-b977-0a7e6dc8de85" />

1. Return back to the pull request's convesation page when you are done.

### ⌨️ Activity: Provide Copilot feedback

1. At the top of the page, click the **Add your review** button.

   <img width="350" src="https://github.com/user-attachments/assets/d71847b9-573b-451e-9c85-946a6988e3f0" />

1. Find the new entry created by Copilot and click on the line to open the add comment dialog box.

   <img width="350" src="https://github.com/user-attachments/assets/729ab9cd-83f6-400d-8ebf-d0fc7673144c" />

1. Reading the description, we think it should be more interesting to match the Manga spirit.
   Let's ask Copilot to fix that. Enter the following text and click **Start a review**.

   ```md
   Please change this description to be inspired by Japanese Manga.
   It needs more personality to attract students.
   ```

1. At the top of the changes list, click the **Finish your review** button and select **Submit Review**.

1. After a moment, Copilot will add a session entry and indicate progress on the timeline. Click the **View changes** button to see the updated description.

   <img width="350" src="https://github.com/user-attachments/assets/a5ccd7b5-4df8-406a-b3a8-80328ba210e5" />

1. With our review submitted, Mona should be checking our work. Wait a moment for her to share the next steps.

<details>
<summary>Having trouble? 🤷</summary><br/>

If you don't get feedback, here are some things to check:

- Make sure your commit the changes in the `src/static/` directory to the branch `accelerate-with-copilot` and pushed/synchronized to GitHub.
- If Mona found a mistake, simply make a correction and push your changes again. Mona will check your work as many times as needed.

</details>

### ⌨️(optional) Activity: Manually make a change

Just like working with colleague, it often makes sense to push simple changes rather than explain them. Fortunately, this is still true with Copilot coding agent as well, since all work is done on a normal branch. That means we can make changes like normal. Nice!

1. Ensure you are on the page for the pull request.

1. In the top right, click the **Code** button
