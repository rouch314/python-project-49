install:
	uv sync

brain-games:
	uv run brain-games
brain-even:
	uv run brain-even
brain-calc:
	poetry run brain-calc
brain-gcd:
	poetry run brain-gcd
brain-progression:
	poetry run brain-progression
brain-prime:
	poetry run brain-prime
build:
	uv build
package-install:
	uv tool install --force dist/*.whl
pack:
	build package-install
lint:
	uv run ruff check brain_games