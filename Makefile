all: build

html:
	make --directory=_data all
	mv -f _data/*.html _includes

build:
	make html
	make index_slides
	rm docs/ -rf
	jekyll build --incremental

index_slides: # index for slides folder
	rm -f slides/index.html
	ls
	tree -H '.' -L 2 --noreport --charset utf-8 -T "My Slides" slides > slides/index.html
	cat slides/index.html

serve:
	make build
	jekyll s --future --drafts --livereload

deploy:
	make build index_slides
	mv _site/ docs/
	git add .
	# Commit changes.
	git commit -m "rebuilding site"
	# Push source and build repos.
	#git push --all

clean:
	jekyll clean
