# 🔨 Blind Auction Python

A beginner-friendly Python terminal project that simulates a blind auction. Users can enter their names and bid amounts, while previous bids are hidden from the next bidder. At the end, the program announces the highest bidder as the winner.


## 🔗 Project Links

- 📂 **GitHub Repository:** [numair-2003/Blind-Auction-Python](https://github.com/numair-2003/Blind-Auction-Python)
- 🌐 **Run on Replit:** [Blind Auction Python on Replit](https://replit.com/@numair1919/Blind-Auction-Python)
- 🧭 **Draw.io Flowchart:** [Open Blind Auction Flowchart on draw.io](https://app.diagrams.net/#G1ZWoMXL_PMoSwjG1y5KwMYZVrbarVVzZk#%7B%22pageId%22%3A%222h3YnR6jpbWVX-HiOQlN%22%7D)
- 🎨 **ASCII Art Website:** [ASCII Art Archive](https://ascii.co.uk/art)


## 📌 What Is a Blind Auction?

A **blind auction** is an auction where bidders submit their bids privately. Other bidders cannot see the previous bid amounts. After all bids are submitted, the highest bidder wins the auction.

This Python project recreates that idea in the terminal by hiding previous entries before the next bidder enters their bid.

## 📖 Learn More About Blind Auctions

If you're unfamiliar with the concept of a blind auction, this article provides a clear explanation of how blind auctions work and where they are commonly used:

🔗 https://www.ourauctionhub.com/archives/2759

This resource was used as a reference to better understand the auction concept before implementing it as a Python terminal application.


## ✨ Features

- 🔨 Displays a gavel ASCII art logo
- 👤 Takes bidder names as input
- 💵 Takes bid amounts as decimal numbers using `float`
- 📦 Stores bidders and bids in a Python dictionary
- 🙈 Hides previous bids using blank lines
- 🔁 Allows multiple bidders
- 🏆 Finds the highest bidder using a function
- 💻 Runs directly in the terminal

## 🛠️ Technologies Used

- 🐍 Python 3
- 💻 PyCharm or any Python IDE
- 🎨 ASCII art
- 🧭 Draw.io / diagrams.net
- 📦 Python dictionaries
- 🔁 Loops and conditionals

## 📁 Project Structure

```text
Blind-Auction-Python/
|
|-- main.py
|-- art.py
|-- blind_auction_flowchart.png
|-- README.md
```

## 🧭 Flowchart

The project includes a flowchart that explains the Blind Auction program logic.

🔗 **View Flowchart on Draw.io:** [Open Blind Auction Flowchart](https://app.diagrams.net/#G1ZWoMXL_PMoSwjG1y5KwMYZVrbarVVzZk#%7B%22pageId%22%3A%222h3YnR6jpbWVX-HiOQlN%22%7D)

If you upload the flowchart image to your GitHub repository, you can display it in the README using:

```md
![Blind Auction Flowchart](blind_auction_flowchart.png)
```

## ⚙️ How It Works

1. The program imports the gavel logo from `art.py`.
2. The logo is printed when the program starts.
3. An empty dictionary named `bidders_dictionary` is created.
4. The program asks the user for their name.
5. The program asks the user for their bid amount.
6. The name is stored as the dictionary key.
7. The bid amount is stored as the dictionary value.
8. The program asks if there are more bidders.
9. If the user types `yes`, the screen is hidden using blank lines.
10. If the user types `no`, the auction ends.
11. The `find_largest_bidder()` function checks all bids.
12. The program prints the winner and the highest bid.

## 🧪 Example Gameplay

```text
What is your name? Ali
What is your bid? $150
Are there any other bidders? Type 'yes' or 'no'.
yes
```

After the next bidder enters their bid:

```text
What is your name? Ahmed
What is your bid? $250
Are there any other bidders? Type 'yes' or 'no'.
no
The winner is Ahmed with a bid of $250.0.
```

## 🚀 How to Run Locally

1. Clone the GitHub repository:

```bash
git clone https://github.com/numair-2003/Blind-Auction-Python.git
```

2. Open the project folder:

```bash
cd Blind-Auction-Python
```

3. Run the Python file:

```bash
python main.py
```

or:

```bash
python3 main.py
```

## 🌐 How to Run on Replit

You can run this project online using Replit without installing Python on your computer.

🔗 **Replit Link:** [Blind Auction Python on Replit](https://replit.com/@numair1919/Blind-Auction-Python)

### Steps to Run on Replit

1. Open the Replit project link.
2. Click the **Run** button.
3. The program will start in the Replit console.
4. Enter the first bidder's name.
5. Enter the bid amount.
6. Type `yes` if there are more bidders.
7. Type `no` when all bidders have entered their bids.
8. The program will display the winner with the highest bid.

### If You Are Creating a New Replit Project

1. Go to [Replit](https://replit.com/).
2. Create a new Repl.
3. Choose **Python** as the language.
4. Upload or create these files:
   - `main.py`
   - `art.py`
   - `blind_auction_flowchart.png`
5. Make sure `main.py` and `art.py` are in the same Replit project.
6. Click the **Run** button.
7. If needed, open the Shell and run:

```bash
python main.py
```

## 🐙 How to Push This Project to GitHub

### Method 1: Upload Files Using GitHub Website

1. Go to [GitHub](https://github.com/).
2. Click **New repository**.
3. Use this repository name:

```text
Blind-Auction-Python
```

4. Add this description:

```text
A beginner-friendly Python Blind Auction app that collects hidden bids, stores bidders in a dictionary, and announces the highest bidder in the terminal.
```

5. Keep the repository public.
6. Click **Create repository**.
7. Click **Add file**.
8. Click **Upload files**.
9. Upload these files:
   - `main.py`
   - `art.py`
   - `blind_auction_flowchart.png`
   - `README.md`
10. Add a commit message:

```text
Initial commit
```

11. Click **Commit changes**.

### Method 2: Push Using Git Commands

Run these commands inside your project folder:

```bash
git init
git add .
git commit -m "Initial commit"
git branch -M main
git remote add origin https://github.com/numair-2003/Blind-Auction-Python.git
git push -u origin main
```

## 🎨 ASCII Art Logo

This project uses a gavel ASCII art logo stored in `art.py`.

The ASCII art logo was created using inspiration from:

🔗 [ASCII Art Archive](https://ascii.co.uk/art)

### How to Use ASCII Art in Python

1. Visit [ASCII Art Archive](https://ascii.co.uk/art).
2. Search for words such as:
   - `auction`
   - `gavel`
   - `hammer`
   - `bid`
3. Copy the ASCII art you like.
4. Open `art.py`.
5. Store the ASCII art inside triple quotes.

Example:

```python
logo = r'''
YOUR ASCII ART HERE
'''
```

6. Import and print it inside `main.py`:

```python
import art

print(art.logo)
```

## 🧠 Python Concepts Practiced

- Variables
- Functions
- User input
- Dictionaries
- Loops
- Conditional statements
- Importing custom files
- Finding the maximum value
- Terminal-based program flow

## 📄 Code Files

### `main.py`

This file contains the main Blind Auction program logic.

It handles:

- Printing the logo
- Creating the bidders dictionary
- Asking for bidder names
- Asking for bid amounts
- Storing bids
- Asking if more bidders should be added
- Hiding previous bids
- Calling `find_largest_bidder()`

### `art.py`

This file contains the gavel ASCII art logo displayed at the start.

## 🏆 Winner Selection Logic

The winner is selected using this function:

```python
def find_largest_bidder(bidders_dictionary):
    largest_bid_price = 0
    winner_name = ""
    for name in bidders_dictionary:
        if bidders_dictionary[name] > largest_bid_price:
            winner_name = name
            largest_bid_price = bidders_dictionary[name]

    print(f"The winner is {winner_name} with a bid of ${largest_bid_price}.")
```

The dictionary stores data like this:

```python
{
    "Ali": 150.0,
    "Ahmed": 250.0
}
```

## 🌱 Possible Improvements

- ✅ Add input validation for empty names
- 🔢 Prevent invalid bid amounts
- 💵 Format winning bid to two decimal places
- 🔁 Add an option to restart the auction
- 🧹 Use a stronger screen-clearing method
- 🏆 Handle tied bids
- 📊 Show all bids after the winner is announced
- 🖥️ Create a GUI version

## 👨‍💻 Author

Created by **Numair Fahad**.

## 📜 License

This project is open source and available under the MIT License.