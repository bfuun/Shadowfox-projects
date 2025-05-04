{
 "cells": [
  {
   "cell_type": "markdown",
   "id": "53942929-b76d-4b7e-a41f-483ae363169f",
   "metadata": {},
   "source": [
    "BEGINNER LEVEL"
   ]
  },
  {
   "cell_type": "markdown",
   "id": "3787b83a-278f-41d6-b222-2ca71703316c",
   "metadata": {},
   "source": [
    "TASK 1:"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 4,
   "id": "31454521-3a96-4360-a116-a8f22a1dcdc7",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "Value of pi: 3.142857142857143\n",
      "Data type of variable 'pi': <class 'float'>\n"
     ]
    }
   ],
   "source": [
    "#Task 1\n",
    "pi = 22 / 7\n",
    "print(\"Value of pi:\", pi)\n",
    "print(\"Data type of variable 'pi':\", type(pi))\n"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 6,
   "id": "70dc9f59-9af8-4fe4-9812-7994baf14995",
   "metadata": {},
   "outputs": [
    {
     "ename": "SyntaxError",
     "evalue": "invalid syntax (3373042149.py, line 3)",
     "output_type": "error",
     "traceback": [
      "\u001b[1;36m  Cell \u001b[1;32mIn[6], line 3\u001b[1;36m\u001b[0m\n\u001b[1;33m    for = 4  # Attempt to assign a value to a reserved keyword\u001b[0m\n\u001b[1;37m        ^\u001b[0m\n\u001b[1;31mSyntaxError\u001b[0m\u001b[1;31m:\u001b[0m invalid syntax\n"
     ]
    }
   ],
   "source": [
    "#Task 2\n",
    "try:\n",
    "    for = 4  \n",
    "except SyntaxError as e:\n",
    "    print(\"Error:\", e)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 8,
   "id": "a124ad48-442a-4dc5-ad24-82748cfb13c4",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "Simple Interest for 3 years is: 150.0\n"
     ]
    }
   ],
   "source": [
    "#Task 3\n",
    "# Variables for principal, rate, and time\n",
    "principal = 1000  # Example value in currency units\n",
    "rate_of_interest = 5  # Annual interest rate in percentage\n",
    "time = 3  # Time in years\n",
    "simple_interest = (principal * rate_of_interest * time) / 100\n",
    "print(\"Simple Interest for\", time, \"years is:\", simple_interest)"
   ]
  },
  {
   "cell_type": "markdown",
   "id": "c046b496-cc7c-4039-97c3-bb59235ffc22",
   "metadata": {},
   "source": [
    "Task 2:\n"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 14,
   "id": "500b36d6-79fa-46a2-9876-34ad38d53cf5",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "Task 1 Result: 145 is represented as 'o' in this example.\n",
      "The representation used is the 'format' string method in Python.\n",
      "Task 2 Results:\n",
      "Area of the pond: 22155\n",
      "Total water in the pond: 31018 liters\n",
      "Task 3 Result: Speed is 1 meters per second.\n"
     ]
    }
   ],
   "source": [
    "# Task 1: Function with format\n",
    "def format_example(num, char):\n",
    "    formatted_string = \"{} is represented as '{}' in this example.\".format(num, char)\n",
    "    return formatted_string\n",
    "\n",
    "result = format_example(145, 'o')\n",
    "print(\"Task 1 Result:\", result)\n",
    "print(\"The representation used is the 'format' string method in Python.\")\n",
    "\n",
    "# Task 2: Calculate the area of a circular pond and the total water\n",
    "import math\n",
    "\n",
    "radius = 84 \n",
    "pi_value = 3.14\n",
    "circle_area = pi_value * (radius ** 2) \n",
    "\n",
    "\n",
    "water_per_square_meter = 1.4 \n",
    "total_water = int(circle_area * water_per_square_meter)  \n",
    "\n",
    "print(\"Task 2 Results:\")\n",
    "print(\"Area of the pond:\", int(circle_area)) \n",
    "print(\"Total water in the pond:\", total_water, \"liters\")\n",
    "\n",
    "# Task 3: Calculate speed in meters per second\n",
    "distance = 490 \n",
    "time_in_seconds = 7 * 60 \n",
    "\n",
    "speed = int(distance / time_in_seconds)\n",
    "print(\"Task 3 Result: Speed is\", speed, \"meters per second.\")\n"
   ]
  },
  {
   "cell_type": "markdown",
   "id": "b98a7173-66a8-486b-83e7-07d34aa5b77a",
   "metadata": {},
   "source": [
    "TASK 3:"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 16,
   "id": "096b1749-9a60-4b83-abdf-09b41526b2a5",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "Step 1: Number of members in the Justice League: 6\n",
      "Step 2: Justice League after adding Batgirl and Nightwing: ['Superman', 'Batman', 'Wonder Woman', 'Flash', 'Aquaman', 'Green Lantern', 'Batgirl', 'Nightwing']\n",
      "Step 3: Justice League after making Wonder Woman the leader: ['Wonder Woman', 'Superman', 'Batman', 'Flash', 'Aquaman', 'Green Lantern', 'Batgirl', 'Nightwing']\n",
      "Step 4: Justice League after separating Aquaman and Flash: ['Wonder Woman', 'Superman', 'Batman', 'Flash', 'Aquaman', 'Green Lantern', 'Batgirl', 'Nightwing']\n",
      "Step 5: Justice League after Superman assembled a new team: ['Cyborg', 'Shazam', 'Hawkgirl', 'Martian Manhunter', 'Green Arrow']\n",
      "Step 6: Justice League after sorting alphabetically: ['Cyborg', 'Green Arrow', 'Hawkgirl', 'Martian Manhunter', 'Shazam']\n",
      "The new leader is: Cyborg\n"
     ]
    }
   ],
   "source": [
    "\n",
    "justice_league = [\"Superman\", \"Batman\", \"Wonder Woman\", \"Flash\", \"Aquaman\", \"Green Lantern\"]\n",
    "num_members = len(justice_league)\n",
    "print(\"Step 1: Number of members in the Justice League:\", num_members)\n",
    "justice_league.extend([\"Batgirl\", \"Nightwing\"])\n",
    "print(\"Step 2: Justice League after adding Batgirl and Nightwing:\", justice_league)\n",
    "justice_league.remove(\"Wonder Woman\")\n",
    "justice_league.insert(0, \"Wonder Woman\")\n",
    "print(\"Step 3: Justice League after making Wonder Woman the leader:\", justice_league)\n",
    "justice_league.remove(\"Green Lantern\")\n",
    "aquaman_index = justice_league.index(\"Aquaman\")\n",
    "justice_league.insert(aquaman_index + 1, \"Green Lantern\")\n",
    "print(\"Step 4: Justice League after separating Aquaman and Flash:\", justice_league)\n",
    "justice_league = [\"Cyborg\", \"Shazam\", \"Hawkgirl\", \"Martian Manhunter\", \"Green Arrow\"]\n",
    "print(\"Step 5: Justice League after Superman assembled a new team:\", justice_league)\n",
    "justice_league.sort()\n",
    "print(\"Step 6: Justice League after sorting alphabetically:\", justice_league)\n",
    "new_leader = justice_league[0]\n",
    "print(\"The new leader is:\", new_leader)\n"
   ]
  },
  {
   "cell_type": "markdown",
   "id": "fb8e923a-4423-4414-a786-0691fd8f9557",
   "metadata": {},
   "source": [
    "task 4:if condition"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 18,
   "id": "9cd51bb6-fb0a-4bfa-ad81-90c5a4b7d371",
   "metadata": {},
   "outputs": [
    {
     "name": "stdin",
     "output_type": "stream",
     "text": [
      "Enter your height in meters:  106\n",
      "Enter your weight in kilograms:  45\n"
     ]
    },
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "Your BMI is: 0.00\n",
      "You are classified as: Underweight\n"
     ]
    }
   ],
   "source": [
    "\n",
    "height = float(input(\"Enter your height in meters: \"))\n",
    "weight = float(input(\"Enter your weight in kilograms: \"))\n",
    "bmi = weight / (height ** 2)\n",
    "if bmi >= 30:\n",
    "    category = \"Obesity\"\n",
    "elif 25 <= bmi < 30:\n",
    "    category = \"Overweight\"\n",
    "elif 18.5 <= bmi < 25:\n",
    "    category = \"Normal\"\n",
    "else:\n",
    "    category = \"Underweight\"\n",
    "\n",
    "print(f\"Your BMI is: {bmi:.2f}\")\n",
    "print(f\"You are classified as: {category}\")\n"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 20,
   "id": "470cdb78-5fdf-4bc9-9dc0-5726fbfe507d",
   "metadata": {},
   "outputs": [
    {
     "name": "stdin",
     "output_type": "stream",
     "text": [
      "Enter the name of a city:  Bangalore\n"
     ]
    },
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "The city 'Bangalore' belongs to India.\n"
     ]
    }
   ],
   "source": [
    "\n",
    "countries = {\n",
    "    \"Australia\": [\"Sydney\", \"Melbourne\", \"Brisbane\", \"Perth\"],\n",
    "    \"UAE\": [\"Dubai\", \"Abu Dhabi\", \"Sharjah\", \"Ajman\"],\n",
    "    \"India\": [\"Mumbai\", \"Bangalore\", \"Chennai\", \"Delhi\"]\n",
    "}\n",
    "\n",
    "\n",
    "city = input(\"Enter the name of a city: \")\n",
    "\n",
    "\n",
    "found = False\n",
    "for country, cities in countries.items():\n",
    "    if city in cities:\n",
    "        print(f\"The city '{city}' belongs to {country}.\")\n",
    "        found = True\n",
    "        break\n",
    "\n",
    "\n",
    "if not found:\n",
    "    print(f\"Sorry, the city '{city}' is not in the database.\")\n"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 32,
   "id": "c3dc2fff-a581-4d46-abce-7de9e33b2210",
   "metadata": {},
   "outputs": [
    {
     "name": "stdin",
     "output_type": "stream",
     "text": [
      "Enter the first city:  Sydney\n",
      "Enter the second city:  Mumbai\n"
     ]
    },
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "No, 'Sydney' belongs to Australia and 'Mumbai' belongs to India.\n"
     ]
    }
   ],
   "source": [
    "\n",
    "countries = {\n",
    "    \"Australia\": [\"Sydney\", \"Melbourne\", \"Brisbane\", \"Perth\"],\n",
    "    \"UAE\": [\"Dubai\", \"Abu Dhabi\", \"Sharjah\", \"Ajman\"],\n",
    "    \"India\": [\"Mumbai\", \"Bangalore\", \"Chennai\", \"Delhi\"]\n",
    "}\n",
    "city1 = input(\"Enter the first city: \").strip()\n",
    "city2 = input(\"Enter the second city: \").strip()\n",
    "country1 = next((country for country, cities in countries.items() if city1 in cities), None)\n",
    "country2 = next((country for country, cities in countries.items() if city2 in cities), None)\n",
    "if country1 and country2:\n",
    "    if country1 == country2:\n",
    "        print(f\"Yes, both cities belong to {country1}.\")\n",
    "    else:\n",
    "        print(f\"No, '{city1}' belongs to {country1} and '{city2}' belongs to {country2}.\")\n",
    "else:\n",
    "    print(\"One or both cities are not in the database.\")\n"
   ]
  },
  {
   "cell_type": "markdown",
   "id": "ee496d83-9b4c-4e1c-bae7-1c15feaa6f8d",
   "metadata": {},
   "source": [
    "Task 5:"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 34,
   "id": "a00ff21f-a0cc-4323-a4ae-b06943f9886e",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "Number of times 6 was rolled: 5\n",
      "Number of times 1 was rolled: 3\n",
      "Number of times two 6s were rolled in a row: 1\n"
     ]
    }
   ],
   "source": [
    "import random\n",
    "roll_count_6 = 0\n",
    "roll_count_1 = 0\n",
    "two_sixes_in_a_row = 0\n",
    "previous_roll = None\n",
    "for _ in range(20):\n",
    "    roll = random.randint(1, 6)  # Generate a random roll between 1 and 6\n",
    "    \n",
    "    if roll == 6:\n",
    "        roll_count_6 += 1\n",
    "    \n",
    "    if roll == 1:\n",
    "        roll_count_1 += 1\n",
    "    \n",
    "    if previous_roll == 6 and roll == 6:\n",
    "        two_sixes_in_a_row += 1\n",
    "    \n",
    "    previous_roll = roll\n",
    "\n",
    "print(f\"Number of times 6 was rolled: {roll_count_6}\")\n",
    "print(f\"Number of times 1 was rolled: {roll_count_1}\")\n",
    "print(f\"Number of times two 6s were rolled in a row: {two_sixes_in_a_row}\")\n"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 36,
   "id": "620d8e8e-7dfb-4deb-b33d-a5d5ab3855b9",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "Perform 10 jumping jacks. Total so far: 0\n"
     ]
    },
    {
     "name": "stdin",
     "output_type": "stream",
     "text": [
      "Are you tired? (yes/no):  no\n"
     ]
    },
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "You have 90 jumping jacks remaining.\n",
      "Perform 10 jumping jacks. Total so far: 10\n"
     ]
    },
    {
     "name": "stdin",
     "output_type": "stream",
     "text": [
      "Are you tired? (yes/no):  yes\n",
      "Do you want to skip the remaining sets? (yes/no):  no\n"
     ]
    },
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "Perform 10 jumping jacks. Total so far: 20\n"
     ]
    },
    {
     "name": "stdin",
     "output_type": "stream",
     "text": [
      "Are you tired? (yes/no):  no\n"
     ]
    },
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "You have 70 jumping jacks remaining.\n",
      "Perform 10 jumping jacks. Total so far: 30\n"
     ]
    },
    {
     "name": "stdin",
     "output_type": "stream",
     "text": [
      "Are you tired? (yes/no):  no\n"
     ]
    },
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "You have 60 jumping jacks remaining.\n",
      "Perform 10 jumping jacks. Total so far: 40\n"
     ]
    },
    {
     "name": "stdin",
     "output_type": "stream",
     "text": [
      "Are you tired? (yes/no):  yes\n",
      "Do you want to skip the remaining sets? (yes/no):  yes\n"
     ]
    },
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "You completed a total of 50 jumping jacks.\n"
     ]
    }
   ],
   "source": [
    "\n",
    "total_jumping_jacks = 100\n",
    "completed_jumping_jacks = 0\n",
    "while completed_jumping_jacks < total_jumping_jacks:\n",
    "    print(f\"Perform 10 jumping jacks. Total so far: {completed_jumping_jacks}\")\n",
    "    completed_jumping_jacks += 10\n",
    "    tired = input(\"Are you tired? (yes/no): \").strip().lower()\n",
    "\n",
    "    if tired in ['yes', 'y']:\n",
    "        skip = input(\"Do you want to skip the remaining sets? (yes/no): \").strip().lower()\n",
    "        if skip in ['yes', 'y']:\n",
    "            print(f\"You completed a total of {completed_jumping_jacks} jumping jacks.\")\n",
    "            break\n",
    "    elif tired in ['no', 'n']:\n",
    "        remaining_jumping_jacks = total_jumping_jacks - completed_jumping_jacks\n",
    "        print(f\"You have {remaining_jumping_jacks} jumping jacks remaining.\")\n",
    "if completed_jumping_jacks == total_jumping_jacks:\n",
    "    print(\"Congratulations! You completed the workout.\")\n"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "d5c80474-5ac7-48db-ad15-f94562637f0c",
   "metadata": {},
   "outputs": [],
   "source": []
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
