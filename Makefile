init_submodules:
	git submodule update --init --recursive

pull_submodules:
	git pull --recurse-submodules

push_submodules:
	git push --recurse-submodules

