# requires jekyyl

all: build

html:
	make --directory=_data all
	mv -f _data/*.html _includes

build:
	make html
	rm docs/ -rf
	jekyll build --incremental
	mv _site/ docs/

serve:
	make build
	jekyll s --future --drafts --livereload

deploy:
	make build
	git add .
	# Commit changes.
	git commit -m "rebuilding site"
	# Push source and build repos.
	git push --all

clean:
	jekyll clean
