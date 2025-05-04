{
 "cells": [
  {
   "cell_type": "markdown",
   "id": "3d79fefa-08f0-4994-97ff-547671c00045",
   "metadata": {},
   "source": [
    "INTERMEDIATE LEVEL"
   ]
  },
  {
   "cell_type": "markdown",
   "id": "74ec12e5-f00a-4fff-8f4f-5b60059905e9",
   "metadata": {},
   "source": [
    "TASK 1:"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 6,
   "id": "3a0b3a51-c8d6-4411-baa9-65f15133caec",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "Found 0 articles:\n"
     ]
    }
   ],
   "source": [
    "import requests\n",
    "from bs4 import BeautifulSoup\n",
    "\n",
    "def scrape_website(url):\n",
    "    try:\n",
    "        # Send a GET request to the website\n",
    "        response = requests.get(url)\n",
    "        response.raise_for_status()  # Check for HTTP request errors\n",
    "\n",
    "        # Parse the website content\n",
    "        soup = BeautifulSoup(response.text, 'html.parser')\n",
    "\n",
    "        # Extract specific elements, e.g., article titles\n",
    "        titles = soup.find_all('h2')  # Assuming article titles are within <h2> tags\n",
    "\n",
    "        print(f\"Found {len(titles)} articles:\")\n",
    "        for i, title in enumerate(titles, start=1):\n",
    "            print(f\"{i}: {title.get_text(strip=True)}\")\n",
    "    except requests.exceptions.RequestException as e:\n",
    "        print(f\"An error occurred: {e}\")\n",
    "\n",
    "# Replace 'example.com' with the URL of the website you want to scrape\n",
    "website_url = \"https://example.com\"\n",
    "scrape_website(website_url)\n"
   ]
  },
  {
   "cell_type": "markdown",
   "id": "ed80a2ff-29ae-4f6c-832e-4471ac323235",
   "metadata": {},
   "source": [
    "TASK 2:"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 4,
   "id": "8851510d-3865-4b5b-b34f-4ac11d7317f2",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "Welcome to Hangman!\n",
      "\n",
      "           -----\n",
      "           |\n",
      "           |\n",
      "           |\n",
      "           |\n",
      "           |\n",
      "        \n",
      "Hint: A game where you guess letters to find a word.\n",
      "_______\n",
      "\n",
      "\n"
     ]
    },
    {
     "name": "stdin",
     "output_type": "stream",
     "text": [
      "Please guess a letter or word:  t\n"
     ]
    },
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "t is not in the word.\n",
      "\n",
      "           -----\n",
      "           |   |\n",
      "           |\n",
      "           |\n",
      "           |\n",
      "           |\n",
      "        \n",
      "_______\n",
      "\n",
      "\n"
     ]
    },
    {
     "name": "stdin",
     "output_type": "stream",
     "text": [
      "Please guess a letter or word:  a\n"
     ]
    },
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "Good job! a is in the word.\n",
      "\n",
      "           -----\n",
      "           |   |\n",
      "           |\n",
      "           |\n",
      "           |\n",
      "           |\n",
      "        \n",
      "_a___a_\n",
      "\n",
      "\n"
     ]
    },
    {
     "name": "stdin",
     "output_type": "stream",
     "text": [
      "Please guess a letter or word:  l\n"
     ]
    },
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "l is not in the word.\n",
      "\n",
      "           -----\n",
      "           |   |\n",
      "           |   O\n",
      "           |\n",
      "           |\n",
      "           |\n",
      "        \n",
      "_a___a_\n",
      "\n",
      "\n"
     ]
    },
    {
     "name": "stdin",
     "output_type": "stream",
     "text": [
      "Please guess a letter or word:  h\n"
     ]
    },
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "Good job! h is in the word.\n",
      "\n",
      "           -----\n",
      "           |   |\n",
      "           |   O\n",
      "           |\n",
      "           |\n",
      "           |\n",
      "        \n",
      "ha___a_\n",
      "\n",
      "\n"
     ]
    },
    {
     "name": "stdin",
     "output_type": "stream",
     "text": [
      "Please guess a letter or word:  hangman\n"
     ]
    },
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "\n",
      "           -----\n",
      "           |   |\n",
      "           |   O\n",
      "           |\n",
      "           |\n",
      "           |\n",
      "        \n",
      "hangman\n",
      "\n",
      "\n",
      "Congratulations! You've guessed the word!\n"
     ]
    }
   ],
   "source": [
    "import random\n",
    "\n",
    "def get_word_and_hint():\n",
    "    words_with_hints = {\n",
    "        \"python\": \"A popular programming language.\",\n",
    "        \"hangman\": \"A game where you guess letters to find a word.\",\n",
    "        \"computer\": \"An electronic device for storing and processing data.\",\n",
    "        \"programming\": \"The process of writing code to create software.\",\n",
    "        \"developer\": \"A person who creates software applications.\",\n",
    "        \"shadowfox\": \"An internship company.\"\n",
    "    }\n",
    "    word, hint = random.choice(list(words_with_hints.items()))\n",
    "    return word, hint\n",
    "\n",
    "def display_hangman(tries):\n",
    "    stages = [\n",
    "        \"\"\"\n",
    "           -----\n",
    "           |   |\n",
    "           |   O\n",
    "           |  /|\\\\\n",
    "           |  / \\\\\n",
    "           |\n",
    "        \"\"\",\n",
    "        \"\"\"\n",
    "           -----\n",
    "           |   |\n",
    "           |   O\n",
    "           |  /|\\\\\n",
    "           |  /\n",
    "           |\n",
    "        \"\"\",\n",
    "        \"\"\"\n",
    "           -----\n",
    "           |   |\n",
    "           |   O\n",
    "           |  /|\n",
    "           |\n",
    "           |\n",
    "        \"\"\",\n",
    "        \"\"\"\n",
    "           -----\n",
    "           |   |\n",
    "           |   O\n",
    "           |   |\n",
    "           |\n",
    "           |\n",
    "        \"\"\",\n",
    "        \"\"\"\n",
    "           -----\n",
    "           |   |\n",
    "           |   O\n",
    "           |\n",
    "           |\n",
    "           |\n",
    "        \"\"\",\n",
    "        \"\"\"\n",
    "           -----\n",
    "           |   |\n",
    "           |\n",
    "           |\n",
    "           |\n",
    "           |\n",
    "        \"\"\",\n",
    "        \"\"\"\n",
    "           -----\n",
    "           |\n",
    "           |\n",
    "           |\n",
    "           |\n",
    "           |\n",
    "        \"\"\"\n",
    "    ]\n",
    "    return stages[tries]\n",
    "\n",
    "def play_hangman():\n",
    "    word, hint = get_word_and_hint()\n",
    "    word_completion = \"_\" * len(word)\n",
    "    guessed = False\n",
    "    guessed_letters = []\n",
    "    guessed_words = []\n",
    "    tries = 6\n",
    "\n",
    "    print(\"Welcome to Hangman!\")\n",
    "    print(display_hangman(tries))\n",
    "    print(f\"Hint: {hint}\")\n",
    "    print(word_completion)\n",
    "    print(\"\\n\")\n",
    "\n",
    "    while not guessed and tries > 0:\n",
    "        guess = input(\"Please guess a letter or word: \").lower()\n",
    "\n",
    "        if len(guess) == 1 and guess.isalpha():\n",
    "            if guess in guessed_letters:\n",
    "                print(\"You already guessed that letter.\")\n",
    "            elif guess not in word:\n",
    "                print(f\"{guess} is not in the word.\")\n",
    "                tries -= 1\n",
    "                guessed_letters.append(guess)\n",
    "            else:\n",
    "                print(f\"Good job! {guess} is in the word.\")\n",
    "                guessed_letters.append(guess)\n",
    "                word_completion = \"\".join([letter if letter in guessed_letters else \"_\" for letter in word])\n",
    "                if \"_\" not in word_completion:\n",
    "                    guessed = True\n",
    "        elif len(guess) == len(word) and guess.isalpha():\n",
    "            if guess in guessed_words:\n",
    "                print(\"You already guessed that word.\")\n",
    "            elif guess != word:\n",
    "                print(f\"{guess} is not the word.\")\n",
    "                tries -= 1\n",
    "                guessed_words.append(guess)\n",
    "            else:\n",
    "                guessed = True\n",
    "                word_completion = word\n",
    "        else:\n",
    "            print(\"Invalid input. Please try again.\")\n",
    "\n",
    "        print(display_hangman(tries))\n",
    "        print(word_completion)\n",
    "        print(\"\\n\")\n",
    "\n",
    "    if guessed:\n",
    "        print(\"Congratulations! You've guessed the word!\")\n",
    "    else:\n",
    "        print(f\"Sorry, you ran out of tries. The word was '{word}'.\")\n",
    "\n",
    "if __name__ == \"__main__\":\n",
    "    play_hangman()"
   ]
  }
 ],
 "metadata": {
  "kernelspec": {
   "display_name": "Python [conda env:base] *",
   "language": "python",
   "name": "conda-base-py"
  },
  "language_info": {
   "codemirror_mode": {
    "name": "ipython",
    "version": 3
   },
   "file_extension": ".py",
   "mimetype": "text/x-python",
   "name": "python",
   "nbconvert_exporter": "python",
   "pygments_lexer": "ipython3",
   "version": "3.12.7"
  }
 },
 "nbformat": 4,
 "nbformat_minor": 5
}
