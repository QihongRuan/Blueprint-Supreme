# Blueprint Supreme (大展鸿图)

Our project, "Blueprint Supreme" (reflecting '大展鸿图' - "Realize Grand Ambitions"), is a powerful tool designed to bridge the cultural gap and connect the Super Bowl with its vast and growing Chinese audience. We solve a key problem: making American football not just understood, but culturally resonant and exciting for millions of potential fans in China.

How it works: Our application takes real-time Super Bowl highlights as input. Using the advanced reasoning of Google's Gemini API, it "learns" from the highlight and instantly generates a dynamic, bilingual Chinese rap verse in the epic style of "Blueprint Supreme." A game-winning touchdown isn't just a play; it's a tale of glory, ambition, and a dragon's triumph on the field, all captured in a personalized rap.

Impact: The impact is immense. We are creating a new, culturally-fluent layer of engagement for one of the world's largest markets. This tool makes the Super Bowl more accessible, shareable, and exciting for Chinese-speaking fans, allowing them to experience the game's biggest moments through a unique cultural lens. It's not just about watching the game; it's about participating in its story and its glory, in a language and style that speaks to them, embodying the spirit of "Blueprint Supreme."

## How to Run the Project

### 1. Set up your Gemini API Key

Before you run the application, you need to configure your Gemini API key.

*   Open the `app.py` file.
*   Find the line `genai.configure(api_key="YOUR_GEMINI_API_KEY")`.
*   Replace `"YOUR_GEMINI_API_KEY"` with your actual Gemini API key.

For better security, it is recommended to set your API key as an environment variable named `GEMINI_API_KEY`.

### 2. Install Dependencies

In your terminal, navigate to the `interactive-rap-anthem` directory and run the following command to install the required Python packages:

```bash
pip install -r requirements.txt
```

### 3. Run the Application

Once the dependencies are installed, run the following command to start the Flask web server:

```bash
python app.py
```

You should see an output indicating that the server is running. Now, you can open your web browser and go to `http://127.0.0.1:5000` to see your application in action.

## How to Create a GitHub Repository

Your project is already in a local Git repository. Here's how to publish it to GitHub:

### 1. Create a New Repository on GitHub

*   Go to [GitHub](https://github.com) and log in.
*   Click the **+** icon in the top-right corner and select **New repository**.
*   Give your repository a name (e.g., `Blueprint-Supreme`).
*   You can add a short description.
*   Make sure the repository is set to **Public** for the hackathon submission.
*   Click **Create repository**.

### 2. Push Your Local Repository to GitHub

After creating the repository on GitHub, you will see a page with some commands. You need the commands under the section "...or push an existing repository from the command line".

Copy and run the following commands in your terminal, in the `interactive-rap-anthem` directory. **Remember to replace `YOUR_USERNAME` and `YOUR_REPOSITORY_NAME` with your actual GitHub username and repository name.**

```bash
git remote add origin https://github.com/YOUR_USERNAME/YOUR_REPOSITORY_NAME.git
git branch -M main
git push -u origin main
```

Now, your code is on GitHub and ready for submission!