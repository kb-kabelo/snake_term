# snake_term


Each “tick” is one frame.

On each tick, you update the world (snake, food) and redraw.

2️⃣ Clear / Refresh Screen

Before drawing the new frame, you clear the old frame.

This prevents the snake from leaving trails on the terminal.

In terminal games, this is like wiping the board clean.

3️⃣ Update Game State

Move the snake one step in its current direction.

Check if it has eaten food → grow if needed.

Check for collisions → end game if necessary.

Optionally: update score, apply speed changes, etc.

4️⃣ Redraw Board

Place walls.

Draw the snake (head + body).

Draw the food.

Print the board to the screen.

5️⃣ Wait / Delay

Pause briefly (e.g., 0.2 seconds) so movement is visible.

This creates the perception of animation instead of instantly redrawing everything.

6️⃣ Repeat

Go back to step 2.

The snake moves one step, the board updates, the screen refreshes.

Loop continues until collision/game over.
