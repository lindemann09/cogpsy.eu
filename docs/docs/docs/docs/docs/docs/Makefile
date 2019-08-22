all: build

html:
	make --directory=_data all
	mv -f _data/*.html _includes

build:
	make html
	jekyll build --incremental

serve:
	make html
	jekyll s --future --drafts --livereload

deploy:
	make build
	rm -rf docs/
	mv _site/ docs/

clean:
	jekyll clean
