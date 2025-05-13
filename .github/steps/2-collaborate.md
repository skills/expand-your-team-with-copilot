## Step 2: Collaborate with Copilot

As you saw, Copilot created a Pull Request, the perfect place to work collaboratively. This pull request is very similar to your normal collaboration strategy, but Copilot provides some options to help with collaboration.

- **Pull Request Description** - Copilot will keep a concise overview of its goal and implementation.
- **Timeline** - Copilot will provide high-level notes about starting working sessions and commits.
- **Session History** - A detailed log of the steps Copilot took to implement the issue.

You can provide feedback to Copilot the same way you would a colleague. Similarly, these trigger Copilot to begin another working session.

- **Comments** - Add a comment on the pull request conversation.
- **Reviews** - Combine multiple comments in a pull request review.
- **@ mentions** - You can tag Copilot in a comment just like a coworker.

#### Important Considerations

- Copilot's work is done on a branch with the convention `copilot/*` and does not have access to other branches.
- Copilot cannot trigger Actions workflows.
  - Workflows triggered on pull requests require human approval before running.
- Rulesets and similar protections are still enforced.

> [!TIP]
> All work created by Copilot is committed with the assignee as a co-contributor (keeping your contribution graph safe). 💕

### ⌨️ Activity: View Copilot's progress

1. In the issue, click on the reference link to the pull request. Alternately, use the **Pull Requests** tab in the top navigation.

   <img width="350" src="https://github.com/user-attachments/assets/40245540-e717-43b3-b2be-90f25cc494d0" />

1. Briefly look over the pull request description created by Copilot summarizing the work. Notice that it provides 4 things:

   - A short description of the original request.
   - A summary of the implemented actions.
   - A summary of the changes were verified.
   - A link to the original issue.

   <img width="500" src="https://github.com/user-attachments/assets/acd70a53-b703-493e-9be3-ddfad9ff6d38" />

1. Scroll down slightly to view the timeline and high-level notes provided by Copilot. Click the **View session** button.

   <img width="500" src="https://github.com/user-attachments/assets/088260e6-bae0-40af-8186-864eb3e7b8a2" />

1. The new page shows a journal of Copilot's work. The left navigation is a list of each working session.

   <img width="500" src="https://github.com/user-attachments/assets/2c80fa91-1123-4813-a801-42af368240b9" />

1. Return back to the pull request's convesation page when you are done view the session history.

1. If necessary, wait a moment for Copilot to finish working and request a review from you.

### ⌨️ Activity: Provide Copilot feedback

1. At the top of the page, click the **Add your review** button.

   <img width="350" src="https://github.com/user-attachments/assets/d71847b9-573b-451e-9c85-946a6988e3f0" />

1. Find the new entry created by Copilot. Hover over a line to show the plus sign. **Click** to open the add comment dialog box.

   <img width="350" src="https://github.com/user-attachments/assets/fd1375a4-fbdf-453e-a457-7bcb1fbbea23" />

1. Reading the description, we think it should be more interesting to match the Manga spirit. Let's ask Copilot to fix that. Enter the following text and click **Start a review**.

   ```md
   Please change this description to be inspired by Japanese Manga.
   It needs more personality to attract students.
   ```

   <img width="350" src="https://github.com/user-attachments/assets/f37da948-2062-4f46-ba75-bcff538800e4" />

1. At the top of the changes list, click the **Finish your review** button and select **Submit Review**.

1. After a moment, Copilot will add a session entry and indicate progress on the timeline. Click the **View changes** button to see the updated description.

   <img width="350" src="https://github.com/user-attachments/assets/a5ccd7b5-4df8-406a-b3a8-80328ba210e5" />

1. Wait for Copilot to finish then merge the pull request.

1. With our review submitted and the pull request merged, Mona should be checking our work. Give her a moment to respond with the next lesson.

<details>
<summary>Having trouble? 🤷</summary><br/>

If you don't get feedback, here are some things to check:

- Make sure your commit the changes in the `src/static/` directory to the branch `accelerate-with-copilot` and pushed/synchronized to GitHub.
- If Mona found a mistake, simply make a correction and push your changes again. Mona will check your work as many times as needed.

</details>
