## Step 4: Manage multiple tasks with Agents Panel 🎛️

Now, with Copilot's workspace prepared, let's work on some more complex issues to make the Extra curricular Activities website even more amazing! ✨🚀

Until now, we've been teaming up with Copilot by assigning issues one at a time. 📝🤝

But what if you could skip the extra steps and jump straight into task mode? What if Copilot could juggle several jobs at once, keeping you in the loop as they progress? 🤹‍♂️

Let's see how that's done! 👀

### 📖 Theory: Delegate from anywhere with Agents Panel

The agents panel is your mission control center for agentic workflows on GitHub.

It’s a lightweight overlay that allows you to hand new tasks to Copilot and track existing tasks without navigating away from your current work.

<!-- image source: https://github.blog/news-insights/product-news/agents-panel-launch-copilot-coding-agent-tasks-anywhere-on-github/ -->

   <img width="400" alt="Agents Panel view" src="https://github.blog/wp-content/uploads/2025/08/Agents-panel-with-callout-2.png" />

From the agents panel, you can:

- 🛠️ Assign background tasks without switching pages.
- 👀 Monitor running tasks with real-time status.
- 🔗 Jump into pull requests when you’re ready to review.

With the Agents panel, you can quickly assign multiple issues, track their progress, and review results—all in one place.

### ⌨️ Activity: Assign tasks through the Agents Panel :robot:

> [!IMPORTANT]
> Make sure you merged the `prepare-environment` branch from the previous step before proceeding.

Let's get you familiarized with the Agents panel!

1. In a new tab, open the **Copilot Agents** panel from the top navigation bar
   <img width="600" alt="Agents panel view" src="https://github.com/user-attachments/assets/d0eba779-ab37-4cf9-9229-dca8a64c119c" />

1. Make sure the `{{ full_repo_name }}` repository is selected in the panel and the branch is set to `main`.
1. Assign Copilot to work on the following task:

   > ![Static Badge](https://img.shields.io/badge/-Task%201-text?style=social&logo=github%20copilot)
   >
   > ```prompt
   > Integrate social sharing buttons so
   > users can easily share activities with their friends
   > ```

   > ✨ **Bonus:** Think of something you would want improved on the website and assign it to Copilot. You can use your creativity here!

1. After a moment, you will notice that the task appears in the panel with its current status. You can check back here for a high level overview of all your assigned tasks.

   <img width="400" alt="Agents Panel task in progress view" src="https://github.com/user-attachments/assets/0fc53085-d68d-496e-a81b-1ab78014db63" />

1. Click on the task to open the pull request in a new tab and track how Copilot is working on it in real time - just like you did in the first step.

1. Scroll down and click the **View Session** button.
1. In the session logs, you'll notice Copilot begins by running the customization steps you've setup in the previous step!
   <img width="900" alt="Copilot session logs with copilot setup steps" src="https://github.com/user-attachments/assets/72c282f6-7780-4c8f-ad0b-ac8d21c4661c" />

   
1. Let's leave Copilot to work its magic for now, you can come back to review the results later ✨

> [!TIP]
> You can also access the Agents Panel in full screen mode at https://github.com/copilot/agents



### ⌨️ Activity: Try implementing 2 issues simultaneously

You still have some issues opened on the repository, let's see how Copilot can handle working on multiple issues at the same time!

1. In the top navigation, select the **Issues** tab.

1. Find the the following 2 issues and open each in a new tab.

   - `Difficulty Tracks`

   - `Dark Mode`

1. With both tabs open, assign both to Copilot simultaneously.

1. Open the **Copilot Agents** panel again and notice that the issues you assign also appear here!
   
   <img width="300"  alt="Copilot Agents Panel with three tasks running in parallel" src="https://github.com/user-attachments/assets/dfd77721-c736-470d-89d6-e4cad31edbd5" />


1. In both tasks, navigate to the created pull requests and monitor the progress. Remember you can click the **View Session** button to see what Copilot is doing in real time.
   > 💡 **Tip:**  You can also check the status of the task you assigned in the previous activity.

1. When Copilot is finished on any of the tasks, review the PR description, the changes made and merge the pull request!

1. With at least 1 pull request merged, Mona should be checking your work and preparing your final review.

> [!IMPORTANT]
> Working on multiple issues in parallel is an art-form. 🎨
> Make sure you keep them independent to avoid merge conflicts! 😱
