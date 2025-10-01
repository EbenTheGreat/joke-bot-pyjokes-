# Joke Bot 🤖😂

A simple interactive **Joke Bot** built with
[LangGraph](https://python.langchain.com/docs/langgraph),
[Pydantic](https://docs.pydantic.dev/), and
[PyJokes](https://github.com/pyjokes/pyjokes).\
It demonstrates how to build a **stateful chatbot** **.

------------------------------------------------------------------------

##  Features

-   Tell jokes from different categories (`neutral`, `chuck`, `all`).
-   Support for multiple languages (`en`, `es`, `fr`, etc.).
-   Reset joke history .
-   Interactive command-line interface.
-   Powered by **LangGraph** for flow control.

------------------------------------------------------------------------

##  Project Structure

    joke-bot/
    │── main.py          # Main entry point
    │── README.md        # Project documentation
    │── .venv/           # Virtual environment (ignored in git)

------------------------------------------------------------------------

##  Installation

1.  Clone the repository:

    ``` bash
    git clone https://github.com/yourusername/joke-bot.git
    cd joke-bot
    ```

2.  Create a virtual environment:

    ``` bash
    python -m venv .venv
    source .venv/bin/activate   # Mac/Linux
    .venv\Scripts\activate    # Windows
    ```

3.  Install dependencies:

    ``` bash
    pip install -r requirements.txt
    ```

------------------------------------------------------------------------

##  Usage

Run the bot with:

``` bash
python main.py
```

You'll see:

    [n] Next [c] Category [l] Change language [r] Reset history [q] Quit

### Options:

-   **n** → Get the next joke 
-   **c** → Change joke category 
-   **l** → Change language 
-   **r** → Reset joke history 
-   **q** → Quit 

------------------------------------------------------------------------

##  Dependencies

-   `langgraph`
-   `pydantic`
-   `pyjokes`

Install them with:

``` bash
pip install langgraph pydantic pyjokes
```

------------------------------------------------------------------------

##  Author

Built  by **Ebenezer Tijani**\
 <ezebina360@gmail.com>\
🔗 [LinkedIn](https://www.linkedin.com/in/ebenezer-tijani-874244206)

------------------------------------------------------------------------

##  License

This project is licensed under the MIT License.
