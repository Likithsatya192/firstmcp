# My First MCP Project

This is my first MCP project! It's a simple chatbot that can help you browse the web and search for travel accommodations.

## Tools Used

1. **Playwright**
   - Used for web automation
   - Helps open and control web browsers
   - Can navigate to different websites
   - Performs clicks and interactions on web pages

2. **Airbnb**
   - Searches for available accommodations
   - Finds listings in specific locations
   - Shows detailed information about properties
   - Provides pricing and availability details

3. **DuckDuckGo Search**
   - Performs web searches
   - Finds general information
   - Provides safe and private search results
   - Helps gather information about locations and services

## Package Management

This project uses `uv` instead of `pip` for faster and more efficient Python package management. UV is a modern Python package installer and resolver.

## How to Run

1. Install the required packages using uv:
   ```bash
   uv add mcp-use
   uv add langchain-groq
   ```

2. Install Playwright browsers:
   ```bash
   playwright install
   ```

3. Run the chatbot:
   ```bash
   uv run app.py
   ```

## Basic Commands

- Type "open Google" to open Google in a browser
- Search for hotels by typing "find hotels in [city name]"
- Type "bye" to exit the program

## Note
Make sure you have Python installed on your computer before running the project.

That's it! Enjoy using the chatbot! 😊

## Project Structure

```
firstmcp/
├── app.py              # Main application file
├── README.md          # Project documentation
```

## Commands

- General chat interaction
- "bye" - Exit the program
- Web navigation commands:
  - "open [website]"
  - "search for hotels in [location]"
  - "navigate to [url]"

## License

This project is licensed under the MIT License - see the LICENSE file for details.
