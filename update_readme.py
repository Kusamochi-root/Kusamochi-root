import datetime
import os

# Define the log message with a tech-focused vibe
current_time = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S UTC")
status_message = "System Online"
objective = "Optimizing Neural Patterns & Security Protocols"

log_entry = (
    f"#### ⚡ Automated System Status\n"
    f"- **Timestamp:** `{current_time}`\n"
    f"- **Current Status:** `{status_message}`\n"
    f"- **Objective:** `{objective}`\n"
    f"- **Environment:** `GitHub Actions / Ubuntu-Latest`\n"
)

# Read the existing README
with open("README.md", "r", encoding="utf-8") as f:
    content = f.read()

# Define the markers (Do not change these)
start_marker = "<!-- START_LOG -->"
end_marker = "<!-- END_LOG -->"

# Find the positions to inject the new content
try:
    start_idx = content.find(start_marker) + len(start_marker)
    end_idx = content.find(end_marker)

    if start_idx == -1 or end_idx == -1:
        raise ValueError("Markers not found in README.md")

    # Construct the new content
    new_content = content[:start_idx] + "\n" + log_entry + content[end_idx:]

    # Write back to README
    with open("README.md", "w", encoding="utf-8") as f:
        f.write(new_content)
    print("README updated successfully.")

except Exception as e:
    print(f"Error updating README: {e}")
