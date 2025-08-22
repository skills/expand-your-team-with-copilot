## Step 2: Collaborate with Copilot

When Copilot creates a pull request in which you'll find:

- **Pull Request Description** - Copilot will keep a concise overview of its goal and implementation.
- **Timeline** - Copilot will provide high-level notes about starting working sessions and commits.
- **Session History** - A detailed log of the steps Copilot took to implement the issue.

You can provide feedback to Copilot the same way you would a colleague. These actions trigger Copilot to begin another working session.

- **Comments** - Add a comment on the pull request conversation.
- **Reviews** - Combine multiple comments in a pull request review.
- **@ mentions** - You can tag Copilot in a comment just like a coworker.

> [!IMPORTANT]
> Copilot only acts on review comments when explicitly tagged with `@copilot`. Without this mention, your review feedback will not trigger Copilot to respond or make changes. 

#### Important Considerations

- Copilot's work is done on a branch with the convention `copilot/*` and does not have access to other branches.
- Copilot cannot trigger Actions workflows.
  - Workflows triggered on pull requests require human approval before running.
- Rulesets and similar protections are still enforced.

> [!TIP]
> All work created by Copilot is committed with the assignee as a co-contributor (keeping your contribution graph safe). 💕

### ⌨️ Activity: View Copilot's progress

1. In the issue, click on the reference link to the pull request. Alternately, use the **Pull Requests** tab in the top navigation.

1. Watch in real-time as Copilot updates the pull request description. It will be progresses through 3 phases:

   <details>
      <summary>1. When starting, Copilot provides an initial copy of the issue. <b>[show image]</b></summary>
      <img width="500" alt="image" src="https://github.com/user-attachments/assets/967dbea0-01c2-4531-9bce-5a055d3dad25" />
   </details>

   <details>
      <summary>2. After planning, Copilot provides a set of action items. <b>[show image]</b></summary>
      <img width="500" alt="image" src="https://github.com/user-attachments/assets/acadb796-6545-4b6d-b2b3-9a00ea1744a2" />
   </details>

   <details>
      <summary>3. After finishing, Copilot provides a summary. <b>[show image]</b></summary>
      <img width="500" alt="image" src="https://github.com/user-attachments/assets/61204574-0262-4c2f-af4b-09b284f31b90" />
   </details>

1. Scroll down slightly to view the timeline and high-level notes provided by Copilot. Click the **View session** button.

   <img width="500" src="https://github.com/user-attachments/assets/088260e6-bae0-40af-8186-864eb3e7b8a2" />

1. The new page shows a journal of Copilot's work. The left navigation is a list of each working session.

   <img width="500" src="https://github.com/user-attachments/assets/2c80fa91-1123-4813-a801-42af368240b9" />

1. If necessary, wait for Copilot to finish working on the changes.

> [!TIP]
> You can use the **edited** dropdown to view the pull request description change history.
>
> <details>
> <summary>Show image</summary>
> <img width="500" alt="image" src="https://github.com/user-attachments/assets/cb88a67c-e42f-463c-88cd-b23a391b28a0" />
> </details>

### ⌨️ Activity: Provide Copilot feedback

1. Back in the pull request, click the **Add your review** button.

   <img width="350" src="https://github.com/user-attachments/assets/d71847b9-573b-451e-9c85-946a6988e3f0" />

1. Find the new entry created by Copilot. Hover over a line to show the plus sign. **Click** to open the add comment dialog box.

   <img width="350" src="https://github.com/user-attachments/assets/fd1375a4-fbdf-453e-a457-7bcb1fbbea23" />

1. Reading the description, we think it should be more interesting to match the Manga spirit. Let's ask Copilot to fix that. Enter the following text and click **Start a review**.

   ```md
   @copilot Please change this description to be inspired by Japanese Manga.
   It needs more personality to attract students.
   ```


1. At the top of the changes list, click the **Finish your review** button and select **Submit Review**.

1. After a moment, Copilot will add a new session entry and indicate progress on the timeline.

1. Wait for Copilot to finish working on the change and then click the **View changes** button to see the updated activity description.

   <img width="350" src="https://github.com/user-attachments/assets/a5ccd7b5-4df8-406a-b3a8-80328ba210e5" />

1. Activate the pull requests by clicking the **Ready to Review** button then click the **Merge** button.

1. With our review submitted and the pull request merged, Mona should be checking our work. Give her a moment to respond with the next lesson.

<details>
<summary>Having trouble? 🤷</summary><br/>

If you don't get feedback, here are some things to check:

- Make sure your commit the changes in the `src/static/` directory to the branch `accelerate-with-copilot` and pushed/synchronized to GitHub.
- If Mona found a mistake, simply make a correction and push your changes again. Mona will check your work as many times as needed.

</details>
