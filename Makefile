install:
	uv sync

brain-games:
	uv run brain-games
brain-even:
	uv run brain-even
build:
	uv build
package-install:
	uv tool install --force dist/*.whl
pack:
	build package-install
lint:
	uv run ruff check brain_games