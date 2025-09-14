Project skeleton for the new CLI RPG. This folder contains only structure and documentation for now; implementation will be added incrementally.

Structure overview:
- io/: CLI input/output adapters and rendering helpers.
- models/: Core domain dataclasses (player, enemy, stats, items, effects).
- systems/: Game logic systems (combat, leveling, inventory, encounters).
- utils/: Utilities (RNG seeding, save/load helpers, typing aliases).
- data/: External, data-driven content (enemies, items, encounters, etc.).
- tests/: Unit tests for systems (pure logic) once implemented.

Note: No executable code is included yet; these are placeholders to guide development.

