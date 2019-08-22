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
	git add .
	# Commit changes.
	msg="rebuilding site $(date)"
	if [ -n "$*" ]; then
		msg="$*"
	fi
	git commit -m "$msg"
	# Push source and build repos.
	git push --all

clean:
	jekyll clean
