# Asteroids Game - A Retro Space Shooter 🚀

Welcome to the **Asteroids Game**! A nostalgic space adventure where you control a spaceship to navigate through a field of asteroids and shoot them down. Inspired by the classic arcade game, this project brings the thrill of space battles to your screen with modern Pygame implementation.

## 🚀 Features
- **Player Controls**: Move, rotate, and shoot with responsive keyboard inputs.
- **Asteroids**: Large asteroids split into smaller pieces when destroyed. Keep shooting!
- **Bullet Mechanics**: Shoot bullets with a cooldown mechanic to prevent rapid fire.
- **Collision Detection**: Asteroids and bullets collide, causing destruction (or you might get hit!).
- **Cooldowns**: Manage your shooting cooldown and strategic asteroid destruction.

## 🎮 How to Play
1. **Move**: Use `W` to move forward and `S` to move backward.
2. **Rotate**: Use `A` to rotate left and `D` to rotate right.
3. **Shoot**: Press `Space` to shoot bullets at the asteroids.
4. **Survive**: Avoid asteroids, or shoot them before they hit you! Large asteroids split into smaller ones upon destruction.
5. **Game Over**: The game ends when the player collides with an asteroid.

## 🛠️ How to Run

### Prerequisites:
Make sure you have the following installed:
- Python 3.x
- Pygame library

### Installation:
1. Clone this repository:
   ```bash
   git clone https://github.com/Vrana710/asteroids_game.git
   ```

2. Navigate to the project folder:
   ```bash
   cd asteroids_game
   ```

3. Install the required dependencies:
   ```bash
   pip install pygame
   ```

### Running the Game:
To run the game, simply execute the `main.py` file:
```bash
python main.py
```

The game window should open, and you can start playing right away!

## 🔧 Development

### Key Features Implemented:
- **Player Movement**: Navigate the spaceship with smooth movement and rotation.
- **Shooting**: A shooting cooldown ensures a strategic firing pace.
- **Asteroid Collision and Splitting**: Large asteroids split into smaller pieces, getting faster and more unpredictable with each split.
- **Bullet-Asteroid Collision**: Bullet impact causes asteroids to break into smaller fragments (or disappear if small enough).
  
### Future Improvements:
- **More Levels**: Increase difficulty as you progress through more challenging asteroid fields.
- **Sound Effects**: Add blasting sounds when shooting and asteroid collisions.
- **Graphics & Animations**: Enhance the visuals with better spaceship designs and asteroid textures.

## 🤝 Contributing
We welcome contributions to improve the game! Feel free to fork the repository and submit pull requests. Here’s how you can help:
- Report bugs
- Suggest new features or enhancements
- Contribute code to fix issues or add new gameplay mechanics

## 📜 License
This project is open-source and available under the [MIT License](LICENSE).