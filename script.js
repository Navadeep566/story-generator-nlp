async function generateStory() {
  const result = document.getElementById("result");
  result.innerText = "Generating story... Please wait.";

  const data = {
    genre: document.getElementById("genre").value,
    mood: document.getElementById("mood").value,
    character_name: document.getElementById("character_name").value,
    character_role: document.getElementById("character_role").value,
    setting: document.getElementById("setting").value,
    goal: document.getElementById("goal").value,
    conflict: document.getElementById("conflict").value,
    ending_type: document.getElementById("ending_type").value,
    plot_twist: document.getElementById("plot_twist").value,
    story_length: document.getElementById("story_length").value,
  };

  try {
    const response = await fetch("/generate", {
      method: "POST",
      headers: {
        "Content-Type": "application/json",
      },
      body: JSON.stringify(data),
    });

    const output = await response.json();

    result.innerText = output.result;
  } catch (error) {
    result.innerText = "Error generating story.";
  }
}
