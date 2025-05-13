## Step 3: Preparing Copilot's environment

Let's add some information about the school, roles to assume, and typical tasks the teachers request and a pre-configured development environment to make it faster (so Jessica in IT doesn't ask about increased Actions minutes usage).

- **copilot instructions** - Provide project specific context for copilot before considering the issue.
  - Provide business considerations for developing the project.
  - Provide roles to guide Copilot.
  - Provide useful commands for common tasks.
- **copilot setup steps** - Customize the development environment in advance to make sessions faster.
  - Pre-install useful tools for Copilot.
  - Reducing errors from Copilot installing incorrect versions.
- **environment** - Use repository environments for configurations.
  - Provide variables to adjust deployments for different environments.
  - Provide secrets to access additional resources.

> [!TIP] You can also enable an MCP server. Check out the dedicate exercise on that, which will also make it available for Copilot coding agent.

### ⌨️ Activity: Make instructions to guide Copilot

1. Open the `.github/copilot-instructions.md` file.

1. Replace the placeholder text with a link to the development guide.

   ```md
   ## Development Environment

   For detailed setup and development instructions, please refer to our [Development Guide](../docs/how-to-develop.md).
   ```

1. Add some additional information about the school and teachers to help Copilot interact more naturally.

   ```md
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
   ```

   > 💡 Tip: You can add more detail to your description. Check out the `copilot-instructions-ext.md` file.

1. Update the readme to explain that teachers can now assign issues to Copilot.

### ⌨️ Activity: Prepare the coding environment for copilot

Configuring Copilots environment is very similar to [GitHub Actions]().

1. Open the `.github/workflows/copilot-setup-steps.yml`
1. Verify the job name is `copilot-setup-steps`.
1. Add an entry in the [permissions](https://docs.github.com/en/actions/writing-workflows/choosing-what-your-workflow-does/controlling-permissions-for-github_token) area to grant Copilot access to read the repository content and other issues.

   ```yml
   permissions:
     contents: read
     issues: read
   ```

   > Note: Copilot will automatically retrieve the repository content later. This provides early access during setup to install the dependencies.

1. Add a step to checkout the code. and install our project dependencies.

   ```yml
   steps:
     - name: Checkout code
       uses: actions/checkout@v4
   ```

   > Note: Copilot will automatically determine this is necessary later. Doing it now saves Copilot some time.

1. Add a step to install the project dependencies before starting work.

   ```yml
   steps:
     - name: Set up Python
       uses: actions/setup-python@v4
       with:
         python-version: "3.x"
         cache: "pip"

     - name: Install Python dependencies
       run: |
         python -m pip install --upgrade pip
         pip install -r src/requirements.txt
   ```

   For all configuration options, see the [pre-installing dependencies for Copilot](https://docs.github.com/en/enterprise-cloud@latest/early-access/copilot/coding-agent/customizing-copilot-coding-agents-development-environment#pre-installing-tools-or-dependencies-in-copilots-environment) documentation.

1. With our files committed, wait for mona to provide the next steps.

### (optional) Activity: Provide environment variables

1. Add a repository environment.
2. Add a variable
3. Add a secret.
4. Modify `copilot-step-step.yml` to use the environment.
