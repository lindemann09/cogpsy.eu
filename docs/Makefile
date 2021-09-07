all: build

html:
	make --directory=_data all
	mv -f _data/*.html _includes

build:
	make html
	make slides
	rm docs/ -rf
	jekyll build --incremental

slides: # index for slides folder
	rm slides/index.html
	tree -H '.' -L 1 --noreport --charset utf-8 slides > slides/index.html

serve:
	make build
	jekyll s --future --drafts --livereload

deploy:
	make build
	mv _site/ docs/
	git add .
	# Commit changes.
	git commit -m "rebuilding site"
	# Push source and build repos.
	git push --all

clean:
	jekyll clean
