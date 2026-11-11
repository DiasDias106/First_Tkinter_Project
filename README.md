<h1 align="center">🧠 Moving Robot: Graphical Edition</h1>

<p align="center">
  <i>My first Tkinter project: the Moving Robot simulator rebuilt with a clickable, colour-coded map editor and a timed robot game.</i>
</p>

<p align="center">
  <img src="https://img.shields.io/badge/Python-3.x-3776AB?style=for-the-badge&logo=python&logoColor=white" alt="Python"/>
  <img src="https://img.shields.io/badge/Tkinter-GUI-1a1b27?style=for-the-badge" alt="Tkinter"/>
  <img src="https://img.shields.io/badge/platform-Windows-0078D6?style=for-the-badge&logo=windows&logoColor=white" alt="Windows"/>
</p>

---

## 📖 About

This is the graphical evolution of **[Moving Robot](https://github.com/DiasDias106/Moving_Robot)**. The same map logic now lives inside a **Tkinter** interface, where you can view the map in several formats, edit it by clicking on cells, and play a timed game guiding the robot from a start point to a finish point.

## ✨ Features

**Main menu**
- 📄 **Show original map**: the raw text map
- 🔣 **Show encoded map**: `.` and `#` replaced by `~` and `X`
- 📍 **Show obstacles**: positions of every obstacle on the grid
- 🟩🟥 **Coloured map**: a grid with free cells in **green** and obstacles in **red**

**Robot game window**
- 🖱️ **Edit mode**: click cells to add or remove obstacles
- 🎯 **Set start / finish**: choose where the robot starts and where it must go
- 📐 **Resize map**: change the number of rows and columns
- ⏱️ **Timer & click counter**: track how long and how many moves you take
- ⏸️ **Stop time**, 🔄 **Restart**, 🧹 **Clear map**
- 🎨 **Change background**: switch to a random background colour
- 🔊 **Sound feedback** through `winsound`

## 🚀 Getting Started

### Requirements
- **Windows** (the project uses the built-in `winsound` module)
- Python **3.6+** (Tkinter is included with the standard installer)

### Run
```bash
git clone https://github.com/DiasDias106/First_Tkinter_Project.git
cd First_Tkinter_Project/primerio_trabalho_tkinter/tkinter_projet
python tkinter_first_project.py
```

> Run it from inside `tkinter_projet/` so the script can find `mapa.txt`.

## 📁 Project Structure

```
primerio_trabalho_tkinter/tkinter_projet/
├── tkinter_first_project.py   # GUI, map rendering, editor and game logic
└── mapa.txt                   # Default map (. = free, # = obstacle)
```

## 🧠 Concepts Practised

- Building multi-window GUIs with Tkinter (`Toplevel`, `Frame`, `Label`, `Button`)
- Event binding (`<Button-1>`) and dynamic widget grids
- Timers with `after()` and real-time UI updates
- Reusing and extending existing console logic in a GUI

## 📜 License

Distributed under the terms of the [LICENSE](LICENSE) file in this repository.

---

<p align="center">Made by <a href="https://github.com/DiasDias106">Francisco Dias</a></p>
