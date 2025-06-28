## 🏰 Dungeon Duel

**A Text-Based Dungeon Crawler Adventure Game**

**By:** Parantap Mishra (Class XI, 2024–25)

---

## 📜 Project Overview

Taking insipiration from Dungeon Adventure, **Dungeon Duel** is a menu-driven, terminal-based Python game where players battle fearsome monsters in a dungeon setting. Starting with a small dagger, leather armor, and 100 coins, players must strategically manage their inventory, buy better gear from the shop, and survive turn-based monster encounters.

This project was created as part of the end-of-year Python coursework for CBSE Class XI.

---

## 🎮 Game Features

* **⚔️ Turn-Based Combat System:**
  Engage in strategic battles using directional attacks and defences (high, medium, low) with an element of randomness.

* **🛍️ Shop System:**
  Buy weapons, armor, and potions using coins collected throughout the game.

* **🎒 Inventory Management:**
  View and manage your inventory with weapons, armor, potions, and coin count.

* **📈 Progressive Difficulty:**
  Fight through levels featuring Goblins, Orcs, Trolls, Giants, and a final Dragon boss.

* **🧠 Strategy + Luck:**
  Balance between attack types and defences to beat monsters efficiently.

---

## 🧠 Skills & Concepts Learned

* Menu-driven programming
* Functions and modular code design
* Random number generation using `random`
* List and dictionary data structures
* Inventory and state management
* Game loop mechanics
* Basic OOP-like logic using procedural code

---

## 🛠️ How It Works

1. **Main Menu:**

   * View Inventory
   * Visit Shop
   * Enter Arena (Combat)
   * Exit Game

2. **Combat Flow:**

   * Player chooses to attack or use potion.
   * Attacks involve choosing a direction (high/medium/low) while monster defends.
   * Then the monster attacks and player must defend.
   * HP is deducted based on damage ranges and outcomes.
   * Win to move to the next level or return to the main menu.

3. **Shop System:**

   * Purchase from 3 categories: Armor, Weapons, Potions.
   * Buyable items are defined with stats and prices.
   * Coins are deducted and inventory updated accordingly.

---

## 💾 How to Run

1. Make sure Python 3 is installed.
2. Download the file: `Parantap Mishra Dungeon Duel.py`
3. Run it using the terminal or any Python IDE:

```bash
python "Parantap Mishra Dungeon Duel.py"
```

---

## 🧪 Sample Equipment & Monsters

### Default Inventory:

* Weapon: Small Dagger (1–3 damage)
* Armor: Leather Armor (5 defense)
* Coins: 100

### Sample Shop Items:

* Weapons: Dagger, Long Sword, Axe
* Armor: Iron Armor, Diamond Armor, Netherite Armor
* Potions: Health Boost (+20 HP), Attack Boost (+5)

### Monster Levels:

| Level | Name   | HP  | Damage Range |
| ----- | ------ | --- | ------------ |
| 1     | Goblin | 50  | 1–5          |
| 2     | Orc    | 75  | 3–7          |
| 3     | Troll  | 100 | 5–10         |
| 4     | Giant  | 150 | 7–12         |
| 5     | Dragon | 200 | 10–15        |

---


## 🛠 Tools & Technologies

* **Language:** Python 3
* **Library Used:** `random`
* **Editor:** IDLE / VS Code
* **Platform:** Windows (Lenovo Ideapad Slim 5i)
