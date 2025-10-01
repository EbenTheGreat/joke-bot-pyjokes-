from langgraph.constants import END
from langgraph.graph.state import CompiledStateGraph
from pydantic import BaseModel
from typing import Annotated, List, Literal
from operator import add
from pyjokes import get_joke
from langgraph.graph import StateGraph

class Joke(BaseModel):
    text: str
    category: str


class JokeState(BaseModel):
    jokes: Annotated[List[Joke], add] = []
    jokes_choice: Literal["n", "c", "l", "r", "q"] = "n"
    category: str= "neutral"
    language: str = "en"
    quit: bool = False


def show_menu(state: JokeState) -> dict:
    user_input = input("[n] Next [c] Category [l] Change language [r] Reset jokes [q] Quit\n>").strip().lower()
    return {"jokes_choice": user_input}

def fetch_joke(state: JokeState) -> dict:
    joke_text = get_joke(language=state.language, category=state.category)
    new_joke = Joke(text=joke_text, category=state.category)

    print(f"\n{new_joke.text}\n")
    return{"jokes": [new_joke]}

def update_category(state: JokeState) -> dict:
    categories = ["neutral", "chuck", "all"]
    selection = int(input("Select Category [0=neutral, 1=chuck, 2= all]: ").strip())
    return {"category": categories[selection]}

def update_language(state: JokeState) -> dict:
    languages = ["cs", "de", "en", "es", "eu", "fr", "gl", "hu", "it", "lt", "pl", "ru", "sv"]
    selection = int(input("Select Language "
                          "[0=cs, 1=de, 2=en, 3=es, 4=eu, 5=fr, 6=gl, 7=hu, =8it, 9=lt, 10=pl, 11=ru, 12=sv]: \n>")
                    .strip())
    return {"language": languages[selection]}

def reset_jokes(state: JokeState) -> dict:
    print("\n Joke history has been reset\n")
    return {"jokes": []}

def exit_bot(state: JokeState) -> dict:
    return {"quit": True}


# define the nodes
def route_choice(state: JokeState) -> str:
    if state.jokes_choice == "n":
        return "fetch_joke"
    if state.jokes_choice == "c":
        return "update_category"
    if state.jokes_choice == "l":
        return "update_language"
    if state.jokes_choice == "r":
        return "reset_jokes"

    if state.jokes_choice == "q":
        return "exit_bot"

    return "exit_bot"


def build_joke_graph() -> CompiledStateGraph:
    workflow = StateGraph(JokeState)

    workflow.add_node("show_menu", show_menu)
    workflow.add_node("fetch_joke", fetch_joke)
    workflow.add_node("update_category", update_category)
    workflow.add_node("update_language", update_language)
    workflow.add_node("reset_jokes", reset_jokes)
    workflow.add_node("exit_bot", exit_bot)

    workflow.set_entry_point("show_menu")

    workflow.add_conditional_edges(
        "show_menu",
        route_choice,
        {
            "fetch_joke": "fetch_joke",
            "update_category": "update_category",
            "update_language": "update_language",
            "reset_jokes": "reset_jokes",
            "exit_bot": "exit_bot"
        }
    )

    workflow.add_edge("fetch_joke", "show_menu")
    workflow.add_edge("update_category", "show_menu")
    workflow.add_edge("update_language", "show_menu")
    workflow.add_edge("reset_jokes", "show_menu")
    workflow.add_edge("exit_bot", END)

    return workflow.compile()


def main():
    graph = build_joke_graph()
    final_state = graph.invoke(JokeState(), config={"recursion_limit": 100})


main()


